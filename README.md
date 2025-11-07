English | [中文](./README%20zh-CN.md)

# What is Sound Library?

**Sound Library** is an acoustics knowledge base, dedicated to helping audiophiles and those interested in high-quality audio learn the knowledge of sound.

If you don't know how to get started or just want to have a glance, you can check this article [_Begin with Digital Audio_](./en-US/Knowledge/Begin%20with%20Digital%20Audio.md).

# Localized Contents

Folders named "en-US", "zh-CN", etc., contain localized content. Users from different regions can find content suitable for themselves in these folders. Currently, there is mainly localized content for mainland China, which includes over-ear headphone reviews, some essays, shopping guides, and knowledge bases. If you are interested in providing localized content or translations for other regions and languages, you are welcome to submit a PR.

For now, please find most of the localized content in the "zh-CN" folder.

# Data

## over-ear sensitivity official.csv

Official over-ear headphone sensitivity table. This table contains information such as the type of sound unit, official sensitivity, official impedance, whether it supports balanced input, the type of cavity (open/closed/semi-closed, etc.), and production status of some over-ear headphones. Since the production status and specifications of a pair of headphones may change (the specification changes of a product are really infuriating!), each piece of data has an addition date for reference.

Because 1. headphones have individual differences, the reproducibility of measurements is poor; 2. measurement equipments and standards of various manufacturers varies, and even the marked parameters may be wrong; 3. editors of this sheet may make mistakes when consulting and entering data; third-party test data may be quite different from official data. The meaning of comparing parameters between products from different manufacturers is limited. When there are rigorous third-party test data or detailed manufacturer test reports, please give priority to those.

## over-ear sensitivity asr.csv

Audio Science Review (ASR) over-ear headphone sensitivity table. [Audio Science Review Forum](https://www.audiosciencereview.com) is one of the more authoritative third-party audio equipment testing websites, and its test data is relatively rigorous. This table contains some data on the voltage (mVrms) needed to drive some ASR-tested over-ear headphones to 94 dBSPL and the impedance data at 1000 hz. If the impedance of the headphones varies greatly with frequency, the change trend of the impedance curve will be briefly summarized in the remarks.

# Analysis Tools & Results

This section contains some scripts and results for analyzing and visualizing data.

## over-ear sensitivity analysis.py

Used to analyze and compare the voltage and power requirements of headphones, it can draw a histogram of the voltage or power requirements to drive the headphones interested to a certain sound pressure level, which can be used as a reference to evaluate the difficulty of driving the headphones.

![Voltage Requirements of Some Headphones to Reach 96 dB](./analysis%20results/Voltage%20Requirements%20of%20Some%20Headphones%20to%20Reach%2096%20dB.png)

![Power Requirements of Some Headphones to Reach 96 dB](./analysis%20results/Power%20Requirements%20of%20Some%20Headphones%20to%20Reach%2096%20dB.png)

![Current Requirements of Some Headphones to Reach 96 dB](./analysis%20results/Current%20Requirements%20of%20Some%20Headphones%20to%20Reach%2096%20dB.png)

It can also be used to analyze the sensitivity, efficiency, and impedance distribution of all headphones ever documented in this database (though without data filtering, it's not particularly meaningful—just for fun).

![Sensitivity Distribution of All Headphones](./analysis%20results/sensitivity%20distribution.png)

![Efficiency Distribution of All Headphones](./analysis%20results/efficiency%20distribution.png)

![Impedance Distribution of All Headphones](./analysis%20results/impedance%20distribution.png)

For specific usage, please refer to the comments and the usage examples in the script.

# To-Do List

...

You are welcomed to contribute to this project or submit your own articles. Your copyright is paid respect here. If you have any questions or suggestions, no matter how insignificant, please feel free to [open an Issue](https://github.com/Sha1rholder/Sound-Library/issues/new) or email me. Thank you for your support!
