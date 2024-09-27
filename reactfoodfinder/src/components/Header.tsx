import React from 'react';
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
        <a href="/">Home</a>
        <a href="/cuisines">Cuisines</a>
        <a href="/login">Login</a>
        <a href="/signup" className="sign-up">Sign Up</a>
      </nav>
    </header>
  );
};

export default Header;