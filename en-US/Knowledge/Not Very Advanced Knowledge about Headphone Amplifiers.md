Headphone amplifiers amplify analog signal to drive headphones. This article will introduce some advanced knowledge of headphone amps for those who are interested in electroacoustics, and help you better choose the right headphone amp for you!

![lcd1](<../../assets/Popular%20Science%20and%20Miscellaneous%20Talks%20on%20Planar%20Magnetic%20Headphones%20(Part%202)/15.jpg>)  
Amplifier doesn't have to be a box or box with bulbs plugged on it. It's built in every audio device used to drive headphones.

# Output Power

One of the most important metrics of a headphone amp is its output power. This section explains the specific impact of power and its significance for audiophiles to choose headphone amp, as well as explaining the concept of gain.

## What is output power?

**Maximum Undistorted Output Power** = the maximum output power of an headphone amp when THD+N is < 1% or 0.1%, audiophiles often abbreviated as power.

![Fosi DS2 Power](../../assets/Fosi%20ds2.webp)

When driving a headphone whose impedance is over 32Ω, the maximum undistorted power of an amp will usually be lower with higher impedance, which indicates that the amplifier's maximum output voltage is limited. Below 32Ω, the power of an amp may be lower with lower impedance, which indicates that the maximum output current of the amp is limited.

**The power of an amp represents its ability to output voltage, current, and energy**

---

Headphones with lower sensitivities require more power and voltage. Clipping distortion will occur when power of the headphone amp is not enough to meet the headphone's need to reach a certain loudness.

[![Clipping Distortion](../../analysis%20results/clipping%20distortion.png)](../../analysis%20tools/clipping%20distortion%20simulator.py)

There are two types of clipping distortion: hard clipping and soft clipping. When hard clipping occurs, the vibration over a certain limit is like being clipped; soft clipping will be smoother in the transition of the clipping amplitude, and the degradation of the listening experience is less obvious. Hard clipping often occors when a transistor amp is experiencing current or voltage overload. Soft clipping happens in the same situation on tube amps.

![Hifiman Shangri-La](../../assets/shangri-la.jpg)

Since electronic tubes have lower native distortion than transistors and higher voltages (you read that right), they are ideal for use in High-End systems to drive high resistance headphones. As electrostatic headphones are essentially a type of headphone with ultra-high impedance, low power requirement, and extremely high voltage requirement, they are also very suitable for tube amps, such as Sennheiser Orpheus and Hifiman Shangri-La.

**It is worth noting that the maximum undistorted power labeled by the manufacturer is usually measured at 1000hz. Power in other frequency varies**.

## What is the use of output power?

**How much power does it take to drive a certain headphone?** There is no standard answer to this question.  
**Can a certain headphone amp drive a certain headphone?** As long as user enjoys music at normal healthy volume, then 99.9% of the time the amp is able to drive the headphone.

---

**Clipping distortion is not a concern in 99% of cases.**

The vast majority of digital audio for human listening is only 16bit deep, which means that the maximum loudness of music without quantization noise is only 96dB. As long as you listen to music at a volume above 96dB for one second, you're probably able to hear that background noise in the quietest part of the music.

Don't say that some classics with super high dynamic range may reach 110dB instantaneous loudness. There won't be a single moment of music you listen to on headphones that can reach the loudness of an airplane taking off. If it does, then Sennheiser is not what you need, what you need is Sennheiser's old man.

![Sonova](../../assets/sonova.webp)

Nowadays, there are more and more low-cost, small-sized, low-distortion, powerful headphone amps on the market, and even entry-level usb dongles can easily drive most headphones above 96dB. Theoretically, the 5 grams Fiio JA11 can drive HD800s to 102dB.

So what's the point of pursuing big thrust?

---

**Loud enough = be able to drive ≠ be able to drive well**

