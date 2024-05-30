#!/usr/bin/python3
import bcrypt

pas = b"wa"

print(bcrypt.hashpw(pas, bcrypt.gensalt()))