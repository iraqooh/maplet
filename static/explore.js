

var map = L.map('map').setView([0.333566, 32.567469], 17);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

const fav_element = document.getElementById("favorites_json")
if(fav_element)
{
    let favs = JSON.parse(fav_element.textContent);
    favs.forEach(favorite => {
        L.marker([favorite.latitude, favorite.longitude]).addTo(map)
        .bindPopup(`<div class="modal fixed inset-0 flex items-center justify-center z-50">
                    <div class="absolute inset-0 bg-gray-900 opacity-50"></div>

                    <!-- Modal Content -->
                    <div class="bg-white p-4 rounded-lg shadow-lg z-10 w-96">
                        <!-- Image Section -->
                        <div class="mb-4">
                            <img src=${favorite.image} alt="Image" class="w-full h-auto rounded-lg">
                        </div>

                        <!-- Title Section -->
                        <h2 class="text-2xl font-semibold mb-2">${favorite.name}</h2>

                        <!-- Close Button -->
                        <button class="mt-4 px-4 py-2 bg-gray-700 text-white rounded-lg hover:bg-gray-800" id="closeButton">Close</button>
                        </div>
                    </div>`
        );
    });
}

map.on('click', (event) => {

    L.marker([event.latlng.lat, event.latlng.lng]).addTo(map)
        .bindPopup(`<p>Lat: ${event.latlng.lat.toFixed(3)}, Lng: ${event.latlng.lng.toFixed(3)}</p>`)
        .openPopup();
});

const close = document.getElementById('closeButton')
if(close)
{
    close.addEventListener('click', function() {
        document.querySelector('.modal').style.display = 'none';
    });
}