import numpy as np
import matplotlib.pyplot as plt

# Generate two random signals
signal1 = np.random.rand(100)
signal2 = np.random.rand(100)

# Perform cross-correlation
cross_corr = np.correlate(signal1, signal2, mode='full')

# Create a time axis for plotting
time_axis = np.arange(-len(signal1)+1, len(signal1))

# Plot the signals and cross-correlation result
plt.subplot(3, 1, 1)
plt.plot(signal1)
plt.title('Signal 1')

plt.subplot(3, 1, 2)
plt.plot(signal2)
plt.title('Signal 2')

plt.subplot(3, 1, 3)
plt.plot(time_axis, cross_corr)
plt.title('Cross-Correlation Result')

plt.tight_layout()
plt.show()
