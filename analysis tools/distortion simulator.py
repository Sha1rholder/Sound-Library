import numpy as np
import matplotlib.pyplot as plt


def clipping_distortion(save=True):
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
    plt.plot(1000*t, hard_clipped_sine_wave_100hz,
             label='Hard Clipped Sine Wave')
    plt.plot(1000*t, soft_clipped_sine_wave_100hz,
             label='Soft Clipped Sine Wave')

    plt.title('Clipping Distortion')
    plt.xlabel('Time [ms]')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid()

    # Hide Y-axis labels but keep ticks
    plt.gca().set_yticklabels([])

    if save:
        plt.savefig('./analysis results/clipping distortion.png')
    else:
        plt.show()


def fr_distortion(save=True):
    # Parameters
    f1 = 100  # Frequency of the first sine wave (100 Hz)
    f2 = 1000  # Frequency of the second sine wave (1000 Hz)
    sampling_rate = 1000000  # Sampling rate
    t = np.linspace(0, 0.01, int(sampling_rate * 0.01),
                    endpoint=False)  # Time array

    # Generate sine waves
    sine_wave_100hz = np.sin(2 * np.pi * f1 * t) * 10
    sine_wave_1000hz = np.sin(2 * np.pi * f2 * t)

    # Apply frequency response distortion (e.g., enhance the 1000 Hz sine wave for 1 dB)
    distorted_sine_wave_1000hz = sine_wave_1000hz * 10**0.1

    # Generate combined signals
    combined_signal = sine_wave_100hz + sine_wave_1000hz
    combined_distorted_signal = sine_wave_100hz + distorted_sine_wave_1000hz

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

    # Plot 3: Combined signal of 100 Hz sine wave and distorted 1000 Hz sine wave
    axs[1, 0].plot(1000*t, combined_distorted_signal,
                   label='Combined Signal (100 Hz + Distorted 1000 Hz)')
    axs[1, 0].set_title(
        '③ Output Signal (100 Hz Sine Wave + Distorted 1000 Hz Sine Wave)')
    axs[1, 0].set_xlabel('Time [ms]')
    axs[1, 0].set_ylabel('Amplitude')
    axs[1, 0].legend()
    axs[1, 0].grid()

    # Plot 4: Original 100 Hz sine wave and distorted 1000 Hz sine wave
    axs[1, 1].plot(1000*t, sine_wave_100hz, label='100 Hz Sine Wave')
    axs[1, 1].plot(1000*t, distorted_sine_wave_1000hz,
                   label='Distorted 1000 Hz Sine Wave')
    axs[1, 1].set_title('④ Decomposed Output Signal')
    axs[1, 1].set_xlabel('Time [ms]')
    axs[1, 1].legend()
    axs[1, 1].grid()

    # Disable y-axis labels for all subplots
    for ax in axs.flat:
        ax.yaxis.set_ticklabels([])

    # Add a title to the entire figure
    fig.suptitle('Frequency-Response Distortion', fontsize=16)

    # Adjust layout and display
    plt.tight_layout(rect=[0, 0, 1, 1])

    if save:
        plt.savefig('./analysis results/fr distortion.png')
    else:
        plt.show()


def harmonic_distortion(save=True):
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

    if save:
        plt.savefig('./analysis results/harmonic distortion.png')
    else:
        plt.show()


def corssover_distortion(save=True):
    import matplotlib.patches as patches

    f = 1000  # Frequency of the sine wave (1000 Hz)
    sampling_rate = 10000000  # Sampling rate
    t = np.linspace(0, 0.002, int(sampling_rate * 0.01),
                    endpoint=False)  # Time array

    # Generate original sine wave
    sine_wave = np.sin(2 * np.pi * f * t)

    def apply_crossover_distortion(signal, cross_point):
        if signal >= cross_point:
            return signal
        elif signal > 0:
            return np.arcsin(signal)**2*cross_point/np.arcsin(cross_point)**2
        elif signal > -cross_point:
            return -np.arcsin(signal)**2*cross_point/np.arcsin(cross_point)**2
        return signal

    distorted_sine_wave = np.array(
        [apply_crossover_distortion(x, 0.3) for x in sine_wave])

    plt.plot(1000 * t, distorted_sine_wave, label='Distorted Sine Wave')
    plt.title('Crossover Distortion')
    plt.xlabel('Time [ms]')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid()

    # Add circles at x=0 every 0.5 ms
    for i in range(0, 2500, 500):  # 0.5 ms intervals
        circle = patches.Circle(
            (0.001*i, 0), 0.1, edgecolor='r', facecolor='none')
        plt.gca().add_patch(circle)

    if save:
        plt.savefig('./analysis results/crossover distortion.png')
    else:
        plt.show()


