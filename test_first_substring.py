import pytest
from first_substring import first_substr


def test_normal_case():
    assert first_substr('animal', 'n') == 'nim'


def test_less_than_two_characters_left():
    assert first_substr('airplane', 'n') == None


def test_character_not_in_word():
    assert first_substr('airplane', 'x') == None


def test_word_is_empty():
    assert first_substr('', 'a') == None


def test_char_is_empty():
    assert first_substr('animal', '') == None


def test_word_and_char_are_empty():
    assert first_substr('', '') == None


def test_word_is_less_than_three_characters():
    assert first_substr('an', 'a') == None



