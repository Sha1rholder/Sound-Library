import sys
import math
import matplotlib.pyplot as plt
import pandas as pd


def plot_voltage_needed(
    headphones,
    title="Voltage Requirement of the Headphones to reach 94 dB",
    target_db=94,
    beginner=0,
    max_shown=30,
    order=True,
    scale="log",
):
    voltage_data = []
    for headphone in headphones:
        voltage_needed = headphone.voltage_needed_official(target_db=target_db)
        if voltage_needed:
            voltage_data.append(
                (
                    f"{headphone.brand} {headphone.model}",
                    voltage_needed,
                    headphone.balance,
                )
            )
        voltage_needed = headphone.voltage_needed_asr(target_db=target_db)
        if voltage_needed:
            voltage_data.append(
                (
                    f"{headphone.brand} {headphone.model} ASR",
                    voltage_needed,
                    headphone.balance,
                )
            )
    voltage_data.sort(key=lambda x: x[1], reverse=not order)

    if beginner > len(voltage_data):
        print("Beginner is too large.")
        return
    elif beginner == 0:
        voltage_data = voltage_data[-max_shown:]
    else:
        voltage_data = voltage_data[-beginner - max_shown : -beginner]

    model, voltages, balance = zip(*voltage_data)
    bars = plt.barh(
        model, voltages, color=["blue" if b == "yes" else "red" for b in balance]
    )
    for bar in bars:
        width = bar.get_width()
        plt.text(
            width, bar.get_y() + bar.get_height() / 2, f"{round(width)}", va="center"
        )
    plt.xlabel("Voltage (Vrms) on Logarithmic Scale")
    plt.title(title)
    plt.xscale(scale)
    plt.show()


def plot_power_needed(
    headphones,
    title="Voltage Requirement of the Headphones to reach 94 dB",
    target_db=94,
    beginner=0,
    max_shown=30,
    order=True,
    scale="log",
):
    power_data = []
    for headphone in headphones:
        power_needed = headphone.power_needed_official(target_db=target_db)
        if power_needed:
            power_data.append(
                (
                    f"{headphone.brand} {headphone.model}",
                    power_needed,
                    headphone.balance,
                )
            )
        power_needed = headphone.power_needed_asr(target_db=target_db)
        if power_needed:
            power_data.append(
                (
                    f"{headphone.brand} {headphone.model} ASR",
                    power_needed,
                    headphone.balance,
                )
            )
        else:
            power_needed = headphone.power_needed_asr_voltage_official_impedance(
                target_db
            )
            if power_needed:
                power_data.append(
                    (
                        f"{headphone.brand} {headphone.model} ASR (official impedance)",
                        power_needed,
                        headphone.balance,
                    )
                )
    power_data.sort(key=lambda x: x[1], reverse=not order)

    if beginner > len(power_data):
        print("Beginner is too large.")
        return
    elif beginner == 0:
        power_data = power_data[-max_shown:]
    else:
        power_data = power_data[-beginner - max_shown : -beginner]

    headphones, power, balance = zip(*power_data)
    bars = plt.barh(
        headphones, power, color=["blue" if b == "yes" else "red" for b in balance]
    )
    for bar in bars:
        width = bar.get_width()
        plt.text(
            width,
            bar.get_y() + bar.get_height() / 2,
            "{:.3g}".format(width),
            va="center",
        )
    plt.xlabel("Power (mW) on Logarithmic Scale")
    plt.title(title)
    plt.xscale(scale)
    plt.show()


