import React, { useState, useEffect } from "react";
import axios from "axios";

function TransactionForm({ selectedTransaction, onFormSubmit }) {
  const [formData, setFormData] = useState({
    description: "",
    amount: "",
    category: "",
    date: "",
  });

  // Update form data when a transaction is selected for editing
  useEffect(() => {
    if (selectedTransaction) {
      setFormData(selectedTransaction);
    } else {
      setFormData({ description: "", amount: "", category: "", date: "" });
    }
  }, [selectedTransaction]);

  // Handle form input changes
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  // Handle form submission
  const handleSubmit = (e) => {
    e.preventDefault();
    if (selectedTransaction) {
      // Update transaction
      axios.put(`http://127.0.0.1:5000/transactions/${selectedTransaction.id}`, formData)
        .then(() => {
          onFormSubmit();
        })
        .catch((error) => console.error("Error updating transaction:", error));
    } else {
      // Add new transaction
      axios.post("http://127.0.0.1:5000/transactions", formData)
        .then(() => {
          onFormSubmit();
        })
        .catch((error) => console.error("Error adding transaction:", error));
    }
  };

  // Handle category prediction
  const handleCategorize = () => {
    axios.post("http://127.0.0.1:5000/predict_category", { description: formData.description })
      .then((response) => {
        setFormData((prev) => ({ ...prev, category: response.data.predicted_category }));
      })
      .catch((error) => console.error("Error predicting category:", error));
  };

  const handleFeedbackSubmit = () => {
    axios.post("http://127.0.0.1:5000/feedback", {
      description: formData.description,
      correct_category: formData.category
    })
    .then(response => {
      alert("Thank you for your feedback!");
    })
    .catch(error => {
      console.error("Error submitting feedback:", error);
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>{selectedTransaction ? "Edit Transaction" : "Add Transaction"}</h2>
      <div>
        <label>Description:</label>
        <input
          type="text"
          name="description"
          value={formData.description}
          onChange={handleChange}
          required
        />
      </div>
      <div>
        <button type="button" onClick={handleCategorize}>
          Categorize
        </button>
      </div>
      <div>
        <label>Amount:</label>
        <input
          type="number"
          name="amount"
          value={formData.amount}
          onChange={handleChange}
          required
        />
      </div>
      <div>
        <label>Category:</label>
        <input
          type="text"
          name="category"
          value={formData.category}
          onChange={handleChange}
          required
        />
      </div>
      <div>
        <label>Date:</label>
        <input
          type="date"
          name="date"
          value={formData.date}
          onChange={handleChange}
          required
        />
      </div>
      <button type="submit">Save</button>
      <div>
        <button type="button" onClick={handleFeedbackSubmit}>
          Submit Feedback
        </button>
      </div>

    </form>
  );
}

export default TransactionForm;
