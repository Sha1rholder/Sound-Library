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
        asr_94db_voltage=math.nan,
        asr_impedance=math.nan,
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
        self.asr_94db_voltage = asr_94db_voltage
        self.asr_impedance = asr_impedance

    def print_info(self):
        for attr, value in self.__dict__.items():
            print(f"{attr}: {value}")

    def voltage_needed_official(self, target_db=96):
        if not math.isnan(self.official_db_vrms):
            return (10 ** ((target_db - self.official_db_vrms) / 20)) * 1000
        elif not math.isnan(self.official_db_mw) and not math.isnan(
            self.official_impedance
        ):
            return 10 ** (
                (
                    target_db
                    - self.official_db_mw
                    + 30
                    + 10 * math.log10(self.official_impedance)
                )
                / 20
            )

    def voltage_needed_asr(self, target_db=96):
        if not math.isnan(self.asr_94db_voltage):
            return 10 ** ((target_db - 94) / 20) * self.asr_94db_voltage

    def power_needed_official(self, target_db=96):
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

    def power_needed_asr(self, target_db=96):
        if not math.isnan(self.asr_94db_voltage) and not math.isnan(self.asr_impedance):
            return (
                10 ** ((target_db - 94) / 10)
                * self.asr_94db_voltage**2
                / self.asr_impedance
                / 1000
            )

    def power_needed_asr_voltage_official_impedance(self, target_db=96):
        if not math.isnan(self.asr_94db_voltage) and not math.isnan(
            self.official_impedance
        ):
            return (
                10 ** ((target_db - 94) / 10)
                * self.asr_94db_voltage**2
                / self.official_impedance
                / 1000
            )

    def current_needed_official(self, target_db=96):
        # db/vrms is prefered for no compelling reason. It's just a choice.
        if not math.isnan(self.official_db_vrms) and not math.isnan(
            self.official_impedance
        ):
            return (
                10 ** ((target_db - self.official_db_vrms) / 20)
                / self.official_impedance
                * 1000
            )
        elif not math.isnan(self.official_db_mw) and not math.isnan(
            self.official_impedance
        ):
            return (
                10
                ** (
                    (
                        target_db
                        - self.official_db_mw
                        + 30
                        + 10 * math.log10(self.official_impedance)
                    )
                    / 20
                )
                / self.official_impedance
            )
        elif not math.isnan(self.official_db_vrms) and not math.isnan(
            self.official_db_mw
        ):
            return (
                10
                ** ((target_db + self.official_db_vrms - 2 * self.official_db_mw) / 20)
                / 1000
            )

    def current_needed_asr(self, target_db=96):
        if not math.isnan(self.asr_94db_voltage) and not math.isnan(self.asr_impedance):
            return (
                10 ** ((target_db - 94) / 20)
                * self.asr_94db_voltage
                / self.asr_impedance
            )

    def current_needed_asr_voltage_official_impedance(self, target_db=96):
        if not math.isnan(self.asr_94db_voltage) and not math.isnan(
            self.official_impedance
        ):
            return (
                10 ** ((target_db - 94) / 20)
                * self.asr_94db_voltage
                / self.official_impedance
            )


def plot(
    data,
    title="",
    xlabel="",
    scale="linear",  # The scale of the x-axis. If data is too spread out, use "log"
    figsize=(16, 10),
    beginner=0,  # How many headphones you want to skip from the start
    max_shown=0,  # The maximum number of headphones to show
    order=True,  # Whether to show the headphones from the highest or the lowest
    save_path=None,
):
    data.sort(key=lambda x: x[1], reverse=not order)
    if beginner > len(data):
        print("Beginner is too large.")
        return
    elif beginner == 0:
        data = data[-max_shown:]
    else:
        data = data[-beginner - max_shown: -beginner]
    models, values, drivers, balances = zip(*data)

    colors = []
    for driver, balance in zip(drivers, balances):
        if driver == "dynamic":
            colors.append("red" if balance == "yes" or balance ==
                          "both" else "darkred")
        elif driver == "planar":
            colors.append(
                "green" if balance == "yes" or balance == "both" else "darkgreen"
            )
        elif driver == "AMT":
            colors.append(
                "magenta" if balance == "yes" or balance == "both" else "darkmagenta"
            )
        elif driver == "planar and dynamic":
            colors.append("blue" if balance == "yes" or balance ==
                          "both" else "darkblue")
        else:
            print(f"Unknown driver: {driver}")
            sys.exit(1)

    plt.figure(figsize=figsize)
    bars = plt.barh(
        models,
        values,
        color=colors,
    )
    for bar in bars:
        width = bar.get_width()
        plt.text(
            width,
            bar.get_y() + bar.get_height() / 2,
            "%.3g" % width,
            va="center",
        )
    plt.xlabel(xlabel)
    plt.title(title)
    plt.xscale(scale)
    plt.tight_layout()
    if save_path:
        plt.savefig(f"{save_path}{title}.png")
        plt.close()
    else:
        plt.show()


def voltage_needed(headphones, target_db):
    voltage_data = []
    for headphone in headphones:
        voltage_needed = headphone.voltage_needed_official(target_db=target_db)
        if voltage_needed:
            voltage_data.append(
                (
                    f"{headphone.brand} {headphone.model}",
                    voltage_needed,
                    headphone.driver,
                    headphone.balance,
                )
            )
        voltage_needed = headphone.voltage_needed_asr(target_db=target_db)
        if voltage_needed:
            voltage_data.append(
                (
                    f"{headphone.brand} {headphone.model} ASR",
                    voltage_needed,
                    headphone.driver,
                    headphone.balance,
                )
            )
    return voltage_data


