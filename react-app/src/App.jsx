import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [data, setData] = useState("");

  useEffect(() => {
    // Fetch data from Flask API
    axios
      .get("/api/data")
      .then((response) => {
        setData(response.data.message);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, []);

  return <h1>{data}</h1>;
}



export default App;
