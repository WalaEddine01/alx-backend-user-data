#!/usr/bin/env python3
"""
User model
"""
from uuid import uuid4
from sqlalchemy import (
    Integer, String, Column
    )
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    The User Class
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

    def __init__(self, *args, **kwargs):
        """
        """
        self.id = uuid4()
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        if kwargs.get("id", None) is None:
                self.id = str(uuid4())
