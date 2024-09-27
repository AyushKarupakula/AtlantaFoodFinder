let map;
let markers = [];

function initMap() {
    if (typeof google === 'undefined') {
        setTimeout(initMap, 100);
        return;
    }

    map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: 33.7490, lng: -84.3880 }, // Atlanta coordinates
        zoom: 12,
    });

    // Fetch restaurants data from the server
    fetch('/api/restaurants/')
        .then(response => response.json())
        .then(restaurants => {
            restaurants.forEach(restaurant => {
                addMarker(restaurant);
            });
            new MarkerClusterer(map, markers, {
                imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'
            });
        });
}

function addMarker(restaurant) {
    if (!restaurant.latitude || !restaurant.longitude) return;

    const marker = new google.maps.Marker({
        position: { lat: restaurant.latitude, lng: restaurant.longitude },
        map: map,
        title: restaurant.name,
    });

    const infoWindow = new google.maps.InfoWindow({
        content: `
            <div class="info-window">
                <h3>${restaurant.name}</h3>
                <p>${restaurant.cuisine}</p>
                <p>Rating: ${restaurant.rating}/5</p>
                <a href="/restaurant/${restaurant.id}">View Details</a>
            </div>
        `
    });

    marker.addListener("click", () => {
        infoWindow.open(map, marker);
    });

    markers.push(marker);
}

// This will be called by the Google Maps API once it's loaded
window.initMap = initMap;