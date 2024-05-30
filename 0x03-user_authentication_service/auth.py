#!/usr/bin/env python3
"""
This mdule for auth
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    takes in a password string arguments and returns bytes.
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
