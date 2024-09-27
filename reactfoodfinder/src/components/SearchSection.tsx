import React from 'react';

interface SearchSectionProps {
  onFindFood: () => void;
}

function SearchSection({ onFindFood }: SearchSectionProps) {
  return (
    <div className="search-section">
      <input type="text" placeholder="Search for restaurants or cuisines..." />
      <select>
        <option value="">All Cuisines</option>
        {/* Add more cuisine options here */}
      </select>
      <button onClick={onFindFood}>Find Food!</button>
    </div>
  );
}

export default SearchSection;