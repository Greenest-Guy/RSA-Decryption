from rsa_decryption import RSADecryption

p = 61
q = 53
e = 17
d = 2753
n = p * q
phi_n = (p-1) * (q-1)

plaintext = "hello"
m = int.from_bytes(plaintext.encode('utf-8'), 'big')
c = pow(104, 17, 3233)

print(c, d, n)

obj = RSADecryption(c, d, n)
print(obj.decrypt())
