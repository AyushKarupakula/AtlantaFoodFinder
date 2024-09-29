import React, { useState } from 'react';
import SearchSection from './SearchSection';
import MapSection from './MapSection';
import RestaurantList from './RestaurantList';
import './Home.css';

function Home() {
  const [showRestaurants, setShowRestaurants] = useState(false);

  const handleFindFood = () => {
    setShowRestaurants(true);
  };

  return (
    <div className="home">
      <div className="title-container">
        <h1 className="title">Discover Atlanta's Best Eats</h1>
      </div>
      <SearchSection onFindFood={handleFindFood} />
      {showRestaurants ? (
        <RestaurantList />
      ) : (
        <>
          <MapSection />
          <h2>Nearby Restaurants</h2>
        </>
      )}
    </div>
  );
}

export default Home;