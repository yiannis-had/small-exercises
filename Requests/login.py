import requests 

with requests.Session() as s:
    url = ""
    username = input("Username:")
    password = input("Password:")
    data = {username: username, password: password}
    r = s.post(url, data=data)
    print(s.cookies.get_dict())
