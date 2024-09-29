import React from 'react';
import { useLoadScript, GoogleMap } from '@react-google-maps/api';

const MapSection: React.FC = () => {
  const { isLoaded } = useLoadScript({
    googleMapsApiKey: "AIzaSyBLZxDKEynXZdwnrfwiLvi6UjkOew7i8-Y",
  });

  const center = React.useMemo(() => ({ lat: 33.7490, lng: -84.3880 }), []); // Atlanta coordinates

  return (
    <div style={{ height: '400px', width: '100%' }}>
      {!isLoaded ? (
        <div>Loading Google Maps...</div>
      ) : (
        <GoogleMap
          mapContainerStyle={{ height: '100%', width: '100%' }}
          center={center}
          zoom={10}
        />
      )}
    </div>
  );
};

export default MapSection;