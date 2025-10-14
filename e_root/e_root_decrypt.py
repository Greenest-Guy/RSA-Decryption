import gmpy2


class ERootDecrypt:
    def __init__(self, ciphertext: int, public_exponent: int, modulus: int):
        self.ciphertext = ciphertext  # c
        self.public_exponent = public_exponent  # e
        self.modulus = modulus  # n

    def decrypt(self) -> tuple:
        m, exact = gmpy2.iroot(self.ciphertext, self.public_exponent)

        if exact:
            plaintext_bytes = m.to_bytes(
                (m.bit_length() + 7) // 8, byteorder='big')

            try:
                plaintext = plaintext_bytes.decode('utf-8')
                utf8 = True

            except UnicodeDecodeError:
                plaintext = plaintext_bytes.decode('latin-1')
                utf8 = False

            return plaintext, utf8

        else:
            raise ValueError(
                "Attack failed: ciphertext is not an exact power e-th power (m^e >= n).")
