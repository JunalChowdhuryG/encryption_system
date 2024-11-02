import unittest
from src.utils import Utils

class TestUtils(unittest.TestCase):
    def setUp(self):
        self.password = "securepassword"
        self.salt = Utils.generate_salt()
        self.hashed_password = Utils.hash_password(self.password, self.salt)

    def test_generate_salt(self):
        salt = Utils.generate_salt()
        self.assertEqual(len(salt), 16)

    def test_hash_password(self):
        hashed_password = Utils.hash_password(self.password, self.salt)
        self.assertEqual(len(hashed_password), 44)  # Hash SHA-256 con encoding base64

    def test_verify_password_success(self):
        self.assertTrue(Utils.verify_password(self.hashed_password, self.password, self.salt))

    def test_verify_password_failure(self):
        wrong_password = "wrongpassword"
        self.assertFalse(Utils.verify_password(self.hashed_password, wrong_password, self.salt))

if __name__ == '__main__':
    unittest.main()
