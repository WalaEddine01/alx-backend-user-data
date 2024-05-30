#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        The method should save the user to the database
        """
        user = User(email=email, hashed_password=hashed_password)
        session = self._session
        session.add(user)
        session.commit()
        return user

    def find_user_by(self, *args, **kwargs) -> User:
        """
        This method takes in arbitrary keyword arguments and returns
        the first row found in the users table as filtered by the method's
        input arguments
        """
        session = self._session
        for key, value in kwargs.items():
            if not hasattr(User, key):
                raise InvalidRequestError
            for obj in session.query(User):
                if getattr(obj, key) == value:
                    return obj
                else:
                    raise NoResultFound

    def update_user(self, *args, **kwargs) -> None:
        """
        locate the user to update, then will update the user’s
        attributes as passed in the method’s arguments then commit
        changes to the database
        """
        session = self._session
        try:
            user = self.find_user_by(id=args[0])
        except NoResultFound:
            raise ValueError()
        for key, value in kwargs.items():
            if hasattr(user, key):
                setattr(user, key, value)
            else:
                raise ValueError
        session.commit()
