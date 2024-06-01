#!/usr/bin/env python3
"""
"""
from auth import Auth
from db import *
EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    Auth.register_user(EMAIL, PASSWD)
    Auth.log_in_wrong_password(EMAIL, NEW_PASSWD)
    Auth.profile_unlogged()
    session_id = Auth.log_in(EMAIL, PASSWD)
    Auth.profile_logged(session_id)
    Auth.log_out(session_id)
    reset_token = Auth.reset_password_token(EMAIL)
    Auth.update_password(EMAIL, reset_token, NEW_PASSWD)
    Auth.log_in(EMAIL, NEW_PASSWD)