def phase_distortion(save=True):
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

    if save:
        plt.savefig('./analysis results/phase distortion.png')
    else:
        plt.show()


def intermodulation_distortion(save=True):
    f1 = 800  # Frequency of the first sine wave (100 Hz)
    f2 = 1000  # Frequency of the second sine wave (1000 Hz)
    sampling_rate = 1000000  # Sampling rate
    t = np.linspace(0, 0.01, int(sampling_rate * 0.01),
                    endpoint=False)  # Time array

    # Generate sine waves
    sine_wave_800hz = np.sin(2 * np.pi * f1 * t) * 2
    sine_wave_1000hz = np.sin(2 * np.pi * f2 * t)

    # Apply intermodulation distortion (e.g., create sum and difference frequencies)
    sum_freq = 0.25 * np.sin(2 * np.pi * (f1 + f2) * t)
    beat_freq = 0.25 * np.sin(2 * np.pi * (f2 - f1) * t)

    # Create 2x2 subplot
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))

    # Plot 1: Combined signal of original 100 Hz and 1000 Hz sine waves
    axs[0, 0].plot(1000 * t, sine_wave_800hz + sine_wave_1000hz,
                   label='Combined Signal (800 Hz + 1000 Hz)')
    axs[0, 0].set_title('① Input Signal (800 Hz + 1000 Hz Sine Waves)')
    axs[0, 0].set_ylabel('Amplitude')
    axs[0, 0].legend()
    axs[0, 0].grid()

    # Plot 2: Original 100 Hz and 1000 Hz sine waves
    axs[0, 1].plot(1000 * t, sine_wave_800hz, label='800 Hz Sine Wave')
    axs[0, 1].plot(1000 * t, sine_wave_1000hz, label='1000 Hz Sine Wave')
    axs[0, 1].set_title('② Decomposed Input Signal')
    axs[0, 1].legend()
    axs[0, 1].grid()

    # Plot 3: Combined signal with intermodulation distortion
    axs[1, 0].plot(1000 * t, sine_wave_1000hz+sine_wave_800hz +
                   sum_freq+beat_freq, label='IMD Signal (800 Hz + 1000 Hz + IMD)')
    axs[1, 0].set_title('③ Output Signal with IMD')
    axs[1, 0].set_xlabel('Time [ms]')
    axs[1, 0].set_ylabel('Amplitude')
    axs[1, 0].legend()
    axs[1, 0].grid()

    # Plot 4: Intermodulation distortion components
    axs[1, 1].plot(1000 * t, sine_wave_800hz, label='800 Hz Sine Wave')
    axs[1, 1].plot(1000 * t, sine_wave_1000hz, label='1000 Hz Sine Wave')
    axs[1, 1].plot(1000 * t, sum_freq, label='IMD Component (f1 + f2)')
    axs[1, 1].plot(1000 * t, beat_freq, label='IMD Component (f2 - f1)')
    axs[1, 1].set_title('④ IMD Components')
    axs[1, 1].set_xlabel('Time [ms]')
    axs[1, 1].legend()
    axs[1, 1].grid()

    # Disable y-axis labels for all subplots
    for ax in axs.flat:
        ax.yaxis.set_ticklabels([])

    # Add a title to the entire figure
    fig.suptitle('Intermodulation Distortion', fontsize=16)

    # Adjust layout and display
    plt.tight_layout(rect=[0, 0, 1, 1])

    if save:
        plt.savefig('./analysis results/intermodulation distortion.png')
    else:
        plt.show()


# clipping_distortion()
# fr_distortion()
# harmonic_distortion()
# corssover_distortion()
# phase_distortion()
# intermodulation_distortion()
