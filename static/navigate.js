
if(document.getElementById("nav_map"))
{
    var map = L.map('nav_map').setView([0.3335662314797733, 32.56746934703034], 17);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    var routingControl = L.Routing.control({
        waypoints: [],
        routeWhileDragging: true
    }).addTo(map);

    var navigation = JSON.parse(document.getElementById("navigation").textContent)[0]
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