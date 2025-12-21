from flask import Flask, request, jsonify
import logging
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

JWT_SECRET = "jwt-demo-secret"   
JWT_ALGORITHM = "HS256"
JWT_EXP_SECONDS = 3600

logging.basicConfig(level=logging.DEBUG)

# JWT Middleware

def jwt_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({"error": "Missing or invalid Authorization header"}), 401

        token = auth_header.split(" ")[1]

        try:
            decoded = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            request.user = decoded["sub"]
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 401

        return f(*args, **kwargs)
    return decorated

# Login Endpoint (JWT Issue)
@app.route("/login", methods=["POST"])
def login():
    data = request.json

    if not data:
        return jsonify({"error": "Missing request body"}), 400

    username = data.get("username")
    password = data.get("password")

    # Demo authentication (replace later with DB/Auth service)
    if username == "admin" and password == "Yousef,110098":
        payload = {
            "sub": username,
            "iat": datetime.datetime.utcnow(),
            "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=JWT_EXP_SECONDS)
        }

        token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return jsonify({"token": token})

    return jsonify({"error": "Unauthorized"}), 401


# Protected Chat Endpoint

@app.route('/api/chat/message', methods=['POST'])
@jwt_required
def handle_message():
    try:
        message = request.json.get('message')

        if not message:
            app.logger.error("No message provided")
            return jsonify({"error": "No message provided"}), 400

        app.logger.debug(f"Received message from {request.user}: {message}")

        return jsonify({
            "user": request.user,
            "response": f"Message received: {message}"
        })

    except Exception as e:
        app.logger.error(f"Error: {str(e)}")
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
