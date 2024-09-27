import React, { useState } from 'react';
import { GoogleMap, LoadScript, Marker } from '@react-google-maps/api';

const mapContainerStyle = {
  width: '100%',
  height: '400px'
};

const center = {
  lat: 33.7490, // Atlanta's latitude
  lng: -84.3880 // Atlanta's longitude
};

interface Restaurant {
  id: number;
  name: string;
  rating: number;
}

const Home: React.FC = () => {
  const [nearbyRestaurants, setNearbyRestaurants] = useState<Restaurant[]>([]);

  const handleFindFood = () => {
    // Simulating fetching nearby restaurants
    const restaurants: Restaurant[] = [
      { id: 1, name: "Pizza Place", rating: 4.5 },
      { id: 2, name: "Burger Joint", rating: 4.2 },
      { id: 3, name: "Sushi Bar", rating: 4.8 },
      { id: 4, name: "Taco Stand", rating: 4.0 },
      { id: 5, name: "Chinese Restaurant", rating: 4.3 },
    ];
    setNearbyRestaurants(restaurants);
  };

  const cuisines = [
    "All Cuisines", "American", "Italian", "Chinese", "Japanese", "Mexican",
    "Indian", "Thai", "Mediterranean", "French", "Greek", "Vietnamese",
    "Korean", "Spanish", "Middle Eastern", "Brazilian", "African",
    "Caribbean", "German", "Turkish"
  ];

  return (
    <>
      <h2>Discover Atlanta's Best Eats</h2>
      <div className="search-bar">
        <input type="text" placeholder="Search for restaurants or..." />
        <select>
          {cuisines.map((cuisine, index) => (
            <option key={index} value={cuisine.toLowerCase().replace(' ', '-')}>
              {cuisine}
            </option>
          ))}
        </select>
        <button>Find Food!</button>
      </div>
      <h3>Explore Restaurants in Atlanta</h3>
      <div className="map-controls">
        <span>Find Restaurants Near Me</span>
        <select>
          <option>All Ratings</option>
        </select>
      </div>
      <div className="map-container">
        <LoadScript googleMapsApiKey="AIzaSyBLZxDKEynXZdwnrfwiLvi6UjkOew7i8-Y">
          <GoogleMap
            mapContainerStyle={mapContainerStyle}
            center={center}
            zoom={10}
          >
            <Marker position={center} />
          </GoogleMap>
        </LoadScript>
      </div>
      <h3>Nearby Restaurants</h3>
      <button onClick={handleFindFood}>Find Food!</button>
      {nearbyRestaurants.length > 0 && (
        <div>
          <ul>
            {nearbyRestaurants.map((restaurant) => (
              <li key={restaurant.id}>
                {restaurant.name} - Rating: {restaurant.rating}
              </li>
            ))}
          </ul>
        </div>
      )}
    </>
  );
};

export default Home;