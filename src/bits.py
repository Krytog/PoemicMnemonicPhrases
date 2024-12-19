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


def get_bits_from_number(number, bits_count):
    output = ""
    while number > 0:
        if number % 2 == 1:
            output += '1'
        else:
            output += '0'
        number = number // 2
    if len(output) > bits_count:
        raise RuntimeError(f"Tried to get lesser bits from number than it has: {len(output)} > {bits_count}")
    for _ in range(len(output), bits_count):
        output += '0'
    output = output[::-1]
    return output
