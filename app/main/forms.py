from app.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length

# class LoginForm(FlaskForm):
#   username = StringField('Username', validators=[DataRequired()])
#   password = PasswordField('Password', validators=[DataRequired()])
#   submit = SubmitField('Log In')

# class RegistrationForm(FlaskForm):
#   username = StringField('Username', validators=[DataRequired()])
#   email = StringField('Email', validators=[DataRequired(), Email()])
#   password = PasswordField('Password', validators=[DataRequired()])
#   password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
#   submit = SubmitField('Register')

#   def validate_username(self, username):
#     user = User.query.filter_by(username=username.data).first()
#     if user is not None:
#       raise ValidationError('Please select a different username.')
  
#   def validate_email(self, email):
#     user = User.query.filter_by(email=email.data).first()
#     if user is not None:
#       raise ValidationError('This email address is already in use.')

# class TopicForm(FlaskForm):
#   name = StringField('Name', validators=[DataRequired()])
#   description = TextAreaField('Description', validators=[DataRequired(), Length(min=1, max=255)])
#   submit = SubmitField('Submit')