import React from 'react';
import { Link } from 'react-router-dom';

interface RestaurantProps {
  restaurant: {
    id: string;
    name: string;
    cuisine: string;
    rating: number;
  };
}

function RestaurantCard({ restaurant }: RestaurantProps) {
  return (
    <Link to={`/restaurant/${restaurant.id}`} className="restaurant-card">
      <h3>{restaurant.name}</h3>
      <p>Cuisine: {restaurant.cuisine}</p>
      <p>Rating: {restaurant.rating}</p>
    </Link>
  );
}

export default RestaurantCard;