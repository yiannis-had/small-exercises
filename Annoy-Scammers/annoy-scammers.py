import requests
import random
import string
import json

chars = 3 * string.ascii_letters + string.digits + "!@#$%^&*.()"

url = "https://secure-update.authveri-fynetflix.net/ajax/submit.php"  # replace appropriately

emails = ["@gmail.com", "@hotmail.com", "@outlook.com"]

digits = [x for x in range(100)]

names = json.loads(open("names.json").read())

for name in names:
    name_extra = str(random.choice(digits))

    username = name.lower() + name_extra + random.choice(emails)
    password = "".join(random.choice(chars) for i in range(10))

    requests.post(
        url,
        allow_redirects=False,
        data={
            "email": username,  # replace appropriately
            "pass": password,  # replace appropriately
        },
    )

    print(f"Sent username is {username} and password is {password}")
