from app import db, login
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
  
  def __repr__(self):
    return '<Answer {}>'.format(self.text)