[English](./README.md) / 中文

# Sound Library 是什么？

**Sound Library** 是一个声学知识和数据库，致力于帮助发烧友和对高质量音频感兴趣的人了解声音重放的知识。目前本库主要专注于头戴式耳机的评测、知识和购物指南

如果你不知道从何读起或只是想随便看看，可以从这篇文章开始[《初始数字音频》](./zh-CN/Knowledge/初始数字音频.md)

# 本土化内容

名为“en-US”、“zh-CN”等文件夹包含本地化内容。来自不同地区的用户可以在这些文件夹中找到适合自己的内容。目前主要有针对中国大陆的本地化内容，包括耳机评测、一些散文随笔、购物指南和知识库。如果您有兴趣为其他地区和语言提供本地化内容或翻译，欢迎提交 PR

# Data 数据

## over-ear sensitivity official.csv

官方头戴式耳机灵敏度表。本表存有一些头戴式耳机的发声单元类型、官方灵敏度、官方阻抗、是否支持平衡输入、腔体类型（开放式/封闭式/半封闭式等）以及生产状态等信息。由于一款耳机的生产状态和规格可能发生变动（一款产品的规格变动实在令人深恶痛绝！），每一条数据都有添加日期，以便参考

由于 1. 电声转换设备个体区别较大，测试结果可复现性很差 2. 各厂家测量设备和测量标准不同，甚至标的参数可能出现错误 3. 作者查阅和录入资料时可能出现疏漏，第三方测试数据可能与官方数据差别较大，在不同厂商的产品之间对比参数意义也比较有限。在有严谨的第三方测试数据或详实的厂商测试报告时请优先采用那些结果

## over-ear sensitivity asr.csv

Audio Science Review（ASR）头戴式耳机灵敏度表。[Audio Science Review 论坛](https://www.audiosciencereview.com) 是比较权威的第三方音频设备测试网站之一，其测试数据相对较为严谨。本表存有一些 ASR 测试过的头戴式耳机驱动到 94 dBSPL 所需的电压（mVrms）以及 1000 hz 下的阻抗数据，如果耳机的阻抗随频率变化较大，备注中会对阻抗曲线变化趋势作简单概括

# Analysis Tools & Results 数据分析工具和结果

这里包含一些用于分析和可视化数据的脚本和结果

## over-ear sensitivity analysis.py

用于分析和对比头戴式耳机的电压和功率需求，能够绘制你感兴趣的耳机驱动到一定声压级所需电压或功率的直方图，可作为评估耳机驱动难度的一个参考

![Voltage Requirements of Some Headphones to Reach 96 dB](./analysis%20results/Voltage%20Requirements%20of%20Some%20Headphones%20to%20Reach%2096%20dB.png)

![Power Requirements of Some Headphones to Reach 96 dB](./analysis%20results/Power%20Requirements%20of%20Some%20Headphones%20to%20Reach%2096%20dB.png)

![Current Requirements of Some Headphones to Reach 96 dB](./analysis%20results/Current%20Requirements%20of%20Some%20Headphones%20to%20Reach%2096%20dB.png)

它还可以用作分析有史以来本库记载的所有耳机的灵敏度、效率和阻抗分布（虽然没有经过数据筛选，意义不大，仅图一乐）

![Sensitivity Distribution of All Headphones](./analysis%20results/sensitivity%20distribution.png)

![Efficiency Distribution of All Headphones](./analysis%20results/efficiency%20distribution.png)

![Impedance Distribution of All Headphones](./analysis%20results/impedance%20distribution.png)

具体使用方法请参考该脚本内的注释和使用实例

# 任务清单

……

欢迎任何贡献或投稿您的文章，我尊重您的著作权。如果您有任何问题或建议，无论多微不足道，都可以 [创建 Issue](https://github.com/Sha1rholder/Sound-Library/issues/new/choose) 或直接邮件联系我。感谢您的支持!
