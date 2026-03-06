from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = "proj-RJ11Us6I_dC6FbyZ0Bvsi3OmqXXpHqBrY52QTOB-eO7fRKWN36syY39aCcAl6tzHWeUIpgYpu4T3BlbkFJOEakZffSu4QVG0XVrxdp_VrS67-CbWNyy2yDdzpF_-nup9TZAb5tUX0BttTiY1Qp4FrDttrOoA"

def chatbot_response(user_input):

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":user_input}]
    )

    return response.choices[0].message.content

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    reply = chatbot_response(user_message)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)