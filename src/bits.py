class BitsWord:
    def __init__(self, size, bits):
        if size != len(bits):
            raise RuntimeError(f"Created BitsWord with mismatching sizes: {size}!={len(bits)}")

        self.bits = bits
        self.size = size
        self.num = 0

        multiple = 1
        for i in range(size):
            if self.bits[len(self.bits) - 1 - i] == '1':
                self.num += multiple
            multiple *= 2
