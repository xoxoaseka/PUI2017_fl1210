from __future__ import print_function
import os
import json
import sys
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
    
# examine the format of input arguments
if not len(sys.argv) == 3:
    print ("Invalid number of arguments. Run as: python show_bus_locations_netID.py MTA_KEY BUS_LINE")
    sys.exit()

# get the MTA key and bus line from the input arguments    
MTAKEY = sys.argv[1]
busline = sys.argv[2]

# download the data from MTA
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + MTAKEY + "&VehicleMonitoringDetailLevel=calls&LineRef=" + busline

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

BusActivity = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
BusNum = len(BusActivity)

# print out the information of bus acitivity of the selected bus line
print("Bus Line : {}".format(busline))
print("Number of Active Buses : {}".format(BusNum))
for i in range(BusNum):
    latitude = BusActivity[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    longitude = BusActivity[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    print("Bus {} is at latitude {} and longitude {}".format(i, latitude, longitude))



