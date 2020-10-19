from app.models import User, Question
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField, TextAreaField, HiddenField
from wtforms.validators import DataRequired

class AnswerForm(FlaskForm):
  text = TextAreaField('Answer', validators=[DataRequired()])
  up_votes = IntegerField('Up Votes', validators=[])
  down_votes = IntegerField('Down Votes', validators=[])
  question_id = SelectField('Question', coerce=int, validators=[DataRequired()])
  user_id = IntegerField('User ID', validators=[])
  submit = SubmitField('Submit')

class QAForm(FlaskForm):
  text = TextAreaField('Answer', validators=[DataRequired()])
  question_id = HiddenField('Question ID', validators=[DataRequired()])
  submit = SubmitField('Post Answer')