def power_needed(headphones, target_db):
    power_data = []
    for headphone in headphones:
        power_needed = headphone.power_needed_official(target_db=target_db)
        if power_needed:
            power_data.append(
                (
                    f"{headphone.brand} {headphone.model}",
                    power_needed,
                    headphone.driver,
                    headphone.balance,
                )
            )
        power_needed = headphone.power_needed_asr(target_db=target_db)
        if power_needed:
            power_data.append(
                (
                    f"{headphone.brand} {headphone.model} ASR",
                    power_needed,
                    headphone.driver,
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
                        f"{headphone.brand} {
                            headphone.model} ASR (official impedance)",
                        power_needed,
                        headphone.driver,
                        headphone.balance,
                    )
                )
    return power_data


def current_needed(headphones, target_db):
    current_data = []
    for headphone in headphones:
        current_needed = headphone.current_needed_official(target_db=target_db)
        if current_needed:
            current_data.append(
                (
                    f"{headphone.brand} {headphone.model}",
                    current_needed,
                    headphone.driver,
                    headphone.balance,
                )
            )
        current_needed = headphone.current_needed_asr(target_db=target_db)
        if current_needed:
            current_data.append(
                (
                    f"{headphone.brand} {headphone.model} ASR",
                    current_needed,
                    headphone.driver,
                    headphone.balance,
                )
            )
        else:
            current_needed = headphone.current_needed_asr_voltage_official_impedance(
                target_db
            )
            if current_needed:
                current_data.append(
                    (
                        f"{headphone.brand} {
                            headphone.model} ASR (official impedance)",
                        current_needed,
                        headphone.driver,
                        headphone.balance,
                    )
                )
    return current_data


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
official = official[official["driver"].isin(
    ["dynamic", "planar", "AMT", "planar and dynamic"])]
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
        )
    )
for index, data in asr.iterrows():
    found = False
    for headphone in headphones:
        if headphone.brand == data["brand"] and headphone.model == data["model"]:
            headphone.asr_94db_voltage = data["94db voltage"]
            headphone.asr_impedance = data["impedance"]
            found = True
            break
    if not found:
        print("Error! ASR has "+data['brand']+" " +
              data['model']+" but official data does not")
        sys.exit(1)

plot(
    voltage_needed(
        [
            headphone
            for headphone in headphones
            if headphone.production in ["producing", "inventory"]
        ],
        96,
    ),
    max_shown=30,
    title="Voltage Requirements of the Hardest-to-Drive Producing or Inventory Headphones to Reach 96 dB",
    xlabel="Voltage (mV)",
    save_path="./analysis results/",
)

plot(
    power_needed(
        [
            headphone
            for headphone in headphones
            if headphone.production in ["producing", "inventory"]
            and headphone.driver == "planar"
        ],
        96,
    ),
    max_shown=30,
    title="Power Requirements of the Hardest-to-Drive Producing or Inventory Planar Headphones to Reach 96 dB",
    xlabel="Power (mW)",
    save_path="./analysis results/",
)

plot(
    current_needed(
        [
            headphone
            for headphone in headphones
            if headphone.production in ["producing", "inventory"]
        ],
        96,
    ),
    max_shown=30,
    title="Current Requirements of the Hardest-to-Drive Producing or Inventory Headphones to Reach 96 dB",
    xlabel="Current (mA)",
    save_path="./analysis results/",
)

reference_headphones_names = dict(
    {
        "sennheiser": ["hd800s", "hd600"],
        "dca": ["expanse"],
        "fiio": ["jt1"],
        "akg": ["k701"],
        "audeze": ["lcd-5"],
        "sony": ["mdr-7506"],
        "beyer": ["dt880 250", "dt900 prox", "dt880 600"],
        "philips": ["shp9500"],
        "focal": ["utopia 2022"],
        "hifiman": ["susvara", "he400se stealth", "susvara unveiled", "ananda nano"],
        "zmf": ["caldera"],
        "abyss": ["1266 phi tc"],
        "anan audio": ["nan-7"],
        "moondrop": ["cosmo", "para"],
        "ath": ["adx5000", "r70x"],
        "xk audio": ["serene"],
        "aune": ["ar5000"]
    }
)

reference_headphones = []
for brand in reference_headphones_names:
    for headphone in headphones:
        if (
            headphone.brand == brand
            and headphone.model in reference_headphones_names[brand]
        ):
            reference_headphones.append(headphone)

plot(
    voltage_needed(reference_headphones, 96),
    title="Voltage Requirements of Some Headphones to Reach 96 dB",
    xlabel="Voltage (mV)",
    save_path="./analysis results/",
)

plot(
    power_needed(reference_headphones, 96),
    title="Power Requirements of Some Headphones to Reach 96 dB",
    xlabel="Power (mW)",
    save_path="./analysis results/",
)

plot(
    current_needed(reference_headphones, 96),
    title="Current Requirements of Some Headphones to Reach 96 dB",
    xlabel="Current (mA)",
    save_path="./analysis results/",
)
