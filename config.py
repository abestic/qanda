import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
  SQLALCHEMY_TRACK_MODIFICATIONS = False



# TO-DO:
# - Set SECRET_KEY as an OCP secret that populates an env variable
# - Set DATABASE_URL as an OCP secret that populates an env variable
# - Determine if config.py needs to be treated as a config map when deploying to OCP...
