import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import SearchSection from './SearchSection';
import MapSection from './MapSection';
import './Home.css';

function Home() {
  const navigate = useNavigate();
  const [maxDistance, setMaxDistance] = useState(5); // Default 5 miles

  const handleFindFood = () => {
    navigate('/results');
  };

  const handleDistanceChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setMaxDistance(Number(event.target.value));
  };

  return (
    <div className="home">
      <div className="title-container">
        <h1 className="title">Discover Atlanta's Best Eats</h1>
      </div>
      <SearchSection />
      <div className="filter-card">
        <div className="filter-section">
          <h3>Maximum Distance: {maxDistance} miles</h3>
          <div className="slider-container">
            <input 
              type="range" 
              min="1" 
              max="50" 
              value={maxDistance}
              onChange={handleDistanceChange}
            />
          </div>
        </div>
        <button className="find-food-btn" onClick={handleFindFood}>Find Food!</button>
      </div>
      <MapSection />
    </div>
  );
}

export default Home;