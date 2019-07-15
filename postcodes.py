#!/usr/bin/env python3
# coding: utf-8
import requests
from requests.exceptions import HTTPError
import sys
import json

input_code = sys.argv[1]
actual_postcode = input_code.replace(" ", "")

url = "http://api.postcodes.io/postcodes/" + actual_postcode + "/validate"
try:
        response = requests.get(url)
        response.raise_for_status() # If the response from above was successful, no exception will be raised.
        if json.loads(response.text)['result'] == 'success':
            print("The response is successfull:" + response.text)
except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        print(response.text)

url = "http://api.postcodes.io/postcodes/" + actual_postcode
try:
    response = requests.get(url)
    response.raise_for_status()
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')

exact = response.json()
postcode = exact['result']
print("The country for this postcode is " + postcode['country'] +" and the region is " + postcode['region'])

url = "http://api.postcodes.io/postcodes/" + actual_postcode + "/nearest"
try:
        response = requests.get(url)
        response.raise_for_status()
except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')

nearest = response.json()
near_list = []
print("Nearest postcodes:")
for item in nearest['result']:
    near_list.append([item['postcode'],item['country'],item['region']])
print(near_list)
