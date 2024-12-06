from flask import Flask, jsonify 
from flask_cors import CORS
import sqlite3

# App + Flask API with jsonify 

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"message": "hellow world!"})

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"message": "Hello from Flask!"})

if __name__ == '__main__':
    app.run(debug=True)




# Database connection with SQLite

connection = sqlite3.connect('personal_budget.db') # Connection sqlite and connection object 

cursor_obj = connection.cursor() # Cursor connection to fetch data from the results of queries

