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
