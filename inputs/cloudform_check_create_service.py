import requests
from requests.auth import HTTPBasicAuth
#https://ec2-35-180-190-19.eu-west-3.compute.amazonaws.com/api/service_templates/1000000000002

params = {'url': 'https://ec2-35-180-190-19.eu-west-3.compute.amazonaws.com', 'username': 'admin', 'password': 'XXXXX', 'template_id':'1000000000001'}

headers= {"Accept":"application/json","Content-Type":"application/json"}
print('check connection')
r = requests.get("{0}/api".format(params['url']), headers=headers,verify=False, auth=(params['username'], params['password']))

if r.status_code == requests.codes.ok:
    print("Successfully connected to {0}".format(params['url']))
    print(r.json())
else:
    raise Exception("%s: HTTP response code %s (%s)" % (url,r.status_code, r.json()))

print('check service template')
service_template_url = "{0}/api/service_templates/{1}".format(params['url'],params['template_id'])
r = requests.get(service_template_url, headers=headers,verify=False, auth=(params['username'], params['password']))
if r.status_code == requests.codes.ok:
    print("Successfully connected to {0}".format(params['url']))
    print(r.json())
else:
    raise Exception("%s: HTTP response code %s (%s)" % (url,r.status_code, r.json()))



#input doc
###
print ("---------------------------------")
body_data =  {
        'action' : 'order',
        'resource' : {
            'href' : '{0}/api/service_templates/{1}'.format(params['url'],params['template_id']),
            }
        }
###
print (body_data)
r = requests.post(service_template_url, json=body_data , headers=headers, verify=False, auth=(params['username'], params['password']))
if r.status_code == requests.codes.ok:
    print("Successfully connected to {0}".format(params['url']))
    response = r.json()
    print (response)
    print('----')
    print(response['href'])
    print(response['message'])
    print(response['request_state'])
else:
    raise Exception("%s: HTTP response code %s (%s)" % (service_template_url,r.status_code, r.json()))





