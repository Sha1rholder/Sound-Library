import numpy as np
import matplotlib.pyplot as plt

# Parameters
f = 1000  # Frequency of the sine wave (1000 Hz)
sampling_rate = 1000000  # Sampling rate
t = np.linspace(0, 0.002, int(sampling_rate * 0.01),
                endpoint=False)  # Time array

# Generate original sine wave
sine_wave_1 = np.sin(2 * np.pi * f * t)
sine_wave_2 = 0.5*np.sin(4 * np.pi * f * t+0.5*np.pi)


def crossover_distortion(signal, zero_point, start_point):
    if signal <= zero_point and signal >= -zero_point:
        return signal
    elif signal <= start_point and signal >= -start_point:
        if signal >= 0:
            return zero_point
        return -zero_point
    return signal


b_distorted_sine_wave_1 = np.array(
    [crossover_distortion(x, 0, 0.05) for x in sine_wave_1])
b_distorted_sine_wave_2 = np.array(
    [crossover_distortion(x, 0, 0.05) for x in sine_wave_2])
ab_distorted_sine_wave_1 = np.array(
    [crossover_distortion(x, 0.6, 0.7) for x in sine_wave_1])
ab_distorted_sine_wave_2 = np.array(
    [crossover_distortion(x, 0.6, 0.7) for x in sine_wave_2])

# Create 1x2 subplot with adjusted figure size
fig, axs = plt.subplots(1, 2, figsize=(10, 4))

# Plot 1: Crossover distorted 1000 Hz sine wave
axs[0].plot(1000 * t, b_distorted_sine_wave_1,
            label='Distorted Strong Sine Wave')
axs[0].plot(1000 * t, b_distorted_sine_wave_2,
            label='Distorted Weak Sine Wave')
axs[0].set_title('Class B Amplifier')
axs[0].set_xlabel('Time [ms]')
axs[0].set_ylabel('Amplitude')
axs[0].legend()
axs[0].grid()
axs[0].fill_between(1000 * t, -0.1, 0.1, color='red', alpha=0.3)

# Plot 2: AB class crossover distorted 1000 Hz sine wave
axs[1].plot(1000 * t, ab_distorted_sine_wave_1,
            label='Distorted Strong Sine Wave')
axs[1].plot(1000 * t, ab_distorted_sine_wave_2,
            label='Undistorted Weak Sine Wave')
axs[1].set_title('Class AB Amplifier')
axs[1].set_xlabel('Time [ms]')
axs[1].legend()
axs[1].grid()
axs[1].fill_between(1000 * t, 0.6, 0.7, color='red', alpha=0.3)
axs[1].fill_between(1000 * t, -0.7, -0.6, color='red', alpha=0.3)

# Disable y-axis labels for all subplots
for ax in axs.flat:
    ax.yaxis.set_ticklabels([])

plt.suptitle('Crossover Distortion', fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 1])

# Save the figure as an image
plt.savefig('./analysis results/crossover distortion.png')

# Display the plot
plt.show()
