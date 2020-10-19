from app.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Length

class TopicForm(FlaskForm):
  name = StringField('Name', validators=[DataRequired()])
  description = TextAreaField('Description', validators=[DataRequired(), Length(min=1, max=255)])
  submit = SubmitField('Submit')