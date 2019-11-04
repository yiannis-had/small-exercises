import requests
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'

url = 'http://craigslist.scam.com/index.php' # replace appropriately

names = json.loads(open('names.json').read())

for name in names:
	name_extra = ''.join(random.choice(string.digits))

	username = name.lower() + name_extra + '@gmail.com'
	password = ''.join(random.choice(chars) for i in range(10))

	requests.post(url, allow_redirects=False, data={
	'login': username,	# replace appropriately
	'password': password	# replace appropriately
    })

	print(f"Sent username is {username} and password is {password}")
