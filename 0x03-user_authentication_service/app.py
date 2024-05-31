#!/usr/bin/env python3
"""
This is the asic Flask app Module
"""
from flask import (
    jsonify, Flask, request,
    abort)
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route("/")
def greet():
    """
    THis basic greeting method
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users")
def users():
    """
    s
    """
    data = request.get_json()
    if data:
        if 'email' not in request.get_json():
            abort(400, description="Missing email")
        if 'password' not in request.get_json():
            abort(400, description="Missing password")
    else:
        abort(400, description="Not a JSON")
    try:
        user = AUTH.register_user(data["email"], data["password"])
    except ValueError:
        return jsonify({"message": "email already registered"})
    return jsonify({"email": "{}".format(data["email"]),
                    "message": "{}".format(user)})
        

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
