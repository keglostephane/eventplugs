from . import auth_bp
from flask import render_template


@auth_bp.route('/', methods=["GET"])
def index():
    """display index page"""
    return render_template('index.html')
