import React, { useState } from 'react';
import axios from 'axios';
import './App.css'; // Ensure your CSS is imported

function App() {
  const [prompt, setPrompt] = useState('');
  const [response, setResponse] = useState('');

  const handleSubmit = async (e) => {

    //Stops the form from default submission
    e.preventDefault();

    try {
      const response = await axios.post('http://localhost:5000/advice', { prompt })

      console.log('Response Data:', response.data)
      setResponse(response.data.message)
    } catch (error) { console.error('Error:', error); }

    // try {
    //   const result = await axios.post('http://localhost:5000/advice', { prompt });
    //   setResponse(result.data.advice);
    // } catch (error) {
    //   console.error('Error generating text:', error);
    // }
  };

  const handleAuthClick = () => {
    // Redirect to Strava authentication URL
    window.location.href = 'https://www.strava.com/oauth/authorize?client_id=YOUR_CLIENT_ID&response_type=code&redirect_uri=YOUR_REDIRECT_URI&scope=read';
  };

  const handleChange = (e) => {
    setPrompt(e.target.value)
    console.log(prompt)
  }

  return (
    <div className="app-container">
      <div className="auth-container">
        <button className="auth-button" onClick={handleAuthClick}>
          Authenticate with Strava
        </button>
      </div>
      <div className="app-header">
        <h1>Generate Text and Authenticate with Strava</h1>
      </div>
      <div className="form-container">
        <form onSubmit={handleSubmit} className="form">
          <textarea
            className="input-prompt"
            value={prompt}
            onChange={handleChange}
            placeholder="Enter your prompt"
          />
          <button type="submit" className="submit-button">Generate</button>
        </form>
        <div className="response-container">
          <h3>Response:</h3>
          <p>{response}</p>
        </div>
      </div>
    </div>
  );
}

export default App;
