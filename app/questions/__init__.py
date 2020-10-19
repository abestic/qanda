from flask import Blueprint

bp = Blueprint('questions', __name__, template_folder='templates')

from app.questions import routes