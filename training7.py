import json
import requests

class User:
    pass


class GithubScraper:
    def __init__(self, url):
        self.url = url
        self.user = User()


    def scrape_user_info(self):
        user_info = requests.get(self.url).json() # dict
        self.user.name = user_info["name"]
        self.user.login_id = user_info["login"]
        self.user.email = user_info["email"]
        self.user.location = user_info["location"]
        self.user.company = user_info["company"]



    def scrape_repos(self):
        user_info = requests.get(self.url).json()
        repos_list = requests.get(user_info["repos_url"]).json() # list
        self.user.repos = repos_list


    def get_user(self):
        return self.user




####

'''
実装、合ってます！！

Userは別にこれでもいいんですが、

class User:
    def __init__(self, name="", login_id="", email="", location="", company=""):
        self.name = name
        self.login_id = login_id
        self.email = email
        self.location = location
        self.company = company

としておくと、より柔軟性が高まります。
    def __init__(self, name="", login_id="", email="", location="", company=""):
みたいな感じで、パラメータに name="" というかんじで値を代入すると「初期値」として扱われ、nameが与えられなかった時に 自動的に""がnameに代入されます。

こうしておくと、 User() としてもいいし、User("Hiroki Shimada", "functionp") と呼び出すこともできるので柔軟。


'''
