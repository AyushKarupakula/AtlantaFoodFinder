import React from 'react';

const NearbyRestaurants: React.FC = () => {
  const cuisines = [
    "All Cuisines",
    "American",
    "Italian",
    "Chinese",
    "Japanese",
    "Mexican",
    "Indian",
    "Thai",
    "Mediterranean",
    "French",
    "Greek",
    "Vietnamese",
    "Korean",
    "Spanish",
    "Middle Eastern"
  ];

  return (
    <div className="nearby-restaurants">
      <h3>Nearby Restaurants</h3>
      <div className="filters">
        <select>
          {cuisines.map((cuisine, index) => (
            <option key={index} value={cuisine.toLowerCase().replace(' ', '-')}>
              {cuisine}
            </option>
          ))}
        </select>
        <select>
          <option value="rating">Rating</option>
          <option value="distance">Distance</option>
        </select>
      </div>
      <button className="find-food-btn">Find Food!</button>
    </div>
  );
};

export default NearbyRestaurants;