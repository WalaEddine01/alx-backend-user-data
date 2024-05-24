#!/usr/bin/env python3
"""
This is the auth Module
"""
from api.v1.auth.auth import Auth
import base64
from models.base import Base
from models.user import User


class BasicAuth(Auth):
    """
    BasicAuth class
    """
    pass
