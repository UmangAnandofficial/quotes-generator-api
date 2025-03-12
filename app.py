from flask import Flask, jsonify
import random
import json

app = Flask(__name__)

# Load quotes from JSON file
with open("quotes.json", "r") as file:
    quotes = json.load(file)

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Quote Generator API! Use /quote to get a random quote."

@app.route('/quote', methods=['GET'])
def get_quote():
    quote = random.choice(quotes)
    return jsonify(quote)

if __name__ == '__main__':
    app.run(debug=True)
