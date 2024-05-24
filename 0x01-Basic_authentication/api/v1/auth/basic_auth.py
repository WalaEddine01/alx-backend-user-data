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
        pass