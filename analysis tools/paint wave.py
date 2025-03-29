import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# 读取WAV文件
fs, data = wavfile.read(
    './draft/Hotel California (Live On MTV, 1994) mono.wav')  # 替换为你的文件路径

# 确保单声道
if data.ndim > 1:
    data = data[:, 0]

# 计算起始和结束索引
start_index = int(30 * fs)
end_index = int(30.05 * fs)

# 检查索引是否越界
if end_index > len(data):
    end_index = len(data)
    print("警告：结束时间超出音频长度，已自动调整。")

audio_segment = data[start_index:end_index]

# 根据位深归一化数据
if audio_segment.dtype == np.int16:
    audio_segment = audio_segment.astype(np.float32) / 32768.0
elif audio_segment.dtype == np.int32:
    audio_segment = audio_segment.astype(np.float32) / 2147483648.0
elif audio_segment.dtype == np.uint8:
    audio_segment = (audio_segment.astype(np.float32) - 128) / 128.0
# 其他格式可根据需要添加

# 生成时间轴
time = np.linspace(30, 30.05, len(audio_segment))

# 绘制波形图
plt.figure(figsize=(12, 4))
plt.plot(time, audio_segment, linewidth=0.5)
plt.xlim(30, 30.05)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Hotel California (Live On MTV, 1994) 30s - 30.05s')
plt.grid(True)
# plt.show()
plt.savefig(
    "./analysis results/Waveform of Hotel California (Live On MTV, 1994).png")
