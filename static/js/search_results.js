document.addEventListener('DOMContentLoaded', function() {
    // Initialize Google Map
    function initMap() {
        const atlanta = { lat: 33.7490, lng: -84.3880 };
        const map = new google.maps.Map(document.getElementById("results-map"), {
            zoom: 12,
            center: atlanta,
        });

        // Add markers for search results (you'll need to pass this data from the backend)
        // searchResults.forEach(restaurant => {
        //     new google.maps.Marker({
        //         position: { lat: restaurant.lat, lng: restaurant.lng },
        //         map: map,
        //         title: restaurant.name
        //     });
        // });
    }

    // Call initMap when the Google Maps API is loaded
    window.initMap = initMap;
});