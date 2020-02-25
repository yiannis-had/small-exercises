from linkedin import linkedin

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
USER_TOKEN = ""
USER_SECRET = ""
RETURN_URL = "http://www.google.com"

auth = linkedin.LinkedInDeveloperAuthentication(
    CONSUMER_KEY,
    CONSUMER_SECRET,
    USER_TOKEN,
    USER_SECRET,
    RETURN_URL,
    linkedin.PERMISSIONS.enums.values(),
)

app = linkedin.LinkedInApplication(auth)

app.get_profile()

connections = app.get_connections()
