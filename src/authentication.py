from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os
from base64 import urlsafe_b64encode

class Authentication:
    def __init__(self, password: str):
        self.salt = os.urandom(16)  # Sal aleatorio para el hash
        self.password_hash = self._hash_password(password)

    def _hash_password(self, password: str):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=100000,
        )
        return urlsafe_b64encode(kdf.derive(password.encode()))

    def verify_password(self, password: str):
        test_hash = self._hash_password(password)
        return test_hash == self.password_hash
