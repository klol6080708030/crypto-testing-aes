import time
from Crypto.Cipher import AES

def test_aes_performance():
    key = b'0123456789abcdef'
    data = b'1234567890123456'

    start = time.time()

    for _ in range(10000):
        cipher = AES.new(key, AES.MODE_ECB)
        cipher.encrypt(data)

    end = time.time()

    print("AES PyCryptodome time:", end - start)