**More output power is not for more loudness, but for better distortion performance at normal volume levels.** For example, if a 800mW@32Ω amplifier and a 400mW@32Ω amplifier with similar design are connected to the same headphone and output the same volume, although they both output 1mW, the distortion performance of the former is more likely to be better than that of the latter.

This is because the nature of the amplifier is a transistor-based signal transmission device, and the linear relationship between the input and output of transistor triode tends to deteriorate as the signal strength increases, so the distortion of the amplifier tends to be more significant as the signal increases.

![triode](../../assets/triode.png)

In other words, **more powerful, less distortion**. This is one of the reasons why veteran audiophiles used to loud volumes are more likely to hear the difference between amps than average audiophiles. The louder the volume is turned up, the more noticeable the differences in the performance of headphone amps are.

**This section does not apply to tube amps and Class D amplifiers.**

## Characteristics of various headphone loads

Headphones vary greatly in sensitivity and impedance characteristics, so performs very different when being driven. As a result, headphone amps produce different distortion characteristics when driving different headphones, which is the origin of statements like “xx amp can't drive a planar headphone well, but performs good with a high-impedance dynamic headphone”, etc. The following table shows some examples of typical headphone loads. The following table shows some examples of how some typical headphones require amps.

| Headphone     | Load                                                                  | Voltage Demand | Current Demand |
| ------------- | --------------------------------------------------------------------- | -------------- | -------------- |
| Empty Load    | Equal to open circuit                                                 |                |                |
| HD800s、HD600 | Dynamic headphone with high impedance                                 | ⭐⭐⭐⭐⭐     | ⭐             |
| Utopia        | Dynamic headphone with low nominal impedance but high peak impedance  | ⭐⭐⭐⭐       | ⭐             |
| AR5000、FT1   | Dynamic headphone with low nominal impedance and flat impedance curve | ⭐             | ⭐⭐           |
| MM100         | Planar headphone with low impedance and high power sensitivity        | ⭐             | ⭐⭐           |
| Edition XS    | Planar headphone with low impedance and lower power sensitivity       | ⭐             | ⭐⭐⭐         |
| Susvara       | Planar headphone with low impedance and super low power sensitivity   | ⭐⭐⭐         | ⭐⭐⭐⭐⭐     |

As you can see, different types of headphones have different demands on various capabilities of amps. Among them, dynamic headphones with high nominal impedance or peak impedance are expecially voltage-demanding. Though some planar headphones such as the Susvara, which is known as super hard to drive, have lower voltage sensitivity than traditional high-impedance dynamic headphones such as the HD800s, the latter may have higher voltage demand. This is because high-impedance dynamic headphones tend to have significant inductance. The inductance brings significant back electromotive force while being driven, and leads to phase problem. To ease this phase problem, higher voltage output capacity of headphone amps is required to drive these high-impedance dynamic headphones.

## How to drive a headphone "well"?

Audiophiles argue about how much power is required to drive a headphone well. There's a rumor that “Headphones are harder to drive in bass and have fewer bass with not enough power.”

In fact, most headphone amps don't change the fr (frequency response) of headphones. Bass strength doesn't vary with power.

