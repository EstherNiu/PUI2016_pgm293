# Author: Patrick Gitundu pgm293
##############################
# Assignment 2 of HW2
##############################

from __future__ import print_function

import sys
import json
import urllib.request as ulr
import csv


if not len(sys.argv) == 4:
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

with open(bus+'.csv', 'w', newline='') as buscsv:
    buscsv.write("Latitude,Longitude,Stop Name,Stop Status\n")
    busses = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    i=0
    for bus in busses:
        latitude = str(busses[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
        longitude = str(busses[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
        stopname = busses[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
        stopstatus = busses[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
        buscsv.write(latitude + "," + longitude + "," + stopname + "," + stopstatus + "\n")
        i += 1