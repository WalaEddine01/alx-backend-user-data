#!/usr/bin/env python3
"""
This is the auth Module
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    BasicAuth class
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        This is the def extract_base64_authorization_header method
        """
        if not authorization_header or type(authorization_header) != str\
                or not authorization_header.startswith("Basic "):
            return None
        return str(authorization_header.split(" ")[1])