![iPhone6s driving HD800s](../../assets/iphone6s%20driving%20800s.png)  
[_Is iPhone able to drive HD800s?!_ - Zhihu 村姑阳子](https://zhuanlan.zhihu.com/p/51180207)

This rumor comes from various reasons. First of all, energy of music concentrates in low frequencies, so it's easier to notice the distortion performance in bass.

[![Hotel California Energy Distribution 1](<../../analysis%20results/freq%20power%20spectrum%20of%20Hotel%20California%20(Live%20On%20MTV,%201994).png>)  
![Hotel California Energy Distribution 2](<../../analysis%20results/power%20spectrum%20of%20Hotel%20California%20(Live%20On%20MTV,%201994).png>)](../../analysis%20tools/power%20analysis%20of%20music.py)  
The energy distribution in frequencies of Hotel California supports this.

On the other hand, dynamic headphones are prone to resonance at low frequencies, resulting in a sharp increase in inductive reactance. A peak in the impedance curve (f0) indicates the phenomenon, which may leads to increased phase shift in specific frequency bands. If the amplifier's control over this phase distortion is bad, it may produce a weird listening experience.

[![HD800s Impedance Curve](../../assets/hd800s%20impedance%20curve.jpg)](https://reference-audio-analyzer.pro/en/param14.php?&tit_head=1&tit_graph=6&tit_channel=2&idr0=706&idmain=706&report_page=2&chanell=2&hdnx=0&tpdisp=st&idu=0&format=2&vstyle=0&n_canvas=1&lng=eng)

---

The essence of **"Is xx amp able to drive xx headphone well?"** is actually audiophile's subjective evaluation of the sound of a headphone system, which current development of psychoacoustic is unable to tell. Not yet any objective standard. The so-called “over-drive 过推” and “can't drive well” are essentially the same, just the words of audiophile who's not satisfied with a certain headphone system.

![headphone amp coordinates](../../assets/headphone%20amp%20coordinates.png)

Again, **Loud enough = be able to drive ≠ be able to drive well**. Building a Hi-Fi headphone system is an example of Cannikin's law. In 99% of cases, amp is not the shortest board, while headphone is.

![Focal sounds good when amp is bad](../../assets/focal%20sounds%20good%20when%20amp%20is%20bad.png)  
[《【茶音社 HIFI 月报】北京耳机展特别作战记录！（上篇）》- Bilibili](https://www.bilibili.com/video/BV1HG411R7bb)

## What is gain?

There's a huge difference in the sensitivities of different speakers and headphones, and to make them reach a certain volume, the volume knob is often screwed to an extreme position, which is not only inconvenient, but also prone to sound bias caused by potentiometer at low volumes.

For this reason, it is common for modern amplifiers to have both gain and volume adjustments. **The purpose of gain is to provide right volume range for speakers and headphones of all sensitivities**.

The graph below shows some of the output power parameters of Fiio K19.

![K19 Power](../../assets/k19%20power.png)

We can interpret from this table that a higher gain magnifies the output power of this amp, and therefore the distortion performance may be better at the same load. However, at 16Ω load, higher gain does not increase the maximum output power. This is because the current hits the maximum before the voltage does.

We also found that the signal-to-noise ratio (SNR) is greater at higher gain, which is misleading as the SNR is measured at maximum output. With a higher signal strength, SNR is naturally higher, but at a certain volume, higher gain is usually accompanied by a higher noise floor. However, the noise floor of a modern headphone amp should be inaudible, so this is usually not a problem.

![Lena Noise](../../assets/lena%20noise.jpg)

Modern headphone amps are designed in a variety of ways, so does the implementation of gain. Thus, **the exact effect of gain varies**. Since modern headphone amps generally have super low noise, there is usually no need for separate noise suppression measures for high-sensitivity headphones. **Sometimes adjusting gain is simply a matter of changing the volume adjustment step size and upper limit, with completely no effect on sound quality**.

In the case of K19, "Low", "Medium" and "High" gain are software- and affect neither distortion nor noise; while "Super High" and "Ultra High" gain are hardware-implemented as the traditional sense, and may have a real impact on the sound quality.

# Distortion

Distortion is the alteration of original signal. Distortion is the essence of the difference of headphone amps' sound.

Insufficient output power causes distortion. Enough output power is also accompanied by distortion. Where does distortion come from? How does distortion affect subjective listening experience? Read this section to unveil the distortion and the measurements of distortion.

![The Scream](../../assets/the%20scream.jpg)

## Frequency-Response Distortion

Frequency-response distortion (fr distortion) is a type of linear distortion, i.e., it does not produce extra frequencies which doesn't exist in the original signal. Fr distortion refers to the gain difference of frequencies. In other words, not-flat frequency response (fr) curve. Fr is one of the most basic indicators of headphone amps.

[![fr distortion](../../analysis%20results/fr%20distortion.png)](../../analysis%20tools/fr%20distortion%20simulator.py)  
Fig. 1. Input signal to the amplifier.  
Fig. 2. Decomposition of the input signal.  
Fig. 3. Distorted signal.  
Fig. 4. 1dB gain difference between 100hz and 1000hz signals found by decomposing the distorted signal.

[![k19 fr](../../assets/k19%20fr.png)](https://fiio.com/k19_parameters)

This figure shows the fr of K19. As you can see it's flat in 20-20000Hz. If K19's fr doesn't vary with load, the fr of the headphone it's driving won't change significantly either. In other words, the headphone will sound more "original".

Not all headphone amps have a flat fr. **Some unique-sounding amps which hide their fr from customers may have done some thing to it**.

## Harmonic distortion

Harmonic distortion is the most common type of nonlinear distortion. Nonlinear distortion, i.e., distortion that produce frequency which the original signal doesn't have. Harmonic distortion refers to the phenomenon that output signal contains harmonic of input frequency. Total harmonic distortion (THD) is one of the most valued indicators for modern audiophiles.

[![harmonic distortion](../../analysis%20results/harmonic%20distortion.png)](../../analysis%20tools/harmonic%20distortion%20simulator.py)  
Fig. 1. Comparison chart of input signal and odd harmonic distorted signal.  
Fig. 2. Decomposition of odd harmonic distorted signal.  
Fig. 3. Comparison chart of input signal and even harmonic distorted signal.  
Fig. 4. Decomposition of even harmonic distorted signal.

Since harmonic distortion is rather noticable in hearing and the measurement method is very mature and easy to understand, audiophiles know pretty much about it. Thus modern "scientific" headphone amps tend to reach a very low harmonic distortion.

I heard that before the rise of Chinese "scientific" headphone amps (like Topping's and SMSL's), dac and amplifier manufacturers in China love to boast with slogans like "We applied xxx technology and reduced xxx much of harmonic distortion" so much that at that time academism audiophiles took THD as the golden rule for measuring sound quality.

![None Distortion!](../../assets/none%20distortion.jpg)

---<!--  -->

Harmonic distortion is divided into odd and even harmonic distortion. Audiophiles generally believe that odd harmonic distortion is much worse for listening than even harmonic distortion, and there are even those who believe that “even harmonic distortion is the source of the warm, pleasant sound of a gallbladder” to the extent that it is not the end of the story, or the other side of the coin. However, the relationship between sound and psychological mapping is extremely complex\*\*, and all kinds of harmonic distortion are important factors in the composition of timbre!

! [Stimulator] (... /... /assets/actuator.jpg)  
An exciter is an effector that uses harmonic distortion to adjust timbre by combining odd and even harmonics to produce a variety of subjective listening sensations.

The essential reason why gallows have not been phased out by stoners is the high linearity of tubes; linearity is antithetical to any distortion, and buying a gallows for the sake of even-order harmonic distortion is akin to buying a box. If you really like the richness of even harmonic tones, why not add a dsp in front of a lower priced, better spec'd stone machine to add and customize your own harmonic distortion?

! [Gallbladders & Stones](...) /... /assets/tube%20and%20transistor.jpg)

If one believes in arbitrary superiority or inferiority, and scoffs at stone machines, while leaving the even harmonic distortion of gallows completely unchecked, and calling it “gallows flavor”, one can be said to be going against the grain of the original intent of **Hi**gh-**Fi**delity!

## Cross-over distortion and temperature drift

Cross-over distortion is a type of non-linear distortion commonly found in Class B amplifiers. This type of amplifier uses a push-pull structure to increase efficiency, causing the output signal to become distorted at the crossover point, where the rising and falling edges of the output signal are asymmetrical.

Class A and B (Class AB) amplifiers are amplifiers that operate in Class A (Class A) at low power and in Class B at high power. Its crossover distortion is only visible when it reaches a certain power level.

[The cross over distortion is only visible at a certain power level. [crossover distortion](...) /... /analysis%20results/crossover%20distortion.png)](... /... /analysis%20tools/crossover%20distortion%20simulator.py)

Most amplifiers used to drive speakers these days are either Class D or Class A or B. There are quite a few pure Class A amplifiers due to the low power consumption of earphones. Pure Class A amplifiers are very inefficient and consume a lot of power, so you need to pay attention to heat dissipation and beware of the effect of temperature on component life and performance. If heat dissipation is poor, components such as transistors may be damaged or suffer from temperature drift, a condition in which performance deviates from ideal conditions due to temperature changes. However, there are some pure-A earphones specifically designed to operate at high temperatures, such as the Burson Soloist Voyager

! [Big A and A-B] (<... /... /assets/Popular%20Science%20and%20Miscellaneous%20Talks%20on%20Planar%20Magnetic%20Headphones%20(Part%201)/51.jpg>)  
Upper left: Fiona K19, a class A and B amplifier designed to operate at room temperature.  
Bottom left: Burson Soloist Voyager, a large A amplifier designed to work at high temperatures, with warm-up required for optimal sound quality.  
Top right: Aurel X1s GT, Big A  
Bottom right: Aurel S17pro, a big A that avoids overheating through heat dissipation

The human ear is highly sensitive to transverse distortion, so high-end ear amplifiers are mostly pure Armor. With similar materials, Class B amplifiers will have more thrust than Class A. Since Class B is more energy efficient, it is also less affected by temperature drift. Therefore, there is no difference between Class A and Class B. There is only a difference between suitable and unsuitable.

## “Polyphonic Distortion”

“Multi-tone distortion is a term I made up to differentiate between simple single-signal distortion and distortion involving multiple signals, so don't worry about it. This section describes harmonic distortion, clipping distortion, and distortion other than noise.

---.

Phase distortion is a type of linear distortion that refers to the distortion of the phase of the input signal by the earphone, in other words, the time difference between the output of various frequencies.

[! [phase distortion] (... /... /analysis%20results/phase%20distortion.png)](... /... /analysis%20tools/phase%20distortion%20simulator.py)  
Figure 1: Input signal to the amplifier.  
Figure ②: Decomposition of the input signal  
Figure 3: Phase distortion signal  
Figure 4: Phase difference between 100hz and 1000hz signals found by decomposing the distorted signal.

---.

Intermodulation distortion is a kind of nonlinear distortion, which refers to the distortion caused by different frequency signals interacting with each other to produce frequencies that do not exist in the input signal.

[! [intermodulation distortion](...) /... /analysis%20results/intermodulation%20distortion.png)](... /... /analysis%20tools/intermodulation%20distortion%20simulator.py)  
Figure 1: Input signal to the amplifier.  
Figure 2: Decomposition of the input signal  
Figure 3: Intermodulation distortion signal  
Fig. 4: The decomposition of the distorted signal reveals that there are more sum and difference signals in addition to the 800hz and 1000hz signals.

## Output Impedance

Not all of the voltage output from the amplifier can be poured into the headphones, part of the energy will be absorbed by the amplifier's own output impedance, which will cause all kinds of problems!

! [Voyager interface](...) /... /assets/voyager%20out.jpg)