def compare_voltage(
    target,
    reference_headphones_official,
    reference_headphones_asr,
    headphones,
    title="Comparing Voltage Requirements of Headphones to Reach 94 dB",
    target_db=94,
    order=True,
    scale="log",
):
    voltage_data = []
    for brand in reference_headphones_official:
        for model in reference_headphones_official[brand]:
            for headphone in headphones:
                if headphone.brand == brand and headphone.model == model:
                    voltage_needed = headphone.voltage_needed_official(
                        target_db=target_db
                    )
                    if voltage_needed:
                        voltage_data.append(
                            (
                                f"{brand} {model}",
                                voltage_needed,
                                headphone.balance,
                                False,
                            )
                        )
    for brand in reference_headphones_asr:
        for model in reference_headphones_asr[brand]:
            for headphone in headphones:
                if headphone.brand == brand and headphone.model == model:
                    voltage_needed = headphone.voltage_needed_asr(target_db=target_db)
                    if voltage_needed:
                        voltage_data.append(
                            (
                                f"{brand} {model} ASR",
                                headphone.voltage_needed_asr(target_db=target_db),
                                headphone.balance,
                                False,
                            )
                        )
    for brand in target:
        for model in target[brand]:
            for headphone in headphones:
                if headphone.brand == brand and headphone.model == model:
                    voltage_needed = headphone.voltage_needed_official(
                        target_db=target_db
                    )
                    if voltage_needed:
                        voltage_data.append(
                            (
                                f"{brand} {model}",
                                voltage_needed,
                                headphone.balance,
                                True,
                            )
                        )
                    voltage_needed = headphone.voltage_needed_asr(target_db=target_db)
                    if voltage_needed:
                        voltage_data.append(
                            (
                                f"{brand} {model} ASR",
                                voltage_needed,
                                headphone.balance,
                                True,
                            )
                        )
    voltage_data.sort(key=lambda x: x[1], reverse=not order)

    model, voltages, balance, is_target = zip(*voltage_data)
    color = []
    for b, t in zip(balance, is_target):
        if t:
            color.append("green")
        else:
            color.append("blue" if b == "yes" else "red")
    bars = plt.barh(model, voltages, color=color)
    for bar in bars:
        width = bar.get_width()
        plt.text(
            width, bar.get_y() + bar.get_height() / 2, f"{round(width)}", va="center"
        )
    plt.xlabel("Voltage (Vrms) on Logarithmic Scale")
    plt.title(title)
    plt.xscale(scale)
    plt.show()


def compare_power(
    target,
    reference_headphones_official,
    reference_headphones_asr,
    headphones,
    title="Comparing Power Requirements of Headphones to Reach 94 dB",
    target_db=94,
    order=True,
    scale="log",
):
    power_data = []
    for brand in reference_headphones_official:
        for model in reference_headphones_official[brand]:
            for headphone in headphones:
                if headphone.brand == brand and headphone.model == model:
                    power_needed = headphone.power_needed_official(target_db=target_db)
                    if power_needed:
                        power_data.append(
                            (
                                f"{brand} {model}",
                                power_needed,
                                headphone.balance,
                                False,
                            )
                        )
    for brand in reference_headphones_asr:
        for model in reference_headphones_asr[brand]:
            for headphone in headphones:
                if headphone.brand == brand and headphone.model == model:
                    power_needed = headphone.power_needed_asr(target_db=target_db)
                    if power_needed:
                        power_data.append(
                            (
                                f"{brand} {model} ASR",
                                power_needed,
                                headphone.balance,
                                False,
                            )
                        )
                    else:
                        power_needed = (
                            headphone.power_needed_asr_voltage_official_impedance(
                                target_db
                            )
                        )
                        if power_needed:
                            power_data.append(
                                (
                                    f"{brand} {model} ASR (official impedance)",
                                    power_needed,
                                    headphone.balance,
                                    False,
                                )
                            )
    for brand in target:
        for model in target[brand]:
            for headphone in headphones:
                if headphone.brand == brand and headphone.model == model:
                    power_needed = headphone.power_needed_official(target_db=target_db)
                    if power_needed:
                        power_data.append(
                            (
                                f"{brand} {model}",
                                power_needed,
                                headphone.balance,
                                True,
                            )
                        )
                    power_needed = headphone.power_needed_asr(target_db=target_db)
                    if power_needed:
                        power_data.append(
                            (
                                f"{brand} {model} ASR",
                                power_needed,
                                headphone.balance,
                                True,
                            )
                        )
                    else:
                        power_needed = (
                            headphone.power_needed_asr_voltage_official_impedance(
                                target_db
                            )
                        )
                        if power_needed:
                            power_data.append(
                                (
                                    f"{brand} {model} ASR (official impedance)",
                                    power_needed,
                                    headphone.balance,
                                    True,
                                )
                            )
    power_data.sort(key=lambda x: x[1], reverse=not order)

    model, powers, balance, is_target = zip(*power_data)
    color = []
    for b, t in zip(balance, is_target):
        if t:
            color.append("green")
        else:
            color.append("blue" if b == "yes" else "red")
    bars = plt.barh(model, powers, color=color)
    for bar in bars:
        width = bar.get_width()
        plt.text(
            width,
            bar.get_y() + bar.get_height() / 2,
            "{:.3g}".format(width),
            va="center",
        )
    plt.xlabel("Power (mW) on Logarithmic Scale")
    plt.title(title)
    plt.xscale(scale)
    plt.show()


