var map;
var view;
var myLoc;

function init(){
  myLoc = ol.proj.fromLonLat([-84.196359, 34.028401]);
  view = new ol.View({
    center: myLoc,
    zoom: 4
  })

  map = new ol.Map({
       target: 'map',
       layers: [
         new ol.layer.Tile({
           source: new ol.source.OSM()
         })
       ],
       loadTilesWhileAnimating: true,
       view: view
     });
}

function panHome() {
  view.animate({
         center: myLoc,
         duration: 2000
       });
}

function panLocation(){
  var userInput = document.getElementById("Country-Name-Input").value;

if (userInput == ""){
  alert("Error! Please type a country name.");
  return;
}
var query = "http://restcountries.eu/rest/v2/name/" +userInput;
query = query.replace(/ /g, "%20" );

countryRequest = new XMLHttpRequest();
countryRequest.open('GET', query, true);
countryRequest.onload = processCountryRequest;
countryRequest.send();

}
function processCountryRequest(){
  console.log("Ready State " + countryRequest.readyState);
  console.log("Status " + countryRequest.status);
  console.log("Response " + countryRequest.responseText);

  if(countryRequest.readyState != 4){
    return;
  }
  else if(countryRequest.status != 200){
    return;
  }
  else if(countryRequest.responseText == ""){
    return;
  }
  var countryInfo = JSON.parse(countryRequest.responseText);
  var lon = countryInfo[0].latlng[1];
  var lat = countryInfo[0].latlng[0];
  view.animate({
    center: ol.proj.fromLonLat([lon,lat]),
    duration: 2000 //2 seconds
  });

}

window.onload = init;
