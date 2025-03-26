from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    return jsonify({"response": f"You said: {user_message}"})

if __name__ == "__main__":
    app.run(debug=True)

