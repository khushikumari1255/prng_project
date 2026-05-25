import struct

FILE_SIZE = 1024 * 1024  # 1 MB


# ==========================================================
# LCG
# ==========================================================

class LCG:
    def __init__(self, seed=123456789):
        self.seed = seed
        self.a = 1664525
        self.c = 1013904223
        self.m = 2**32

    def next(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed


# ==========================================================
# XORSHIFT128+
# ==========================================================

class XORShift128Plus:
    def __init__(self, seed1=123456789, seed2=987654321):
        self.s0 = seed1 & 0xFFFFFFFFFFFFFFFF
        self.s1 = seed2 & 0xFFFFFFFFFFFFFFFF

    def next(self):

        x = self.s0
        y = self.s1

        self.s0 = y

        x ^= (x << 23) & 0xFFFFFFFFFFFFFFFF
        x ^= (x >> 17)
        x ^= y
        x ^= (y >> 26)

        self.s1 = x & 0xFFFFFFFFFFFFFFFF

        return (self.s0 + self.s1) & 0xFFFFFFFFFFFFFFFF


# ==========================================================
# LFSR
# ==========================================================

class LFSR:
    def __init__(self, seed=0xACE1):
        self.state = seed & 0xFFFF

    def next_bit(self):

        bit = (
            ((self.state >> 0) ^
             (self.state >> 2) ^
             (self.state >> 3) ^
             (self.state >> 5)) & 1
        )

        self.state = (self.state >> 1) | (bit << 15)

        return self.state & 1

    def next_byte(self):

        value = 0

        for _ in range(8):
            value = (value << 1) | self.next_bit()

        return value


# ==========================================================
# FILE GENERATOR
# ==========================================================

def generate_files(generator_name, generator):

    bin_filename = f"{generator_name}.bin"
    hex_filename = f"{generator_name}.hex"

    print(f"\nGenerating {bin_filename} ...")

    data = bytearray()

    while len(data) < FILE_SIZE:

        if generator_name == "lfsr":

            random_byte = generator.next_byte()
            data.append(random_byte)

        elif generator_name == "xorshift128plus":

            random_64 = generator.next()
            data.extend(struct.pack("Q", random_64))

        else:

            random_32 = generator.next()
            data.extend(struct.pack("I", random_32))

    data = data[:FILE_SIZE]

    # Write BIN
    with open(bin_filename, "wb") as bin_file:
        bin_file.write(data)

    # Write HEX
    with open(hex_filename, "w") as hex_file:
        hex_file.write(data.hex())

    print(f"{bin_filename} generated")
    print(f"{hex_filename} generated")


# ==========================================================
# MAIN
# ==========================================================

lcg = LCG(seed=123456)
generate_files("lcg", lcg)

xorshift = XORShift128Plus(
    seed1=123456789,
    seed2=987654321
)

generate_files("xorshift128plus", xorshift)

lfsr = LFSR(seed=0xACE1)
generate_files("lfsr", lfsr)

print("\nAll files generated successfully!")