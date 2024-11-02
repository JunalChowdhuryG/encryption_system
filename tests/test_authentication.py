import unittest
from src.authentication import Authentication
from src.utils import Utils

class TestAuthentication(unittest.TestCase):
    def setUp(self):
        self.password = "securepassword"
        self.auth = Authentication(self.password)
        self.salt = Utils.generate_salt()
        self.hashed_password = Utils.hash_password(self.password, self.salt)

    def test_password_verification_success(self):
        self.assertTrue(Utils.verify_password(self.hashed_password, self.password, self.salt))

    def test_password_verification_failure(self):
        wrong_password = "wrongpassword"
        self.assertFalse(Utils.verify_password(self.hashed_password, wrong_password, self.salt))

if __name__ == '__main__':
    unittest.main()