The output impedance causes frequency response distortion in the audio system and is not reflected in the frequency response curve of the earphone amplifier itself. If headphones have different impedances at different frequencies (e.g. all moving coil headphones and very few flat panel headphones), then an earphone amplifier with a high output impedance will distribute less voltage to the headphones at frequencies where the headphones have a lower impedance, resulting in a change in the frequency response of the entire headphone system.

The Sennheiser HDV820 is a typical example of an amplifier that has a flat frequency response but can be distorted due to high output impedance. The image below is taken from the HDV820 review on the ASR forums.

[! [HDV820 Frequency Response and Impedance](...) /assets/hdv820 frequency response and impedance.png)](https://www.audiosciencereview.com/forum/index.php?threads/sennheiser-hdv-820-usb-dac-headphone-amp- review.10393)

Similarly, output impedance can cause “polyphonic distortion” with its inductive, capacitive, and resistive characteristics, and this gets complicated. However, toxicity is not a good idea, and modern stone machines generally have very low internal resistance, so these problems have very little effect!

Gallows usually have high output impedance, high output impedance caused by all kinds of distortion is one of the sources of the unique tone of the gallows. Nowadays, there are also some manufacturers who use “front and rear stone”, impedance selection, etc. to realize the “modern sound” of the gallows.

## Distortion Measurement and Psychoacoustics

Non-linear distortion can be categorized into many types depending on the source, characteristics, etc., and each has its own measurement index and method. Interpretation of the various distortion indicators requires a certain degree of specialized knowledge, and will not be repeated here. In this section, we will only talk about some of the most representative indicators.

The most representative indicators will be discussed in this section. [APx555](... /... /assets/apx555.png)

**SINAD (Signal to noise and distortion ratio)** is the most important indicator of an earphone amplifier, including all the components that make up noise and distortion. SINAD at a given load is the best single measure of an ear amplifier's **acoustic reproduction** performance.

However, SINAD does not represent the **psychoacoustic reproduction** performance of an ear amplifier. This is because the human ear is sensitive to different types of distortion, e.g. the human ear is particularly sensitive to transient intermodulation and crossover distortion, and less sensitive to phase distortion, and an ear amplifier with the same SINAD may sound very different depending on the type of distortion!

---SINAD

**Transient intermodulation distortion** is a concept that is very popular amongst the more advanced sections of hi. This type of distortion is usually caused by negative feedback hysteresis, and manifests itself in measurements as phase and nonlinear distortion problems with multi-tone signals, and can be very well visualized in square wave tests!

! [Square Wave Testing](... /... /assets/square%20wave%20test.png)  
Square wave test (time-amplitude)

However, square waves don't exist in nature as instantaneous spikes or drops, and pure square waves are not a direct measure of transient intermodulation distortion, so they don't reflect any metrics and don't represent any performance. The square wave test is more of a visual demonstration to show the consumer how much muscle you have, like maximum undistorted power!

Note that transient intermodulation distortion is only one source of distortion, and does not directly correspond to subjective listening experience. For example, transient intermodulation distortion includes distortion caused by insufficient swing rate, poor power supply, and deep negative feedback, but their waveform characteristics are different from each other. **Transient intermodulation distortion does not directly correspond to the subjective “transients” **sometimes the subjective “transients” are just some harmonic excitation effects!

! [Virtual Bass Enhancement System](...) /... /assets/virtual%20bass%20system.gif)  
A low-frequency transient enhancement system

