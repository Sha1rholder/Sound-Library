import math
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import LogLocator

# read the fr of the headphone
headphone_fr = pd.read_csv(
    "./data/dt1990 freq.csv", dtype={"freq": float, "db l": float, "db r": float})
freq = headphone_fr["freq"]
freq_num = freq.count()
db_headphone = (headphone_fr["db l"]+headphone_fr["db r"])/2

# read the impedance curve of the headphone
headphone_impedance_data = pd.read_csv("./data/dt1990 impedance.csv")
freq_record = headphone_impedance_data["freq"]
impedance_record = headphone_impedance_data["impedance"]
freq_record_num = freq_record.count()
headphone_resistance = 250

# simulating an extremely low impedance case
impedance_reduction = 230
impedance_record -= impedance_reduction
headphone_resistance -= impedance_reduction

# calculate the impedance of the headphone at each frequency
impedance_headphone = []
i = 0
ii = 0
while i < freq_num and ii < freq_record_num-1:
    if freq[i] >= freq_record[ii] and freq[i] <= freq_record[ii+1]:
        impedance_headphone.append(
            freq[i] * (impedance_record[ii]+impedance_record[ii+1])/(freq_record[ii]+freq_record[ii+1]))
        i += 1
    else:
        ii += 1


# simulating a tube amp with extremely high output impedance
tube_reactance = 0.01*freq+100/freq
tube_resistance = 300

# simplify calculations
headphone_resistance_square = headphone_resistance**2
total_resistance = headphone_resistance + tube_resistance
total_resistance_square = total_resistance**2
tube_resistance_square = tube_resistance**2

# calculate fr of the headphone driven by the tube amp
db_tube = []
i = 0
while i < freq_num:
    db_tube.append(db_headphone[i] - 10*math.log10(total_resistance_square+(tube_reactance[i]+(
        impedance_headphone[i]**2-headphone_resistance_square)**0.5)**2)/(impedance_headphone[i]**2))
    i += 1

# plot
plt.figure(figsize=(16, 10))
plt.plot(freq, db_tube, label='Tube', color='red')
plt.plot(freq, db_headphone, label='Original', color='blue')
plt.xscale('log')
plt.xlim(20, 20000)

# custom X-axis scale
ax = plt.gca()
ax.xaxis.set_major_locator(LogLocator(base=10.0, subs=(
    1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0), numticks=10))
ax.xaxis.set_minor_locator(LogLocator(base=10.0, subs='auto', numticks=100))

plt.xlabel('Frequency (Hz)')
plt.ylabel('dB SPL')
plt.title('Frequency Response Curve')
plt.legend()
plt.grid(True, which='both', linestyle='--')
plt.savefig("./analysis results/extreme tube amp fr.png")
