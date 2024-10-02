function initMap() {
    const atlanta = { lat: 33.7490, lng: -84.3880 };
    const map = new google.maps.Map(document.getElementById('map'), {
        zoom: 12,
        center: atlanta,
    });
    fetch('/api/restaurants/')
    .then(response => response.json())
    .then(data => {
        data.forEach(restaurant => {
            // Create a marker for each restaurant
            const marker = new google.maps.Marker({
                position: { lat: restaurant.latitude, lng: restaurant.longitude },
                map: map,
                title: restaurant.name,
            });

            // Optional: Add InfoWindow
            const infoWindow = new google.maps.InfoWindow({
                content: `<h3>${restaurant.name}</h3><p>${restaurant.address}</p>`,
            });

            // Add click listener to open InfoWindow
            marker.addListener('click', () => {
                infoWindow.open(map, marker);
            });
        });
    })
    .catch(error => console.error('Error fetching restaurant data:', error));

    const restaurants = document.querySelectorAll('.restaurant-card');
    const bounds = new google.maps.LatLngBounds();

    restaurants.forEach(restaurant => {
        const lat = parseFloat(restaurant.dataset.lat);
        const lng = parseFloat(restaurant.dataset.lng);
        const name = restaurant.querySelector('h3').textContent;

        if (!isNaN(lat) && !isNaN(lng)) {
            const position = new google.maps.LatLng(lat, lng);
            const marker = new google.maps.Marker({
                position: position,
                map: map,
                title: name
            });

            bounds.extend(position);

            const infoWindow = new google.maps.InfoWindow({
                content: `
                    <h3>${name}</h3>
                    <p>${restaurant.querySelector('p:nth-of-type(1)').textContent}</p>
                    <p>${restaurant.querySelector('p:nth-of-type(2)').textContent}</p>
                    <a href="${restaurant.querySelector('.btn-view').href}">View Details</a>
                `
            });

            marker.addListener('click', () => {
                infoWindow.open(map, marker);
            });
        }
    });

    if (!bounds.isEmpty()) {
        map.fitBounds(bounds);
    }
}

// Make sure initMap is globally accessible
window.initMap = initMap;