import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Parameters
f = 1000  # Frequency of the sine wave (1000 Hz)
sampling_rate = 10000000  # Sampling rate
t = np.linspace(0, 0.002, int(sampling_rate * 0.01),
                endpoint=False)  # Time array

# Generate original sine wave
sine_wave = np.sin(2 * np.pi * f * t)


def crossover_distortion(signal, cross_point):
    if signal >= cross_point:
        return signal
    elif signal > 0:
        return np.arcsin(signal)**2*cross_point/np.arcsin(cross_point)**2
    elif signal > -cross_point:
        return -np.arcsin(signal)**2*cross_point/np.arcsin(cross_point)**2
    return signal


distorted_sine_wave = np.array(
    [crossover_distortion(x, 0.3) for x in sine_wave])

plt.plot(1000 * t, distorted_sine_wave, label='Distorted Sine Wave')
plt.title('Crossover Distortion')
plt.xlabel('Time [ms]')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()

# Add circles at x=0 every 0.5 ms
for i in range(0, 2500, 500):  # 0.5 ms intervals
    circle = patches.Circle((0.001*i, 0), 0.1, edgecolor='r', facecolor='none')
    plt.gca().add_patch(circle)

# Save the figure as an image
plt.savefig('./analysis results/crossover distortion.png')

# Display the plot
plt.show()
