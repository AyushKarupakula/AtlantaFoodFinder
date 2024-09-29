"use client";

import { useLoadScript, GoogleMap } from '@react-google-maps/api';
import { useMemo } from 'react';
// ... existing imports ...

export default function Home() {
  // ... existing code ...

  const { isLoaded } = useLoadScript({
    googleMapsApiKey: "AIzaSyBLZxDKEynXZdwnrfwiLvi6UjkOew7i8-Y",
  });

  const center = useMemo(() => ({ lat: 44, lng: -80 }), []);

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      {/* ... existing code ... */}
      
      <div className="mb-32 grid text-center lg:max-w-5xl lg:w-full lg:mb-0 lg:grid-cols-4 lg:text-left">
        {/* ... existing code ... */}
        
        <a
          href="https://nextjs.org/learn?utm_source=create-next-app&utm_medium=appdir-template-tw&utm_campaign=create-next-app"
          className="group rounded-lg border border-transparent px-5 py-4 transition-colors hover:border-gray-300 hover:bg-gray-100 hover:dark:border-neutral-700 hover:dark:bg-neutral-800/30"
          target="_blank"
          rel="noopener noreferrer"
        >
          <h2 className={`mb-3 text-2xl font-semibold`}>
            Google Maps Integration{' '}
            <span className="inline-block transition-transform group-hover:translate-x-1 motion-reduce:transform-none">
              -&gt;
            </span>
          </h2>
          <p className={`m-0 max-w-[30ch] text-sm opacity-50`}>
            {!isLoaded ? (
              "Loading Google Maps..."
            ) : (
              <GoogleMap
                mapContainerClassName="w-full h-[200px]"
                center={center}
                zoom={10}
              />
            )}
          </p>
        </a>
      </div>
    </main>
  );
}