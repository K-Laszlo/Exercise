import pytest
from day4.teszteles.tut0.myapp.main10 import say_hello_class


def test_is_it_saying():
    excepted = 'Hello Class'
    actual = say_hello_class()
    assert excepted == actual
    assert 'Hello Class' == say_hello_class()


def test_is_it_saying2():
    assert not 'Hello Class2' == say_hello_class()
