import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import stft

sample_rate, data = wavfile.read(
    "./draft/Hotel California (Live On MTV, 1994) mono.wav")


def freq_power(data):
    frequencies, times, Zxx = stft(data, fs=sample_rate, nperseg=8192)
    power = np.abs(Zxx) ** 2
    avg_power = np.mean(power, axis=1)
    plt.fill_between(frequencies, 10*np.log10(avg_power),
                     color='skyblue')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlim(20, 20000)
    plt.ylim(5, 65)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Relative Power (dB)')
    plt.title('Frequency-Power Spectrum of Hotel California (Live On MTV, 1994)')
    plt.grid(True)
    plt.xticks([20, 50, 100, 500, 1000, 5000, 10000, 20000], [
               '20', '50', '100', '500', '1000', '5000', '10000', '20000'])
    plt.yticks([5, 8, 15, 35, 65], ['0', '3', '10', '30', '60'])
    plt.savefig(
        './analysis results/freq power spectrum of Hotel California (Live On MTV, 1994).png')


def time_freq_power(data):
    frequencies, times, Zxx = stft(data, fs=sample_rate, nperseg=2048)
    power = np.abs(Zxx) ** 2
    plt.pcolormesh(times, frequencies, 10*np.log(power)+50,
                   shading='gouraud', vmin=0)
    plt.colorbar(label='Relative Power (dB)')
    plt.yscale('log')
    plt.ylim(20, 20000)
    plt.title(
        'Power Spectrum of Hotel California (Live On MTV, 1994)')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.yticks([20, 50, 100, 500, 1000, 5000, 10000, 20000], [
               '20', '50', '100', '500', '1000', '5000', '10000', '20000'])
    plt.savefig(
        './analysis results/power spectrum of Hotel California (Live On MTV, 1994).png')


# freq_power(data)
time_freq_power(data)
