from functools import wraps
import jwt
from flask import app, request


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # Here you would add your token validation logic
        token = request.args.get("token")
        if not token:
            return {"message": "Token is missing or invalid!"}
        try:
            payload = jwt.decode(token, app.config["SECRET_KEY"])
        except:
            return {"message": "Token is invalid!"}

    return decorated
