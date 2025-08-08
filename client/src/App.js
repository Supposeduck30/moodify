import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await axios.get('/api/data');
      setData(response.data);
      setLoading(false);
    } catch (error) {
      console.error('Error fetching data:', error);
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Kiro Hackathon</h1>
        {loading ? (
          <p>Loading...</p>
        ) : (
          <div>
            <p>{data?.message}</p>
            <p>Server timestamp: {data?.timestamp}</p>
          </div>
        )}
        <button onClick={fetchData}>Refresh Data</button>
      </header>
    </div>
  );
}

export default App;