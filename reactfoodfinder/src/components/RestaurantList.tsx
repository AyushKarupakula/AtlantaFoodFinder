import React from 'react';
import { Link } from 'react-router-dom';
import './RestaurantList.css';

interface Restaurant {
  id: number;
  name: string;
  cuisine: string;
  rating: number;
  image: string;
  priceRange: string;
}

const restaurants: Restaurant[] = [
  { id: 1, name: "Joe's Pizza", cuisine: "Italian", rating: 4.5, image: "https://example.com/joes-pizza.jpg", priceRange: "$$" },
  { id: 2, name: "Sushi Palace", cuisine: "Japanese", rating: 4.2, image: "https://example.com/sushi-palace.jpg", priceRange: "$$$" },
  { id: 3, name: "Taco Town", cuisine: "Mexican", rating: 4.0, image: "https://example.com/taco-town.jpg", priceRange: "$" },
];

function RestaurantList() {
  return (
    <div className="restaurant-list">
      {restaurants.map((restaurant) => (
        <Link to={`/restaurant/${restaurant.id}`} key={restaurant.id} className="restaurant-card">
          <div className="restaurant-image" style={{ backgroundImage: `url(${restaurant.image})` }}>
            <span className="price-range">{restaurant.priceRange}</span>
          </div>
          <div className="restaurant-info">
            <h2>{restaurant.name}</h2>
            <p className="cuisine">{restaurant.cuisine}</p>
            <div className="rating">
              <span className="stars" style={{ '--rating': restaurant.rating } as React.CSSProperties}></span>
              <span className="rating-number">{restaurant.rating.toFixed(1)}</span>
            </div>
          </div>
        </Link>
      ))}
    </div>
  );
}

export default RestaurantList;