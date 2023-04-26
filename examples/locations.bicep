
module myLocation 'br:bartvdbraak.azurecr.io/bicep/modules/locations:v1' = {
  name: 'myLocation'
  params: {
    location: 'francecentral'
  }
}

var geocode = myLocation.outputs.geoCode
