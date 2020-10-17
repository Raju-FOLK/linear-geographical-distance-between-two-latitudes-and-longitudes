# Importing the geodesic module  from the library
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

address1=input("Enter the location=")

#n = int(input("\nEnter the other total number of location "))

#addresslist = list(name for name in input("Enter the list location names separated by /:").split("/"))[:n]
addresslist=['Electronic City, Bengaluru, Karnataka','BTM Layout, Bengaluru, Karnataka','Rajajinagar, Bengaluru, Karnataka','Brookefield, Bengaluru, Karnataka','Kengeri, Bengaluru, Karnataka 560060','Kumaraswamy Layout, Bengaluru, Karnataka 560078','Bellandur, Bengaluru, Karnataka']
print("\nUser List: ", addresslist)

locationlist=list()
locaddresslist=list()

#getting latitude and longnitude values
geolocator=Nominatim(user_agent="Your_Name")
location1=geolocator.geocode(address1)
loc1=location1.latitude, location1.longitude
i=0
for x in addresslist:
    location2=geolocator.geocode(x)
    add2=location2.address
    loc2=location2.latitude, location2.longitude
    locationlist.insert(i,loc2)
    locaddresslist.insert(i,add2)
    i=i+1
print("\nlocations:",locationlist)
#print("address:",locaddresslist)

geodistance=list()
j=0
for y in locationlist:
    geodistance.insert(j,geodesic(loc1, y).km)
    j=j+1

print("\n Geo distances:",geodistance)
# Print the distance calculated in km 
pos=geodistance.index(min(geodistance))
print("\nNearest linear geographical distance for:",address1,"   is:",locaddresslist[pos],":distance:",min(geodistance))
