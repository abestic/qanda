from app import db
from app.main import bp
from app.main.forms import SearchForm
from app.models import User, Topic, Question, Answer
from flask import current_app, render_template, flash, redirect, url_for, request, g
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse


@bp.before_app_request
def before_request():
  g.search_form = SearchForm()


@bp.route('/')
@bp.route('/index')
def index():
  popular_questions = Question.query.order_by(Question.total_votes.desc()).limit(10)
  recent_questions = Question.query.order_by(Question.id.desc()).limit(10)
  if current_user.is_authenticated:
    my_question_count = Question.query.filter_by(user_id=current_user.id).count()
    my_answer_count = Answer.query.filter_by(user_id=current_user.id).count()
    return render_template('index.html', title='Home', my_question_count=my_question_count, my_answer_count=my_answer_count, popular_questions=popular_questions, recent_questions=recent_questions)
  else:
    return render_template('index.html', title='Home', popular_questions=popular_questions, recent_questions=recent_questions)

@bp.route('/search')
def search():
  if not g.search_form.validate():
    return redirect(url_for('questions.index')) # if search form is blank, redirect to quesions index view
  page = request.args.get('page', 1, type=int)
  results, total = Question.search(g.search_form.q.data, page, current_app.config['RESULTS_PER_PAGE'])
  next_url = url_for('main.search', q=g.search_form.q.data, page=page + 1) \
    if total > page * current_app.config['RESULTS_PER_PAGE'] else None
  prev_url = url_for('main.search', q=g.search_form.q.data, page=page - 1) \
    if page > 1 else None
  return render_template('search.html', title='Search', results=results, total=total, next_url=next_url, prev_url=prev_url)