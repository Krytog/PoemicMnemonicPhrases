from mnemonic_generator import MnemonicGenerator
from numbers import get_random_number128_bits

if __name__ == "__main__":
    generator = MnemonicGenerator()

    number_bits = get_random_number128_bits()

    mnemonic_phrase = generator.get_mnemonic_from_number(number_bits)
    print(generator.get_mnemonic_beautiful(mnemonic_phrase))
