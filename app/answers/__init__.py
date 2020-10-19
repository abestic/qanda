from flask import Blueprint

bp = Blueprint('answers', __name__, template_folder='templates')

from app.answers import routes