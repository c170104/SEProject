var map;

function initMap(latLng) {
    map = new google.maps.Map(document.getElementById('map'), {
        center: latLng,
        zoom: 18
    });
    var marker = new google.maps.Marker({
        position: latLng,
        map: map
    });
}

function getLatLng(address) {
    var geocoder_url = "https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyCZYP8lJtnTmatEBazCSE3Tf10KmfnvcBw&address=" + address; 
    var xhttp = new XMLHttpRequest();
    xhttp.open("GET", encodeURI(geocoder_url), false);
    xhttp.send();
    var response = JSON.parse(xhttp.responseText);
    // console.log(response)
    return response['results']['0']['geometry']['location'];
}

window.onload = function()  {
    var address = document.getElementById('address').innerHTML + this.document.getElementById('postal_code');
    var latLng;
    latLng = (getLatLng(address));
    initMap(latLng);
}