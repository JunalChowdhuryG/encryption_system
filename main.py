from src.symmetric_encryption import SymmetricEncryption
from src.asymmetric_encryption import AsymmetricEncryption
from src.key_manager import KeyManager
from src.authentication import Authentication
import os

def main():
    print("Bienvenido al Sistema de Encriptación de Archivos")
    while True:
        print("\n--- Menú Principal ---")
        print("1. Encriptar un archivo")
        print("2. Desencriptar un archivo")
        print("3. Salir")
        choice = input("Seleccione una opción: ")

        if choice == '1':
            encrypt_file()
        elif choice == '2':
            decrypt_file()
        elif choice == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida, por favor intente de nuevo.")



def encrypt_file():
    print("\n--- Encriptar Archivo ---")
    print("Seleccione el tipo de cifrado:")
    print("1. AES (Simétrico)")
    print("2. RSA (Asimétrico)")
    choice = input("Seleccione una opción: ")

    if choice == '1':
        key = KeyManager.generate_aes_key()
        KeyManager.save_key(key, "data/aes_key.key")

        encryptor = SymmetricEncryption(key)
        file_name = input("Ingrese el nombre del archivo a encriptar (coloque el archivo en 'data/input/'): ")
        file_path = os.path.join("data/input", file_name)
        output_path = "data/encrypted/encrypted_aes.enc"
        encryptor.encrypt_file(file_path, output_path)
        print(f"Archivo encriptado guardado en {output_path}")

    elif choice == '2':
        encryptor = AsymmetricEncryption()
        encryptor.save_keys("data/private_key.pem", "data/public_key.pem")

        file_name = input("Ingrese el nombre del archivo a encriptar (coloque el archivo en 'data/input/'): ")
        file_path = os.path.join("data/input", file_name)
        output_path = "data/encrypted/encrypted_rsa.enc"
        encryptor.encrypt_file(file_path, "data/public_key.pem", output_path)
        print(f"Archivo encriptado guardado en {output_path}")

    else:
        print("Opción inválida. Volviendo al menú principal.")


def decrypt_file():
    print("\n--- Desencriptar Archivo ---")
    print("Seleccione el tipo de cifrado:")
    print("1. AES (Simétrico)")
    print("2. RSA (Asimétrico)")
    choice = input("Seleccione una opción: ")

    if choice == '1':
        key = KeyManager.load_key("data/aes_key.key")
        decryptor = SymmetricEncryption(key)

        file_name = input("Ingrese el nombre del archivo a desencriptar (debe estar en 'data/encrypted/'): ")
        file_path = os.path.join("data/encrypted", file_name)
        output_path = "data/decrypted/decrypted_aes.txt"
        decryptor.decrypt_file(file_path, output_path)
        print(f"Archivo desencriptado guardado en {output_path}")

    elif choice == '2':
        file_name = input("Ingrese el nombre del archivo a desencriptar (debe estar en 'data/encrypted/'): ")
        file_path = os.path.join("data/encrypted", file_name)
        output_path = "data/decrypted/decrypted_rsa.txt"

        decryptor = AsymmetricEncryption()
        decryptor.decrypt_file(file_path, "data/private_key.pem", output_path)
        print(f"Archivo desencriptado guardado en {output_path}")

    else:
        print("Opción inválida. Volviendo al menú principal.")










if __name__ == "__main__":
    main()
