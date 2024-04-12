from sqlalchemy.orm import mapped_column
from sqlalchemy import String, Integer, Uuid, Text, Date, Time, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from uuid import uuid4
from eventplugs import db


class Suscriptions(db.Model):
    """Table suscriptions"""
    suscription_id = mapped_column(Integer, primary_key=True, unique=True,
                                   autoincrement=True, default=uuid4)
    publisher_id = mapped_column(Uuid, ForeignKey('publishers.publisher_id'),
                                 nullable=False)
    user_id = mapped_column(Uuid, ForeignKey('users.user_id'), nullable=False)
    topic_id = mapped_column(Integer, ForeignKey('topics.topic_id'),
                             nullable=False)


class Topics(db.Model):
    """Table topics"""
    topic_id = mapped_column(Integer, primary_key=True, autoincrement=True)
    topic_name = mapped_column(String(50), nullable=False)


class Contents(db.Model):
    """Table contents"""
    content_id = mapped_column(Integer, primary_key=True, autoincrement=True)
    title = mapped_column(String(50), nullable=False)
    body = mapped_column(Text, nullable=False)
    type = mapped_column(String(15), nullable=False)
    suscription_id = mapped_column(Integer,
                                   ForeignKey('suscriptions.suscription_id'),
                                   nullable=False)


class Events(db.Model):
    """Table events"""
    event_id = mapped_column(Integer, primary_key=True, autoincrement=True)
    title = mapped_column(String(50), nullable=False)
    description = mapped_column(Text)
    location = mapped_column(JSONB, nullable=False)
    valid = mapped_column(Boolean, default=True)
    start_date = mapped_column(Date, nullable=False)
    end_date = mapped_column(Date, nullable=False)
    start_time = mapped_column(Time, nullable=False)
    end_time = mapped_column(Time, nullable=False)
    content_id = mapped_column(Integer, ForeignKey('contents.content_id'),
                               nullable=False)