class Headphone:
    def __init__(
        self,
        brand,
        model,
        driver=None,
        official_db_mw=None,
        official_db_vrms=None,
        official_impedance=None,
        balance=None,
        back=None,
        production=None,
        official_note=None,
        asr_94db_voltage=None,
        asr_impedance=None,
        asr_note=None,
    ):
        self.brand = brand
        self.model = model
        self.driver = driver
        self.official_db_mw = official_db_mw
        self.official_db_vrms = official_db_vrms
        self.official_impedance = official_impedance
        self.balance = balance
        self.back = back
        self.production = production
        self.official_note = official_note
        self.asr_94db_voltage = asr_94db_voltage
        self.asr_impedance = asr_impedance
        self.asr_note = asr_note

    def print_original_info(self):
        for attr, value in self.__dict__.items():
            print(f"{attr}: {value}")

    def voltage_needed_official(self, target_db=94):
        if not math.isnan(self.official_db_vrms):
            return (10 ** ((target_db - self.official_db_vrms) / 20)) * 1000
        elif not math.isnan(self.official_db_mw) and not math.isnan(
            self.official_impedance
        ):
            return (
                10
                ** (
                    (
                        target_db
                        - self.official_db_mw
                        - 30
                        + 10 * math.log10(self.official_impedance)
                    )
                    / 20
                )
                * 1000
            )

    def voltage_needed_asr(self, target_db=94):
        if self.asr_94db_voltage:
            return 10 ** ((target_db - 94) / 20) * self.asr_94db_voltage

    def power_needed_official(self, target_db=94):
        if not math.isnan(self.official_db_mw):
            return 10 ** ((target_db - self.official_db_mw) / 10)
        elif not math.isnan(self.official_db_vrms) and not math.isnan(
            self.official_impedance
        ):
            return (
                10
                ** (
                    (
                        target_db
                        - self.official_db_vrms
                        - 10 * math.log10(self.official_impedance)
                    )
                    / 10
                )
                * 1000
            )

    def power_needed_asr(self, target_db=94):
        if self.asr_94db_voltage and self.asr_impedance:
            return (
                10 ** ((target_db - 94) / 10)
                * self.asr_94db_voltage**2
                / self.asr_impedance
                / 1000
            )

    def power_needed_asr_voltage_official_impedance(self, target_db=94):
        if self.asr_94db_voltage and self.official_impedance:
            return (
                10 ** ((target_db - 94) / 10)
                * self.asr_94db_voltage**2
                / self.official_impedance
                / 1000
            )


official = pd.read_csv(
    "./data/over-ear sensitivity official.csv",
    dtype={
        "brand": str,
        "model": str,
        "driver": str,
        "db/mw": float,
        "db/vrms": float,
        "impedance": float,
        "balance": str,
        "back": str,
        "production": str,
        "note": str,
    },
)
asr = pd.read_csv(
    "./data/over-ear sensitivity asr.csv",
    dtype={
        "brand": str,
        "model": str,
        "94db voltage": int,
        "impedance": float,
        "note": str,
    },
)
asr = asr[asr["impedance"].notna()]
headphones = []
for index, data in official.iterrows():
    headphones.append(
        Headphone(
            data["brand"],
            data["model"],
            data["driver"],
            data["db/mw"],
            data["db/vrms"],
            data["impedance"],
            data["balance"],
            data["back"],
            data["production"],
            data["note"],
        )
    )
