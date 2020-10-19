from app import db
from app.questions import bp
from app.questions.forms import QuestionForm
from app.answers.forms import QAForm
from app.models import Question, Topic, User

from flask import render_template, flash, redirect, url_for, jsonify
from flask_login import current_user, login_user, logout_user, login_required


@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET'])
def index():
  questions = Question.query.all()
  return render_template('questions.html', title='Question Index', questions=questions)

@bp.route('/create', methods=['POST'])
def create():
  form = QuestionForm()
  if form.validate_on_submit():
    question = Question(text=form.text.data, description=form.description.data, topic_id=form.topic_id.data, up_votes=0, down_votes=0, total_votes=0)
    db.session.add(question)
    db.session.commit()
    flash('New Question Added!')
    return redirect(url_for('questions.show', id=question.id)) # redirect to the question.show view for the newly created topic
  form.topic_id.choices = [(t.id, t.name) for t in Topic.query.order_by('name')]
  backroute = '/questions/create'
  verb='POST'
  return render_template('question_form.html', title='Ask Question', form=form, backroute=backroute, verb=verb)

@bp.route('/new', methods=['GET'])
def new():
  form = QuestionForm()
  form.topic_id.choices = [(t.id, t.name) for t in Topic.query.order_by('name')]
  backroute = '/questions/create'
  verb = 'POST'
  return render_template('question_form.html', title='Ask Question', form=form, backroute=backroute, verb=verb)

@bp.route('<id>', methods=['GET'])
def show(id):
  question = Question.query.filter_by(id=id).first()
  form = QAForm(question_id = id)
  return render_template('question_detail.html', title=question.text, question=question, form=form)

@bp.route('/<id>', methods=['POST'])
def update(id):
  form = QuestionForm()
  question = Question.query.get(id)
  question.text = form.text.data
  question.description = form.description.data
  question.topic_id = form.topic_id.data
  db.session.add(question)
  db.session.commit()
  return redirect(url_for('questions.show', id=id)) # redirect to the show view

@bp.route('/<id>/edit', methods=['GET'])
def edit(id):
  question = Question.query.filter_by(id=id).first()
  form = QuestionForm(obj=question) # pre-populate the form with the representation of the current record in the DB
  form.topic_id.choices = [(t.id, t.name) for t in Topic.query.order_by('name')]
  backroute = '/questions/' + id
  verb = 'POST'
  return render_template('question_form.html', title='Edit Question', form=form, backroute=backroute, verb=verb)

@bp.route('/<id>/delete', methods=['POST'])
def delete(id):
  question = Question.query.filter_by(id=id).first()
  db.session.delete(question)
  db.session.commit()
  return redirect(url_for('questions.index'))

@bp.route('/<id>/vote/<type>', methods=['POST'])
def vote(id, type):
  question = Question.query.filter_by(id=id).first()
  if type == 'up':
    question.up_votes += 1
    question.total_votes += 1
  elif type == 'down':
    question.down_votes += 1
    question.total_votes -= 1  
  db.session.add(question)
  db.session.commit()
  return jsonify({'total_votes': question.total_votes, 'up_votes': question.up_votes, 'down_votes': question.down_votes,})
