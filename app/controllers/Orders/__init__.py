from flask import Blueprint

blueprint = Blueprint('orders', __name__, url_prefix='/orders')

from . import new
from . import lookup