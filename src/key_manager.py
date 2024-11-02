import os

class KeyManager:
    @staticmethod
    def generate_aes_key():
        return os.urandom(32)  # Clave de 256 bits para AES-256

    @staticmethod
    def save_key(key: bytes, filename: str):
        with open(filename, 'wb') as f:
            f.write(key)

    @staticmethod
    def load_key(filename: str):
        with open(filename, 'rb') as f:
            return f.read()
