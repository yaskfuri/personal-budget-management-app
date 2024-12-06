from flask import Flask, jsonify 
from flask_cors import CORS
import sqlite3

# App + Flask API with jsonify 

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "hellow world!"})

if __name__ == '__main__':
    app.run(debug=True)

CORS(app)


# Database connection with SQLite

connection = sqlite3.connect('personal_budget.db') # Connection sqlite and connection object 

cursor_obj = connection.cursor() # Cursor connection to fetch data from the results of queries

