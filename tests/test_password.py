import unittest
from logic import check_password

class TestPassword(unittest.TestCase):

    def test_strong_password(self):
        result = check_password("Abc123!@#")
        self.assertGreaterEqual(result["score"], 70)

    def test_weak_password(self):
        result = check_password("123")
        self.assertEqual(result["strength"], "WEAK")

if __name__ == "__main__":
    unittest.main()