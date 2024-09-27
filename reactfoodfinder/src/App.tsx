import React from 'react';
import { GoogleMap, LoadScript, Marker } from '@react-google-maps/api';
import Header from './components/Header';
import './App.css';

const mapContainerStyle = {
  width: '100%',
  height: '400px'
};

const center = {
  lat: 33.7490, // Atlanta's latitude
  lng: -84.3880 // Atlanta's longitude
};

function App() {
  return (
    <div className="App">
      <Header />
      <main className="main-content">
        <h2>Discover Atlanta's Best Eats</h2>
        <div className="search-bar">
          <input type="text" placeholder="Search for restaurants or..." />
          <select>
            <option>All Cuisines</option>
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
        {/* Add nearby restaurants list here */}
      </main>
      <footer>
        <p>© 2023 AtlantaFoodFinder. All rights reserved.</p>
      </footer>
    </div>
  );
}

export default App;