Some enthusiasts take transient intermodulation distortion as a standard, take a square wave test and equate it to the transient response performance of the ear amplifier, and subjectively attribute the subjective “high-frequency chaos”, “false dynamics” and “poor transients” to the negative feedback. Listening feeling is simply attributed to negative feedback, and even extended to the conclusion that “THD indicators good-looking scientific machine are transient poor impotence sound”, is extremely irresponsible!

---

How to look at various measurements is a typical characterization of the distinction between science hi and metaphysical old burners. The old burner criticizes hi for blindly following measurements instead of subjective hearing, while hi criticizes the old burner for blindly following subjective hearing instead of measurements. ...... I can't say much about these two kinds of people 🙂 !

! [5128](... /... /assets/5128.webp)

The causes of distortion in earphones and their impact on subjective listening perception are diverse, they influence each other, intermingle and depend on each other, and they are also reflected in various measurement metrics at the same time. Therefore, a dialectical view of the measurement indicators, do not blindly pursue a certain data, do not impose cause and effect for the subjective sense of hearing and test indicators, is the correct attitude towards electroacoustics, psychoacoustics and audio audiophile!

**Listening to the sound is sound, listening to the sound is not sound, listening to the sound is still sound **  
\*\*Looking at a measurement indicator is a measurement indicator, looking at a measurement indicator is not a measurement indicator, looking at a measurement indicator is still a measurement indicator

