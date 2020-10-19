from app import db
from app.main import bp
from app.models import User, Topic, Question, Answer
from flask import current_app, render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse


##################################
# Main View                      #
##################################
@bp.route('/')
@bp.route('/index')
def index():
  topics = Topic.query.all()
  return render_template('index.html', title='Home', topics=topics)