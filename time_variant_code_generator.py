#!/usr/bin/env python3

# time_variant_code_generator

import time
import hashlib


def generate_hash(input):
    h = hashlib.sha256()
    h.update(str(time_f).encode())
    return h.digest().hex()


if __name__ == "__main__":
    while True:
        time_f = int(time.time())

        if time_f % 10 == 0:
            hash = generate_hash(str(time_f).encode())
            print(time_f, hash)
        
        time.sleep(1)