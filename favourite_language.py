from dotenv import Dotenv
import requests
import json
import urllib2
from collections import Counter



class FavouriteLanguage:
    end_point = 'https://api.github.com/users/'
    token = "?access_token=" + Dotenv('./.env')['TOKEN']

    def get_username(self):
        username = raw_input("Please enter Github username: ")
        self.validate_name(username)

    def validate_name(self, username):
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
            repositories = json.load(urllib2.urlopen(url))
            self.get_repositories_language(username, repositories)
        else:
            print "Sorry no repositories found for {}".format(username)

    def get_repositories_language(self, username, repositories):
        language = []

        for i in range(0, len(repositories)):
            language.append(repositories[i]["language"])
        if language != []:
            self.get_favourite_language(username, language)
        else:
            print "Sorry, no language found in {} repositories".format(username)

    def get_favourite_language(self, language):
        lang = [i for i in language if i is not None]
        data = Counter(lang)
        for k,v in data.iteritems():
            if v == sorted(data.values())[-1]:
                print k


favouritelang = FavouriteLanguage()
favouritelang.get_username()
