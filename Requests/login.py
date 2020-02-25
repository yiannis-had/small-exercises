import requests  # Can also use requests-html

with requests.Session() as session:
    url = ""
    USERNAME = raw_input("Enter your Username: ")
    PASSWORD = raw_input("Enter your Password: ")
    login_data = dict(username=USERNAME, password=PASSWORD)
