from flask_bootstrap import Bootstrap5
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


# flask-sqlalchemy
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
# flask-migrate
migrate = Migrate()

# bootstrap-flask
bootstrap = Bootstrap5()
