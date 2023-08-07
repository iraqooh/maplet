var map = L.map('nav_map').setView([0.3335662314797733, 32.56746934703034], 17);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

var routingControl = L.Routing.control({
    waypoints: [],
    routeWhileDragging: true
}).addTo(map);

// ... (previous code)

document.getElementById('calculateRoute').addEventListener('click', function() {
    document.getElementById("output").style.display = "block";
    const MAPBOX_ACCESS_TOKEN = 'pk.eyJ1IjoiaXJhcW9vaCIsImEiOiJjbGsyMmhoejkwYXdwM2ZwandiMXlpb24xIn0.CpRSRkl4IFH181kdkJGNOQ';
    var startLocation = document.getElementById('startLocation').value;
    var endLocation = document.getElementById('endLocation').value;
    document.getElementById("from").innerHTML = startLocation;
    document.getElementById("to").innerHTML = endLocation;
    let startCoordinates, endCoordinates;

    if (startLocation && endLocation) {
        // Geocode start and end locations using Mapbox Geocoding API
        const geocodingUrl = `https://api.mapbox.com/geocoding/v5/mapbox.places/${startLocation}.json?access_token=${MAPBOX_ACCESS_TOKEN}`;
        const geocodingUrl2 = `https://api.mapbox.com/geocoding/v5/mapbox.places/${endLocation}.json?access_token=${MAPBOX_ACCESS_TOKEN}`;
        
        fetch(geocodingUrl)
            .then(response => response.json())
            .then(data => {
                startCoordinates = data.features[0].geometry.coordinates;

                fetch(geocodingUrl2)
                    .then(response2 => response2.json())
                    .then(data2 => {
                        if (data2.features && data2.features.length > 0) {
                            endCoordinates = data2.features[0].geometry.coordinates;

                            // Set waypoints for the routing control
                            routingControl.setWaypoints([
                                L.latLng(startCoordinates[1], startCoordinates[0]), // Start location coordinates
                                L.latLng(endCoordinates[1], endCoordinates[0])      // End location coordinates
                            ]);

                            // Fit map bounds to show the entire route
                            var bounds = L.latLngBounds([
                                L.latLng(startCoordinates[1], startCoordinates[0]),
                                L.latLng(endCoordinates[1], endCoordinates[0])
                            ]);
                            map.fitBounds(bounds);

                            routingControl.on('routeselected', function(e) {
                            var route = e.route;
                            var distanceInKm = (route.summary.totalDistance / 1000).toFixed(2); // Convert meters to kilometers
                            var walkingDuration = Math.round(route.summary.totalTime / 60); // Convert seconds to minutes
                    
                            // Update the output div
                            document.getElementById("output").style.display = "block";
                            document.getElementById("from").innerHTML = startLocation;
                            document.getElementById("to").innerHTML = endLocation;
                            document.getElementById("distance").innerHTML = `${distanceInKm} km`;
                            document.getElementById("duration").innerHTML = `${walkingDuration} min`;
                            })
                        }
                        else
                        {
                            console.error('No features found for end location');
                            document.getElementById("error").style.display = "block";
                        }
                    })
                    .catch(error2 => console.error('Error fetching geocoding data:', error2));
            })
            .catch(error => console.error('Error fetching geocoding data:', error));
}})
