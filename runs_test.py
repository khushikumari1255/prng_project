from math import erfc, sqrt

# Read bits
with open("random_bits.txt", "r") as f:
    bits = f.read()

n = len(bits)

# Proportion of 1s
pi = bits.count('1') / n

# Check prerequisite
if abs(pi - 0.5) >= (2 / sqrt(n)):
    print("Runs Test Not Applicable")
    exit()

# Count runs
runs = 1

for i in range(1, n):
    if bits[i] != bits[i - 1]:
        runs += 1

# Compute p-value
numerator = abs(runs - (2 * n * pi * (1 - pi)))
denominator = 2 * sqrt(2 * n) * pi * (1 - pi)

p_value = erfc(numerator / denominator)

print("P-value:", p_value)

if p_value >= 0.01:
    print("Runs Test PASSED")
else:
    print("Runs Test FAILED")