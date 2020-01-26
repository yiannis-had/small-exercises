import requests


class RESTApp:
    def __init__(self, URL):
        self.url = URL

    def getAllUsers(self):
        self.url = "https://jsonplaceholder.typicode.com/users"
        r = requests.get(self.url)
        return r.json()

    def getAllPosts(self):
        self.url = "https://jsonplaceholder.typicode.com/posts"
        r = requests.get(self.url)
        return r.json()

    def getUserDetails(self, username):
        for user in self.getAllUsers():
            if user["username"] == username:
                return user

    def getAllUserPosts(self, username):
        for user in self.getAllUsers():
            if user["username"] == username:
                id = user["id"]
                break
        for post in self.getAllPosts():
            if id == post["userId"]:
                print(post)

    def getCommentsTotal(self, username):
        return None


if __name__ == "__main__":
    test = RESTApp("https://jsonplaceholder.typicode.com")
