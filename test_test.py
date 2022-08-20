# content of test_class.py
import pytest


# declaring class
class GfG:
    name = "GeeksforGeeks"
    age = 24

class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x
        
    def test_three(self):
        assert 1 == 1

    def test_two(self):
        # initializing object
        obj = GfG()
        assert hasattr(obj, "age")
