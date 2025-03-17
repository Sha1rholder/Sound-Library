import numpy as np
import soundfile as sf
from scipy.signal import get_window
import matplotlib.pyplot as plt


def compute_energy_distribution(file_path, num_bands=24, window_size=4096, overlap=0.5):
    """
    计算音频文件在20-20000Hz范围内的能量频段分布

    参数：
    file_path: WAV文件路径
    num_bands: 频段数量（默认24）
    window_size: FFT窗口大小（默认4096）
    overlap: 窗口重叠比例（默认0.5）
    """
    # 读取音频文件
    data, samplerate = sf.read(file_path)

    # 转换为单声道并归一化
    if len(data.shape) > 1:
        data = np.mean(data, axis=1)
    data = data / np.max(np.abs(data))  # 归一化到[-1, 1]

    # 计算实际参数
    nyquist = samplerate / 2
    max_freq = min(20000, nyquist)  # 自动调整最大频率
    min_freq = 20
    hop_size = int(window_size * (1 - overlap))
    window = get_window('hann', window_size)
    freqs = np.fft.rfftfreq(window_size, 1/samplerate)  # 预计算频率轴

    # 生成对数频段边缘
    freq_edges = np.logspace(
        np.log10(min_freq), np.log10(max_freq), num=num_bands+1)
    band_centers = (freq_edges[:-1] + freq_edges[1:]) / 2  # 用于绘图

    # 初始化能量数组
    energy = np.zeros(num_bands)
    total_frames = 0

    # 分帧处理
    for i in range(0, len(data) - window_size, hop_size):
        frame = data[i:i+window_size]
        if len(frame) < window_size:
            continue  # 跳过不完整的最后一帧

        # 加窗并计算功率谱
        frame_windowed = frame * window
        fft = np.fft.rfft(frame_windowed)
        power = np.abs(fft) ** 2

        # 频率分类到频段
        bin_indices = np.searchsorted(freq_edges, freqs, side='right') - 1
        valid = (bin_indices >= 0) & (bin_indices < num_bands)
        energy += np.bincount(bin_indices[valid],
                              weights=power[valid], minlength=num_bands)
        total_frames += 1

    # 转换为分贝并归一化
    energy_avg = energy / total_frames  # 平均能量
    energy_db = 10 * np.log10(energy_avg + 1e-12)  # 防止log(0)
    energy_db -= np.max(energy_db)  # 归一化到0dB最大值

    # 绘图
    plt.figure(figsize=(12, 6))
    plt.semilogx(band_centers, energy_db, 'b-', linewidth=1.5)
    plt.xlim(freq_edges[0], freq_edges[-1])
    plt.xlabel('Frequency (Hz)', fontsize=12)
    plt.ylabel('Normalized Energy (dB)', fontsize=12)
    plt.title('Energy-Frequency Distribution', fontsize=14)
    plt.grid(True, which='both', linestyle='--', alpha=0.7)
    plt.xticks([20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000], [
               '20', '50', '100', '200', '500', '1k', '2k', '5k', '10k', '20k'])
    # plt.show()
    plt.savefig("./analysis results/Energy-Frequency Distribution of Hotel California (Live On MTV, 1994)")

    return band_centers, energy_db


# 使用示例
compute_energy_distribution(
    "./draft/Hotel California (Live On MTV, 1994) mono.wav")
