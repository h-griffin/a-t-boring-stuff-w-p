import pytest
from whiteboards.acronym import acronym


def test_nypd():
    actual = acronym('new york police department')
    expected = 'NYPD'
    assert actual == expected


