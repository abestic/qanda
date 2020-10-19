from app import create_app, db
from app.models import User, Topic, Question, Answer

app = create_app()

# Provide python interpreter shell with this app's context
@app.shell_context_processor
def make_shell_context():
  return {'db': db, 'User': User, 'Topic': Topic, 'Question': Question, 'Answer': Answer}