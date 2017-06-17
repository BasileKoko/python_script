from favourite_language import FavouriteLanguage
import pytest
import sys


def test_validate_username(capsys):
    instance = FavouriteLanguage()
    instance.validate_name("")
    out, err = capsys.readouterr()
    sys.stdout.write(out)
    sys.stderr.write(err)
    assert out == "Sorry username was not found\n"

def test_get_repositories(capsys):
    instance = FavouriteLanguage()
    instance.get_repositories("testfortest2017")
    out, err = capsys.readouterr()
    sys.stdout.write(out)
    sys.stderr.write(err)
    assert out == "Sorry no repositories found for testfortest2017\n"
