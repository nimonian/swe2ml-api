from src.utils import randex


def test_should_exclude_list():
    x = randex(1, 5, [1, 2, 4, 5])
    assert x == 3
