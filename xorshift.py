class XORShift:
    def __init__(self, seed=123456789):
        self.state = seed

    def next(self):
        x = self.state

        x ^= (x << 13) & 0xFFFFFFFF
        x ^= (x >> 17)
        x ^= (x << 5) & 0xFFFFFFFF

        self.state = x

        return x