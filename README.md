# Security Package

A simple Python package for encryption and decryption using the `cryptography` library.

## Installation

Install the package via PyPI:

`pip install security`

## Usage

### Importing the Module
To use the package, import it in your python script:
`from security`

### Setting the Working Directory (Optional)
By default, the package uses the current working directory to store the encryption key (`security-secret.key`).
You can change this directory using the `set_directory()` function:

`security.set_directory("/path/to/directory")`
**Note:** If the directory does not exist, the package will raise an error.

### Encrypting a Message
To encrypt a message, use the `encrypt()` function:
```
encrypted_message = security.encrypt("Hello, this is a secret message!")
print(f"Encrypted Message: {encrypted_message}")
```
The `encrypt()` function returns the encypted message as bytes.

### Decrypting a Message
To decrypt a message, use the `decrypt()` function:
```
decrypted_message = security.decrypt(encrypted_message)
print(f"Decrypted Message: {decrypted_message}")
```
The `decrypt()` function returns the original plaintext message as a string.
<hr>

## Important Notes

### Key File:
- The package generates and saves an encryption key in a file named secret.key in the working directory.
- If you delete or lose this file, you will not be able to decrypt any previously encrypted messages.

### Resetting the module:
- If you delete files labeled `security-*` or the `secret.key` file, the module will generate a new key the next time it is used.
- **All messages encrypted with the old key will no longer be decryptable.**

### Dependencies:
- The package requires the `cryptography` library, which is automatically installed when you install the `security` package.

<hr>

## Example
Here's a complete example of how to use the package:
```
from security import encrypt, decrypt, set_directory

# Set a custom directory for the key (optional)
set_directory("/path/to/your/directory/")

# Encrypt a message
encrypted_message = encrypt("Hello, this is a secret message!")
print(f"Encrypted Message: {encrypted_message}")

# Decrypt the message
decrypted_message = decrypt(encrypted_message)
print(f"Decrypted Message: {decrypted_message}")
```

<hr>

## Troubleshooting
- Directory Does Not Exist:
    If you specify a directory that does not exist, the `set_directory()` function will raise a `ValueError`. Ensure the directory exists before setting it.
- Key File Corruption:
    If the secret.key file is corrupted or deleted, you will need to generate a new key. Be aware that this will render previously encrypted messages undecryptable.

<hr>

##  Support
For issues or feature requests, please open an issue on the [GitHub repository.](https://github.com/EliMontgomer-y/security)

