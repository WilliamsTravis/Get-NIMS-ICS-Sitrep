"""
Functions for requests to the ArcGIS REST API Wildfire Reports through IRWIN.

Created on Wed Aug 15 23:42:13 2018

@author: Travis
"""
import json
import os
import pandas as pd
import requests

class IrwinAccess:
    def __init__(self):
        self.get_credentials()
        self.get_token()
        
    def get_credentials(self):
        home = os.path.expanduser("~")
        cred_dir = os.path.join(home, ".credentials")
        cred_file = os.path.join(cred_dir, "irwin_access.txt")
        if os.path.exists(cred_file):
            with open(cred_file, "r") as file:
                cred_dict = json.loads(file.readlines()[0])
        else:
            os.makedirs(cred_dir)
            username = input('username: ')
            password = input('password: ')
            cred_dict = {"username": username, 
                         "password": password}
            cred_json = json.dumps(cred_dict)
            with open(cred_file, 'w') as file:
                 file.write(cred_json)

        self.username = cred_dict["username"]
        self.password = cred_dict["password"]

    def get_token(self):
        payload = {'f' : 'json',
                   'client':'referer',
                   'referer' : 'www.arcgis.com',
                   'username' : self.username,
                   'password': self.password,
                   'expiration' : '60'}
        url = 'https://www.arcgis.com/sharing/generateToken'  
        response = requests.post(url, payload)
        rdict = json.loads(response.text)
        self.token = rdict['token']


class IrwinQuery:
    def __init__(self, token):
        self.token = token
        self.url = ("https://services1.arcgis.com/Hp6G80Pky0om7QvQ/arcgis/" +
                    "rest/services/IRWIN_Incidents/FeatureServer")
    def get_query(self, state, fields):
         query = ("/0/query?where=POOState='" + state +
                  "'&outFields=" + fields + "&f=json&token=")
         request = self.url + query + self.token
         response = requests.post(request)
         text = response.text
         return text
