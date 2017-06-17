from favourite_language import FavouriteLanguage
import pytest
import sys

@pytest.fixture
def output(capsys):
    out, err = capsys.readouterr()
    sys.stdout.write(out)
    sys.stderr.write(err)
    return out

def test_validate_username(capsys):
    instance = FavouriteLanguage()
    instance.validate_name("")
    output(capsys)
    assert output(capsys) == "Sorry username was not found\n"

def test_get_repositories(capsys):
    instance = FavouriteLanguage()
    instance.get_repositories("testfortest2017")
    output(capsys)
    assert output(capsys) == "Sorry no repositories found for testfortest2017\n"

def test_get_repositories_language(capsys):
    instance = FavouriteLanguage()
    instance.get_repositories_language("userfor2017", [])
    output(capsys)
    assert output(capsys) == "Sorry no language found in userfor2017 repositories\n"

def test_get_favourite_language(capsys):
    instance = FavouriteLanguage()
    instance.get_favourite_language(["Python", "Ruby", "Python"])
    output(capsys)
    assert output(capsys) == "Python\n"
