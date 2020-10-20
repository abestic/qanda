from app import db
from app.answers import bp
from app.answers.forms import AnswerForm, QAForm
from app.models import Answer, Question, Topic, User #eliminate any that aren't actually used

from flask import render_template, flash, redirect, url_for, jsonify
from flask_login import current_user, login_user, logout_user, login_required

@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET'])
def index():
  answers = Answer.query.all()
  return render_template('answers.html', title="Answer Index", answers=answers)

@bp.route('/create', methods=['POST'])
def create():
  form = QAForm()
  answer = Answer(text=form.text.data, question_id=form.question_id.data, up_votes=0, down_votes=0, total_votes=0, user_id=current_user.id)
  db.session.add(answer)
  db.session.commit()
  flash('Your answer was posted!')
  return redirect(url_for('questions.show', id=answer.question_id)) # redirect to the show view for the question of the newly created answer
  
@bp.route('/new', methods=['GET'])
def new():
  form = AnswerForm()
  form.question_id.choices = [(q.id, q.text) for q in Question.query.order_by('text')]
  backroute = '/answers/create'
  verb = 'POST'
  return render_template('answer_form.html', title='New Question', form=form, backroute=backroute, verb=verb)

@bp.route('<id>', methods=['GET'])
def show(id):
  answer = Answer.query.filter_by(id=id).first()
  return render_template('answer_detail.html', title='Answer Detail', answer=answer)

@bp.route('/<id>', methods=['POST'])
def update(id):
  form = AnswerForm()
  answer = Answer.query.get(id)
  answer.text = form.text.data
  answer.question_id = form.question_id.data
  db.session.add(answer)
  db.session.commit()
  return redirect(url_for('answers.show', id=id)) # redirect to the show view

@bp.route('/<id>/edit', methods=['GET'])
def edit(id):
  answer = Answer.query.filter_by(id=id).first()
  form = AnswerForm(obj=answer) # pre-populate the form with the representation of the current record in the DB
  form.question_id.choices = [(q.id, q.text) for q in Question.query.order_by('text')]
  backroute = '/answers/' + id
  verb = 'POST'
  return render_template('answer_form.html', title='Edit Answer', form=form, backroute=backroute, verb=verb)

# TO-DO: dynamically route user after delete based on where they came from
@bp.route('/<id>/delete', methods=['GET','POST'])
def delete(id):
  answer = Answer.query.filter_by(id=id).first()
  db.session.delete(answer)
  db.session.commit()
  return redirect(url_for('answers.index'))

@bp.route('/<id>/vote/<type>', methods=['POST'])
def vote(id, type):
  answer = Answer.query.filter_by(id=id).first()
  if type == 'up':
    answer.up_votes += 1
    answer.total_votes += 1
  elif type == 'down':
    answer.down_votes += 1
    answer.total_votes -= 1  
  db.session.add(answer)
  db.session.commit()
  return jsonify({'total_votes': answer.total_votes, 'up_votes': answer.up_votes, 'down_votes': answer.down_votes,})