# Importing the geodesic module  from the library
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

address1=input("Enter the input location=")

#n = int(input("\nEnter the other total number of location "))

#addresslist = list(name for name in input("Enter the list location names separated by /:").split("/"))[:n]
addresslist=[(12.845214500000012,77.66016950000001),(12.916575700000015,77.61011629999999),(12.998173200000016,77.5530446),(12.96899679999999,77.72088529999999),(12.899667600000006,77.48268369999998),(12.9044382,77.5649278),(12.930427800000015,77.67840400000003)]
#print("\nUser List: ", addresslist)

#locationlist=list()
#locaddresslist=list()

#getting latitude and longnitude values
geolocator=Nominatim(user_agent="Your_Name")
location1=geolocator.geocode(address1)
loc1=location1.latitude, location1.longitude



#i=0
#for x in addresslist:
#    location2=geolocator.geocode(x)
#    add2=location2.address
#    loc2=location2.latitude, location2.longitude
#    locationlist.insert(i,loc2)
#    locaddresslist.insert(i,add2)
#    i=i+1
#print("\nlocations:",locationlist)
#print("address:",locaddresslist) 


geodistance=list()
j=0
for y in addresslist:
    geodistance.insert(j,geodesic(loc1, y).km)
    j=j+1

#print("\n Geo distances:",geodistance)
# Print the distance calculated in km 
pos=geodistance.index(min(geodistance))

place= geolocator.reverse(addresslist[pos])
print("Nearest Center is",place)
#print("\nNearest linear geograp[pos]hical distance for:",address1,"   is:",locaddresslist[pos],":distance:",min(geodistance))
#print(min(geodistance)
