We usually judge how difficulty it is to drive a certain headphone by its sensitivity and impedance, while sensitivity is further divided into voltage sensitivity (measured in dB/Vrms) and power sensitivity (measured in dB/mW).

Since some headphone manufacturers indicate sensitivity in dB/Vrms, while others indicate sensitivity in dB/mW (if only how many dB is mentioned, it usually refers to power sensitivity), we sometimes need to convert the two types of sensitivities to the same unit for comparison.

Editor has also prepared a small puzzle, which you will be able to solve after understanding this article.

![here comes mathemetics](../../resource/here%20comes%20mathemetics.jpg)

> mrima bought a new dynamic headphone and began reviewing it. He started by measuring the frequency response and discovered that the headphone is exactly 92 dB at 1 kHz and exactly 97 dB at 5 kHz. However, right after the measurement, he realized he forgot to record the voltage used for the frequency response test!
>
> Then, mrima used a 1 kHz sine wave to drive the headphone to exactly 94 dB and noted down the equivalent voltage as $U(mV)$. He continued to measure the impedance curve and found that the headphone had an impedance of $Z_1(Ω)$ at 1 kHz and $Z_2(Ω)$ at 5 kHz. After the measurements, mrima asked the manufacturer about the headphone's linear resistance and got an answer of $R(Ω)$.
>
> Assuming the headphone has good consistency and the internal resistance of the amplifier used is negligible, can you calculate the actual power required to drive the headphone to exactly 100 dB using a 5 kHz sine wave in mW?
>
> **(The answer is at the end)**

To achieve $I(dB)$ for a headphone, the required equivalent voltage $U(V)$ and actual power $P(mW)$ are given by:

$$
U=10^\frac{I-S_{V}}{20}\\
P=10^\frac{I-S_{mW}}{10}
$$

Assuming a headphone has a voltage sensitivity of $S_{V}(dB/V)$, power sensitivity of $S_{mW}(dB/mW)$, impedance $Z(Ω)$, and resistance $R(Ω)$, they satisfy the following relationship:

$$S_{mW}=S_{V}+20lg|Z|-10lgR-30$$

In most cases, the impedance and resistance of headphones are quite similar, i.e., $|Z|\approx R$. Therefore, the above equation can usually be simplified to:

$$S_{mW}=S_{V}+10lgR-30$$

# Basic Background Knowledge

Electrical Power Law:

$$
P=\frac{U^2}{R}\\
U=\sqrt{P*R}
$$

The sound pressure produced by headphones at a certain frequency is proportional to the equivalent voltage, known as the **proportional relationship between sound pressure and equivalent voltage**.

$$\frac{P_1}{U_1}=\frac{P_2}{U_2}$$

The definition of sound pressure level $I$ in decibels is:

$$I=20lg\frac{P}{P_0}$$

The definitions of voltage sensitivity $S_{V}$ and power sensitivity $S_{mW}$ are:

$$
S_{V}=20lg\frac{P_{1V}}{P_0}\\
S_{mW}=20lg\frac{P_{1mW}}{P_0}
$$

Where $I$ is the sound pressure level in decibels (dBSPL, abbreviated as dB); $P$ is the sound pressure in Pascals (Pa); $P_0$ is the minimum audible sound pressure level for humans, defined as $2*10^{-5}Pa$; $S_{V}$ and $S_{mW}$ are sensitivities, i.e., the sound pressure level of headphones at 1 V or 1 mW, respectively, in dB/V or dB/mW.

# Preliminary Derivation

> Understanding the following derivation requires knowledge of logarithmic operations and basic electrical principles.

By **subtracting the definition of voltage sensitivity from the definition of sound pressure level**, we obtain:

$$
I(dB)-S_{V}(dB/V)=20lg\frac{P(Pa)}{P_0(Pa)}-20lg\frac{P_{1V}(Pa)}{P_0(Pa)}\\
I(dB)-S_{V}(dB/V)=20lg\frac{P(Pa)}{P_{1V}(Pa)}
$$

Based on the **proportional relationship between sound pressure and equivalent voltage**, we can derive the equivalent voltage $U(V)$ needed to achieve $I(dB)$:

$$
I(dB)-S_{V}(dB/V)=20lg\frac{U(V)}{U_{1V}(V)}\\
U(V)=10^\frac{I(dB)-S_{V}(dB/V)}{20}
$$

---

By **subtracting the definition of power sensitivity from the definition of sound pressure level**, we obtain:

$$
I(dB)-S_{mW}(dB/mW)=20lg\frac{P(Pa)}{P_0(Pa)}-20lg\frac{P_{1mW}(Pa)}{P_0(Pa)}\\
I(dB)-S_{mW}(dB/mW)=20lg\frac{P(Pa)}{P_{1mW}(Pa)}
$$

