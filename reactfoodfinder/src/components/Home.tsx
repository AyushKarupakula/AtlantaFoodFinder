import React from 'react';
import { useNavigate } from 'react-router-dom';
import SearchSection from './SearchSection';
import MapSection from './MapSection';
import './Home.css';

function Home() {
  const navigate = useNavigate();

  const handleFindFood = () => {
    navigate('/results');
  };

  return (
    <div className="home">
      <div className="title-container">
        <h1 className="title">Discover Atlanta's Best Eats</h1>
      </div>
      <SearchSection onFindFood={handleFindFood} />
      <MapSection />
    </div>
  );
}

export default Home;