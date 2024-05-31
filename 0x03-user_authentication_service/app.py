#!/usr/bin/env python3
"""
This is the asic Flask app Module
"""
from flask import jsonify, Flask

app = Flask(__name__)


@app.route("/")
def greet():
    """
    THis basic greeting method
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
