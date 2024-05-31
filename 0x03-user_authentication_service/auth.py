#!/usr/bin/env python3
"""
This mdule for auth
"""
from user import User
from uuid import uuid4
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from flask import session


def _hash_password(password: str) -> bytes:
    """
    takes in a password string arguments and returns bytes.
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        """
        try:
            if self._db.find_user_by(email=email):
                raise ValueError("User <user's email> already exists")
        except NoResultFound:
            pass
        hashed_password = _hash_password(password=password)
        user = self._db.add_user(email=email, hashed_password=hashed_password)
        return user

    def valid_login(self, email: str, password: str) -> bool:
        """
        This method checks if the user can login
        With his intred infos
        """
        Bpass = password.encode()
        try:
            user = self._db.find_user_by(email=email)
            if user:
                return bcrypt.checkpw(Bpass, user.hashed_password)
            return False
        except NoResultFound:
            return False

    def _generate_uuid() -> str:
        """
        The function should return a string representation
        of a new UUID
        """
        return str(uuid4())
