import React from 'react';
import RestaurantList from './RestaurantList';
import './ResultsPage.css';

function ResultsPage() {
  return (
    <div className="results-page">
      <div className="results-header">
        <h1>Discover Atlanta's Culinary Gems</h1>
        <p>Explore the vibrant food scene of the city</p>
      </div>
      <div className="results-container">
        <aside className="filters">
          <h2>Refine Your Search</h2>
          <div className="filter-group">
            <h3>Cuisine</h3>
            <div className="checkbox-group">
              <label><input type="checkbox" /> American</label>
              <label><input type="checkbox" /> Italian</label>
              <label><input type="checkbox" /> Asian</label>
              <label><input type="checkbox" /> Mexican</label>
            </div>
          </div>
          <div className="filter-group">
            <h3>Price Range</h3>
            <div className="price-range">
              <button>$</button>
              <button>$$</button>
              <button>$$$</button>
              <button>$$$$</button>
            </div>
          </div>
          <div className="filter-group">
            <h3>Rating</h3>
            <input type="range" min="1" max="5" step="0.5" />
          </div>
          <button className="apply-filters">Apply Filters</button>
        </aside>
        <div className="restaurant-list-container">
          <div className="sort-options">
            <span>Sort by:</span>
            <select>
              <option>Relevance</option>
              <option>Rating</option>
              <option>Distance</option>
            </select>
          </div>
          <RestaurantList />
        </div>
      </div>
    </div>
  );
}

export default ResultsPage;