from flask import Flask, render_template, request
import json
from scripts.language_modeling import get_stmt

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/get", methods=["GET", "POST"])
def get_response():
    user_input = request.form.get('msg')
    print(f"Sentence: {user_input}")
    og_sent, pred_sent = get_stmt(user_input)
    print(f"Original Sentence: {og_sent}\n Predicted Sentence: {pred_sent}")
    return str(pred_sent)


@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)