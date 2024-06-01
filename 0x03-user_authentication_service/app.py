#!/usr/bin/env python3
"""
This is the asic Flask app Module
"""
from flask import (
    jsonify, Flask, request,
    abort, make_response)
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route("/", methods=["GET"])
def greet():
    """
    THis basic greeting method
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['POST'], strict_slashes=False)
def register() -> str:
    """
    function that implements the POST /users route
    """
    data = request.form
    if data:
        if 'email' not in data:
            abort(400, description="Missing email")
        if 'password' not in data:
            abort(400, description="Missing password")
    else:
        abort(400, description="Not a JSON")
    try:
        AUTH.register_user(data["email"], data["password"])
        return jsonify({"email": f"{data['email']}",
                        "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login() -> str:
    """
    """
    data = request.form
    if data:
        if 'email' not in data:
            abort(400, description="Missing email")
        if 'password' not in data:
            abort(400, description="Missing password")
    else:
        abort(400, description="Not a JSON")
    try:
        AUTH.register_user(data["email"], data["password"])
    except ValueError:
        pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
