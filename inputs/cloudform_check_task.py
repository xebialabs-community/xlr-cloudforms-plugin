import requests
from requests.auth import HTTPBasicAuth
import json


params = {'url': 'https://ec2-35-180-190-19.eu-west-3.compute.amazonaws.com', 'username': 'admin', 'password': 'XXXXX'}

headers= {"Accept":"application/json"}

url = "{0}/api".format(params['url'])

r = requests.get(url, headers=headers,verify=False, auth=(params['username'], params['password']))

if r.status_code == requests.codes.ok:
    print("Successfully connected to {0}".format(params['url']))
    print(r.json())
else:
    raise Exception("%s: HTTP response code %s (%s)" % (url,r.status_code, r.json()))


