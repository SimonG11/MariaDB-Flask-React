import React, { useEffect, useState } from 'react';

const Dashboard = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch('http://localhost:5000/servertest') // Adjust the endpoint as needed
      .then(response => response.json())
      .then(data => setData(data))
      .catch(error => console.error("There was an error fetching the data:", error));
  }, []);

  return (
    <div>
      <h1>Dashboard</h1>
      {data ? (
        <div>
          {/* Render your data here */}
          <pre>{JSON.stringify(data, null, 2)}</pre>
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default Dashboard;
