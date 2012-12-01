#!/usr/bin/python

import simplekml, pickle
from googlemaps import GoogleMaps

# Replace for your own key
# https://developers.google.com/maps/documentation/javascript/tutorial#api_key
gmaps = GoogleMaps('AIzaSyAmEvPWMafJFafvXGR-ampYOLQVSWmP5xM')

kml = simplekml.Kml()

# read python dict back from the file
pkl_file = open('tweet_user_data.pkl', 'rb')
users = pickle.load(pkl_file)
pkl_file.close()

for user, attributes in users.items():
    try:
        pnt = kml.newpoint()
        pnt.name = attributes['name']
        pnt.description = attributes['description']
        address = attributes['location']
        pnt.coords = [gmaps.address_to_latlng(address)]
    except:
        pass

# Save the KML
kml.save("gangnam.kml")
