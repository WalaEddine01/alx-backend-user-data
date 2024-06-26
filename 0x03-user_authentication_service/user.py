#!/usr/bin/env python3
"""
User model
"""
from sqlalchemy import (
    Integer, String, Column
    )
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4

Base = declarative_base()


class User(Base):
    """
    The User Class
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
