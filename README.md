English / [中文](./README%20zh-CN.md)

# What is Sound Library?

**Sound Library** is an acoustics knowledge base, dedicated to helping audiophiles and those interested in high-quality audio understand the knowledge of sound playback.

If you don't know how to get started or just want to have a glance, you can check this article [_Conversion Relation between Sensitivities and Impedance of Headphones_](./en-US/Knowledge/Conversion%20Relation%20between%20Sensitivities%20and%20Impedance%20of%20Headphones.md).

# Localized Contents

Folders named "en-US", "zh-CN", etc., contain localized content. Users from different regions can find content suitable for themselves in these folders. Currently, there is mainly localized content for mainland China, which includes over-ear headphone reviews, some essays, shopping guides, and knowledge bases. If you are interested in providing localized content or translations for other regions and languages, you are welcome to submit a PR.

For now, please find most of the localized content in the "zh-CN" folder.

# Data

## over-ear sensitivity official.csv

Official over-ear headphone sensitivity table. This table contains information such as the type of sound unit, official sensitivity, official impedance, whether it supports balanced input, the type of cavity (open/closed/semi-closed, etc.), and production status of some over-ear headphones. Since the production status and specifications of a pair of headphones may change (the specification changes of a product are really infuriating!), each piece of data has an addition date for reference.

Because 1. The reproducibility of various indicators of electro-acoustic conversion equipment is very poor, and physical conditions vary. 2. The measurement equipment and measurement standards of various manufacturers are different, and even the marked parameters may be wrong. 3. The author may overlook when consulting and entering data, the third-party test data may be quite different from the official data. The meaning of comparing parameters between products from different manufacturers is limited. When there are rigorous third-party test data or detailed manufacturer test reports, please give priority to those results.

## over-ear sensitivity asr.csv

Audio Science Review (ASR) over-ear headphone sensitivity table. ASR is one of the more authoritative third-party audio equipment testing websites, and its test data is relatively rigorous. This table contains some data on the voltage (mVrms) needed to drive some ASR-tested over-ear headphones to 94dBSPL and the impedance data at 1000 hz. If the impedance of the headphones varies greatly with frequency, the change trend of the impedance curve will be briefly summarized in the remarks.

## over-ear assessments cn.csv

Over-ear headphone rating table (mainland China). This is the subjective rating, remarks, and rating date of the headphones by the contributors of this library. Each headphone can get 1 to 5 points. 0 points for not yet reviewed; 1 point for garbage, not recommended for purchase under any circumstances; 2 points for products with low cost performance, generally not recommended for purchase; 3 points for average products, can consider buying; 4 points for products with high cost performance, recommended for purchase; 5 points for almost perfect choices at this price point, strongly recommended.

The score mainly considers its price, sound quality, wearing comfort, workmanship, quality control, appearance, and after-sales at the time of scoring. Since the price of a pair of headphones may change, and the production line may also be updated, the scoring date is also an important reference factor. Generally speaking, the closer the scoring date, the more reference value the score has. Also, products with the same score do not mean that their product power is close. For example, Philips shp9500 and Sennheiser hd800s both get 3 points does not mean that their overall quality is similar. This score is a comprehensive consideration of its price and performance.

You may notice that some classic products like hd600 score low at 2 points. This is because this rating only focuses on the practicality and cost performance of these headphones, and does not consider their historical status. Many classic headphone products are objectively behind newer products in terms of workmanship, sound quality, and power requirements, and their competitiveness at the same price point is really not high.

Since the main contributors of this library are in mainland China, the scoring is based on the domestic price of the headphones and the warranty plan and reputation in the mainland China region. If you are in other parts of the world, the price of headphones and the warranty plan may be different, and the score will also be different.

# Analysis Tools & Results

## Over-ear sensitivity.py

Used to analyze and compare the voltage and power requirements of headphones, it can draw a histogram of the voltage or power requirements to drive the headphones interested to a certain sound pressure level, which can be used as a reference to evaluate the difficulty of driving the headphones.

![Voltage Requirements of the Hardest-to-Drive Producing or Inventory Planar Headphones to Reach 94 dB](./analysis%20results/Voltage%20Requirements%20of%20the%20Hardest-to-Drive%20Producing%20or%20Inventory%20Planar%20Headphones%20to%20Reach%2094%20dB.png)

![Power Requirements of the Easiest-to-Drive Producing or Inventory Closed-Back Headphones to Reach 110 dB](./analysis%20results/Power%20Requirements%20of%20the%20Easiest-to-Drive%20Producing%20or%20Inventory%20Closed-Back%20Headphones%20to%20Reach%20110%20dB.png)

![Comparing Voltage Requirements of Headphones to Reach 94 dB](./analysis%20results/Comparing%20Voltage%20Requirements%20of%20Headphones%20to%20Reach%2094%20dB.png)

![Comparing Power Requirements of Headphones to Reach 100 dB](./analysis%20results/Comparing%20Power%20Requirements%20of%20Headphones%20to%20Reach%20100%20dB.png)

For specific usage, please refer to the comments and the usage examples in the script.

# To-Do List

- Translate articles in [zh-CN/knowledge](./zh-CN/Knowledge/) to English
- [zh-CN/Knowledge/分析耳机的推力需求.md](./zh-CN/Knowledge/分析耳机的推力需求.md)
- Fill comments in [data/over-ear assessments cn.csv](./data/over-ear%20assessments%20cn.csv)
- ...

You are welcomed to contribute to this project. If you have any questions or suggestions, no matter how insignificant, please feel free to [open an Issue](https://github.com/Sha1rholder/Sound-Library/issues/new) or email me. Thank you for your support!
