import numpy as np
import matplotlib.pyplot as plt

with open("random_bits.txt", "r") as f:
    bits = f.read().strip()

sequence = np.array([1 if b == '1' else -1 for b in bits])

fft_values = np.fft.fft(sequence)

magnitudes = np.abs(fft_values)

threshold = np.sqrt(len(sequence) * np.log(1/0.05))

count = np.sum(magnitudes < threshold)

print("FFT Peaks Below Threshold:", count)

plt.plot(magnitudes[:1000])

plt.title("FFT Magnitudes")

plt.xlabel("Frequency")
plt.ylabel("Magnitude")

plt.show()