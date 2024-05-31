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


@app.route("/", methods=["GET"])
def greet():
    """
    THis basic greeting method
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['POST'], strict_slashes=False)
def register():
    """
    function that implements the POST /users route
    """
    data = request.get_json()
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
        return abort(400, description="email already registered")
    return jsonify({"email": data["email"], "message": "user created"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
