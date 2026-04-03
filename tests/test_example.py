import unittest

class TestApp(unittest.TestCase):
    def test_addition(self):
        # This is a simple test that will pass
        self.assertEqual(2 + 3, 5)

if __name__ == "__main__":
    unittest.main()
