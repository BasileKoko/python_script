from dotenv import Dotenv
import requests
import json
from collections import Counter


class FavouriteLanguage:
    end_point = 'https://api.github.com/users/'
    token = "?access_token=" + Dotenv('./.env')['TOKEN']

    def start(self):
        username = raw_input("Please enter Github username: ")
        self.validate_username(username)

    def validate_username(self, username):
        url = FavouriteLanguage.end_point + username + FavouriteLanguage.token
        r = requests.get(url)

        if r.status_code == 200:
            self.get_repositories(username)
        else:
            print "Sorry username was not found"

    def get_repositories(self, username):
        url = FavouriteLanguage.end_point + username + "/repos" + FavouriteLanguage.token
        r = requests.get(url)

        if r.status_code == 200:
            repositories = r.json()
            self.get_repositories_language(repositories)
        else:
            print "Sorry no repositories found for {}".format(username)

    def get_repositories_language(self, repositories):
        language = []

        for i in range(0, len(repositories)):
            language.append(repositories[i]["language"])

        if filter(None, language) != []:
            self.get_favourite_language(language)
        else:
            print "Sorry no language found in the user repositories"


    def get_favourite_language(self, language):
        data = Counter(language)
        for k,v in data.iteritems():
            if v == sorted(data.values())[-1]:
                print k
