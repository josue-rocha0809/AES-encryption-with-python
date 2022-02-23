from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

key = b'mysecretpassword'

cipher = AES.new(key, AES.MODE_CBC)

with open('C:/Cursos/bigData/crypto/crypt.txt', 'rb') as f:
    orig_file = f.read()

encrypted_message = cipher.encrypt(pad(orig_file,AES.block_size))

with open('encrypted_file', 'wb') as e:
    e.write(cipher.iv)
    e.write(encrypted_message)
print(encrypted_message)
