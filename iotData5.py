import json
import random
import datetime
import time
import requests
from requests.exceptions import HTTPError
from datetime import datetime
import http.client
from random import randint, choice
import urllib

#from manufacturingdevices table in ATP
#PressureDeviceNames = ['JN1994', 'BB4848']
#TemperatureDeviceNames = ['BB200','BB207', 'AB9191']
#FlowDeviceNames = ['BB201', 'XX9888']

def getFlowDevices():
    url = 'BASE_URL/ords/apexuser/devices/Flow'
    r = requests.request("GET", url)
    json_data = json.loads(r.text)
    response = json_data['items']
    x = []
    for (deviceid) in response:
        for deviceidfield in deviceid:
            if not deviceidfield == 'deviceid':
                pass
            else:
                #time.sleep(1)
                answer = (deviceid[deviceidfield])
                if answer not in x:
                    x.append(answer)
        if len(x) > 1:
            #print(x)
            pass
    FlowDeviceNames = x
    return FlowDeviceNames
def getTemperatureDevices():
    url = 'BASE_URL/ords/apexuser/devices/Temperature'
    r = requests.request("GET", url)
    json_data = json.loads(r.text)
    response = json_data['items']
    x = []
    for (deviceid) in response:
        for deviceidfield in deviceid:
            if not deviceidfield == 'deviceid':
                pass
            else:
                #time.sleep(1)
                answer = (deviceid[deviceidfield])
                if answer not in x:
                    x.append(answer)
        if len(x) > 1:
            pass
    TemperatureDeviceNames = x
    return TemperatureDeviceNames
def getPressureDevices():
    url = 'BASE_URL/ords/apexuser/devices/Pressure'
    r = requests.request("GET", url)
    json_data = json.loads(r.text)
    response = json_data['items']
    x = []
    for (deviceid) in response:
        for deviceidfield in deviceid:
            if not deviceidfield == 'deviceid':
                pass
            else:
                answer = (deviceid[deviceidfield])
                if answer not in x:
                    x.append(answer)
        if len(x) > 1:
            pass
    PressureDeviceNames = x
    return PressureDeviceNames
def getFlow(timee, FlowDeviceNames):
    data = {}
    data['deviceid'] = random.choice(FlowDeviceNames)
    data['measurement'] = choice([(random.randint(60,100)),(random.randint(101,105))])
    data['datetime'] = timee
    data['parameter'] = 'Flow'
    return data
def getTemperature(timee, TemperatureDeviceNames):
    data = {}
    data['deviceid'] = random.choice(TemperatureDeviceNames)
    data['measurement'] = choice([(random.randint(15,35)),(random.randint(36,50))])
    data['datetime'] = timee
    data['parameter'] = 'Temperature'
    return data
def getPressure(timee, PressureDeviceNames):
    data = {}
    data['deviceid'] = random.choice(PressureDeviceNames)
    data['measurement'] = choice([(random.randint(50,90)),(random.randint(91,105))])
    data['datetime'] = timee
    data['parameter'] = 'Pressure'
    return data
# Generate each parameter's data input in varying proportions
def submitData(data):
    headers = {
        'Content-Type': "application/json",
        'Content-Transfer-Encoding': "buffered"
            }
    payload = data
    print(payload)  
    url='BASE_URL/ords/apexuser/deviceTimes/times'
    r = requests.request("POST", url, data=payload, headers=headers)
    print(r.status_code)
    response = requests.Session()
# Send payload to database API
def deleteData():
    url='BASE_URL/ords/apexuser/deviceTimes/times'
    r = requests.request("DELETE", url)
    print(r.status_code)
    response = requests.Session()
# Deletes data from time table
while True:
    getFlowDevices()
    getTemperatureDevices()
    getPressureDevices()
    FlowDeviceNames = getFlowDevices()
    TemperatureDeviceNames = getTemperatureDevices()
    PressureDeviceNames = getPressureDevices()
    time.sleep(1)
    rnd = random.random()
    #print(rnd)
    dateTimeObj = datetime.now()
    timee = dateTimeObj.strftime("%Y-%m-%dT%H:%M:%SZ")
    if (0 <= rnd < 0.20):
        data = json.dumps(getFlow(timee, FlowDeviceNames))
        submitData(data)
        print('flow data submitted')
    elif (0.20<= rnd < 0.55):
        data = json.dumps(getTemperature(timee, TemperatureDeviceNames))
        submitData(data)
        print('temperature data submitted')
    elif (0.55<= rnd < 0.70):
        data = json.dumps(getPressure(timee, PressureDeviceNames))
        submitData(data)
        print('pressure data submitted')
    elif (0.7255<= rnd < 0.73):
        deleteData()
        print('data deleted, restarting monitoring')

        
