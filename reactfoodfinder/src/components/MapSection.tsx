import React from 'react';

const MapSection: React.FC = () => {
  return (
    <section className="map-section">
      <h3>Explore Restaurants in Atlanta</h3>
      <div className="map-controls">
        <span>Find Restaurants Near Me</span>
        <select>
          <option value="all">All Ratings</option>
          {/* Add more rating options here */}
        </select>
      </div>
      <div className="map-container">
        {/* Google Maps will be integrated here */}
        <p>Google Maps will be integrated here</p>
      </div>
    </section>
  );
};

export default MapSection;