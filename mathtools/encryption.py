# (c) Rafael Urben - 2021

def ascii2str(ascii: list) -> str:
    """Convert a list of ascii-codes to a string"""
    return ''.join(chr(i) for i in ascii)


def str2ascii(string: str) -> list:
    """Convert a string to a list of ascii-codes"""
    return [ord(i) for i in string]


class BabyRSA():
    """This is not real RSA encryption"""

    @classmethod
    def encrypt_msg(self, e: int, n: int, message: str) -> list:
        return [(m**e) % n for m in str2ascii(message)]

    @classmethod
    def decrypt_msg(self, d: int, n: int, message: list) -> str:
        return ascii2str([(m**d) % n for m in message])

    #

    def __init__(self, n: int, e: int, d: int = None):
        self.n = n
        self.e = e
        self.d = d

    def encrypt(self, message):
        return BabyRSA.encrypt_msg(self.e, self.n, message)

    def decrypt(self, message):
        return BabyRSA.decrypt_msg(self.d, self.n, message)
