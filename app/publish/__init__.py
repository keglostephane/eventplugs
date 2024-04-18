from flask import Blueprint

publish_bp = Blueprint('publish', __name__)

from publish import views
