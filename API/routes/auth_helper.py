from functools import wraps
import jwt
from flask import app, current_app, request


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # Here you would add your token validation logic
        token = request.cookies.get("access_token")

        if not token:
            return {"message": "Token is missing or invalid!"}
        try:
            test = current_app.config["SECRET_KEY"]
            payload = jwt.decode(
                token, current_app.config["SECRET_KEY"], algorithms=["HS256"]
            )
        except Exception as e:
            return {"message": e}
        return f(*args, **kwargs)

    return decorated
