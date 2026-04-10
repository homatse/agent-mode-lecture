import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
          <div className="container-fluid">
            <Link className="navbar-brand" to="/">Octofit Tracker</Link>
            <div className="navbar-nav">
              <Link className="nav-link" to="/activities">Activities</Link>
              <Link className="nav-link" to="/leaderboard">Leaderboard</Link>
              <Link className="nav-link" to="/teams">Teams</Link>
              <Link className="nav-link" to="/users">Users</Link>
              <Link className="nav-link" to="/workouts">Workouts</Link>
            </div>
          </div>
        </nav>
        <div className="container mt-4">
          <Routes>
            <Route path="/activities" element={<Activities />} />
            <Route path="/leaderboard" element={<Leaderboard />} />
            <Route path="/teams" element={<Teams />} />
            <Route path="/users" element={<Users />} />
            <Route path="/workouts" element={<Workouts />} />
            <Route path="/" element={
              <div className="text-center mt-5">
                <h1 className="display-4">Welcome to Octofit Tracker</h1>
                <p className="lead">Track your activities, join teams, and compete on the leaderboard!</p>
                <div className="mt-4">
                  <Link className="btn btn-primary me-2" to="/activities">View Activities</Link>
                  <Link className="btn btn-secondary" to="/leaderboard">View Leaderboard</Link>
                </div>
              </div>
            } />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
