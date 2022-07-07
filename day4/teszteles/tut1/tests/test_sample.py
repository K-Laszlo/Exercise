from day4.teszteles.tut1.myapp.sample import add


def test_add_num():  # Test1
    expected = 3
    actual = add(1, 2)
    assert expected == actual


def test_add_str():  # Test2
    assert add('a', 'b') == 'ab'


class TestSample:  # Kell a Test kezdes a classnak.
    def test_add_num(self):  # Test3
        assert add(1, 2) == 3

    def test_add_str(self):  # Test4
        assert add('a', 'b') == 'ab'
