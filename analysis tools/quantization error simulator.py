import numpy as np
import matplotlib.pyplot as plt

# 生成一个1秒的音频信号
fs = 400000
bitdepth = 4
t = np.linspace(0, 1, fs, endpoint=False)
frequency = 10000  # 给定频率的正弦波
original_signal = np.sin(2 * np.pi * frequency * t)

# 量化
quantized_signal = np.round(original_signal * 2**(bitdepth-1))/2**(bitdepth-1)

# 计算量化误差
quantization_error = original_signal - quantized_signal

# 计算频谱
original_spectrum = np.fft.fft(original_signal)
error_spectrum = np.fft.fft(quantization_error)

# 计算频率轴
freqs = np.fft.fftfreq(len(t), 1/fs)

# 计算声压级（dB）
original_spectrum_db = 20 * np.log10(np.abs(original_spectrum))
error_spectrum_db = 20 * np.log10(np.abs(error_spectrum))

# 绘制频谱图
plt.figure(figsize=(10, 6))

plt.plot(freqs[:len(freqs)//2], error_spectrum[:len(freqs)//2],
         label='Quantization Error')
plt.plot(freqs[:len(freqs)//2],
         original_spectrum[:len(freqs)//2], label='Original Signal')
plt.ylabel('Sound Pressure')

""" plt.plot(freqs[:len(freqs)//2], error_spectrum_db[:len(freqs)//2],
         label='Quantization Error')
plt.plot(freqs[:len(freqs)//2],
         original_spectrum_db[:len(freqs)//2], label='Original Signal')
plt.ylabel('Sound Pressure Level (dB)') """

plt.xlabel('Frequency (Hz)')

plt.title('Frequency Spectrum of Original Signal and Quantization Error')
plt.legend()
plt.grid()
plt.show()
