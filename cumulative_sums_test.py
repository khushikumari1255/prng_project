import matplotlib.pyplot as plt

with open("random_bits.txt", "r") as f:
    bits = f.read().strip()

values = []

s = 0

for bit in bits:

    if bit == '1':
        s += 1
    else:
        s -= 1

    values.append(s)

max_excursion = max(abs(v) for v in values)

print("Maximum Excursion:", max_excursion)

if max_excursion < 500:
    print("Cumulative Sums Test PASSED")
else:
    print("Cumulative Sums Test FAILED")

plt.plot(values[:1000])

plt.title("Cumulative Sums Random Walk")

plt.xlabel("Bit Index")
plt.ylabel("Cumulative Sum")

plt.show()