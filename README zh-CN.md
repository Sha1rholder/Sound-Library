[English](./README.md) / 中文

# Sound Library 是什么？

**Sound Library** 是一个声学知识和数据库，致力于帮助发烧友和对高质量音频感兴趣的人了解声音重放的知识。目前本库主要专注于头戴式耳机的评测、知识和购物指南

如果你不知道从何读起或只是想随便看看，可以看看这篇文章 [《耳机的两种灵敏度和阻抗的换算关系》](./zh-CN/Knowledge/耳机的两种灵敏度和阻抗的换算关系.md)

# 本土化内容

名为“en-US”、“zh-CN”等文件夹包含本地化内容。来自不同地区的用户可以在这些文件夹中找到适合自己的内容。目前主要有针对中国大陆的本地化内容，包括耳机评测、一些散文随笔、购物指南和知识库。如果您有兴趣为其他地区和语言提供本地化内容或翻译，欢迎提交 PR

# Data 数据

## over-ear sensitivity official.csv

官方头戴式耳机灵敏度表。本表存有一些头戴式耳机的发声单元类型、官方灵敏度、官方阻抗、是否支持平衡输入、腔体类型（开放式/封闭式/半封闭式等）以及生产状态等信息。由于一款耳机的生产状态和规格可能发生变动（一款产品的规格变动实在令人深恶痛绝！），每一条数据都有添加日期，以便参考

由于 1. 电声转换设备个体区别较大，测试结果可复现性很差 2. 各厂家测量设备和测量标准不同，甚至标的参数可能出现错误 3. 作者查阅和录入资料时可能出现疏漏，第三方测试数据可能与官方数据差别较大，在不同厂商的产品之间对比参数意义也比较有限。在有严谨的第三方测试数据或详实的厂商测试报告时请优先采用那些结果

## over-ear sensitivity asr.csv

Audio Science Review（ASR）头戴式耳机灵敏度表。[Audio Science Review 论坛](https://www.audiosciencereview.com) 是比较权威的第三方音频设备测试网站之一，其测试数据相对较为严谨。本表存有一些 ASR 测试过的头戴式耳机驱动到 94 dBSPL 所需的电压（mVrms）以及 1000 hz 下的阻抗数据，如果耳机的阻抗随频率变化较大，备注中会对阻抗曲线变化趋势作简单概括

## over-ear score cn.csv

头戴式耳机评分表（基于中国大陆），包含本库主要贡献者对耳机的综合评分、音质评分、做工评分、佩戴舒适度评分以及备注和评分日期。每个评分都在 1 到 5 之间

**Score** 总分，综合考虑了评分时的价格、音质、做工、佩戴舒适度、外观、品控以及售后等因素。1 分为纯粹的垃圾，无论如何都不推荐购买；2 分为产品性价比较低，一般不推荐购买；3 分为平均水平的产品，可以购买；4 分为性价比较高的产品，推荐购买；5 分为这个价位下几乎完美的选择，强烈推荐

**Sound** 音质评分，依赖于评分时的价格和驱动难度。在价格相似的产品中，1 分为声音垃圾至极；2 分为音质 **明显** 逊色；3 分是声音中规中矩；4 分是音质出色；5 分是音质出类拔萃远超竞品

> 你可能会注意到一些如 hd600 的经典产品获得 2 分的低分，这是因为该评分仅关注这些耳机的声价比，或者说聆听愉悦感和金钱代价本身，而不会考虑其历史地位。客观上，许多经典耳机产品的音质已经落后于较新的产品
>
> 另外，耳机的驱动难度不同，对前端的要求也不同。更难推的耳机通常需要搭配更昂贵的前端，这也会对声价比产生负面影响

**Build** 做工评分，依赖于评分时的价格。在相近价位横向对比，1 分为做工垃圾至极；2 分为做工质量略显不佳；3 分是中规中矩；4 分是做工优良；5 分是做工出类拔萃远超竞品

**Comfort** 佩戴舒适度评分，和价格无关。1 分为折磨般的佩戴；2 分为对许多人来说佩戴不舒适；3 分是大多数人能够久戴；4 分是大多数人会觉得舒适；5 分是轻盈的重量加近乎完美的佩戴。超过 400 g 的耳机无法获得 5 分

由于一款耳机的价格可能发生变动，产线也可能更新，评分日期也是一个重要的参考因素。一般来说评分日期越近，评分越有参考价值。产品评分相同并不意味着它们质量相近，比如 Audeze LCD-5 和拜亚 dt880 都获得 3 分并不意味着它们质量差不多

由于本库的主要贡献者在中国大陆，打分会依据耳机在中国大陆的售价、保修以及口碑等。如果您在其他地区，以上因素可能有所不同，分数也会不同

# Analysis Tools & Results 数据分析工具和结果

## over-ear sensitivity analysis.py

用于分析和对比头戴式耳机的电压和功率需求，能够绘制你感兴趣的耳机驱动到一定声压级所需电压或功率的直方图，可作为评估耳机驱动难度的一个参考

![Voltage Requirements of the Hardest-to-Drive Producing or Inventory Headphones to Reach 110 dB](./analysis%20results/Voltage%20Requirements%20of%20the%20Hardest-to-Drive%20Producing%20or%20Inventory%20Headphones%20to%20Reach%20110%20dB.png)

![Power Requirements of Some Headphones to Reach 110 dB](./analysis%20results/Power%20Requirements%20of%20Some%20Headphones%20to%20Reach%20110%20dB.png)

![Current Requirements of the Hardest-to-Drive Producing or Inventory Headphones to Reach 110 dB](./analysis%20results/Current%20Requirements%20of%20the%20Hardest-to-Drive%20Producing%20or%20Inventory%20Headphones%20to%20Reach%20110%20dB.png)

具体使用方法请参考该脚本内的注释和使用实例

# 任务清单

- 翻译 [zh-CN/knowledge](./zh-CN/Knowledge/) 中的文章
- [zh-CN/Knowledge/分析耳机的推力需求.md](./zh-CN/Knowledge/分析耳机的推力需求.md)
- 写一句话产品评论 [data/over-ear assessments cn.csv](./data/over-ear%20assessments%20cn.csv)
- …

欢迎任何贡献或投稿您的文章，我尊重你的著作权。如果您有任何问题或建议，无论多微不足道，都可以 [创建 Issue](https://github.com/Sha1rholder/Sound-Library/issues/new/choose) 或直接邮件联系我。感谢您的支持!
