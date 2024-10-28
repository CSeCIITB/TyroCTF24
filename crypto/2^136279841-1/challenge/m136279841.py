#!/usr/local/bin/python3

from Crypto.Util.number import bytes_to_long
from os import urandom, getenv

flag = getenv("FLAG", "tyroCTF{w0rld'5_l4r6357_pr1m3}")


def encrypt(m, e, n):
    return pow(m, e, n)


def decrypt(c, p, q):
    return pow(c, (p - 1) * (q - 1), p * q)


def main():
    e = 65537
    print("Enter your favourite 1024 bit number p: ")
    p = int(input())
    print("\n\n")
    print("Enter your next favourite 1024 bit number q: ")
    q = int(input())

    if p.bit_length() != 1024 or q.bit_length() != 1024:
        print("Your primes are not 1024 bits long! Try again next time.")
        return

    n1 = p * q
    n2 = (p**2 + 3 * p + 1) * (q**2 + 3 * q + 1)

    m1 = bytes_to_long(urandom(16))
    c1 = encrypt(m1, e, n1)
    print("\n\n")
    print(f"c1 = {c1}")
    print("\n\n")

    print("Enter your guess for m1: ")
    m1_guess = int(input())

    if m1_guess != m1:
        print("\n\n")
        print("\nYour guess is wrong! Try again next time.")
        return

    m2 = bytes_to_long(urandom(16))
    c2 = encrypt(m2, e, n2)
    print(f"c2 = {c2}")
    print("\n\n")

    print("Enter your guess for m2: ")
    m2_guess = int(input())

    if m2_guess != m2:
        print("\n\n")
        print("\nYour guess is wrong! Try again next time.")
        return

    print("\n\n")
    print("Congratulations! The flag is", flag)


if __name__ == "__main__":
    main()
