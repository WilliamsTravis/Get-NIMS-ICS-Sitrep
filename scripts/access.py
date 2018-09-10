"""
Authenticating a request to the ArcGIS REST API. Ultimately, we'll use this to access the Situational 
    Wildfire Reports through IRWIN.

Created on Wed Aug 15 23:42:13 2018

@author: Travis
"""
import json
import os
import pandas as pd
import requests

# What's the best way to set this for shared projects?
os.chdir("C:/Users/User/desktop/StDenis/irwin/")

# Set Credentials
username = input('username: ')
password = input('password: ')

# Build token request
url = ("https://www.arcgis.com/sharing/" +
       "generatetoken?expiration=7200&referer=localhost&f=json&username=" +
       username+"&password="+password)
response = requests.post(url)
token = json.loads(response.text)
token = token['token']

# Other ways of building the token request 
url = 'https://www.arcgis.com/sharing/generateToken'  
payload = {'f' : 'json',
           'client':'referer',
           'referer' : 'www.arcgis.com',
           'username' : username,
           'password': password,
           'expiration' : '60'
           }
response = requests.post(url,payload)
rdict = json.loads(response.text)
token = rdict['token']

# Build example request - we may have to use more secure methods in the future
sample = ("https://services1.arcgis.com/Hp6G80Pky0om7QvQ/arcgis/" +
          "rest/services/Current_Wildland_Fires/FeatureServer/0/" +
          "query?where=POOState='US-CA'&outFields=*&f=json&token=")
url3 = sample + token
response = requests.post(url3)
text = response.text
file = open("temp_request.txt", 'w')
file.write(text)
file.close()
data = json.loads(text)

# Create a data frame?
#df = pd.DataFrame(data) # pssh no
