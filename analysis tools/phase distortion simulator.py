import numpy as np
import matplotlib.pyplot as plt

# Parameters
f1 = 100  # Frequency of the first sine wave (100 Hz)
f2 = 1000  # Frequency of the second sine wave (1000 Hz)
sampling_rate = 1000000  # Sampling rate
t = np.linspace(0, 0.01, int(sampling_rate * 0.01),
                endpoint=False)  # Time array

# Generate sine waves
sine_wave_100hz = np.sin(2 * np.pi * f1 * t) * 10
sine_wave_1000hz = np.sin(2 * np.pi * f2 * t)

# Apply phase distortion (shift the 1000 Hz sine wave)
shifted_sine_wave_1000hz = np.sin(2 * np.pi * f2 * (t - 1/4000))

# Generate combined signals
combined_signal = sine_wave_100hz + sine_wave_1000hz
combined_shifted_signal = sine_wave_100hz + shifted_sine_wave_1000hz

# Create 2x2 subplot
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Plot 1: Combined signal of original 100 Hz and 1000 Hz sine waves
axs[0, 0].plot(1000*t, combined_signal,
               label='Combined Signal (100 Hz + 1000 Hz)')
axs[0, 0].set_title('① Input Signal (100 Hz + 1000 Hz Sine Waves)')
axs[0, 0].set_ylabel('Amplitude')
axs[0, 0].legend()
axs[0, 0].grid()

# Plot 2: Original 100 Hz and 1000 Hz sine waves
axs[0, 1].plot(1000*t, sine_wave_100hz, label='100 Hz Sine Wave')
axs[0, 1].plot(1000*t, sine_wave_1000hz, label='1000 Hz Sine Wave')
axs[0, 1].set_title('② Decomposed Input Signal')
axs[0, 1].legend()
axs[0, 1].grid()

# Plot 3: Combined signal of 100 Hz sine wave and phase-distorted 1000 Hz sine wave
axs[1, 0].plot(1000*t, combined_shifted_signal,
               label='Combined Signal (100 Hz + Shifted 1000 Hz)')
axs[1, 0].set_title(
    '③ Output Signal (100 Hz Sine Wave + Shifted 1000 Hz Sine Wave)')
axs[1, 0].set_xlabel('Time [ms]')
axs[1, 0].set_ylabel('Amplitude')
axs[1, 0].legend()
axs[1, 0].grid()

# Plot 4: Original 100 Hz sine wave and phase-distorted 1000 Hz sine wave
axs[1, 1].plot(1000*t, sine_wave_100hz, label='100 Hz Sine Wave')
axs[1, 1].plot(1000*t, shifted_sine_wave_1000hz,
               label='Shifted 1000 Hz Sine Wave')
axs[1, 1].set_title('④ Decomposed Output Signal')
axs[1, 1].set_xlabel('Time [ms]')
axs[1, 1].legend()
axs[1, 1].grid()

# Disable y-axis labels for all subplots
for ax in axs.flat:
    ax.yaxis.set_ticklabels([])

# Add a title to the entire figure
fig.suptitle('Phase Distortion', fontsize=16)

# Adjust layout and display
plt.tight_layout(rect=[0, 0, 1, 1])

# Save the figure as an image
plt.savefig('./analysis results/phase distortion.png')

# Display the plot
plt.show()