Based on the **proportional relationship between sound pressure and equivalent voltage**, we can derive:

$I(dB)-S_{mW}(dB/mW)=20lg\frac{U(V)}{U_{1mW}(V)}$

Substituting the **Electrical Power Law** into the above equation, we can derive the actual power $P(mW)$ needed to achieve $I(dB)$:

$$
I(dB)-S_{mW}(dB/mW)=20lg\frac{\sqrt{P(mW)*R(Ω)}}{\sqrt{1(mW)*R(Ω)}}\\
P(mW)=10^\frac{I(dB)-S_{mW}(dB/mW)}{10}
$$

---

Based on the **proportional relationship between sound pressure and equivalent voltage**, we know that the ratio of sound pressure to voltage at 1 V is equal to the ratio of sound pressure to voltage at 1 mW:

$$\frac{P_{1V}(Pa)}{1(V)}=\frac{P_{1mW}(Pa)}{U_{1mW}(V)}$$

Substituting this into the **definition of power sensitivity**, we obtain:

$$
S_{mW}(dB/mW)=20lg\frac{P_{1V}(Pa)*U_{1mW}(V)}{P_0(Pa)}\\
S_{mW}(dB/mW)=20lg\frac{P_{1V}(Pa)}{P_0(Pa)}+20lgU_{1mW}(V)
$$

Substituting the **definition of voltage sensitivity** into the above equation, we obtain the **relationship between voltage sensitivity, power sensitivity, and the effective voltage at 1 mW actual power**:

$$S_{mW}(dB/mW)=S_{V}(dB/V)+20lgU_{1mW}(V)$$

According to the **Electrical Power Law**, when the power is 1 mW:

$$U_{1mW}(V)=\sqrt{10^{-3}(W)*R(Ω)}$$

Substituting this into the **relationship between voltage sensitivity, power sensitivity, and the effective voltage at 1 mW actual power**, we obtain:

$$
S_{mW}(dB/mW)=S_{V}(dB/V)+20lg\sqrt{10^{-3}(W)*R(Ω)}\\
S_{mW}(dB/mW)=S_{V}(dB/V)+10lgR(Ω)-30
$$

Therefore, when the resistance is approximately equal to the impedance, the conversion between voltage sensitivity and power sensitivity can be made based on the impedance.

# Advanced Background Knowledge

The power sensitivity of headphones usually refers to the sound pressure level of the headphones at an actual power of 1 mW. However, the power sensitivity calculated from the voltage sensitivity and impedance is the sound pressure level at a visible power of 1 mW, not the actual power. When the impedance is significantly higher than the linear resistance, the actual power will be significantly lower than the visible power, and in such cases, the conversion between voltage sensitivity and power sensitivity cannot be made based on the impedance alone.

The relationship between visible power $S$, actual power $P$, impedance $Z$, and resistance $R$ is:

$$\frac{S}{P}=\frac{Z}{R}$$

The relationship between visible power $S$, equivalent voltage $U$, and impedance $Z$ is:

$$
S=\frac{U^2}{Z}\\
U=\sqrt{S*Z}
$$

# Advanced Derivation

> Understanding the following derivation requires knowledge of complex number operations and the distinction between visible power and actual power.

According to the **relationship between visible power and actual power**, when the actual power is 1 mW:

$$\frac{S(W)}{10^{-3}(W)}=\frac{Z(Ω)}{R(Ω)}$$

Substituting this into the **relationship between visible power, voltage, and impedance**, we obtain:

$$U_{1mW}(V)=\sqrt{\frac{10^{-3}(W)*Z^2(Ω^2)}{R(Ω)}}$$

Substituting this into the **relationship between voltage sensitivity, power sensitivity, and the effective voltage at 1 mW actual power**, we obtain:

$$
S_{mW}(dB/mW)=S_{V}(dB/V)+20lg\sqrt{\frac{10^{-3}(W)*Z^2(Ω^2)}{R(Ω)}}\\
S_{mW}(dB/mW)=S_{V}(dB/V)+20lg|Z|(Ω)-10lgR(Ω)-30
$$

Therefore, the conversion between voltage sensitivity and power sensitivity can be made based on the linear resistance and impedance.

> Try to prove that the actual power $P(mW)$ required to achieve $I(dB)$ still satisfies $P=10^\frac{I-S_{mW}}{10}$ when the impedance is much greater than the linear resistance!

---

> **Answer:** $10^{-2.9}*U^2*R*Z_2^{-2}$ mW
