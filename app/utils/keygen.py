"""
Updation Key Generation
"""

from random import choice , randint

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

def genkey():
    s = ""
    for _ in range(randint(4, 8)):
        s += choice(chars)
    return s
