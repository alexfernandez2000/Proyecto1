import uuid
from flask import Flask, jsonify, render_template, request, session
from routes.loggin_request import loggin_request_bluebrint

app = Flask(__name__)
app.register_blueprint(loggin_request_bluebrint)
app.config["SECRET_KEY"] = "4145a376-19b7-40db-8e6b-2f124b700376"


@app.route("/")
def root():
    print(session)
    if not session.get("logged_in"):
        return render_template("login.html")
    return "Logged in successfullyy!"


@app.route("/user/<user_id>", methods=["GET"])
def get_user(user_id):
    user = {"user_id": user_id, "name": "John Doe", "age": 30}
    query = request.args.get("query")
    if query:
        user["query"] = query
    return jsonify(user), 200


@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    data["id"] = str(uuid.uuid4())  # Simulate adding an ID
    return jsonify(data), 201


if __name__ == "__main__":
    app.run(debug=True)