! [Human technological development is not very advanced](...) /assets/the-development-of-human-technology-is-not-very-advanced.jpg)

# How to talk to audiophiles about earplugs

Audiophiles communicate with each other to form the Hi-Fi circle, which is a circle full of all kinds of anti-intellectual statements, robber baron logic and hate speech, full of pseudoscience, leek cutting, cult followers and all kinds of strange people. The following should not only be the conduct of audiophiles, but also a tool to deal with some exchanges with gunpowder flavor!

! [I see you are listening to the sound view owes the corrections is it] (...) /assets/ I think you are listening to the sound view is not correct, right.jpg)

0. ~~ The most important thing to talk to an audiophile is that your equipment is more expensive than his.

1. Responsible communication, do not think that their ears are beryllium suspension diaphragm, can not hear the difference is not shameful. Modern audio products are highly developed in the case of psychological factors on the subjective sense of hearing significantly greater than the difference between the sound of the equipment

2. Your ears have not been trained to make the connection between subjective listening perception and objective factors. Nine times out of ten, judgments such as “bile,” “r2r sound,” “digital sound,” “hairy power supply,” and so on are impositions of Cause and effect. Let's talk about subjective listening, not superficial science; if you have to, add adverbs of degree!

3. Don't despise other people's subjective sense of hearing, and don't assume that they are wrong just because they have a different sense of hearing than you do. The subjective sense of hearing is influenced by psychological, environmental, physiological structure differences, objective sound and other factors, there is no right or wrong to say!

