from app.models import User, Topic
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField, TextAreaField
from wtforms.validators import DataRequired

class QuestionForm(FlaskForm):
  text = StringField('Summary', validators=[DataRequired()])
  description = TextAreaField('Description', validators=[DataRequired()])
  up_votes = IntegerField('Up Votes', validators=[])
  down_votes = IntegerField('Down Votes', validators=[])
  topic_id = SelectField('Topic', coerce=int, validate_choice=False, validators=[DataRequired()])
  user_id = IntegerField('User ID', validators=[])
  submit = SubmitField('Submit')