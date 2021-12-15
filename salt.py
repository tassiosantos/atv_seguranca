import random


chars = []
alfabeto =  "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def generate_salt():
    for i in range(16):
        chars.append(random.choice(alfabeto))
    
    salt = "".join(chars)
    return salt
