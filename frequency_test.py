from math import erfc, sqrt

# Read random bits
with open("random_bits.txt", "r") as f:
    bits = f.read()

n = len(bits)

# Convert bits
sum_bits = 0

for bit in bits:
    if bit == '1':
        sum_bits += 1
    else:
        sum_bits -= 1

# Test statistic
s_obs = abs(sum_bits) / sqrt(n)

# P-value
p_value = erfc(s_obs / sqrt(2))

print("P-value:", p_value)

# Decision
if p_value >= 0.01:
    print("Frequency Test PASSED")
else:
    print("Frequency Test FAILED")