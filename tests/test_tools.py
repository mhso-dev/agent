from src.tools import multiply


def test_multiply_basic():
    assert multiply.invoke({"a": 7, "b": 6}) == 42


def test_multiply_zero():
    assert multiply.invoke({"a": 7, "b": 0}) == 0
