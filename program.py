# Importing the geodesic module  from the library
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

#two location names which want calculate the linear geographical distance
address1=input("Enter the first location=")
address2=input("Enter the second location=")

#getting latitude and longnitude values
geolocator=Nominatim(user_agent="Your_Name")
location1=geolocator.geocode(address1)
location2=geolocator.geocode(address2)
print(location1.address)
print((location1.latitude, location1.longitude))
print(location2.address)
print((location2.latitude, location2.longitude))
loc1=location1.latitude, location1.longitude
loc2=location2.latitude, location2.longitude
# Print the distance calculated in km 
print('linear geographical distance:',geodesic(loc1, loc2).km)
