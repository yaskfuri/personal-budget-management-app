import React, { useState } from "react";
import TransactionList from "./TransactionList";
import TransactionForm from "./TransactionForm";

function App() {
  const [selectedTransaction, setSelectedTransaction] = useState(null);

  // Handle form submission (refresh transaction list and reset selection)
  const handleFormSubmit = () => {
    setSelectedTransaction(null);
  };

  return (
    <div>
      <TransactionForm
        selectedTransaction={selectedTransaction}
        onFormSubmit={handleFormSubmit}
      />
      <TransactionList onEdit={setSelectedTransaction} />
    </div>
  );
}

export default App;

