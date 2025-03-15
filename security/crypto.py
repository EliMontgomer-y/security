from cryptography.fernet import Fernet
import os
import glob

# Global variables
_working_directory = os.getcwd()  # Default to the current working directory
_key = None
_cipher = None

# Internal functions
def _generate_key():
    """
    Generates a key and saves it into a file in the working directory.
    """
    key = Fernet.generate_key()
    key_path = os.path.join(_working_directory, "security-secret.key")
    with open(key_path, "wb") as key_file:
        key_file.write(key)

def _load_key():
    """
    Loads the key from the working directory.
    If the key doesn't exist, it generates a new one.
    """
    key_path = os.path.join(_working_directory, "security-secret.key")
    if not os.path.exists(key_path):
        _generate_key()
    return open(key_path, "rb").read()

def _initialize_cipher():
    """
    Initializes the cipher with the key from the working directory.
    """
    global _key, _cipher
    _key = _load_key()
    _cipher = Fernet(_key)

# Public functions
def set_directory(directory: str):
    """
    Sets the working directory for key storage and reloads the key.

    Args:
        directory (str): The path to the working directory.
    """
    global _working_directory
    if not os.path.isdir(directory):
        raise ValueError(f"The directory '{directory}' does not exist.")
    _working_directory = directory
    _initialize_cipher()  # Reinitialize the cipher with the new key location

def encrypt(message: str) -> bytes:
    """
    Encrypts a message.

    Args:
        message (str): The plaintext message to encrypt.

    Returns:
        bytes: The encrypted message.
    """
    if _cipher is None:
        _initialize_cipher()
    encoded_message = message.encode()
    encrypted_message = _cipher.encrypt(encoded_message)
    return encrypted_message

def decrypt(encrypted_message: bytes) -> str:
    """
    Decrypts an encrypted message.

    Args:
        encrypted_message (bytes): The encrypted message to decrypt.

    Returns:
        str: The decrypted plaintext message.
    """
    if _cipher is None:
        _initialize_cipher()
    decrypted_message = _cipher.decrypt(encrypted_message)
    return decrypted_message.decode()

def reset_module():
    """
    Resets the module by deleting all security-related files (e.g., secret.key)
    and generating a new key.
    """
    global _key, _cipher
    # Delete all files matching the pattern "security-*" in the working directory
    for file_path in glob.glob(os.path.join(_working_directory, "security-*")):
        try:
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")
    # Reinitialize the cipher with a new key
    _initialize_cipher()
