from . import publish_bp


@publish_bp.route('/', methods=['GET'])
def index():
    """display index page"""
    return "<h1>Hello World</h1>"
