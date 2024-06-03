import math

def encrypt(msg, pub_key):
    ciphertext = pow(msg, pub_key[0], pub_key[1])
    return ciphertext

def decrypt(msg, pri_key):
    plaintext = pow(msg, pri_key[0], pri_key[1])
    return plaintext

def generate_keys():
    global e
    p = int(input("enter first prime number:"))
    q = int(input("enter second prime number:"))
    n = p * q
    m = (p - 1) * (q - 1)

    for i in range(2, m):
        if math.gcd(i, m) == 1:
            e = i
            break

    for i in range(m):
        if (e * i) % m == 1:
            d = i
            break

    pub_key = (e, n)
    pri_key = (d, n)

    return pub_key, pri_key


msg = int(input("Enter msg to be encrypted: "))
pub_key, pri_key = generate_keys()

print("original msg = ", msg)
CT = encrypt(msg, pub_key)
print("Encrypted msg: ", CT)
PT = decrypt(CT, pri_key)
print("Decrypted msg: ", PT)