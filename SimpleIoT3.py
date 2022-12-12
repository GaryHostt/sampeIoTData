import json
import random
import asyncio
import datetime
import time
import requests
from requests.exceptions import HTTPError
from datetime import datetime
import http.client
from random import randint, choice
from datetime import datetime
import urllib
import logging
import string

def getData(timee):
    data = {}
    data["deviceid"] = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(10))
    data["measurement"] = choice([(random.randint(115,135)),(random.randint(300,500))])
    data["datetime"] = timee
    data["parameter"] = 'customer'
    return json.dumps(data)

def submitData(data):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'client_id': 'ecf4c636f5644b078d74785278745361',
        'client_secret': 'd4a6FD80Bd144f029Ab54c8Af99c44BC'
            }
    payload = data
    print(payload)  
    #url='https://v8uivlpip7dqhaw-ramautodb.adb.us-ashburn-1.oraclecloudapps.com/ords/apexuser/deviceTimes/times'
    url='http://alarm-xapi-v2.us-e1.cloudhub.io/api/accounts/alarm/5'
    #url='http://localhost:8081/api/accounts/alarm/1'
    r = requests.request("POST", url, data=payload, headers=headers)
    #print(r.status_code)
    response = requests.Session()

while True:
	now = datetime.now() # current date and time
	timee = now.strftime("%m/%d/%Y, %H:%M:%S")
	data = getData(timee)
	#print(data)
	submitData(data)
	print ("submitted 1 event")
	time.sleep(1)