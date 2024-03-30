from . import auth_bp


@auth_bp.route('/', methods=["GET"])
def index():
    """display index page"""
    return "<h1>Hello World</h1>"
