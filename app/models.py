from app import db, login
from app.search import add_to_index, remove_from_index, query_index

from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


# User Loader
@login.user_loader
def user_loader(id):
  return User.query.get(int(id))

# Users Table
# UserMixin provides is_authenticated, is_active, is_anonymous, and get_id() methods needed by Flask-Login
class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), index=True, unique=True)
  email = db.Column(db.String(120), index=True, unique=True)
  password_hash = db.Column(db.String(128))
  questions = db.relationship('Question', backref='author', lazy='dynamic')
  answers = db.relationship('Answer', backref='author', lazy='dynamic')

  # format the object output
  def __repr__(self):
    return '<User {}>'.format(self.username)

  def set_password(self, password):
    self.password_hash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password_hash, password)


# Topics Table
class Topic(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), index=True, unique=True)
  description = db.Column(db.String(255), index=True)
  questions = db.relationship('Question', backref='topic', lazy='dynamic')
  __searchable__ = ['name', 'description']

  # format the object output
  def __repr__(self):
    return '<Topic {}>'.format(self.name)


# Questions Table
class Question(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  text = db.Column(db.String(255), index=True, unique=True)
  description = db.Column(db.Text, index=True)
  up_votes = db.Column(db.Integer, index=True)
  down_votes = db.Column(db.Integer, index=True)
  total_votes = db.Column(db.Integer, index=True)
  topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'))
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  answers = db.relationship('Answer', backref='question', lazy='dynamic')
  __searchable__ = ['text', 'description']

  # format the object output
  def __repr__(self):
    return '<Question {}>'.format(self.text)


# Answers Table
class Answer(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  text = db.Column(db.Text, index=True)
  up_votes = db.Column(db.Integer, index=True)
  down_votes = db.Column(db.Integer, index=True)
  total_votes = db.Column(db.Integer, index=True)
  question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  __searchable__ = ['text']
  
  # format the object output
  def __repr__(self):
    return '<Answer {}>'.format(self.text)


# Searchable Mixin
class SearchableMixin(object):
  @classmethod
  def search(cls, expression, page, per_page):
    ids, total = query_index(cls.__tablename__, expression, page, per_page)
    if total == 0:
      return cls.query.filter_by(id=0), 0
    when = []
    for i in range(len(ids)):
      when.append((ids[i], i))
    return cls.query.filter(cls.id.in_(ids)).order_by(db.case(when, value=cls.id)), total

  @classmethod
  def before_commit(cls, session):
    session._changes = {
      'add': list(session.new),
      'update': list(session.dirty),
      'delete': list(session.deleted)
    }

  @classmethod
  def after_commit(cls, session):
    for obj in session._changes['add']:
      if isinstance(obj, SearchableMixin):
        add_to_index(obj.__tablename__, obj)
    for obj in session._changes['update']:
      if isinstance(obj, SearchableMixin):
        add_to_index(obj.__tablename__, obj)
    for obj in session._changes['delete']:
      if isinstance(obj, SearchableMixin):
        remove_from_index(obj.__tablename__, obj)
    session._changes = None

  @classmethod
  def reindex(cls):
    for obj in cls.query:
      add_to_index(cls.__tablename__, obj)

db.event.listen(db.session, 'before_commit', SearchableMixin.before_commit)
db.event.listen(db.session, 'after_commit', SearchableMixin.after_commit)