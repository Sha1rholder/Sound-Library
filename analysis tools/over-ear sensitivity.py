import sys
import math
import matplotlib.pyplot as plt
import pandas as pd


class Headphone:
    def __init__(
        self,
        brand,
        model,
        driver=None,
        official_db_mw=math.nan,
        official_db_vrms=math.nan,
        official_impedance=math.nan,
        balance=None,
        back=None,
        production=None,
        official_note=None,
        asr_94db_voltage=math.nan,
        asr_impedance=math.nan,
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

    def print_info(self):
        for attr, value in self.__dict__.items():
            print(f"{attr}: {value}")

    def voltage_needed_official(self, target_db=110):
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

    def voltage_needed_asr(self, target_db=110):
        if not math.isnan(self.asr_94db_voltage):
            return 10 ** ((target_db - 94) / 20) * self.asr_94db_voltage

    def power_needed_official(self, target_db=110):
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

    def power_needed_asr(self, target_db=110):
        if not math.isnan(self.asr_94db_voltage) and not math.isnan(self.asr_impedance):
            return (
                10 ** ((target_db - 94) / 10)
                * self.asr_94db_voltage**2
                / self.asr_impedance
                / 1000
            )

    def power_needed_asr_voltage_official_impedance(self, target_db=110):
        if not math.isnan(self.asr_94db_voltage) and not math.isnan(
            self.official_impedance
        ):
            return (
                10 ** ((target_db - 94) / 10)
                * self.asr_94db_voltage**2
                / self.official_impedance
                / 1000
            )


def plot_voltage_needed(
    headphones,  # select headphones interested
    title="Voltage Requirements of the Headphones to reach 110 dB",
    target_db=94,  # How loud you want to drive the headphones
    beginner=0,  # How many headphones you want to skip from the start
    max_shown=30,  # The maximum number of headphones to show
    order=True,  # Whether to show the headphones with the highest voltage requirement or the lowest
    scale="log",  # The scale of the x-axis
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

    plt.figure(figsize=(16, 10))
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
    plt.tight_layout()
    plt.savefig(f"./analysis results/{title}.png")
    plt.close()


def plot_power_needed(
    headphones,
    title="Voltage Requirements of the Headphones to reach 110 dB",
    target_db=110,
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

    plt.figure(figsize=(16, 10))
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
    plt.tight_layout()
    plt.savefig(f"./analysis results/{title}.png")
    plt.close()


def compare_voltage_needed(
    target_headphones,
    reference_headphones_official,
    reference_headphones_asr,
    headphones,
    title="Comparing Voltage Requirements of Headphones to Reach 110 dB",
    target_db=110,
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
    for brand in target_headphones:
        for model in target_headphones[brand]:
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

    plt.figure(figsize=(16, 10))
    model, voltages, balance, is_target = zip(*voltage_data)
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
    plt.tight_layout()
    plt.savefig(f"./analysis results/{title}.png")
    plt.close()


def compare_power_needed(
    target_headphones,
    reference_headphones_official,
    reference_headphones_asr,
    headphones,
    title="Comparing Power Requirements of Headphones to Reach 110 dB",
    target_db=110,
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
                                target_db=target_db
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
    for brand in target_headphones:
        for model in target_headphones[brand]:
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
                                target_db=target_db
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

    plt.figure(figsize=(16, 10))
    model, powers, balance, is_target = zip(*power_data)
    bars = plt.barh(
        model, powers, color=["blue" if b == "yes" else "red" for b in balance]
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
    plt.tight_layout()
    plt.savefig(f"./analysis results/{title}.png")
    plt.close()


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
official = official[
    official["driver"].isin(["dynamic", "planar", "AMT", "planar magnetostatic"])
]
asr = pd.read_csv(
    "./data/over-ear sensitivity asr.csv",
    dtype={
        "brand": str,
        "model": str,
        "94db voltage": float,
        "impedance": float,
        "note": str,
    },
)
asr = asr[asr["ignore"] != "yes"]
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


plot_voltage_needed(
    headphones=[
        headphone
        for headphone in headphones
        if headphone.production in ["producing", "inventory"]
        and headphone.driver == "planar"
    ],
    title="Voltage Requirements of the Hardest-to-Drive Producing or Inventory Planar Headphones to Reach 110 dB",
)
plot_power_needed(
    headphones=[
        headphone
        for headphone in headphones
        if not headphone.back in ["open", "speaker", ""]
        and headphone.production in ["producing", "inventory"]
    ],
    order=False,
    title="Power Requirements of the Easiest-to-Drive Producing or Inventory Closed-Back Headphones to Reach 94 dB",
    target_db=94,
)


reference_headphones_official = dict(
    Sennheiser=["hd800s", "hd600"],
    DCA=["Expanse"],
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
    DCA=["Expanse"],
    AKG=["k701"],
    Beyer=["dt880 600"],
    Aune=["AR5000"],
    Focal=["Utopia 2016"],
    Philips=["Fidelio X2HR"],
)
target_headphones = dict(
    Fiio=["jt1"],
    Hifiman=["Sundara Closed", "Ananda Nano"],
    ATH=["adx5000"],
    Moondrop=["Cosmo"],
    NAN=["NAN-7"],
    Abyss=["1266 Phi TC"],
    ZMF=["Caldera"],
)


compare_voltage_needed(
    target_headphones,
    reference_headphones_official,
    reference_headphones_asr,
    headphones,
    title="Comparing Voltage Requirements of Headphones to Reach 110 dB",
)

compare_power_needed(
    target_headphones,
    reference_headphones_official,
    reference_headphones_asr,
    headphones,
    title="Comparing Power Requirements of Headphones to Reach 110 dB",
)
