from flask import Blueprint

suscribe_pb = Blueprint('suscribe', __name__)

from suscribe import views
