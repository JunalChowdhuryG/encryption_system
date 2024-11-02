# Sistema de Encriptación de Archivos

Un programa para encriptar y desencriptar archivos usando criptografía simétrica y asimétrica, desarrollado en Python. Este proyecto utiliza algoritmos de cifrado AES (simétrico) y RSA (asimétrico), con una capa de autenticación mediante contraseña para una mayor seguridad.

## Descripción

Este proyecto permite:
1. **Encriptación y desencriptación simétrica (AES)**: Usada para cifrar y descifrar archivos con una clave secreta.
2. **Encriptación y desencriptación asimétrica (RSA)**: Permite cifrar y descifrar archivos utilizando una pareja de claves (pública y privada).
3. **Gestión de claves seguras**: Las claves de cifrado se generan y gestionan de manera segura.
4. **Autenticación por contraseña**: Para desencriptar un archivo, es necesario proporcionar una contraseña, agregando una capa adicional de seguridad.

## Tecnologías

- **Python**: Lenguaje principal de desarrollo.
- **cryptography** o **PyCrypto**: Bibliotecas de Python para implementar cifrado simétrico y asimétrico.

## Estructura del Proyecto

- `main.py`: Archivo principal para ejecutar el programa.
- `src/`: Carpeta que contiene los módulos de encriptación y autenticación.
  - `symmetric_encryption.py`: Funciones para encriptar y desencriptar archivos con AES.
  - `asymmetric_encryption.py`: Funciones para encriptar y desencriptar archivos con RSA.
  - `key_manager.py`: Generación y gestión segura de claves.
  - `authentication.py`: Implementación de autenticación por contraseña.
  - `utils.py`: Utilidades varias como generación de hashes.
- `data/`: Carpeta para almacenar los archivos encriptados y desencriptados.
- `tests/`: Contiene pruebas unitarias para verificar el funcionamiento de cada módulo.

## Instalación

1. Clona este repositorio:

    ```bash
    git clone https://github.com/tu_usuario/encryption_system.git
    cd encryption_system
    ```

2. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```



¡Claro! Revisé el flujo de la interacción y todo parece estar funcionando de manera correcta: el usuario puede encriptar y desencriptar archivos a través del menú, utilizando el cifrado AES o RSA según su elección. Además, los archivos encriptados y desencriptados se almacenan en las carpetas designadas. 

A continuación, te comparto una sección de **Uso** para el `README.md` explicando cómo funciona el programa. También agregaré algunos detalles para asegurar que el usuario siga los pasos correctamente.

---

### Uso

Este programa permite encriptar y desencriptar archivos mediante cifrado simétrico (AES) o asimétrico (RSA). A continuación, se explican los pasos detallados para cada operación.

#### 1. Ejecutar el programa

Desde la terminal, navega hasta el directorio raíz del proyecto y ejecuta:

```bash
python main.py
```

#### 2. Opciones del menú principal

Al ejecutar `main.py`, verás el siguiente menú:

```
--- Menú Principal ---
1. Encriptar un archivo
2. Desencriptar un archivo
3. Salir
Seleccione una opción:
```

### Encriptar un archivo

1. Selecciona la opción `1` en el menú principal para encriptar un archivo.
2. A continuación, elige el tipo de cifrado:
   - `1` para AES (cifrado simétrico).
   - `2` para RSA (cifrado asimétrico).
3. Cuando se te pida, **coloca el archivo que deseas encriptar en la carpeta `data/input/`**.
4. Escribe el nombre del archivo que quieres encriptar, por ejemplo, `info_a_encriptar.txt`.
5. El archivo encriptado se guardará en `data/encrypted/`:
   - Si elegiste AES, el archivo encriptado se llamará `encrypted_aes.enc`.
   - Si elegiste RSA, el archivo encriptado se llamará `encrypted_rsa.enc`.

**Ejemplo de flujo para encriptación AES**:

```
Seleccione una opción: 1
Seleccione el tipo de cifrado:
1. AES (Simétrico)
2. RSA (Asimétrico)
Seleccione una opción: 1
Ingrese el nombre del archivo a encriptar (coloque el archivo en 'data/input/'): info_a_encriptar.txt
Archivo encriptado guardado en data/encrypted/encrypted_aes.enc
```

### Desencriptar un archivo

1. Selecciona la opción `2` en el menú principal para desencriptar un archivo.
2. A continuación, elige el tipo de cifrado:
   - `1` para AES (cifrado simétrico).
   - `2` para RSA (cifrado asimétrico).
3. Cuando se te pida, **asegúrate de que el archivo encriptado esté en la carpeta `data/encrypted/`**.
4. Escribe el nombre del archivo que deseas desencriptar, como `encrypted_aes.enc` o `encrypted_rsa.enc`.
5. El archivo desencriptado se guardará en `data/decrypted/`:
   - Si desencriptaste un archivo AES, el archivo resultante se llamará `decrypted_aes.txt`.
   - Si desencriptaste un archivo RSA, el archivo resultante se llamará `decrypted_rsa.txt`.

**Ejemplo de flujo para desencriptación AES**:

```
Seleccione una opción: 2
Seleccione el tipo de cifrado:
1. AES (Simétrico)
2. RSA (Asimétrico)
Seleccione una opción: 1
Ingrese el nombre del archivo a desencriptar (debe estar en 'data/encrypted/'): encrypted_aes.enc
Archivo desencriptado guardado en data/decrypted/decrypted_aes.txt
```

### Salir

Para finalizar el programa, selecciona la opción `3` en el menú principal.

---

















## Seguridad y Buenas Prácticas

Este programa ha sido diseñado con un enfoque en la seguridad. Algunas prácticas utilizadas incluyen:
- **Gestión segura de claves**: Las claves no se almacenan en texto plano.
- **Autenticación mediante contraseña**: Solo usuarios con la contraseña correcta pueden desencriptar archivos.
- **Funciones hash seguras**: Se utilizan funciones hash como SHA-256 para almacenar y verificar contraseñas.

## Pruebas

Las pruebas unitarias están disponibles en el directorio `tests/`. Para ejecutar las pruebas:

```bash
python -m unittest discover -s tests
```

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar este proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio. 
2. Crea una nueva rama (git checkout -b feature/nueva-funcion). 
3. Haz tus cambios y sube la rama (git push origin feature/nueva-funcion). 
4. Abre un Pull Request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Para más detalles, consulta el archivo LICENSE.


### Notas adicionales

- En `requirements.txt`, incluye las bibliotecas necesarias, por ejemplo:


