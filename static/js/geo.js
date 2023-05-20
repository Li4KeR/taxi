var x = document.getElementById("myGeo");
function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else {
    x.innerHTML = "Геолокация не поддерживается этим браузером.";
  }
}

function showPosition(position) {
  x.innerHTML = "Широта: " + position.coords.latitude +
  "<br>Долгота: " + position.coords.longitude;
}