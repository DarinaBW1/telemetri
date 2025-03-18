import os 
key = os.urandom(16) 

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes 
from cryptography.hazmat.backends import default_backend 
aesCipher = Cipher(algorithms.AES(key), modes.ECB(), 
backend=default_backend()) 
aesEncryptor = aesCipher.encryptor() 
aesDecryptor = aesCipher.decryptor()

encrypter_message= b'\x08r\x9b*\xeee\x96a\xafdY\x05F\t:\x95:I.\xabU\xa6S\x8a\xbaw\xf8V\x16sa\xbe'
super_secret_key = 1234654# здесь должен быть числовой ключ
key = super_secret_key.to_bytes(16, 'big')

aesCipher = Cipher(algorithms.AES(key), modes.ECB(), 
backend=default_backend()) 
aesEncryptor = aesCipher.encryptor() 
aesDecryptor = aesCipher.decryptor()

print(aesDecryptor.update(encrypter_message))

pop=b'bjfvbjkvbjkebjk      '
milk=aesEncryptor.update(pop) 
print(milk)

encrypter_message= b'\x08r\x9b*\xeee\x96a\xafdY\x05F\t:\x95:I.\xabU\xa6S\x8a\xbaw\xf8V\x16sa\xbe'
super_secret_key = 1234654# здесь должен быть числовой ключ
key = super_secret_key.to_bytes(16, 'big')

aesCipher = Cipher(algorithms.AES(key), modes.ECB(), 
backend=default_backend()) 
aesEncryptor = aesCipher.encryptor() 
aesDecryptor = aesCipher.decryptor()

print(aesDecryptor.update(encrypter_message))

star=b'jfjnfvjnfvakl                '
lol=aesEncryptor.update(star) 
print(lol)

kod=b'\x08r\x9b*\xeee\x96a\xafdY\x05F\t:\x95:I.\xabU\xa6S\x8a\xbaw\xf8V\x16sa\xbe\xecG\x9e\xd8\x8b\x18V\x88\xec\x84\x9b\xa93\xc3}\xe7'
print(aesDecryptor.update(kod))

m=b'\xecG\xd8\x8b\x8b\x18V\x88\xec\x84\x9b\xa93\xc3}\xe7'
print(aesDecryptor.update(m))

# NEVER USE: ECB is not secure!
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Alice and Bob's Shared Key
test_key = bytes.fromhex('00112233445566778899AABBCCDDEEFF')
aesCipher = Cipher(algorithms.AES(test_key), modes.ECB(),
backend=default_backend())
aesEncryptor = aesCipher.encryptor()
aesDecryptor = aesCipher.decryptor()

import sys

ifile, ofile = sys.argv[1:3]
with open(ifile, "rb") as reader:
    with open(ofile, "wb+") as writer:
        image_data = reader.read()
        header, body = image_data[:54], image_data[54:]
        body += b"\x00"*(16-(len(body)%16))
        writer.write(header + aesEncryptor.update(body))

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms,modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

class EncryptionManager:
    def init(self):
        self.key = os.urandom(32)
        self.iv = os.urandom(16)

    def encrypt_message(self, message):
    # WARNING: This code is not secure!!
        encryptor = Cipher(algorithms.AES(self.key),modes.CBC(self.iv),
                             backend=default_backend()).encryptor()
        padder = padding.PKCS7(128).padder()
        padded_message = padder.update(message)
        padded_message += padder.finalize()
        ciphertext = encryptor.update(padded_message)
        ciphertext += encryptor.finalize()
        return ciphertext

    def decrypt_message(self, ciphertext):
        # WARNING: This code is not secure!!
        decryptor = Cipher(algorithms.AES(self.key),
                modes.CBC(self.iv),
                backend=default_backend()).decryptor()
        unpadder = padding.PKCS7(128).unpadder()
        padded_message = decryptor.update(ciphertext)
        padded_message += decryptor.finalize()
        message = unpadder.update(padded_message)
        message += unpadder.finalize()
        return message
    
    # Automatically generate key/IV for encryption.
manager = EncryptionManager()

plaintexts = [
    b"SHORT",
    b"MEDIUM MEDIUM MEDIUM",
     b"LONG LONG LONG LONG LONG LONG"
     ]
class EncryptionManager:
    def init(self):
        key = os.urandom(32)
        nonce = os.urandom(16)
        aes_context = Cipher(algorithms.AES(key),
                            modes.CTR(nonce),
                            backend=default_backend())
        self.encryptor = aes_context.encryptor()
        self.decryptor = aes_context.decryptor()

    def updateEncryptor(self, plaintext):
        return self.encryptor.update(plaintext)
    def finalizeEncryptor(self):
        return self.encryptor.finalize()
    def updateDecryptor(self, ciphertext):
        return self.decryptor.update(ciphertext)
    def finalizeDecryptor(self):
        return self.decryptor.finalize()

# Auto generate key/IV for encryption
manager = EncryptionManager()

plaintexts = [
    b"SHORT",
    b"MEDIUM MEDIUM MEDIUM",
    b"LONG LONG LONG LONG LONG LONG"
    ]

ciphertexts = []

for m in plaintexts:
    ciphertexts.append(manager.updateEncryptor(m))
ciphertexts.append(manager.finalizeEncryptor())

for c in ciphertexts:
    print("Recovered", manager.updateDecryptor(c))
print("Recovered", manager.finalizeDecryptor())

ciphertexts = []
for m in plaintexts:
    ciphertexts.append(manager.encrypt_message(m))
    for c in ciphertexts:
        print("Recovered", manager.decrypt_message(c))

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os