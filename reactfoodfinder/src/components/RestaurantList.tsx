import React, { useEffect, useState } from 'react';
import RestaurantCard from './RestaurantCard';

interface Restaurant {
  id: string;
  name: string;
  cuisine: string;
  rating: number;
}

function RestaurantList() {
  const [restaurants, setRestaurants] = useState<Restaurant[]>([]);

  useEffect(() => {
    // TODO: Fetch nearby restaurants from an API
    // For now, we'll use dummy data
    const dummyData: Restaurant[] = [
      { id: '1', name: "Joe's Pizza", cuisine: "Italian", rating: 4.5 },
      { id: '2', name: "Sushi Palace", cuisine: "Japanese", rating: 4.2 },
      { id: '3', name: "Taco Town", cuisine: "Mexican", rating: 4.0 },
    ];
    setRestaurants(dummyData);
  }, []);

  return (
    <div className="restaurant-list">
      <h2>Nearby Restaurants</h2>
      {restaurants.map(restaurant => (
        <RestaurantCard key={restaurant.id} restaurant={restaurant} />
      ))}
    </div>
  );
}

export default RestaurantList;