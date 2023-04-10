import pytest
from utils import arrs

@pytest.fixture
def coll_get():
    return [1, 2, 3]

@pytest.fixture
def coll_slice():
    return [1, 2, 3, 4]

def test_get(coll_get):
    assert arrs.get(coll_get, 1, "test") == 2
    assert arrs.get(coll_get, -1, "test") == "test"
    with pytest.raises(IndexError):
        arrs.get([], 0, "test")


def test_slice(coll_slice):
    assert arrs.my_slice(coll_slice, 1, 3) == [2, 3]
    assert arrs.my_slice(coll_slice, 1) == [2, 3, 4]
    assert arrs.my_slice(coll_slice, -1) == [4]
    assert arrs.my_slice(coll_slice, -9) == [1, 2, 3, 4]
    assert arrs.my_slice([], 1) == []
