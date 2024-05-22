#!/usr/bin/env python3
"""
This is the auth Module
"""
from flask import request, jsonify, abort
from typing import List, TypeVar


class Auth:
    """
    This is the auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        require_auth method
        """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        elif path in excluded_paths:
            return False
        else:
            for p in excluded_paths:
                if p.startswith(path) or path.startswith(p):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        authorization_header method
        """
        if request is None or "Authorization" not in request.headers:
            return None
        return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar('User'):  # type: ignore
        """
        current_user method
        """
        return None
