from flask import Blueprint

blueprint = Blueprint('reviews', __name__, url_prefix='/reviews')

from . import new