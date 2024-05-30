#!/usr/bin/env python3
"""
This mdule for auth
"""
import bcrypt
import encodings


def _hash_password(password: str) -> bytes:
    """
    takes in a password string arguments and returns bytes.
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
