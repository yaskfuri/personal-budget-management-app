import React, { useState, useEffect } from "react";
import axios from "axios";

function TransactionList({ onEdit }) {
  const [transactions, setTransactions] = useState([]);

  // Fetch transactions from the API
  useEffect(() => {
    axios.get("http://127.0.0.1:5000/transactions")
      .then((response) => {
        setTransactions(response.data);
      })
      .catch((error) => console.error("Error fetching transactions:", error));
  }, []);

  // Delete a transaction
  const handleDelete = (id) => {
    axios.delete(`http://127.0.0.1:5000/transactions/${id}`)
      .then(() => {
        // Remove the deleted transaction from the list
        setTransactions(transactions.filter(tx => tx.id !== id));
      })
      .catch((error) => console.error("Error deleting transaction:", error));
  };

  return (
    <div>
      <h2>Transactions</h2>
      <ul>
        {transactions.map((tx) => (
          <li key={tx.id}>
            {tx.description}: ${tx.amount} ({tx.category}) on {tx.date}
            <button onClick={() => onEdit(tx)}>Edit</button>
            <button onClick={() => handleDelete(tx.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default TransactionList;
