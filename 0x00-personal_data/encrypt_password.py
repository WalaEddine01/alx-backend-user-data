#!/usr/bin/env python3
"""
A module that defines a hash_password function
to return a hashed password and checks hashed_password
validity
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Args:
        password (str): password to be hashed

    Return:
        A hashed password
    """
    p_enc = password.encode('utf-8')
    return bcrypt.hashpw(p_enc, bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Check whether a password is valid
    Args:
        hashed_password (bytes): hashed password
        password (str): password in string

    Return:
        bool
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
