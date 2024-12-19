from mnemonic_generator import MnemonicGenerator
from numbers import get_random_number128_bits

if __name__ == "__main__":
    generator = MnemonicGenerator()

    for _ in range(100000):
        number_bits = get_random_number128_bits()
        mnemonic_phrase = generator.get_mnemonic_from_number(number_bits)
        bits_from_mnemonic = generator.get_bits_from_mnemonic(mnemonic_phrase)

        if number_bits != bits_from_mnemonic:
            print("Something went really wrong :(")
