from favourite_language import FavouriteLanguage
import pytest
import sys

@pytest.fixture
def output(capsys):
    out, err = capsys.readouterr()
    sys.stdout.write(out)
    sys.stderr.write(err)
    return out

@pytest.fixture()
def instance():
    instance = FavouriteLanguage()
    return instance

def test_validate_username(capsys, instance):
    instance
    instance.validate_name("")
    output(capsys)
    assert output(capsys) == "Sorry username was not found\n"

def test_get_repositories(capsys, instance):
    instance
    instance.get_repositories("testfortest2017")
    output(capsys)
    assert output(capsys) == "Sorry no repositories found for testfortest2017\n"

def test_get_repositories_language(capsys, instance):
    instance
    instance.get_repositories_language("userfor2017", [])
    output(capsys)
    assert output(capsys) == "Sorry no language found in userfor2017 repositories\n"

def test_get_favourite_language(capsys, instance):
    instance
    instance.get_favourite_language(["Python", "Ruby", "Python"])
    output(capsys)
    assert output(capsys) == "Python\n"
