import React from 'react';
import { Link } from 'react-router-dom';
import logo from '../logo.png';

const Header: React.FC = () => {
  return (
    <header className="header">
      <div className="logo-container">
        <img src={logo} alt="AtlantaFoodFinder" className="logo" />
        <h1>AtlantaFoodFinder</h1>
      </div>
      <div className="search-container">
        <input type="text" placeholder="Search for restaurants or cuisines..." />
        <button className="search-button">
          <i className="fa fa-search"></i>
        </button>
      </div>
      <nav>
        <Link to="/">Home</Link>
        <Link to="/cuisines">Cuisines</Link>
        <Link to="/login">Login</Link>
        <Link to="/signup" className="sign-up">Sign Up</Link>
      </nav>
    </header>
  );
};

export default Header;