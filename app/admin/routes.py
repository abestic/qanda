from app import db
from app.admin import bp
from app.answers.forms import AnswerForm
from app.questions.forms import QuestionForm
from app.topics.forms import TopicForm
from app.models import Answer, Question, Topic, User

from flask import render_template, flash, redirect, url_for, request, current_app
from flask_login import current_user, login_user, logout_user, login_required

@bp.route('/', methods=['GET'])
def panel():

  main = True

  return render_template('admin.html', title="Admin Panel", main=main)


@bp.route('/users', methods=['GET'])
def users():
  page = request.args.get('page', 1, type=int)
  users = User.query.paginate(page, current_app.config['RESULTS_PER_PAGE'], False)
  next_url = url_for('admin.users', page=users.next_num) \
    if users.has_next else None
  prev_url = url_for('admin.users', page=users.prev_num) \
    if users.has_prev else None

  return render_template('admin.html', title="User Administration", users=users.items, next_url=next_url, prev_url=prev_url)


@bp.route('/topics', methods=['GET'])
def topics():
  page = request.args.get('page', 1, type=int)
  topics = Topic.query.paginate(page, current_app.config['RESULTS_PER_PAGE'], False)
  next_url = url_for('admin.topics', page=topics.next_num) \
    if topics.has_next else None
  prev_url = url_for('admin.topics', page=topics.prev_num) \
    if topics.has_prev else None

  return render_template('admin.html', title="Topic Administration", topics=topics.items, next_url=next_url, prev_url=prev_url)


@bp.route('/questions', methods=['GET'])
def questions():
  page = request.args.get('page', 1, type=int)
  questions = Question.query.paginate(page, current_app.config['RESULTS_PER_PAGE'], False)
  next_url = url_for('admin.questions', page=questions.next_num) \
    if questions.has_next else None
  prev_url = url_for('admin.questions', page=questions.prev_num) \
    if questions.has_prev else None

  return render_template('admin.html', title='Question Administration', questions=questions.items, next_url=next_url, prev_url=prev_url)


@bp.route('/answers', methods=['GET'])
def answers():
  page = request.args.get('page', 1, type=int)
  answers = Answer.query.paginate(page, current_app.config['RESULTS_PER_PAGE'], False)
  next_url = url_for('admin.answers', page=answers.next_num) \
    if answers.has_next else None
  prev_url = url_for('admin.answers', page=answers.prev_num) \
    if answers.has_prev else None

  return render_template('admin.html', title='Answer Administration', answers=answers.items, next_url=next_url, prev_url=prev_url)