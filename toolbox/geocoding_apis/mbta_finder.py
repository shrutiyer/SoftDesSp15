""" @author: siyer """

"""
Geocoding and Web APIs Project Toolbox exercise

Find the MBTA stops closest to a given location.

Full instructions are at:
https://sites.google.com/site/sd15spring/home/project-toolbox/geocoding-and-web-apis
"""

import urllib   # urlencode function
import urllib2  # urlopen function (better than urllib version)
import json
from pprint import pprint

# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json?address="
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"
#The three important parts of the url
MTBA_FULL_URL_1 = "http://realtime.mbta.com/developer/api/v2/stopsbylocation?api_key=wX9NwuHnZU2ToO7GmGR9uw&lat=" #Divided the url into three parts
MTBA_FULL_URL_2 = "&lon="
MTBA_FULL_URL_3 = "&format=json"

# A little bit of scaffolding if you want to use it

def get_json(BASE_URL):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib2.urlopen(BASE_URL)
    response_text = f.read()
    response_data = json.loads(response_text) #The ouputs are separated into latitude and longitude
    pretty_json_lat = response_data["results"][0]["geometry"]["location"]['lat']
    pretty_json_lng = response_data["results"][0]["geometry"]["location"]['lng']
    return pretty_json_lat, pretty_json_lng

def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.

    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """
    place_name_list = place_name.split() 
    blank_space = '%20' #This adds %20 after each word.
    url_addition = ''
    for items in place_name_list:
        url_addition = url_addition + items + blank_space #Adds the place to the url
    total_url = GMAPS_BASE_URL + url_addition
    return get_json(total_url)
    
def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.

    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """
    mtba_url = MTBA_FULL_URL_1 + str(latitude) + MTBA_FULL_URL_2 + str(longitude) + MTBA_FULL_URL_3 #converted to str because the output was a float
    f = urllib2.urlopen(mtba_url)
    response_text_mtba = f.read()
    response_data_mtba = json.loads(response_text_mtba)
    station_name = response_data_mtba["stop"][0]["stop_name"]
    distance = response_data_mtba["stop"][0]["distance"]
    return station_name, distance

def find_stop_near(place_name):
    """
    Given a place name or address, print the nearest MBTA stop and the 
    distance from the given place to that stop.
    """
    lata = get_lat_long(place_name)[0]
    longi = get_lat_long(place_name)[1]
    return get_nearest_station(lata,longi)

#print find_stop_near('Fenway Park')
#output is (u'Brookline Ave opp Yawkey Way', u'0.0881209298968315')

if __name__ == '__main__':
    mbta_finder = find_stop_near('Fenway Park')
    print mbta_finder