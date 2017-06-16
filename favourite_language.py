from dotenv import Dotenv

class FavouriteLanguage:
    end_point = 'https://api.github.com/users/'
    token = "?access_token=" + Dotenv('./.env')['TOKEN']

    def get_username(self):
        username = raw_input("Please enter Github username: ")
