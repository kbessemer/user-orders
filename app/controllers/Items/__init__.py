from flask import Blueprint

items = Blueprint('items', __name__, url_prefix='/items')

from . import post
from . import get