import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = 'http://craigslist.scam.com/index.php' # replace appropriately

names = json.loads(open('names.json').read())

for name in names:
	name_extra = ''.join(random.choice(string.digits))

	username = name.lower() + name_extra + '@gmail.com'
	password = ''.join(random.choice(chars) for i in range(10))

	requests.post(url, allow_redirects=False, data={
	'auid2yjauysd2uasdasdasd': username, # replace appropriately
	'kjauysd6sAJSDhyui2yasd': password	 # replace appropriately
    })

	print(f"username is {username} & password is {password}")