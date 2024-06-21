Assume the voltage sensitivity of a headphone is $S_{Vrms}(dB/Vrms)$, the power sensitivity is $S_{mW}(dB/mW)$, and the impedance is $R(Ω)$. They usually satisfy the following relationship:

$$S_{mW}=S_{Vrms}+10lgR-30$$

To drive a headphone to a loudness of $I(dB)$, the required power $P(mW)$ and equivalent voltage $U(Vrms)$ are respectively:

$$P=10^\frac{I-S_{mW}}{10}$$
$$U=10^\frac{I-S_{Vrms}}{20}$$

# Background Knowledge

Most headphones, including dynamic, planar, and electrostatic headphones, have a constant impedance at a constant frequency. The sound pressure (Pa) they produce is directly proportional to the equivalent voltage (Vrms). In other words, the ratio of sound pressure to voltage is a fixed value. We refer to this as **the Direct Proportionality between Sound Pressure and Equivalent Voltage**. That is:

$$\frac{P_1}{U_1}=\frac{P_2}{U_2}$$

The definition of Decibel Sound Pressure Level

$$I=20lg\frac{P}{P_0}$$

The definition of voltage sensitivity $S_{Vrms}$

$$S_{Vrms}=20lg\frac{P_{1Vrms}}{P_0}$$

The definition of power sensitivity $S_{mW}$

$$S_{mW}=20lg\frac{P_{1mW}}{P_0}$$

Where $I$ is the sound pressure level in decibels (dBSPL, abbreviated as dB); $P$ is the sound pressure in pascals (Pa); $P_0$ is the minimal audible sound pressure level, known as the Hearing Thresholdin, defined as $2*10^{-5}Pa$; $S$ is the sensitivity, that is, the loudness of the headphone at 1 Vrms or 1 mW, measured in dB/Vrms or dB/mW.

# Derivation

> For the convenience of subsequent calculations, the units were removed from the formulas.

First, according to **the Direct Proportionality between Sound Pressure and Equivalent Voltage** , when the voltage is 1 Vrms, the ratio of sound pressure to voltage should be equal to the ratio of sound pressure to power when the power is 1 mW. That is:

$$\frac{P_{1Vrms}(Pa)}{1(Vrms)}=\frac{P_{1mW}(Pa)}{U_{1mW}(Vrms)}$$

Substituting into the **definition of power sensitivity**, we get:

$$S_{mW}(dB/mW)=20lg\frac{P_{1Vrms}(Pa)*U_{1mW}(Vrms)}{P_0(Pa)}$$

After a simple transformation:
$$S_{mW}(dB/mW)=20lg\frac{P_{1Vrms}(Pa)}{P_0(Pa)}+20lgU_{1mW}(Vrms)$$

Then substitute the **definition of voltage sensitivity** into the above equation, we get:

$$S_{mW}(dB/mW)=S_{Vrms}(dB/Vrms)+20lgU_{1mW}(Vrms)$$

According to **Ohm's Law**:

$$P(W)=\frac{U^2(Vrms)}{R(Ω)}$$

After a slight transformation:

$$U(Vrms)=\sqrt{P(W)*R(Ω)}$$

Therefore, when the power is 1 mW:

$$U_{1mW}(Vrms)=\sqrt{10^{-3}(W)*R(Ω)}$$

Combining the above two formulas, we get:

$$S_{mW}(dB/mW)=S_{Vrms}(dB/Vrms)+20lg\sqrt{10^{-3}(W)*R(Ω)}$$

After a slight transformation:

$$S_{mW}(dB/mW)=S_{Vrms}(dB/Vrms)+10lgR(Ω)-30$$

Therefore, we can calculate the third parameter based on any two parameters of voltage sensitivity, power sensitivity, and impedance.
