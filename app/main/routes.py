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
  