from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

class SymmetricEncryption:
    def __init__(self, key: bytes):
        self.key = key

    def encrypt_file(self, file_path: str, output_path: str):
        # Genera un IV único para cada encriptación
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(self.key), modes.CFB(iv), backend=default_backend())
        encryptor = cipher.encryptor()

        with open(file_path, 'rb') as f:
            data = f.read()

        encrypted_data = iv + encryptor.update(data) + encryptor.finalize()

        with open(output_path, 'wb') as f:
            f.write(encrypted_data)

    def decrypt_file(self, file_path: str, output_path: str):
        with open(file_path, 'rb') as f:
            iv = f.read(16)
            encrypted_data = f.read()

        cipher = Cipher(algorithms.AES(self.key), modes.CFB(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

        with open(output_path, 'wb') as f:
            f.write(decrypted_data)
