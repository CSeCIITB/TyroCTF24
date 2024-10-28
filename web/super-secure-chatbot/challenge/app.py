from flask import Flask, render_template, render_template_string, request

app = Flask(__name__)
app.static_folder = "static"


def chatbot_response(msg):
    if msg.lower() in ["hi", "hello"]:
        return "Welcome to SecureBot! Try asking me anything... 😄"
    return f"I'm not sure how to respond to \"{msg}\", but I'll try my best!"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    try:
        userText = request.args.get("msg")
        return render_template_string(chatbot_response(userText))
    except Exception as e:
        return f"Oops! Something went wrong: {str(e)}"
