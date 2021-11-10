#!/usr/bin/env python3

# time_variant_code_generator


import getpass
import os
import time
import hashlib


hard_coded_password = "12345"


# define clear function
def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')


def generate_hash(input):
    h = hashlib.sha256()
    h.update(str(time_f).encode())
    return h.hexdigest()


def get_password_and_compare():
    h = hashlib.sha256()
    h.update(getpass.getpass("Passwort: ").encode())
    hash1 = h.hexdigest()
    h = hashlib.sha256()
    h.update(hard_coded_password.encode())
    hash2 = h.hexdigest()
    return hash1 == hash2


if __name__ == "__main__":

    #if get_password_and_compare():
    if True:
        clear()

        time_f = int(time.time())
        time_new = time_f - (time_f % 10)
        hash = generate_hash(str(time_new).encode())
        print(time_new, hash)

        while True:
            time_f = int(time.time())

            if time_f % 10 == 0:
                hash = generate_hash(str(time_f).encode())
                print(time_f, hash)
            
            time.sleep(1)

    else:
        print("Wrong Password!")
        exit()