from flask import Flask, jsonify, request
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


# Helper function for database connection
def get_db_connection():
    conn = sqlite3.connect('personal_budget.db')
    conn.row_factory = sqlite3.Row  # Results as dictionaries
    return conn

# Database connection with SQLite

# cursor_obj = conn.cursor() # Cursor connection to fetch data from the results of queries

@app.route('/transactions', methods=['POST'])
def add_transaction():
    data = request.json
    description = data.get('description')
    amount = data.get('amount')
    category = data.get('category')
    date = data.get('date')

    if not all([description, amount, category, date]):
        return jsonify({'error': 'Missing required fields'}), 400

    conn = get_db_connection()
    conn.execute(
        'INSERT INTO transactions (description, amount, category, date) VALUES (?, ?, ?, ?)',
        (description, amount, category, date)
    )
    conn.commit()
    conn.close()

    return jsonify({'message': 'Transaction added successfully'}), 201

@app.route('/transactions', methods=['GET'])
def get_transactions():
    conn = get_db_connection()
    transactions = conn.execute('SELECT * FROM transactions').fetchall()
    conn.close()

    return jsonify([dict(tx) for tx in transactions])



