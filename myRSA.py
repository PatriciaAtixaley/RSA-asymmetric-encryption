import random
import sympy

def get_d(e, m):
    d = sympy.mod_inverse(e, m)
    return d

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a  

def generate_keypair(p, q):
    n = p * q
    m = (p - 1) * (q - 1)
    e = random.randrange(1, m)
    g = gcd(e, m)
    while g != 1:
        e = random.randrange(1, m)
        g = gcd(e, m)
    d = get_d(e, m)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    key, n = pk
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain)

p = sympy.randprime(1, 100)
q = sympy.randprime(1, 100)

(public, private) = generate_keypair(p, q)
message = input("Type message: ")
encrypted_msg = encrypt(public, message)
print(f"Encrypted Message: {encrypted_msg}")
print(f"Decrypted Message: {decrypt(private, encrypted_msg)}")
