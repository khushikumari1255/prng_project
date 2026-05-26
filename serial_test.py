from collections import Counter

with open("random_bits.txt", "r") as f:
    bits = f.read().strip()

patterns = []

for i in range(len(bits)-1):

    patterns.append(bits[i:i+2])

count = Counter(patterns)

print("Pattern Counts:")

for pattern, value in count.items():
    print(pattern, ":", value)

expected = len(patterns) / 4

passed = True

for value in count.values():

    if abs(value - expected) > 0.1 * expected:
        passed = False

if passed:
    print("Serial Test PASSED")
else:
    print("Serial Test FAILED")