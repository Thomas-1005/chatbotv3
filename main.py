from flask import Flask, render_template, request
from chatbot import get_bot_response

app = Flask(__name__, static_folder="templates/static")

@app.route('/')
def index():
    return render_template('indextest.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['user_message']
    bot_response = get_bot_response(user_message)
    return bot_response

if __name__ == '__main__':
    app.run(debug=True)







