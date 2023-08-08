/*
var centered = {latitude: 0.333566, longitude: 32.567469}
var mapOptions = {
  center: centered,
  zoom: 17,
  mapTypeId: google.maps.MapTypeId.ROADMAP
}

var map = new google.maps.Map(
  document.getElementById("googleMap"),
  mapOptions
)

var directionsService = new google.maps.DirectionsService()
var directionsDisplay = new google.maps.DirectionsRenderer()
directionsDisplay.setMap(map)

function calculateRoute()
{
    var request = {
        origin: document.getElementById("source").ariaValueMax,
        dest: document.getElementById("dest").value,
        travelMode: google.maps.TravelMode.WALKING,
        unitSystem: google.maps.UnitSystem.IMPERIAL
    }

    directionsService.route(request, (result, status) => {
        if(status == google.maps.DirectionStatus.OK)
        {
            document.getElementById("output").style.display = 'block'
            document.querySelector("#from").innerHTML = document.getElementById("source").value
            document.querySelector("#to").innerHTML = document.getElementById("dest").value
            document.querySelector("#distance").innerHTML = result.routes[0].legs[0].distance.text
            document.querySelector("#duration").innerHTML = result.routes[0].legs[0].duration.text

            directionsDisplay.setDirections(result)
        }
        else
        {
            document.getElementById("error").style.display = 'block'
            directionsDisplay.setDirections({routes: []})
            map.setCenter(centered)
        }
    })
}

var options = {
    types: ['cities']
}

var input1 = document.getElementById("source")
var autocomplete1 = new google.maps.places.Autocomplete(input1, options)

var input2 = document.getElementById("dest")
var autocomplete2 = new google.maps.places.Autocomplete(input2, options)

*/