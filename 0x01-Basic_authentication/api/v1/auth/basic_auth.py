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
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        This is the extract_base64_authorization_header method
        """
        if not authorization_header or type(authorization_header) != str\
                or not authorization_header.startswith("Basic "):
            return None
        return str(authorization_header.split(" ")[1])

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """
        This is the decode_base64_authorization_header
        """
        if not base64_authorization_header\
                or type(base64_authorization_header) != str:
            return None
        try:
            return base64.b64decode(
                base64_authorization_header
                ).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str
            ) -> (str, str):  # type: ignore
        """
        This is the method extract_user_credentials
        """
        if not decoded_base64_authorization_header or\
            type(decoded_base64_authorization_header) != str or\
                len(decoded_base64_authorization_header.split(":")) == 1:
            return None, None
        user_data = decoded_base64_authorization_header.split(':')
        return user_data[0], user_data[1]

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str
            ) -> TypeVar('User'):  # type: ignore
        """ This is the user_object_from_credentials method
        """
        if not user_email or type(user_email) != str or\
                not user_pwd or type(user_pwd) != str:
            return None
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None

        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):  # type: ignore
        """
        Tis is the current_user method
        """
        try:
            auth_header = self.authorization_header(request)
            encoded = self.extract_base64_authorization_header(auth_header)
            decoded = self.decode_base64_authorization_header(encoded)
            email, password = self.extract_user_credentials(decoded)
            return self.user_object_from_credentials(email, password)
        except Exception:
            return None
