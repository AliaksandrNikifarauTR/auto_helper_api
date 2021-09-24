import json
import os

import requests

API_URL = 'https://vpic.nhtsa.dot.gov/api/vehicles/'


def parse(vin: str):
    raw_data = make_request(vin)
    data = {}
    for item in raw_data['Results']:
        if item.get('Value'):
            data[item.get('Variable')] = item.get('Value')
    return data


def make_request(vin: str):
    # request_headers = {
    #     "content-type": "application/json",
    #     "authorization": os.environ.get('carmd_auth_key'),
    #     "partner-token": os.environ.get('carmd_partner_token')
    # }
    r = requests.get(f'{API_URL}decodevin/{vin}?format=json')
    content = r.content.decode('utf8')
    data = json.loads(content)
    # s = json.dumps(data, indent=4, sort_keys=True)
    return data
