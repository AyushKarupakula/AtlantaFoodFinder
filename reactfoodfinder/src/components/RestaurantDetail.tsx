import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

interface RestaurantDetails {
  id: string;
  name: string;
  cuisine: string;
  rating: number;
  address: string;
  phone: string;
  reviews: string[];
}

function RestaurantDetail() {
  const { id } = useParams<{ id: string }>();
  const [restaurant, setRestaurant] = useState<RestaurantDetails | null>(null);

  useEffect(() => {
    // TODO: Fetch restaurant details from an API
    // For now, we'll use dummy data
    const dummyData: RestaurantDetails = {
      id: id || '',
      name: "Joe's Pizza",
      cuisine: "Italian",
      rating: 4.5,
      address: "123 Peachtree St, Atlanta, GA 30303",
      phone: "(404) 555-1234",
      reviews: ["Great pizza!", "Friendly staff", "Will come again"]
    };
    setRestaurant(dummyData);
  }, [id]);

  if (!restaurant) return <div>Loading...</div>;

  return (
    <div className="restaurant-detail">
      <h2>{restaurant.name}</h2>
      <p>Cuisine: {restaurant.cuisine}</p>
      <p>Rating: {restaurant.rating}</p>
      <p>Address: {restaurant.address}</p>
      <p>Phone: {restaurant.phone}</p>
      <h3>Reviews</h3>
      <ul>
        {restaurant.reviews.map((review, index) => (
          <li key={index}>{review}</li>
        ))}
      </ul>
      <div className="map">
        {/* TODO: Implement Google Maps integration */}
        <p>Google Maps will be displayed here</p>
      </div>
    </div>
  );
}

export default RestaurantDetail;