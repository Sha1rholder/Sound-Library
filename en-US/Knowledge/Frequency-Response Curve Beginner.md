The Frequency-Response (FR) Curve illustrates the relationship between the sound pressure level produced by electroacoustic devices such as headphones and speakers, and the frequency. Its horizontal axis typically represents the logarithmic scale of the audible range for human ears, i.e., 20 to 20,000 Hz, while its vertical axis represents the variance in sound pressure level under sinusoidal alternating current electricity of different frequencies but the same intensity.

This article uses the FR and compensation curves of the Sennheiser HD800s provided by the frequency response query and EQ suggestion website [AutoEQ.app](https://www.autoeq.app) as an example to introduce how to interpret FR curve.

![freq](../../assets/freq%20example.png)  
The x-axis represents frequency, in Hz; the y-axis represents the relative intensity of the sound produced at a specific frequency, in dBSPL.

- Raw: The original FR curve. The FR of the same type of headphones may vary significantly under different test conditions, especially the results of the ultra-high frequency part.
- Error: The deviation curve. This result is the deviation between the original curve and the target curve. The higher the Error at a certain frequency band, the more this band is emphasized compared to the target curve; conversely, the more this band is weakened. A flatter Error curve usually means that the FR of these headphones is closer to the target curve.
- Target: The target FR curve. This curve is not the target tuning curve of a product, but the target of EQ adjustment. Harman curve is the most famous target curves.
- Equalizer: The EQ curve. This result is the compensation applied to the original curve using an equalizer, usually compensating for low frequencies when there are fewer and suppressing high frequencies when there are more. EqualizerAPO's GraphicEq is a typical software equalizer that can achieve EQ by adjusting the gain of each frequency band.
- Equalized: The post-EQ curve. This result is the superimposed result of the EQ curve and the original curve. This curve usually matches the target curve in the mid and low frequency bands, but there is often a difference in the high frequency.

Below is a non-authoritative frequency band division table provided by [Mixing Techniques > Audio Spectrum - Teach Me Audio](https://www.teachmeaudio.com/mixing/techniques/audio-spectrum)

| Frequency Range | Frequency Values |
| --------------- | ---------------- |
| sub-bass        | 20 - 60 Hz       |
| bass            | 60 - 250 Hz      |
| low midrange    | 250 - 500 Hz     |
| midrange        | 500 - 2000 Hz    |
| upper midrange  | 2000 - 4000 Hz   |
| presence        | 4000 - 6000 Hz   |
| brilliance      | 6000 - 20000 Hz  |

The FR curve can only reflect the tuning orientation of an acoustic product to a certain extent. The actual auditory perception is also affected by many factors beyond the FR, such as harmonics, and cannot be used to judge the quality of a product.
