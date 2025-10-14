class RSADecryption:
    def __init__(self, ciphertext: int, private_exponent: int, modulus: int):
        self.ciphertext = ciphertext  # c
        self.private_exponent = private_exponent  # d
        self.modulus = modulus  # n

    def decrypt(self) -> tuple:
        m = pow(self.ciphertext, self.private_exponent, self.modulus)

        plaintext_bytes = m.to_bytes(
            (m.bit_length() + 7) // 8, byteorder='big')

        try:
            plaintext = plaintext_bytes.decode('utf-8')
            utf8 = True

        except UnicodeDecodeError:
            plaintext = plaintext_bytes.decode('latin-1')
            utf8 = False

        return plaintext, utf8
