import numpy as np
import matplotlib.pyplot as plt

# Parameters
f = 100
sampling_rate = 1000000  # Sampling rate
t = np.linspace(0, 0.01, int(sampling_rate * 0.01),
                endpoint=False)  # Time array

threshold = 0.7
clip_begin = 0.5
upper_limit = 0.8


def hard_clip(x):
    return np.clip(x, -threshold, threshold)


def soft_clip(x, clip_begin, upper_limit):
    return np.where(np.abs(x) < clip_begin, x, np.sign(x) * (clip_begin + (upper_limit - clip_begin) * np.tanh((np.abs(x) - clip_begin) / (upper_limit - clip_begin))))


# Generate sine wave
sine_wave_100hz = np.sin(2 * np.pi * f * t)

# Apply custom clipping
hard_clipped_sine_wave_100hz = hard_clip(sine_wave_100hz)
soft_clipped_sine_wave_100hz = soft_clip(
    sine_wave_100hz, clip_begin, upper_limit)

# Plotting
# plt.figure(figsize=(10, 6))

plt.plot(1000*t, sine_wave_100hz, label='100 Hz Sine Wave')
plt.plot(1000*t, hard_clipped_sine_wave_100hz, label='Hard Clipped Sine Wave')
plt.plot(1000*t, soft_clipped_sine_wave_100hz, label='Soft Clipped Sine Wave')

plt.title('Clipping Distortion')
plt.xlabel('Time [ms]')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()

# Hide Y-axis labels but keep ticks
plt.gca().set_yticklabels([])

# Save the figure as an image
plt.savefig('./analysis results/clipping distortion.png')

# Display the plot
plt.show()
