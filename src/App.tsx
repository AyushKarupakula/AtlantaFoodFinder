import React from 'react';
import Header from './components/Header';
import SearchBar from './components/SearchBar';
import Map from './components/Map';

function App() {
  return (
    <div className="App">
      <Header />
      <main className="container mx-auto px-4">
        <h2 className="text-2xl font-bold my-4">Discover Atlanta's Best Eats</h2>
        <SearchBar />
        <h3 className="text-xl font-semibold my-4">Explore Restaurants in Atlanta</h3>
        <Map />
        <h3 className="text-xl font-semibold my-4">Nearby Restaurants</h3>
        {/* Add a list or grid of nearby restaurants here */}
      </main>
      <footer className="bg-gray-800 text-white text-center py-4 mt-8">
        © 2023 AtlantaFoodFinder. All rights reserved.
      </footer>
    </div>
  );
}

export default App;