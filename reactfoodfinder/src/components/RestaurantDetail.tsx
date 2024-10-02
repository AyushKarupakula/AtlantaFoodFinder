import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { GoogleMap, LoadScript, Marker } from '@react-google-maps/api';
import './RestaurantDetail.css';

interface Restaurant {
  id: number;
  name: string;
  cuisine: string;
  rating: number;
  address: string;
  phone: string;
  reviews: string[];
  lat: number;
  lng: number;
}

const RestaurantDetail: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const [restaurant, setRestaurant] = useState<Restaurant | null>(null);
  const [isFavorite, setIsFavorite] = useState<boolean>(false); // New state for favorite status

  useEffect(() => {
    // In a real application, you would fetch the restaurant data from an API
    // For this example, we'll use mock data
    const mockRestaurant: Restaurant = {
      id: 1,
      name: "Joe's Pizza",
      cuisine: "Italian",
      rating: 4.5,
      address: "123 Peachtree St, Atlanta, GA 30303",
      phone: "(404) 555-1234",
      reviews: ["Great pizza!", "Friendly staff", "Will come again"],
      lat: 33.7490, // Example latitude for Atlanta
      lng: -84.3880, // Example longitude for Atlanta
    };
    setRestaurant(mockRestaurant);
  }, [id]);

  const handleFavoriteClick = () => {
    setIsFavorite(!isFavorite);
  };

  if (!restaurant) {
    return <div>Loading...</div>;
  }

  const mapContainerStyle = {
    width: '100%',
    height: '400px'
  };

  const center = {
    lat: restaurant.lat,
    lng: restaurant.lng
  };

  return (
    <div className="restaurant-detail">
      <h1>{restaurant.name}</h1>
      <div className="restaurant-info">
        <p><strong>Cuisine:</strong> {restaurant.cuisine}</p>
        <p><strong>Rating:</strong> {restaurant.rating}</p>
        <p><strong>Address:</strong> {restaurant.address}</p>
        <p><strong>Phone:</strong> {restaurant.phone}</p>
      </div>
      <button className="favorite-button" onClick={handleFavoriteClick}>
        {isFavorite ? 'Remove from Favorites' : 'Add to Favorites'}
      </button>
      <div className="reviews">
        <h2>Reviews</h2>
        <ul>
          {restaurant.reviews.map((review, index) => (
            <li key={index}>{review}</li>
          ))}
        </ul>
      </div>
      <div className="map-container">
        <LoadScript googleMapsApiKey="AIzaSyBLZxDKEynXZdwnrfwiLvi6UjkOew7i8-Y">
          <GoogleMap
            mapContainerStyle={mapContainerStyle}
            center={center}
            zoom={14}
          >
            <Marker position={center} />
          </GoogleMap>
        </LoadScript>
      </div>
    </div>
  );
};

export default RestaurantDetail;