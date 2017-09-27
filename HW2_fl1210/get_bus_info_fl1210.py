import pylab as pl
import os
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
import sys

# examine the format of input arguments
if not len(sys.argv) == 4:
    print ("Invalid number of arguments. Run as: python get_bus_info_netID.py MTA_KEY BUS_LINE BUS_LINE.csv")
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

try:
    with open(sys.argv[3], "w") as fhandler:
        fhandler.write("Latitude,Longitude,Stop Name,Stop Status\n")
        for i in range(BusNum):
            latitude = BusActivity[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
            longitude = BusActivity[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
            onward_info = BusActivity[i]['MonitoredVehicleJourney']['OnwardCalls']
            # check if the OnwardCalls field is empty
            if onward_info == {}:
                stop = "N/A"
                distance = "N/A"
            else:
                stop = BusActivity[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
                distance = BusActivity[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
            # output to a CSV file named <BUS_LINE>.csv
            fhandler.write("{},{},{},{}".format(str(latitude),str(longitude),stop,distance))
            fhandler.write("\n")
except IOError as ex:
    print("Error performing I/O operations on the file: ",ex)
        






