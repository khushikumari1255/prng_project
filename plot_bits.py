import matplotlib.pyplot as plt

# Read first 1000 bits
with open("random_bits.txt", "r") as f:
    bits = f.read()[:1000]

# Convert to integers
values = [int(bit) for bit in bits]

# Plot
plt.figure(figsize=(12, 4))

plt.plot(values)

plt.title("Random Bit Sequence")

plt.xlabel("Bit Position")

plt.ylabel("Bit Value")

plt.show()