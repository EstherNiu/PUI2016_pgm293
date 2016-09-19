# Author: Patrick Gitundu pgm293
##############################
# Assignment 1 of HW2
##############################

from __future__ import print_function

import sys
import json
import urllib.request as ulr


if not len(sys.argv) == 3:
    print("Invalid number of arguments. \nPlease run the script again with the correct number of arguments.")
    sys.exit()
#check the length of the API key
'''
elif not len(sys.argv[1]) == 25:
    print("Invalid API key. \nPlease ensure your API key is correct. (e.g. it might not be 25 characters long)")
'''
#additional code could be simple Yes/No input to confirm API and Bus Line
#Also we could check the order of the arguments provided. 
#Provide a mechanism to use the arguments in whatever order they were given
  
url ="http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + sys.argv[1] + \
"&&LineRef=" + sys.argv[2] + "VehicleMonitoringDetailLevel=calls"
response = ulr.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

print ("Bus Line: " + sys.argv[2]) 
print ("Number of Active Buses: " + str(len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])))

busses = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
i=0
for bus in busses:
    ref = busses[i]['MonitoredVehicleJourney']['VehicleRef']
    latitude = str(busses[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
    longitude = str(busses[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
    print ("Bus " + ref + " is at latitude: " + latitude + " and at longitude: " + longitude)
    i += 1