from flask import Flask
from extensions import db


def create_app():
    """Flask instance factory"""
    app = Flask(__name__)
    app.config.from_object('config.Development')

    # Initialize Flask extensions
    db.init_app(app)

    # Import blueprints
    from auth import auth_bp

    # Register blueprints
    app.register_blueprint(auth_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
