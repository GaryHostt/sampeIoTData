# inspired by https://github.com/aws-samples/sbs-iot-data-generator

import json
import random
import datetime
import time
import requests
from requests.exceptions import HTTPError
from datetime import datetime

dateTimeObj = datetime.now()

import http.client

PressureDeviceNames = ['JN1994']
TemperatureDeviceNames = ['BB200','BB207']
FlowDeviceNames = ['BB201']

def getFlow():
    data = {}
    data['deviceid'] = random.choice(FlowDeviceNames)
    data['measurement'] = random.randint(60, 100)
    data['datetime'] = dateTimeObj.strftime("%Y-%m-%dT%H:%M:%SZ")
    data['parameter'] = 'Flow'
    #data['datetime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return data
def getTemperature():
    data = {}
    data['deviceid'] = random.choice(TemperatureDeviceNames)
    data['measurement'] = random.randint(15, 35)
    data['datetime'] = dateTimeObj.strftime("%Y-%m-%dT%H:%M:%SZ")
    data['parameter'] = 'Temperature'
    return data
def getPressure():
    data = {}
    data['deviceid'] = random.choice(PressureDeviceNames)
    data['measurement'] = random.randint(50, 90)
    data['datetime'] = dateTimeObj.strftime("%Y-%m-%dT%H:%M:%SZ")
    data['parameter'] = 'Pressure'
    return data
# Generate each parameter's data input in varying proportions
def submitData(data):
    print('stuck here in function')
    #conn = http.client.HTTPConnection("v8uivlpip7dqhaw-ramautodb.adb.us-ashburn-1.oraclecloudapps.com")
    headers = {
        'Content-Type': "application/json",
        'Content-Transfer-Encoding': "buffered"
            }
    #conn.request("POST", "/ords/apexuser/deviceTimes/times", data, headers)
    #res = conn.getresponse()
    #requests.post('https://v8uivlpip7dqhaw-ramautodb.adb.us-ashburn-1.oraclecloudapps.com/ords/apexuser/deviceTimes/times', data, headers, timeout=5)
    requests.post('https://v8uivlpip7dqhaw-ramautodb.adb.us-ashburn-1.oraclecloudapps.com/ords/apexuser/deviceTimes/times', data, headers)
    #except socket.timeout as e:
        #print(e)
    #except Exception as e:
        #print(e)
    response = requests.Session()
    #print(response)
    #data2 = res.read()
    #HTTPResponse.read()
    #print(data2.decode("utf-8")) 
    print('function executed')
    #print(Response.status_code)
while True:
    time.sleep(2)
    rnd = random.random()
    if (0 <= rnd < 0.20):
        data = json.dumps(getFlow())
        print(data)
        print('stuck here')
        submitData(data)
        print('flow data submitted')
    elif (0.20<= rnd < 0.55):
        data = json.dumps(getTemperature())
        print(data)
        print('stuck here')
        submitData(data)
        print('temperature data submitted')
    elif (0.55<= rnd < 0.70):
        data = json.dumps(getPressure())
        print(data)
        print('stuck here')
        submitData(data)
        print('pressure data submitted')
        