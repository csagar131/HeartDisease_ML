#!/usr/bin/python3

# Import modules for CGI handling
import cgi, cgitb
import os
import googlemaps
import folium
import time

# Create instance of FieldStorage
form = cgi.FieldStorage()


city = form.getvalue('city')

os.system("python3 Maps.py "+city)
print("Content-type:text/html\r\n\r\n")
print('<script>window.location.href="http://13.126.204.181/my_map1.html";</script>')



#define our client
'''
api_key=""
gmaps = googlemaps.Client(api_key)




your_city = city.replace(' ','+')
current_location = gmaps.geocode(your_city)
time.sleep(3)



user_city = list(current_location[0]['geometry']['location'].values())
user_city_string=[str(i) for i in user_city]
city_string=','
city_string=city_string.join(user_city_string)



places_result = gmaps.places_nearby(location=city_string,radius=5000, open_now=False, type='hospital')



my_map3 = folium.Map(location = user_city, zoom_start = 15) 


for place in places_result['results']:
    
    try:
        hospital_loc = list(place['geometry']['location'].values())
        rating = place['rating']
        name = place['name']
        rating_person = place['user_ratings_total']
        vicinity = place['vicinity']
        folium.Marker(hospital_loc, popup = f'Rating: {rating} \n Vicinity: {vicinity}',tooltip=name).add_to(my_map3) 
    except:
        pass

print("<h1>",your_city,"</h1>")
print("Content-type:text/html\n")
print('<script>window.location.href="my_map3";</script>')
#my_map3.save("http://13.232.35.109/var/www/html/my_map1.html")     
print("<h1>",your_city,"</h1>")
'''
