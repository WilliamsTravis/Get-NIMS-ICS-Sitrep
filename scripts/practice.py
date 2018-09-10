# -*- coding: utf-8 -*-
"""
Practice with Rest API
Created on Sun Aug 19 15:38:26 2018

@author: User
"""

import os
os.chdir("c:/Users/User/Desktop/StDenis/irwin/scripts/")
import requests
import json

# Attempt to download data on flood insurance rates in Iowa:
url = "https://programs.iowadnr.gov/geospatial/rest/services/SurfaceWaters/FloodMapStatus/MapServer/1"
#headers = {'Content-Type': 'application/json'}
r = requests.post(url,auth=HTTPDigestAuth(input("username: "), input("Password: ")), headers = headers,verify=True)
#r = requests.post(url,headers = headers)
#r = requests.post(url)
r.ok
r = r.json()
print(r.text)

# For successful API call, response code will be 200 (OK)
if(myResponse.ok):

    # Loading the response data into a dict variable
    # json.loads takes in only binary or string variables so using content to fetch binary content
    # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
    jData = json.loads(r.content)

    print("The response contains {0} properties".format(len(jData)))
    print("\n")
    for key in jData:
        print(key + " : " + jData[key])
else:
  # If response code is not ok (200), print the resulting http error code with description
    myResponse.raise_for_status()
