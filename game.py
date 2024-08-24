from flask import Flask, render_template, request, jsonify
from player import get_computer_choice
from rules.py import determine_winner

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/play', methods=['POST'])
def play():
    user_choice = request.json.get('choice')
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)

    return jsonify({
        'user_choice': user_choice,
        'computer_choice': computer_choice,
        'result': result
    })


if __name__ == '__main__':
    app.run(debug=True)
