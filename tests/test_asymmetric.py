import unittest
from src.asymmetric_encryption import AsymmetricEncryption
import os

class TestAsymmetricEncryption(unittest.TestCase):
    def setUp(self):
        # Preparación: crear par de claves y archivo de prueba
        self.encryptor = AsymmetricEncryption()
        self.encryptor.save_keys("data/private_key.pem", "data/public_key.pem")
        self.test_file = 'data/sample.txt'
        self.encrypted_file = 'data/encrypted/sample_aes.enc'
        self.decrypted_file = 'data/decrypted/sample_rsa_decrypted.txt'

        with open(self.test_file, 'w') as f:
            f.write("Este es un archivo de prueba para encriptación RSA")

    def test_encrypt_and_decrypt(self):
        self.encryptor.encrypt_file(self.test_file, "data/public_key.pem", self.encrypted_file)
        self.encryptor.decrypt_file(self.encrypted_file, "data/private_key.pem", self.decrypted_file)

        with open(self.decrypted_file, 'r') as f:
            decrypted_data = f.read()

        self.assertEqual(decrypted_data, "Este es un archivo de prueba para encriptación RSA")

    def tearDown(self):
        # Eliminar archivos creados durante la prueba
        os.remove(self.test_file)
        os.remove(self.encrypted_file)
        os.remove(self.decrypted_file)
        os.remove("data/private_key.pem")
        os.remove("data/public_key.pem")

if __name__ == '__main__':
    unittest.main()
