from bits import BitsWord

import random


def get_random_number128_bits():
    output = ""
    for _ in range(128):
        if random.randint(0, 1) == 1:
            output += '1'
        else:
            output += '0'
    return output

def get_random_number128():
    bits = get_random_number128_bits()
    word = BitsWord(128, bits)
    return word.num