4. Do not cloud! Cloud to the sense of hearing is not your sense of hearing, the cloud audition to comment on the equipment or even to other enthusiasts to make recommendations is extremely irresponsible!

5. don't persuade people to spend more money unless they are seeking advice from you. the Hi-Fi world is essentially a luxury world, and it's not worth it to squeeze your wallet for it!

**We always pretend to know a lot more about audio than we really do.**

# Reference

Plomp R, Steeneken HJ. Effect of phase on the timbre of complex tones. J Acoust Soc Am. 1969 Aug;46(2):409-21. doi: 10.1121/1.1911705. PMID: 5804112.

J. Lohstroh and M. Otala, "An audio power amplifier for ultimate quality requirements," in IEEE Transactions on Audio and Electroacoustics, vol. 21, no. 6, pp. 545-551, December 1973, doi: 10.1109/TAU.1973.1162523.

Leinonen, Eero et al. “Method for Measuring Transient Intermodulation Distortion (TIM).” Journal of The Audio Engineering Society 25 (1976): 170-177.

J. Lohstroh and M. Otala, "An audio power amplifier for ultimate quality requirements," in IEEE Transactions on Audio and Electroacoustics, vol. 21, no. 6, pp. 545-551, December 1973, doi: 10.1109/TAU.1973.1162523.

Herzog, Stephan; Investigations of the Effects of Nonlinear Distortions on Psychoacoustical Measures [PDF]; TU Kaiserslautern, Kaiserslautern, Germany; Paper 7751; 2009 Available: https://aes2.org/publications/elibrary-page/?id=14947

H. Mu, W. -S. Gan and E. -L. Tan, "A psychoacoustic bass enhancement system with improved transient and steady-state performance," 2012 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), Kyoto, Japan, 2012, pp. 141-144, doi: 10.1109/ICASSP.2012.6287837.
