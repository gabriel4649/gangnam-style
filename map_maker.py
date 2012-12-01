import simplekml
from googlemaps import GoogleMaps

# Replace for your own key
# https://developers.google.com/maps/documentation/javascript/tutorial#api_key
gmaps = GoogleMaps('AIzaSyAmEvPWMafJFafvXGR-ampYOLQVSWmP5xM')

kml = simplekml.Kml()

address = 'Bangkok, Thailand'
coords = [gmaps.address_to_latlng(address)]
pnt = kml.newpoint(name=address, description="",
                   coords=coords)






# Save the KML
kml.save("T00 Point.kml")
