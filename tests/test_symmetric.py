import unittest
from src.symmetric_encryption import SymmetricEncryption
from src.key_manager import KeyManager
import os

class TestSymmetricEncryption(unittest.TestCase):
    def setUp(self):
        # Preparación: generar una clave y un archivo de prueba
        self.key = KeyManager.generate_aes_key()
        self.encryptor = SymmetricEncryption(self.key)
        self.test_file = "data/test_file.txt"
        self.encrypted_file = 'data/encrypted/test_file_aes.enc'
        self.decrypted_file = 'data/decrypted/test_file_decrypted.txt'

        with open(self.test_file, 'w') as f:
            f.write("Este es un archivo de prueba para encriptación AES")

    def test_encrypt_and_decrypt(self):
        self.encryptor.encrypt_file(self.test_file, self.encrypted_file)
        self.encryptor.decrypt_file(self.encrypted_file, self.decrypted_file)

        with open(self.decrypted_file, 'r') as f:
            decrypted_data = f.read()

        self.assertEqual(decrypted_data, "Este es un archivo de prueba para encriptación AES")

    def tearDown(self):
        # Eliminar archivos creados durante la prueba
        os.remove(self.test_file)
        os.remove(self.encrypted_file)
        os.remove(self.decrypted_file)

if __name__ == '__main__':
    unittest.main()
