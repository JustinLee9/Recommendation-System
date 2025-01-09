import './App.css';
import React, { useEffect } from 'react';
import axios from 'axios';

const App = () => {
  useEffect(() => {
    axios.get('http://127.0.0.1:5000/api/test')
    .then(response => console.log(response.data))
    .catch(error => console.log(error));
  }, []);

  return <div>Check the console!</div>;
};

export default App;
