import React, { useState } from 'react';
import SearchSection from './SearchSection';
import MapSection from './MapSection';
import RestaurantList from './RestaurantList';

function Home() {
  const [showRestaurants, setShowRestaurants] = useState(false);

  const handleFindFood = () => {
    setShowRestaurants(true);
  };

  return (
    <div className="home">
      <h1>Discover Atlanta's Best Eats</h1>
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