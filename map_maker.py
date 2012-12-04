#!/usr/bin/python

import simplekml, csv
from googlemaps import GoogleMaps

def utf_8_encoder(unicode_csv_data):
    for line in unicode_csv_data:
        yield line.encode('utf-8')

def unicode_csv_reader(unicode_csv_data, dialect=csv.excel, **kwargs):
    # csv.py doesn't do Unicode; encode temporarily as UTF-8:
    csv_reader = csv.reader(utf_8_encoder(unicode_csv_data), dialect=dialect, **kwargs)
    for row in csv_reader:
        # decode UTF-8 back to Unicode, cell by cell:
        yield [unicode(cell, 'utf-8') for cell in row]

# Replace for your own key
# https://developers.google.com/maps/documentation/javascript/tutorial#api_key
gmaps = GoogleMaps('AIzaSyAmEvPWMafJFafvXGR-ampYOLQVSWmP5xM')

kml = simplekml.Kml()

# CSV format
# username, tweet, location, profile pic, timestamp, number of tweets, number of followers, numbers of following

with open('demo.csv', 'rb') as csvfile:
    twitter_reader = unicode_csv_reader(csvfile)
    for row in twitter_reader:
        pnt = kml.newpoint()
        pnt.style.iconstyle.icon.href = "http://localhost:8000/gangnam-style.svg"
        pnt.style.iconstyle.scale = 3
        pnt.style.balloonstyle.text = row[1]
        pnt.style.labelstyle.scale = 2  # Make the text twice as big
        pnt.name = row[0]
        pnt.description = row[1]
        address = row[2]
        lat, lng = gmaps.address_to_latlng(address)
        pnt.coords = [(lng, lat)]
        pnt.timestamp.when= row[4]

# Save the KML
kml.save("gangnam.kml")
