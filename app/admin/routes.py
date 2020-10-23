from app import db
from app.admin import bp
from app.answers.forms import AnswerForm
from app.questions.forms import QuestionForm
from app.topics.forms import TopicForm
from app.models import Answer, Question, Topic, User

from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required

@bp.route('/', methods=['GET'])
def admin_panel():
  answers = Answer.query.all()
  questions = Question.query.all()
  topics = Topic.query.all()
  users = User.query.all()
  return render_template('admin.html', title="Admin Panel", answers=answers, questions=questions, topics=topics, users=users)