from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
import pickle

# App + Flask API for react app with jsonify 

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"message": "hellow world!"})

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"message": "Hello from Flask!"}) # api for react app - returning the message from the backend to the front-end 

# Running flask 

if __name__ == '__main__':
    app.run(debug=True)


# Database connection with SQLite
def get_db_connection():
    conn = sqlite3.connect('personal_budget.db')
    conn.row_factory = sqlite3.Row  # Results as dictionaries
    return conn

# cursor = conn.cursor() # Cursor connection to fetch data from the results of queries

# Create a new transaction in the backend ----- applying API CRUD (create, read, update, delete)
@app.route('/transactions', methods=['POST'])
def add_transaction():
    data = request.json  # Get the JSON data from the request body
    
    description = data['description']
    amount = data['amount']
    category = data['category']
    date = data['date']
    user_id = data['user_id']
    
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO transactions (description, amount, category, date, user_id)
        VALUES (?, ?, ?, ?, ?)
    ''', (description, amount, category, date, user_id))

    conn.commit()
    conn.close()

    return jsonify({"message": "Transaction added successfully!"}), 201

# Showing all transactions from the table
@app.route('/transactions', methods=['GET'])
def get_transactions():
    conn = get_db_connection()
    transactions = conn.execute('SELECT * FROM transactions').fetchall()
    conn.close()

    return jsonify([dict(tx) for tx in transactions])

# Showing specific category from a table with GET method 
@app.route('/transactions/category/<category>', methods=['GET'])
def get_transactions_by_category(category):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM transactions WHERE category = ?', (category,))
    transactions = cursor.fetchall()

    conn.close()

    return jsonify([dict(tx) for tx in transactions])

# Updating existing transaction with method PUT / The PUT HTTP method creates a new resource or replaces a representation of the target resource with the request content 
@app.route('/transactions/<int:id>', methods=['PUT'])
def update_transaction(id):
    data = request.json 

    description = data.get('description')
    amount = data.get('amount')
    category = data.get('category')
    date = data.get('date')
    user_id = data.get('user_id')

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE transactions
        SET description = ?, amount = ?, category = ?, date = ?, user_id = ?
        WHERE id = ?
    ''', (description, amount, category, date, user_id, id))

    conn.commit()
    conn.close()

    return jsonify({"message": f"Transaction {id} updated successfully!"})

# Function to delete a transaction 
@app.route('/transactions/<int:id>', methods=['DELETE'])
def delete_transaction(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM transactions WHERE id = ?', (id,))
    conn.commit()
    conn.close()

    return jsonify({"message": f"Transaction {id} deleted successfully!"})

# Load the trained model for categorization
with open("expense_classifier.pkl", "rb") as f:
    model = pickle.load(f)

# Predict category for a given transaction description
@app.route('/predict_category', methods=['POST'])
def predict_category():
    data = request.json
    description = data['description']
    
    # Make prediction
    category = model.predict([description])[0]
    
    return jsonify({"description": description, "predicted_category": category})