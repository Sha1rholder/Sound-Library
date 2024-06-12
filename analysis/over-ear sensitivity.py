import math
import matplotlib.pyplot as plt
import pandas as pd


def plot_power_needed(
    headphones,
    title="Voltage Requirement of the Headphones to reach 94 dB",
    target_db=94,
    beginner=0,
    stopper=0,
    order=True,
):

    power_data = []

    for headphone in headphones:
        if not math.isnan(headphone.official_db_mw):
            power = 10 ** ((target_db - headphone.official_db_mw) / 10)
            power_data.append(
                (f"{headphone.brand} {headphone.model}", power, headphone.balanced)
            )
        elif not math.isnan(headphone.official_db_vrms) and not math.isnan(
            headphone.official_impedance
        ):
            power = (
                10
                ** (
                    (
                        target_db
                        - headphone.official_db_vrms
                        - 10 * math.log10(headphone.official_impedance)
                    )
                    / 10
                )
                * 1000
            )
            power_data.append(
                (f"{headphone.brand} {headphone.model}", power, headphone.balanced)
            )
        if headphone.asr_94db_voltage and headphone.asr_impedance:
            power = (
                10 ** ((target_db - 94) / 10)
                * headphone.asr_94db_voltage**2
                / headphone.asr_impedance
                / 1000
            )
            power_data.append(
                (
                    f"{headphone.brand} {headphone.model} ASR",
                    power,
                    headphone.balanced,
                )
            )
        elif headphone.asr_94db_voltage and headphone.official_impedance:
            power = (
                10 ** ((target_db - 94) / 10)
                * headphone.asr_94db_voltage**2
                / headphone.official_impedance
                / 1000
            )
            power_data.append(
                (
                    f"{headphone.brand} {headphone.model} ASR & Official",
                    power,
                    headphone.balanced,
                )
            )
    power_data.sort(key=lambda x: x[1], reverse=not order)

    if stopper and beginner:
        power_data = power_data[-stopper:-beginner]
    elif stopper:
        power_data = power_data[-stopper:]
    elif beginner:
        power_data = power_data[:-beginner]

    headphones, power, balanced = zip(*power_data)

    plt.barh(
        headphones, power, color=["blue" if b == "yes" else "red" for b in balanced]
    )
    plt.xlabel("Power (mW)")
    plt.ylabel("Headphones")
    plt.title(title)
    plt.show()


def plot_voltage_needed(
    headphones,
    title="Voltage Requirement of the Headphones to reach 94 dB",
    target_db=94,
    beginner=0,
    stopper=0,
    order=True,
):
    voltage_data = []

    for headphone in headphones:
        # nan (not a number) will not be considered as False by if statement
        if not math.isnan(headphone.official_db_vrms):
            voltage = (10 ** ((target_db - headphone.official_db_vrms) / 20)) * 1000
            voltage_data.append(
                (f"{headphone.brand} {headphone.model}", voltage, headphone.balanced)
            )
        elif not math.isnan(headphone.official_db_mw) and not math.isnan(
            headphone.official_impedance
        ):
            voltage = (
                10
                ** (
                    (
                        target_db
                        - headphone.official_db_mw
                        - 30
                        + 10 * math.log10(headphone.official_impedance)
                    )
                    / 20
                )
                * 1000
            )
            voltage_data.append(
                (f"{headphone.brand} {headphone.model}", voltage, headphone.balanced)
            )
        if headphone.asr_94db_voltage:  # None will be considered as False
            voltage = 10 ** ((target_db - 94) / 20) * headphone.asr_94db_voltage
            voltage_data.append(
                (
                    f"{headphone.brand} {headphone.model} ASR",
                    voltage,
                    headphone.balanced,
                )
            )

    voltage_data.sort(key=lambda x: x[1], reverse=not order)

    print(voltage_data)

    if stopper and beginner:
        voltage_data = voltage_data[-stopper:-beginner]
    elif stopper:
        voltage_data = voltage_data[-stopper:]
    elif beginner:
        voltage_data = voltage_data[:-beginner]

    model, voltages, balanced = zip(*voltage_data)

    plt.barh(model, voltages, color=["blue" if b == "yes" else "red" for b in balanced])
    plt.xlabel("Voltage (Vrms)")
    plt.ylabel("Headphones")
    plt.title(title)
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
        balanced=None,
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
        self.balanced = balanced
        self.back = back
        self.production = production
        self.official_note = official_note
        self.asr_94db_voltage = asr_94db_voltage
        self.asr_impedance = asr_impedance
        self.asr_note = asr_note

    def print_original_info(self):
        for attr, value in self.__dict__.items():
            print(f"{attr}: {value}")


headphones = []  # Original data

official = pd.read_csv(
    "./data/over-ear sensitivity official.csv",
    dtype={
        "brand": str,
        "model": str,
        "driver": str,
        "db/mw": float,
        "db/vrms": float,
        "impedance": float,
        "balanced": str,
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

for index, data in official.iterrows():
    headphones.append(
        Headphone(
            data["brand"],
            data["model"],
            data["driver"],
            data["db/mw"],
            data["db/vrms"],
            data["impedance"],
            data["balanced"],
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
        #     headphones.append(
        #         Headphone(
        #             data["brand"],
        #             data["model"],
        #             None,
        #             None,
        #             None,
        #             None,
        #             None,
        #             None,
        #             None,
        #             None,
        #             data["94db voltage"],
        #             data["impedance"],
        #             data["note"],
        #         )
        #     )
        input(
            f"Error! ASR has {data['brand']} {data['model']} but official data doesn't"
        )
    # 这种情况不该出现的，ASR有的且我感兴趣的型号必须有official数据

# plot_power_needed(
#     headphones=headphones,
#     title="Power Requirements of the Hardest-to-Drive Headphones to Reach 94 dB",
#     beginner=0,
#     stopper=31,
#     order=True,
# )

plot_power_needed(
    headphones=[
        headphone
        for headphone in headphones
        if headphone.production == "producing" or headphone.production == "inventory"
    ],
    title="Power Requirements of the Hardest-to-Drive Producing or Just Discontinued Headphones to Reach 94 dB",
    beginner=0,
    stopper=31,
    order=True,
)

plot_power_needed(
    headphones=[
        headphone
        for headphone in headphones
        if headphone.back != "open"
        and (headphone.production == "producing" or headphone.production == "inventory")
    ],
    title="Power Requirements of the Hardest-to-Drive Producing or Just Discontinued Closed-Back Headphones to Reach 94 dB",
    beginner=0,
    stopper=31,
    order=True,
)

# plot_voltage_needed(
#     headphones=headphones,
#     title="Voltage Requirements of the Hardest-to-Drive Headphones to Reach 94 dB",
#     beginner=0,
#     stopper=31,
#     order=True,
# )

plot_voltage_needed(
    headphones=[
        headphone
        for headphone in headphones
        if headphone.production == "producing" or headphone.production == "inventory"
    ],
    title="Voltage Requirements of the Hardest-to-Drive Producing or Just Discontinued Headphones to Reach 94 dB",
    beginner=0,
    stopper=31,
    order=True,
)

plot_voltage_needed(
    headphones=[
        headphone
        for headphone in headphones
        if headphone.back != "open"
        and (headphone.production == "producing" or headphone.production == "inventory")
    ],
    title="Voltage Requirements of the Hardest-to-Drive Producing or Just Discontinued Closed-Back Headphones to Reach 94 dB",
    beginner=0,
    stopper=31,
    order=True,
)
