from sqlalchemy.orm import mapped_column
from sqlalchemy import String, Uuid
from uuid import uuid4
from eventplugs import db


class Users(db.Model):
    """Table users"""
    user_id = mapped_column(Uuid, primary_key=True, unique=True, default=uuid4)
    username = mapped_column(String(15), nullable=False)
    fullname = mapped_column(String(30), nullable=False)
    password = mapped_column(String(100), nullable=False)
    phone = mapped_column(String(15))
    email = mapped_column(String(30))

    def __repr__(self):
        return f"User {self.fullname}"
