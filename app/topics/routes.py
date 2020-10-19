from app import db
from app.topics import bp
from app.topics.forms import TopicForm
from app.models import Topic

from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required


@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET'])
def index():
  topics = Topic.query.all()
  return render_template('topics.html', title='Topic Index', topics=topics)

@bp.route('/create', methods=['POST'])
def create():
  form = TopicForm()
  topic = Topic(name=form.name.data, description=form.description.data)
  db.session.add(topic)
  db.session.commit()
  flash('New Topic Added!')
  return redirect(url_for('topics.show', id=topic.id)) # redirect to the topic.show view for the newly created topic

@bp.route('/new', methods=['GET'])
def new():
  form = TopicForm()
  backroute = '/topics/create'
  verb ='POST' # provide the HTTP verb needed for the create route
  return render_template('topic_form.html', title='New Topic', form=form, backroute=backroute, verb=verb)

@bp.route('/<id>', methods=['GET'])
def show(id):
  topic = Topic.query.filter_by(id=id).first()
  return render_template('topic_detail.html', title='Topic Detail', topic=topic)

@bp.route('/<id>', methods=['POST'])
def update(id):
  form = TopicForm()
  topic = Topic.query.get(id)
  topic.name = form.name.data
  topic.description = form.description.data
  db.session.add(topic)
  db.session.commit()
  return redirect(url_for('topics.show', id=id)) # redirect to the show view

@bp.route('/<id>/edit', methods=['GET'])
def edit(id):
  topic = Topic.query.filter_by(id=id).first()
  form = TopicForm(obj=topic)  # pre-populate the form with a representation of the current record in the DB
  backroute = '/topics/' + id
  verb = 'POST'  # provide the HTTP verb needed for the update route
  return render_template('topic_form.html', title='Edit Topic', form=form, backroute=backroute, verb=verb) 

@bp.route('/<id>/delete', methods=['POST'])
def delete(id):
  topic = Topic.query.filter_by(id=id).first()
  db.session.delete(topic)
  db.session.commit()
  return redirect(url_for('topics.index')) 