from xorshift import XORShift

# Create PRNG object
rng = XORShift()

bits = ""

# Generate random numbers
for _ in range(100000):

    # Get random number
    number = rng.next()

    # Convert to 32-bit binary
    binary = format(number, '032b')

    # Add to bit stream
    bits += binary

# Save bits to file
with open("random_bits.txt", "w") as f:
    f.write(bits)

print("Random bits generated successfully!")