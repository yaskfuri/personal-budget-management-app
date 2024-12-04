from flask import Flask, jsonify, request
import sqlite3


app = Flask(__name__)

# Helper function to get database connection
def get_db_connection():
    conn = sqlite3.connect('personal_budget.db')
    conn.row_factory = sqlite3.Row  # Returns rows as dictionaries
    return conn

# Example route
@app.route('/transactions', methods=['GET'])
def get_transactions():
    conn = get_db_connection()
    transactions = conn.execute('SELECT * FROM transactions').fetchall()
    conn.close()
    return jsonify([dict(row) for row in transactions])

if __name__ == '__main__':
    app.run(debug=True)
