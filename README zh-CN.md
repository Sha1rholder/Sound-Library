[English](./README.md) / 中文

# Sound Library 是什么？

**Sound Library** 是一个声学知识和数据库，致力于帮助发烧友和对高质量音频感兴趣的人了解声音重放的知识。目前本库主要专注于头戴式耳机的评测、知识和购物指南

# 本土化内容

名为“en-US”、“zh-CN”等文件夹包含本地化内容。来自不同地区的用户可以在这些文件夹中找到适合自己的内容。目前主要有针对中国大陆的本地化内容，包括耳机评测、一些散文随笔、购物指南和知识库。如果您有兴趣为其他地区和语言提供本地化内容或翻译，欢迎提交 PR

# Data 数据

## over-ear sensitivity official.csv

官方头戴式耳机灵敏度表。本表存有一些头戴式耳机的发声单元类型、官方灵敏度、官方阻抗、是否支持平衡输入、腔体类型（开放式/封闭式/半封闭式等）以及生产状态等信息。由于一款耳机的生产状态和规格可能发生变动（一款产品的规格变动实在令人深恶痛绝！），每一条数据都有添加日期，以便参考

由于 1. 电声转换设备各项指标的可复现性很差，体质各有区别 2. 各厂家测量设备和测量标准不同，甚至标的参数可能出现错误 3. 作者查阅和录入资料时可能出现疏漏，第三方测试数据可能与官方数据差别较大，在不同厂商的产品之间对比参数意义也比较有限，在有严谨的第三方测试数据或详实的厂商测试报告时请优先采用那些结果

## over-ear sensitivity asr.csv

Audio Science Review（ASR）头戴式耳机灵敏度表。ASR 是比较权威的第三方音频设备测试网站之一，其测试数据相对较为严谨。本表存有一些 ASR 测试过的头戴式耳机驱动到 94dBSPL 所需的电压（mVrms）以及 1000 hz 下的阻抗数据，如果耳机的阻抗随频率变化较大，备注中会对阻抗曲线变化趋势作简单概括

## over-ear assessments cn.csv

头戴式耳机评分表（基于中国大陆）。这是本库贡献者对耳机的主观评分、备注和评分日期。每个耳机可能获得 1 到 5 分。0 分为尚未评测；1 分为纯粹的垃圾，无论如何都不推荐购买；2 分为产品性价比较低，一般不推荐购买；3 分为平均水平的产品，可以考虑购买；4 分为性价比较高的产品，比较推荐购买；5 分为这个价位下几乎完美的选择，强烈推荐

评分主要考虑了其评分时的价格、音质、佩戴舒适度、做工、品控、外观以及售后等因素。由于一款耳机的价格可能发生变动，产线也可能更新，评分日期也是一个重要的参考因素。一般来说评分日期越近，评分越有参考价值。另外，评分相同的产品并不意味着它们产品力相近，比如飞利浦 shp9500 和森海 hd800s 都获得 3 分并不意味着它们音质和做工差不多，这个分数是综合考虑其价格和性能的结果

你可能会注意到一些如 hd600 的经典产品获得 2 分的低分，这是因为该评分仅关注这些耳机的实用性和性价比本身，而不会考虑其历史地位。许多经典耳机产品的做工、音质和功率需求等方面在客观上已经落后于较新的产品，在同价位的竞争力真的不高

由于本库的主要贡献者在中国大陆，打分依据的是耳机的国行售价以及在中国大陆地区的保修方案和口碑。如果您在世界上其他地区，耳机的售价以及保修方案可能有所不同，分数也会不同

# Analysis Tools & Results 数据分析工具和结果

## over-ear sensitivity.py

用于分析和对比头戴式耳机的电压和功率需求，能够绘制你感兴趣的耳机驱动到一定声压级所需电压或功率的直方图，可作为评估耳机驱动难度的一个参考

![Voltage Requirements of the Hardest-to-Drive Producing or Inventory Planar Headphones to Reach 94 dB](./analysis%20results/Voltage%20Requirements%20of%20the%20Hardest-to-Drive%20Producing%20or%20Inventory%20Planar%20Headphones%20to%20Reach%2094%20dB.png)

![Power Requirements of the Easiest-to-Drive Producing or Inventory Closed-Back Headphones to Reach 110 dB](./analysis%20results/Power%20Requirements%20of%20the%20Easiest-to-Drive%20Producing%20or%20Inventory%20Closed-Back%20Headphones%20to%20Reach%20110%20dB.png)

![Comparing Voltage Requirements of Headphones to Reach 94 dB](./analysis%20results/Comparing%20Voltage%20Requirements%20of%20Headphones%20to%20Reach%2094%20dB.png)

![Comparing Power Requirements of Headphones to Reach 100 dB](./analysis%20results/Comparing%20Power%20Requirements%20of%20Headphones%20to%20Reach%20100%20dB.png)

具体使用方法请参考该脚本内的注释和使用实例

# 任务清单

- 翻译 [zh-CN/knowledge](./zh-CN/Knowledge/) 中的文章
- [zh-CN/Knowledge/分析耳机的推力需求.md](./zh-CN/Knowledge/分析耳机的推力需求.md)
- 写一句话产品评论 [data/over-ear assessments cn.csv](./data/over-ear%20assessments%20cn.csv)
- …

欢迎任何贡献。如果您有任何问题或建议，无论多微不足道，都可以 [创建 Issue](https://github.com/Sha1rholder/Sound-Library/issues/new/choose) 或直接邮件联系我。感谢您的支持!
