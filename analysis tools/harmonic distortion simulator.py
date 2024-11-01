import numpy as np
import matplotlib.pyplot as plt

# Parameters
f = 1000  # Frequency of the sine wave (1000 Hz)
sampling_rate = 1000000  # Sampling rate
period = 1 / f  # One period of the sine wave
t = np.linspace(0, period, int(sampling_rate * period),
                endpoint=False)  # Time array for one period

# Generate original sine wave
sine_wave = np.sin(2 * np.pi * f * t)

# Apply odd harmonic distortion (3rd harmonic)
harmonic_distortion_3 = 0.25 * np.sin(2 * np.pi * 3 * f * t)
harmonic_distortion_5 = 0.0625 * np.sin(2 * np.pi * 5 * f * t)

# Apply even harmonic distortion (2nd harmonic)
harmonic_distortion_2 = 0.25 * np.sin(2 * np.pi * 2 * f * t)
harmonic_distortion_4 = 0.0625 * np.sin(2 * np.pi * 4 * f * t)

# Create combined signals
combined_odd_signal = sine_wave + harmonic_distortion_3 + harmonic_distortion_5
combined_even_signal = sine_wave + harmonic_distortion_2 + harmonic_distortion_4

# Create 2x2 subplot
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Plot 1: Combined signal with odd harmonic distortion
axs[0, 0].plot(1000 * t, sine_wave, label='Original 1000 Hz Sine Wave')
axs[0, 0].plot(1000 * t, combined_odd_signal,
               label='Odd Harmonic Distorted Signal')
axs[0, 0].set_title('① Odd Harmonic Distortion')
axs[0, 0].set_ylabel('Amplitude')
axs[0, 0].legend()
axs[0, 0].grid()

# Plot 2: Decomposed odd harmonic distortion signal
axs[0, 1].plot(1000 * t, sine_wave, label='Original 1000 Hz Sine Wave')
axs[0, 1].plot(1000 * t, harmonic_distortion_3,
               label='3rd Harmonic')
axs[0, 1].plot(1000 * t, harmonic_distortion_5,
               label='5th Harmonic')
axs[0, 1].set_title('② Decomposed Odd Harmonic Distortion')
axs[0, 1].legend()
axs[0, 1].grid()

# Plot 3: Combined signal with even harmonic distortion
axs[1, 0].plot(1000 * t, sine_wave, label='Original 1000 Hz Sine Wave')
axs[1, 0].plot(1000 * t, combined_even_signal,
               label='Even Harmonic Distorted Signal')
axs[1, 0].set_title('③ Even Harmonic Distortion')
axs[1, 0].set_xlabel('Time [ms]')
axs[1, 0].set_ylabel('Amplitude')
axs[1, 0].legend()
axs[1, 0].grid()

# Plot 4: Decomposed even harmonic distortion signal
axs[1, 1].plot(1000 * t, sine_wave, label='Original 1000 Hz Sine Wave')
axs[1, 1].plot(1000 * t, harmonic_distortion_2,
               label='2nd Harmonic')
axs[1, 1].plot(1000 * t, harmonic_distortion_4,
               label='4th Harmonic')
axs[1, 1].set_title('④ Decomposed Even Harmonic Distortion')
axs[1, 1].set_xlabel('Time [ms]')
axs[1, 1].legend()
axs[1, 1].grid()

# Disable y-axis labels for all subplots
for ax in axs.flat:
    ax.yaxis.set_ticklabels([])

# Add a title to the entire figure
fig.suptitle('Harmonic Distortion', fontsize=16)

# Adjust layout and display
plt.tight_layout(rect=[0, 0, 1, 1])

# Save the figure as an image
plt.savefig('./analysis results/harmonic distortion.png')

# Display the plot
plt.show()
