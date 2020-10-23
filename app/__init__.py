from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_fontawesome import FontAwesome
from elasticsearch import Elasticsearch


db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
bootstrap = Bootstrap()
fa = FontAwesome()

def create_app(config_class=Config):
  app = Flask(__name__)
  app.config.from_object(config_class)

  app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']]) \
    if app.config['ELASTICSEARCH_URL'] else None

  db.init_app(app)
  migrate.init_app(app, db)
  login.init_app(app)
  bootstrap.init_app(app)
  fa.init_app(app)
  
  from app.main import bp as main_bp
  app.register_blueprint(main_bp)

  from app.errors import bp as errors_bp
  app.register_blueprint(errors_bp)

  from app.auth import bp as auth_bp
  app.register_blueprint(auth_bp, url_prefix='/auth')

  from app.topics import bp as topics_bp
  app.register_blueprint(topics_bp, url_prefix='/topics')

  from app.questions import bp as questions_bp
  app.register_blueprint(questions_bp, url_prefix='/questions')

  from app.answers import bp as answers_bp
  app.register_blueprint(answers_bp, url_prefix='/answers')

  # logging setup will go here

  return app

from app import models