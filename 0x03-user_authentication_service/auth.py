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


def _generate_uuid() -> str:
    """
    The function should return a string representation
    of a new UUID
    """
    return str(uuid4())


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

    def create_session(self, email: str):
        """
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """
        """
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        '''
        '''
        self._db.update_user(user_id=user_id, session_id=None)
        return None

    def get_reset_password_token(self, email: str) -> str:
        """
        """
        try:
            user = self._db.find_user_by(email=email)
            reset_token = str(uuid4())
            self._db.update_user(user.id, reset_token=reset_token)
            return reset_token
        except NoResultFound:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError
        hashed_password = _hash_password(password)
        self._db.update_user(user.id, password=hashed_password)
        self._db.update_user(user.id, reset_token=None)
