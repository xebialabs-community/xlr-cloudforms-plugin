#
# Copyright 2018 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import requests
from requests.auth import HTTPBasicAuth

if cloudformsServer is None:
    print "No cloudform server provided."
    sys.exit(1)

headers= {"Accept":"application/json","Content-Type":"application/json"}
service_template_url = "{0}/api/service_templates/{1}".format(cloudformsServer['url'],serviceTemplate)
print('* url: {0}'.format(service_template_url))

body_data =  {
        'action' : 'order',
        'resource' : {
            'href' : service_template_url
            }
        }
#print (body_data)

r = requests.post(service_template_url, json=body_data , headers=headers, verify=False, auth=(cloudformsServer['username'], cloudformsServer['password']))
if r.status_code == requests.codes.ok:
    response = r.json()
    serviceRequestsId = response['id']
    serviceRequestState = response['request_state']
    serviceRequestMessage = response['message']

    print("* serviceRequestId {0}".format(serviceRequestsId))
    print("* serviceRequestState {0}".format(serviceRequestState))
    print("* serviceRequestMessage {0}".format(serviceRequestMessage))
    print("* href {0}".format(response['href']))

    task.setStatusLine("{0}:{1}".format(serviceRequestState, serviceRequestMessage))
    task.schedule("cloudforms/wait-for-end-service-request.py")
else:
    raise Exception("%s: HTTP response code %s (%s)" % (service_template_url,r.status_code, r.json()))


