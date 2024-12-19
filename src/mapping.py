class Mapping:
    def __init__(self, max_bits):
        self.max_bits = max_bits
        self.max_words = 2 ** self.max_bits
        self.num2word = {}
        self.word2num = {}

    def load_from_file(self, name):
        counter = 0
        with open (name, "r") as file:
            for line in file:
                line = line[:-1]  # get rid of '/n'
                self.num2word[counter] = line
                self.word2num[line] = counter
                counter += 1
                if counter == self.max_words:
                    break

    def get_word(self, num):
        if num not in self.num2word:
            raise KeyError(f"No word for num={num}. Max number: {num}")
        return self.num2word[num]
    
    def get_number(self, word):
        if word not in self.word2num:
            raise KeyError(f"No num for word={word}")
        return self.word2num[word]

class MappingsMaster:
    def __init__(self):
        self.mappings = {}
