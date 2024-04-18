from flask import Flask
from extensions import db, migrate, bootstrap


def create_app():
    """Flask instance factory"""
    app = Flask(__name__)
    app.config.from_object('config.Development')

    # Initialize Flask extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bootstrap.init_app(app)


    # Flask application context
    with app.app_context():
        # Import models
        from auth.models import Users
        from publish.models import Publishers, Categories
        from suscribe.models import Suscriptions, Topics, Contents, Events

        db.create_all()

    # Import blueprints
    from auth import auth_bp
    from publish import publish_bp
    from suscribe import suscribe_pb

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(publish_bp, url_prefix='/publisher')
    app.register_blueprint(suscribe_pb, url_prefix='/suscription')

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
