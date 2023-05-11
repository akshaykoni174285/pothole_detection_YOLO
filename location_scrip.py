from requests.auth import HTTPBasicAuth
import requests

url = ''
headers = {'Accept': 'application/json'}
auth = HTTPBasicAuth('apikey', '1234abcd')
files = {'file': open('filename', 'rb')}

req = requests.get(url, headers=headers, auth=auth, files=files)