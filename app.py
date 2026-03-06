from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def chatbot_response(user_input):
    if "hello" in user_input.lower():
        return "Hello! How can I help you?"
    elif "your name" in user_input.lower():
        return "I am a Python AI chatbot."
    elif "bye" in user_input.lower():
        return "Goodbye! Have a nice day."
    else:
        return "Sorry, I did not understand."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    reply = chatbot_response(user_message)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)