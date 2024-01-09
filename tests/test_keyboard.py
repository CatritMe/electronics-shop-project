from src.keyboard import Keyboard
import pytest

kb = Keyboard('Keyboard123', 2000, 10)


def test_keyboard_str():
    assert str(kb) == "Keyboard123"


def test_keyboard_lang():
    assert str(kb.language) == "EN"
    kb.change_lang()
    assert str(kb.language) == "RU"
    kb.change_lang()
    assert str(kb.language) == "EN"


def test_keyboard_no_lang():
    with pytest.raises(AttributeError):
        kb.language = 'GR'
