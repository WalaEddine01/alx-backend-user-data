#!/usr/bin/env python3
"""
User model
"""
from sqlalchemy import (
    Integer, String, Nullable, Column)

class User:
    """
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String(200), nullable=False)
    hashed_password = Column(String(200), nullable=False)
    session_id = Column(String(200), nullable=True)
    reset_token = Column(String(200), nullable=True)
    
