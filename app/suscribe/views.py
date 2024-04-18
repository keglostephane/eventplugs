from . import suscribe_pb


@suscribe_pb.route('/', methods=['GET'])
def index():
    """display index page"""
    return "<h1>Hello World</h1>"
