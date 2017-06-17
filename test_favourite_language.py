import favourite_language

def test_stdout_message():
    fav = FavouriteLanguage()
    fav.get_username()
    out, err = capsys.readouterr()
    assert out == "Please enter Github username"
