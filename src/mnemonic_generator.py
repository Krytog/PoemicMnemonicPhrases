from mapping import Mapping, MappingsMaster
from bits import BitsWord


class Scheme16:
    def __init__(self):
        self.entries = [
            ("adjective", 6),
            ("noun", 10),
            ("verb", 10),
            ("adverb", 7),
            ("verb", 9),
            ("adjective", 10),
            ("adjective", 6),
            ("noun", 10),
            ("verb", 10),
            ("adverb", 7),
            ("verb", 9),
            ("adjective", 10),
            ("rhyme", 12),
            ("rhyme", 12),
        ]

class MnemonicGenerator:
    def __init__(self):
        self.mappings_master = {}
        self.__add_all_mappings()
        print("Mnemonic generator is successfully initialized!")

    def __add_all_mappings(self):
        self.__add_mapping("noun", 11, "data/nouns.txt")
        self.__add_mapping("adverb", 7, "data/adverbs.txt")
        self.__add_mapping("verb", 10, "data/verbs.txt")
        self.__add_mapping("adjective", 10, "data/adjectives.txt")
        self.__add_mapping("rhyme", 12, "data/rhymes.txt")

    def __add_mapping(self, typename, bits, filename):
        self.mappings_master[typename] = Mapping(bits)
        self.mappings_master[typename].load_from_file(filename)

    def get_bitwords(self, number_bits):
        bitwords = []
        offset = 0
        schema = Scheme16()
        for kind, bits in schema.entries:
            bitwords.append((kind, BitsWord(bits, number_bits[offset:offset + bits])))
            offset += bits
        return bitwords

    def get_mnemonic_from_number(self, number_bits):
        bitwords = self.get_bitwords(number_bits)
        simple_words = []
        rhymes = []
        for kind, bitword in bitwords:
            if kind != "rhyme":
                simple_words.append(self.mappings_master[kind].get_word(bitword.num))
            else:
                rhyme = self.mappings_master[kind].get_word(bitword.num)
                rhyme1, rhyme2 = rhyme.split(' ')
                rhymes.append(rhyme1)
                rhymes.append(rhyme2)
        mnemonic = ""
        for i in range(16):
            mnemonic += " "
            if i % 4 != 3:
                mnemonic += simple_words[i - i // 4]
            else:
                mnemonic += rhymes[i // 4]
        mnemonic = mnemonic[1:]
        return mnemonic

    def get_mnemonic_beautiful(self, mnemonic):
        output = ""
        for index, word in enumerate(list(mnemonic.split(' '))):
            output += word
            if index % 4 == 3:
                output += "\n"
            else:
                output += " "
        output = output[:-1]
        return output
