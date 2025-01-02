# ABX 盲听测试结果可靠性的统计学分析

import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.stats import binom

m = 44
alpha = 0.05
target_accuracy = 0.9

# 计算每个 n 对应的 p 值
p_values = [binom.pmf(n, m, target_accuracy)
            for n in range(math.ceil(target_accuracy*m), m + 1)]

# 绘制长方形色度计
fig, ax = plt.subplots(figsize=(10, 2))
cmap = plt.get_cmap('coolwarm')
norm = plt.Normalize(0, 1)

# 绘制每个格子
for n, p in enumerate(p_values):
    color = cmap(norm(p))
    rect = plt.Rectangle((n, 0), 1, 1, facecolor=color)
    ax.add_patch(rect)
    ax.text(n + 0.5, 0.5, f'{100*p:.1f}',
            ha='center', va='center', color='black')

# 添加分割线
if p_values[-1] <= 0.05:
    split_index = next(i for i, p in enumerate(p_values) if p <= alpha)
    ax.axvline(x=split_index, color='red', linestyle='--')

# 设置坐标轴
start_x = math.ceil(target_accuracy * m)
ax.set_xlim(0, len(p_values))
ax.set_ylim(0, 1)
ax.set_xticks(np.arange(len(p_values)) + 0.5)
ax.set_xticklabels(np.arange(start_x, m + 1))
ax.set_yticks([])

# plt.show()
plt.savefig(f"./assets/abx{m}at{target_accuracy}.png")
