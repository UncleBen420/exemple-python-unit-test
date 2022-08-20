"""
Exemple file for pytest assert
"""

class GfG:
    """other class to use in pytest"""

    name = "GeeksforGeeks"
    age = 24

class TestClass:
    """Main test class"""

    def test_one(self):
        """func 1"""
        x = "this"
        assert "h" in x

    def test_two(self):
        """func 2"""
        obj = GfG()
        assert hasattr(obj, "age")
