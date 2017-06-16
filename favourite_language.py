from dotenv import Dotenv
import requests


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
