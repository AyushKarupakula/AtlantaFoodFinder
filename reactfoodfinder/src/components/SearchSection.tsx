import React from 'react';

const SearchSection: React.FC = () => {
  return (
    <section className="search-section">
      <h2>Discover Atlanta's Best Eats</h2>
      <div className="search-bar">
        <input type="text" placeholder="Search for restaurants or..." className="search-input" />
        <select className="cuisine-select">
          <option value="all">All Cuisines</option>
          {/* Add more cuisine options here */}
        </select>
        <button className="find-food-button">Find Food!</button>
      </div>
    </section>
  );
};

export default SearchSection;