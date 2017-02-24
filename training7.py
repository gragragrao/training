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
