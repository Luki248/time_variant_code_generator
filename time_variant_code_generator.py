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
    h.update(str(input).encode())
    return h.hexdigest()


def get_password_and_compare():
    h = hashlib.sha256()
    h.update(getpass.getpass("Passwort: ").encode())
    hash1 = h.hexdigest()
    h = hashlib.sha256()
    h.update(hard_coded_password.encode())
    hash2 = h.hexdigest()
    return hash1 == hash2, hash1


def make_xor(hash1, hash2):
    hash3 = hex(int(hash1, 16) ^ int(hash2, 16))
    return hash3[2:]


def make_combined_hash(time, hash_pswd):
    hash_time = generate_hash(str(time).encode())
    hash_combined = make_xor(hash_time, hash_pswd)
    return generate_hash(hash_combined)


def generate_passphrase():
    password_compared, hash_pswd = get_password_and_compare()
    if password_compared:
        clear()

        time_f = int(time.time())
        time_new = time_f - (time_f % 10)
        time_struct = time.gmtime(time_new)
        hash = make_combined_hash(time_new, hash_pswd)
        print(time.asctime(time_struct), hash)


        while True:
            time_f = int(time.time())

            if time_f % 10 == 0:
                clear()
                time_struct = time.gmtime(time_f)
                hash = make_combined_hash(time_f, hash_pswd)
                print(time.asctime(time_struct), hash)
            
            print("\r", 9 - (time_f % 10), " ", end="")
            time.sleep(1)

    else:
        print("Wrong Password!")
        exit()


if __name__ == "__main__":
    generate_passphrase()
    