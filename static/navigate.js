var startFocused = false
var endFocused = false

if(document.getElementById("nav_map"))
{
    var map = L.map('nav_map').setView([0.3335662314797733, 32.56746934703034], 17);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    map.on('click', function(event){
        // Check if the clicked element is the startLocation input
        if(startFocused || endFocused) {
            const latitude = event.latlng.lat;
            const longitude = event.latlng.lng;

            // Use the geocoder to reverse geocode the coordinates
            const geocoder = L.Control.Geocoder.nominatim();
            geocoder.reverse(
                { lat: latitude, lng: longitude },
                map.options.crs.scale(map.getZoom()),
                (results) => {
                    if(results.length > 0) {
                        const address = results[0].name || results[0].properties.display_name;
                        // Update the startLocation input value with the address
                        if(startFocused) startLocation.value = address;
                        else if(endFocused) endLocation.value = address;
                    }
                    else
                    {
                        alert("No address found for the given coordinates");
                    }
                }
            );
        }
        startFocused = false
        endFocused = false
    });

    const startLocation = document.getElementById("start")
    const endLocation = document.getElementById("start")

    startLocation.addEventListener('focus', function() {
        startFocused = true
    });

    endLocation.addEventListener('focus', function() {
        endFocused = true
    });

    var routingControl = L.Routing.control({
        waypoints: [],
        routeWhileDragging: true
    }).addTo(map);

    var navigation_json = document.getElementById("navigation")

    if(navigation_json)
    {
        var navigation = JSON.parse(navigation_json.textContent)[0]
        // Set waypoints for the routing control
        routingControl.setWaypoints([
            L.latLng(navigation.source_latitude, navigation.source_longitude), // Start location coordinates
            L.latLng(navigation.destination_latitude, navigation.destination_longitude)      // End location coordinates
        ]);

        // Fit map bounds to show the entire route
        var bounds = L.latLngBounds([
            L.latLng(navigation.source_latitude, navigation.source_longitude),
            L.latLng(navigation.destination_latitude, navigation.destination_longitude) 
        ]);
        map.fitBounds(bounds);

        routingControl.on('routeselected', function(e) {
        var route = e.route;
        var distanceInKm = (route.summary.totalDistance / 1000).toFixed(2); // Convert meters to kilometers
        var walkingDuration = Math.round(route.summary.totalTime / 60); // Convert seconds to minutes

        // Update the output div
        document.getElementById("output").style.display = "block";
        document.getElementById("from").innerHTML = navigation.source;
        document.getElementById("to").innerHTML = navigation.destination;
        document.getElementById("distance").innerHTML = `${distanceInKm} km`;
        document.getElementById("duration").innerHTML = `${walkingDuration} min`;
        })
    }
}