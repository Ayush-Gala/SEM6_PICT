import random

def generate_prime_number():
    # Generate a random prime number
    while True:
        num = random.randint(2 ** 10, 2 ** 11)
        if is_prime(num):
            return num


def is_prime(num):
    # Check if a number is prime
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def extended_euclidean_algorithm(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_euclidean_algorithm(b, a % b)
        return gcd, y, x - (a // b) * y


def generate_keys():
    # Generate public and private keys
    p = generate_prime_number()
    q = generate_prime_number()
    n = p * q
    phi_n = (p - 1) * (q - 1)

    # Choose a public exponent e
    while True:
        e = random.randint(2, phi_n - 1)
        gcd, x, y = extended_euclidean_algorithm(e, phi_n)
        if gcd == 1:
            break

    # Compute the modular inverse of e
    d = x % phi_n
    if d < 0:
        d += phi_n

    return (e, n), (d, n)


def encrypt(message, public_key):
    # Encrypt the message using the public key
    e, n = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    print('Encrypting message: ')
    return encrypted_message


def decrypt(encrypted_message, private_key):
    # Decrypt the encrypted message using the private key
    d, n = private_key
    decrypted_message = [chr(pow(char, d, n)) for char in encrypted_message]
    return ''.join(decrypted_message)


def main():
    # Generate keys
    public_key, private_key = generate_keys()

    # Encrypt and decrypt a message
    message = input("Enter the message you want to encrypt: ")
    encrypted_message = encrypt(message, public_key)
    decrypted_message = decrypt(encrypted_message, private_key)

    print("Original message:", message)
    print("Encrypted message:", encrypted_message)
    print("Decrypted message:", decrypted_message)


if __name__ == "__main__":
    main()


# Only a true RSA algorithm will be able to encrypt and decrypt this message!!@$%