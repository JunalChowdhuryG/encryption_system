from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

class AsymmetricEncryption:
    def __init__(self):
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        self.public_key = self.private_key.public_key()

    def save_keys(self, private_path: str, public_path: str):
        # Guardar la clave privada
        with open(private_path, "wb") as f:
            f.write(self.private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            ))

        # Guardar la clave pública
        with open(public_path, "wb") as f:
            f.write(self.public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ))


    def encrypt_file(self, file_path: str, public_key_path: str, output_path: str):
        with open(public_key_path, "rb") as f:
            public_key = serialization.load_pem_public_key(f.read())

        with open(file_path, 'rb') as f:
            data = f.read()

        encrypted_data = public_key.encrypt(
            data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        with open(output_path, 'wb') as f:
            f.write(encrypted_data)

    def decrypt_file(self, file_path: str, private_key_path: str, output_path: str):
        with open(private_key_path, "rb") as f:
            private_key = serialization.load_pem_private_key(f.read(), password=None)

        with open(file_path, 'rb') as f:
            encrypted_data = f.read()

        decrypted_data = private_key.decrypt(
            encrypted_data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        with open(output_path, 'wb') as f:
            f.write(decrypted_data)
