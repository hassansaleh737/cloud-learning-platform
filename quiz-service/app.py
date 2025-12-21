from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/quiz/generate", methods=["POST"])
def generate_quiz():
    data = request.get_json()
    text = data.get("text") if data else None

    if not text:
        return jsonify({"error": "No text provided"}), 400

    return jsonify({
        "quiz": [
            {
                "question": "What is Docker?",
                "options": ["Virtual Machine", "Container", "Operating System"],
                "answer": "Container"
            },
            {
                "question": "What is a Microservice?",
                "options": ["Monolith", "Independent Service", "Database"],
                "answer": "Independent Service"
            }
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
