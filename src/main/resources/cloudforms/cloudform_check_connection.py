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

headers = {"Accept": "application/json", "Content-Type": "application/json"}
url = "{0}/api".format(configuration.url)
print('* url: {0}'.format(url))

r = requests.get(url,
                 headers=headers,
                 verify=False,
                 auth=(cloudformsServer.username, cloudformsServer.password))

if r.status_code == requests.codes.ok:
    response = r.json()
    print("* CFME version: " + response['server_info']['version'])
else:
    raise Exception("%s: HTTP response code %s (%s)" % (url, r.status_code, r.json()))
