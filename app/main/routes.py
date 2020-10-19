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


# ##################################
# # User / Login Views             #
# ##################################
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#   if current_user.is_authenticated:
#     return redirect(url_for('index'))
#   form = LoginForm()
#   if form.validate_on_submit():
#     user = User.query.filter_by(username=form.username.data).first()
#     if user is None or not user.check_password(form.password.data):
#       flash('Invalid username or password')
#       return redirect(url_for('login'))
#     login_user(user)
#     next_page = request.args.get('next') # argument passed in url query string by flask_login
#     if not next_page or url_parse(next_page).netloc != '':
#       next_page = url_for('index')
#     return redirect(next_page)
#   return render_template('login.html', title='Log In', form=form)

# @app.route('/logout')
# def logout():
#   logout_user()
#   return redirect(url_for('index'))

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#   if current_user.is_authenticated:
#     return redirect(url_for('index'))
#   form = RegistrationForm()
#   if form.validate_on_submit():
#     user = User(username=form.username.data, email=form.email.data)
#     user.set_password(form.password.data)
#     db.session.add(user)
#     db.session.commit()
#     flash('Congratulations, you are now a registered user!')
#     return redirect(url_for('login'))
#   return render_template('register.html', title="Register", form=form)


# ##################################
# # Topic Views                    #
# ##################################
# @app.route('/topics', methods=['GET'])
# def topics_index():
#   topics = Topic.query.all()
#   return render_template('topics.html', title='Topic Index', topics=topics)

# @app.route('/topics', methods=['POST'])
# def topics_create():
#   form = TopicForm()
#   topic = Topic(name=form.name.data, description=form.description.data)
#   db.session.add(topic)
#   db.session.commit()
#   flash('New Topic Added!')
#   return redirect(url_for('index')) #temporary

# @app.route('/topics/new', methods=['GET'])
# def topic_new():
#   form = TopicForm()
#   backroute = '/topics'
#   verb ='POST' # provide the HTTP verb needed for the create route
#   return render_template('topic_form.html', title='New Topic', form=form, backroute=backroute, verb=verb)

# @app.route('/topics/<id>', methods=['GET'])
# def topic_show(id):
#   topic = Topic.query.filter_by(id=id).first()
#   return render_template('topic.html', title='Topic Detail', topic=topic)

# @app.route('/topics/<id>', methods=['POST'])
# def topic_update(id):
#   form = TopicForm()
#   topic = Topic.query.get(id)
#   topic.name = form.name.data
#   topic.description = form.description.data
#   db.session.add(topic)
#   db.session.commit()
#   return redirect(url_for('topic_show', id=id)) # redirect to the show view

# @app.route('/topics/<id>/edit', methods=['GET'])
# def topic_edit(id):
#   topic = Topic.query.filter_by(id=id).first()
#   form = TopicForm(obj=topic)  # pre-populate the form with a representation of the current record in the DB
#   backroute = '/topics/' + id
#   verb = 'DELETE'  # provide the HTTP verb needed for the update route
#   return render_template('topic_form.html', title='Edit Topic', form=form, backroute=backroute, verb=verb) 

# @app.route('/topics/<id>/delete', methods=['POST'])
# def topic_delete(id):
#   topic = Topic.query.filter_by(id=id).first()
#   db.session.delete(topic)
#   db.session.commit()
#   return redirect(url_for('index')) 


# ##################################
# # Question Views                 #
# ##################################
# @app.route('/question', methods=['GET', 'POST'])
# def question():
#   questions = Question.query.all()
#   return render_template('questions.html', title='Questions Index', questions=questions)


# ##################################
# # Answer Views                   #
# ##################################
# @app.route('/answer', methods=['GET', 'POST'])
# def answer():
#   answers = Answer.query.all()
#   return render_template('answers.html', title='Answers Index', answers=answers)