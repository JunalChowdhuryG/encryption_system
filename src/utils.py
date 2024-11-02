from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from base64 import urlsafe_b64encode
import os

class Utils:
    @staticmethod
    def generate_salt():
        """Genera un salt aleatorio de 16 bytes para el hash de contrasenias."""
        return os.urandom(16)

    @staticmethod
    def hash_password(password: str, salt: bytes):
        """Genera un hash seguro para una contrasenia dada y un salt."""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        return urlsafe_b64encode(kdf.derive(password.encode()))

    @staticmethod
    def verify_password(stored_password: bytes, provided_password: str, salt: bytes):
        """Verifica si la contrasenia proporcionada coincide con el hash almacenado."""
        test_hash = Utils.hash_password(provided_password, salt)
        return test_hash == stored_password
