import React from 'react';
import './SearchSection.css'; // We'll create this file for custom styles

interface SearchSectionProps {
  onFindFood: () => void;
}

function SearchSection({ onFindFood }: SearchSectionProps) {
  return (
    <div className="search-section">
      <input
        type="text"
        placeholder="Search for restaurants or cuisines..."
        className="search-input"
      />
      <select className="cuisine-select">
        <option value="">All Cuisines</option>
        {/* Add more cuisine options here */}
      </select>
      <button onClick={onFindFood} className="find-food-button">
        Find Food!
      </button>
    </div>
  );
}

export default SearchSection;