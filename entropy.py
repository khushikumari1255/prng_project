from collections import Counter
from math import log2

# Read bits
with open("random_bits.txt", "r") as f:
    bits = f.read()

# Count frequency
counter = Counter(bits)

entropy = 0

for count in counter.values():

    probability = count / len(bits)

    entropy -= probability * log2(probability)

print("Shannon Entropy:", entropy)