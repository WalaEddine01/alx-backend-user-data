#!/usr/bin/env python3
"""
Main file
"""
from auth import Auth

email = 'bob@bob.com'
password = 'MyPwdOfBob'
auth = Auth()

wa = auth.register_user(email, password)

print(auth.create_session(email))
print(wa.session_id)
print(auth.create_session("unknown@email.com"))