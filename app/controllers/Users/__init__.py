from flask import Blueprint

blueprint = Blueprint('users', __name__, url_prefix='/users')

from . import new
from . import lookup