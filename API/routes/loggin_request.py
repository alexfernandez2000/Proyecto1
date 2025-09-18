from datetime import datetime, timedelta
from flask import (
    Flask,
    current_app,
    make_response,
    request,
    jsonify,
    session,
    Blueprint,
)
import jwt
from routes.auth_helper import token_required

loggin_request_bluebrint = Blueprint("loggin", __name__)


@loggin_request_bluebrint.route("/public")
def public():
    return "Anyone can view this!"


@loggin_request_bluebrint.route("/auth")
@token_required
def auth():
    return "Verified"


@loggin_request_bluebrint.route("/login", methods=["POST"])
def login():
    if request.form["username"] and request.form["password"] == "shiro":
        session["logged_in"] = True
        token = jwt.encode(
            {
                "user": request.form["username"],
                "expiration": str(datetime.utcnow() + timedelta(seconds=60)),
            },
            current_app.config["SECRET_KEY"],
        )
        return jsonify({"token": token})
    else:
        return make_response(
            "Could not verify!",
            403,
            {"WWW-Authenticate": 'Basic realm="Login Required!'},
        )