for index, data in asr.iterrows():
    found = False
    for headphone in headphones:
        if headphone.brand == data["brand"] and headphone.model == data["model"]:
            headphone.asr_94db_voltage = data["94db voltage"]
            headphone.asr_impedance = data["impedance"]
            headphone.asr_note = data["note"]
            found = True
            break
    if not found:
        print(
            f"Error! ASR has {data['brand']} {data['model']} but official data doesn't"
        )
        sys.exit(1)

# plot_voltage_needed(
#     headphones=headphones,
#     title="Voltage Requirements of the Hardest-to-Drive Headphones to Reach 94 dB",
# )

# plot_voltage_needed(
#     headphones=[
#         headphone
#         for headphone in headphones
#         if headphone.production in ["producing", "inventory"]
#     ],
#     title="Voltage Requirements of the Hardest-to-Drive Producing or Just Discontinued Headphones to Reach 94 dB",
# )

# plot_voltage_needed(
#     headphones=[
#         headphone
#         for headphone in headphones
#         if headphone.back != "open"
#         and headphone.production in ["producing", "inventory"]
#     ],
#     title="Voltage Requirements of the Hardest-to-Drive Producing or Just Discontinued Closed-Back Headphones to Reach 94 dB",
# )

# plot_voltage_needed(
#     headphones=[
#         headphone
#         for headphone in headphones
#         if headphone.production in ["producing", "inventory"]
#     ],
#     title="Voltage Requirements of the Easiest-to-Drive Producing or Just Discontinued Headphones to Reach 94 dB",
#     order=False,
# )

# plot_voltage_needed(
#     headphones=[
#         headphone
#         for headphone in headphones
#         if headphone.back != "open"
#         and headphone.production in ["producing", "inventory"]
#         and headphone.driver == "dynamic"
#     ],
#     title="Voltage Requirements of the Hardest-to-Drive Producing or Just Discontinued Dynamic Closed-Back Headphones to Reach 94 dB",
# )

# plot_power_needed(
#     headphones=[
#         headphone
#         for headphone in headphones
#         if headphone.production in ["producing", "inventory"]
#     ],
#     title="Power Requirements of the Hardest-to-Drive Producing or Just Discontinued Headphones to Reach 94 dB",
# )

# plot_power_needed(
#     headphones=[
#         headphone
#         for headphone in headphones
#         if headphone.back != "open"
#         and headphone.production in ["producing", "inventory"]
#     ],
#     title="Power Requirements of the Hardest-to-Drive Producing or Just Discontinued Closed-Back Headphones to Reach 94 dB",
# )

reference_headphones_official = dict(
    Sennheiser=["hd800s", "hd600"],
    Fiio=["jt1"],
    AKG=["k812"],
    Audeze=["LCD-5"],
    Sony=["MDR-Z1R", "MDR-7506"],
    Beyer=["dt880 250", "dt900 prox", "T1 3rd"],
    Philips=["shp9500"],
    Focal=["Utopia 2022"],
)
reference_headphones_asr = dict(
    Hifiman=["Susvara", "he400se Stealth"],
    AKG=["k701"],
    Beyer=["dt880 600"],
    Aune=["AR5000"],
    Focal=["Utopia 2016"],
)
target_headphones = dict(
    Fiio=["jt1", "ft5"],
    Hifiman=["Sundara"],
    Moondrop=["Joker", "Para", "Cosmo"],
    NAN=["NAN-7"],
)

compare_voltage(
    target_headphones,
    reference_headphones_official,
    reference_headphones_asr,
    headphones,
)

compare_power(
    target_headphones,
    reference_headphones_official,
    reference_headphones_asr,
    headphones,
)
