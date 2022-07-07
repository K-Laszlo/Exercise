import pytest

from day4.teszteles.tut4.myapp.sample import add

"""
Parametrizing Unit Tests
"""


def test_add_num():
    assert add(1, 2) == 3


def test_add_str():
    assert add('a', 'b') == 'ab'


def test_add_list():
    assert add([1, 2], [3, 4]) == [1, 2, 3, 4]


@pytest.mark.skip(reason='Reason why we want to skip this test')  # unconditional skip
@pytest.mark.parametrize('a,b,c',
[
    (1, 2, 3),
    ('x', 'y', 'xy'),
    ([1, 2], [3], [1, 2, 3]),
], ids=['num', 'str', 'list'])
def test_add(a, b, c):
    assert add(a, b) == c
