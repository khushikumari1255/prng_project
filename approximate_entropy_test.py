import math

# Read random bits
with open("random_bits.txt", "r") as f:
    bits = f.read().strip()

m = 2

n = len(bits)

# Append beginning bits to end
bits += bits[:m+1]

def pattern_count(m):

    counts = {}

    for i in range(n):

        pattern = bits[i:i+m]

        counts[pattern] = counts.get(pattern, 0) + 1

    return counts

# Count patterns
counts_m = pattern_count(m)
counts_m1 = pattern_count(m+1)

# Compute phi values
def compute_phi(counts):

    phi = 0

    for count in counts.values():

        p = count / n

        phi += p * math.log(p)

    return phi

phi_m = compute_phi(counts_m)
phi_m1 = compute_phi(counts_m1)

apen = phi_m - phi_m1

print("Approximate Entropy:", apen)

if apen > 0.5:
    print("Approximate Entropy Test PASSED")
else:
    print("Approximate Entropy Test FAILED")