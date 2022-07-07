import sys

import pytest

from day4.teszteles.tut3.myapp.sample import add

"""
MARKS: 
https://docs.pytest.org/en/7.1.x/reference/reference.html#marks-ref
"""


@pytest.mark.skip(reason='Reason why we want to skip this test')  # unconditional skip
def test_add_num():  # Test1
    assert add(1, 2) == 3


@pytest.mark.skipif(sys.version_info > (3, 7), reason='Skip if python version is over than 3.7')  # conditional skip
def test_add_str():  # Test2
    assert add('a', 'b') == 'ab'


@pytest.mark.xfail(sys.platform == 'win32', reason='if op windows ignore fail test.') # Ha az op rendszer windows es error-t dob a metodus akkor is pass-kent ertekelje ki. Exception will still raise.
def test_add_num():  # Test3
    assert add([1], [2]) == [1, 2]
    raise Exception
