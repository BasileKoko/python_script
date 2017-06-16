from dotenv import Dotenv

class FavouriteLanguage:
    end_point = 'https://api.github.com/users/'
    token = "?access_token=" + Dotenv('./.env')['TOKEN']
