from src.aes_pycryptodome import encrypt_aes_ecb, decrypt_aes_ecb
from src.aes_cryptography import encrypt_aes

key = b'0123456789abcdef'
data = b'1234567890123456'


def test_pycryptodome_encrypt():
    encrypted = encrypt_aes_ecb(key, data)
    assert encrypted is not None


def test_pycryptodome_decrypt():
    encrypted = encrypt_aes_ecb(key, data)
    decrypted = decrypt_aes_ecb(key, encrypted)
    assert decrypted == data


def test_cryptography_encrypt():
    encrypted = encrypt_aes(key, data)
    assert encrypted is not None