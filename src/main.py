from mnemonic_generator import MnemonicGenerator
from numbers import get_random_number128_bits

if __name__ == "__main__":
    generator = MnemonicGenerator()

    number_bits = get_random_number128_bits()
    print("Our number is:", number_bits)

    mnemonic_phrase = generator.get_mnemonic_from_number(number_bits)
    print(generator.get_mnemonic_beautiful(mnemonic_phrase))

    bits_from_mnemonic = generator.get_bits_from_mnemonic(mnemonic_phrase)
    print("Number from mnemonic:", bits_from_mnemonic)
    print("Are they equal?", number_bits == bits_from_mnemonic)
