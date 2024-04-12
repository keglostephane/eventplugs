from sqlalchemy.orm import mapped_column
from sqlalchemy import String, Integer, Uuid, Text, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from uuid import uuid4
from eventplugs import db


class Publishers(db.Model):
    """Table publishers"""
    publisher_id = mapped_column(Uuid, primary_key=True, unique=True,
                                 default=uuid4)
    name = mapped_column(String(50), nullable=False)
    description = mapped_column(Text, nullable=False)
    address = mapped_column(Text, nullable=False)
    location = mapped_column(JSONB)
    category_id = mapped_column(Integer, ForeignKey('categories.category_id'))


class Categories(db.Model):
    """Table categories"""
    category_id = mapped_column(Integer, primary_key=True, nullable=False,
                                autoincrement=True)
    name = mapped_column(String(30), nullable=False)
