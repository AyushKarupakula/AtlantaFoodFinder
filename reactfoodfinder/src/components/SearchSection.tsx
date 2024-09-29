import React, { useState } from 'react';
import './SearchSection.css';

const cuisineOptions = [
  'All Cuisines',
  'American',
  'Italian',
  'Chinese',
  'Japanese',
  'Mexican',
  'Indian',
  'Thai',
  'Mediterranean',
  'French',
  'Greek',
  'Korean',
  'Vietnamese',
  'Spanish',
  'Middle Eastern',
  'Caribbean'
];

function SearchSection() {
  const [selectedCuisine, setSelectedCuisine] = useState('All Cuisines');
  const [searchQuery, setSearchQuery] = useState('');

  const handleCuisineChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    setSelectedCuisine(event.target.value);
  };

  const handleSearchChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setSearchQuery(event.target.value);
  };

  return (
    <div className="search-section">
      <div className="search-container">
        <input
          type="text"
          value={searchQuery}
          onChange={handleSearchChange}
          placeholder="Search for restaurants..."
          className="search-input"
        />
        <select 
          value={selectedCuisine} 
          onChange={handleCuisineChange}
          className="cuisine-dropdown"
        >
          {cuisineOptions.map((cuisine) => (
            <option key={cuisine} value={cuisine}>{cuisine}</option>
          ))}
        </select>
      </div>
    </div>
  );
}

export default SearchSection;