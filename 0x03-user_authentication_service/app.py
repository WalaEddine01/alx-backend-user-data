#!/usr/bin/env python3
"""
This is the asic Flask app Module
"""
from sqlalchemy.orm.exc import NoResultFound
from flask import (
    jsonify, Flask, request,
    abort, make_response, redirect
    )
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
            abort(401, description="Missing email")
        if 'password' not in data:
            abort(401)
    else:
        abort(401)

    valid = AUTH.valid_login(email=data["email"],
                             password=data["password"])
    if valid:
        session_id = AUTH.create_session(data["email"])
    else:
        abort(401)
    res = make_response(jsonify({"email": "{}".format(data["email"]),
                                 "message": "logged in"}))
    res.set_cookie('session_id', session_id)
    return res


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """
    Handle user logout by destroying the session and redirecting
    to the home page.
    """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if not user or not session_id:
        abort(403)
    AUTH.destroy_session(user_id=user.id)
    return redirect("/", code=302)


@app.route("/profile", methods=["GET"], strict_slashes=False)
def profile():
    """
    """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if not session_id:
        abort(403)
    if user:
        return jsonify({"email": f'{user.email}'})
    abort(403)


@app.route('/reset_password', methods=["POST"])
def get_reset_password_token():
    """
    """
    data = request.form
    if data:
        if 'email' not in data:
            abort(403)
        try:
            token = AUTH.get_reset_password_token(data["email"])
            return jsonify({"email": "{}".format(data["email"]),
                            "reset_token": f"{token}"}), 200
        except ValueError:
            abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
