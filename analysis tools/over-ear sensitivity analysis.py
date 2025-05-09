# Sensitivity: dB/Vrms
# Efficiency: dB/mW

import sys
import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


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
        date=None,
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
        self.date = date
        self.asr_94db_voltage = asr_94db_voltage
        self.asr_impedance = asr_impedance
        self.asr_note = asr_note

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
    headphones_list,
    indicator,
    target_db=96,
    title="",
    xlabel="",
    scale="linear",  # The scale of the x-axis. If data is too spread out, use "log"
    figsize=(16, 10),
    beginner=0,  # How many headphones you want to skip from the start
    max_shown=0,  # The maximum number of headphones to show
    order=True,  # Whether to show the headphones from the highest or the lowest
    save_path=None,
):

    def voltage_needed(headphones, target_db):
        voltage_data = []
        for headphone in headphones:
            voltage_needed = headphone.voltage_needed_official(
                target_db=target_db)
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
                                headphone.model} ASR OI",
                            power_needed,
                            headphone.driver,
                            headphone.balance,
                        )
                    )
        return power_data

    def current_needed(headphones, target_db):
        current_data = []
        for headphone in headphones:
            current_needed = headphone.current_needed_official(
                target_db=target_db)
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
                                headphone.model} ASR OI",
                            current_needed,
                            headphone.driver,
                            headphone.balance,
                        )
                    )
        return current_data

    if indicator == "voltage":
        data = voltage_needed(find_headphones(headphones_list), target_db)
    elif indicator == "power":
        data = power_needed(find_headphones(headphones_list), target_db)
    elif indicator == "current":
        data = current_needed(find_headphones(headphones_list), target_db)
    else:
        print("please input a valid indicator")
        return

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


def inquire(headphones_list):
    def calculate_db_vrms(db_mw, impedance):
        return round(db_mw - 10 * math.log10(impedance) + 30, 1)

    def calculate_db_mw(db_vrms, impedance):
        return round(db_vrms + 10 * math.log10(impedance) - 30, 1)

    def calculate_impedance(db_vrms, db_mw):
        return round(10 ** ((db_mw - db_vrms + 30) / 10), 1)

    def calculate_asr_db_vrms(asr_94db_voltage):
        return round(94 - 20 * math.log10(asr_94db_voltage), 1)

    def calculate_asr_db_mw(asr_94db_voltage, impedance):
        return round(64 - 20 * math.log10(asr_94db_voltage) + 10 * math.log10(impedance), 1)

    data = find_headphones(headphones_list)
    for headphone in data:
        print(f"{headphone.brand} {headphone.model}")
        print(f"Driver type: {headphone.driver}")
        if not math.isnan(headphone.official_db_mw):
            print(f"Official efficiency: {headphone.official_db_mw} dB/mW")
        elif not math.isnan(headphone.official_db_vrms) and not math.isnan(headphone.official_impedance):
            print(f"Official efficiency (calculated): {calculate_db_mw(
                headphone.official_db_vrms, headphone.official_impedance)} dB/mW")
        if not math.isnan(headphone.official_db_vrms):
            print(f"Official sensitivity: {
                  headphone.official_db_vrms} dB/Vrms")
        elif not math.isnan(headphone.official_db_mw) and not math.isnan(headphone.official_impedance):
            print(f"Official sensitivity (calculated): {calculate_db_vrms(
                headphone.official_db_mw, headphone.official_impedance)} dB/Vrms")
        if not math.isnan(headphone.official_impedance):
            print(f"Official impedance: {headphone.official_impedance} Ω")
        elif not math.isnan(headphone.official_db_vrms) and not math.isnan(headphone.official_mw):
            print(f"Official impedance (calculated): {
                  calculate_impedance(headphone.official_db_vrms, headphone.official_db_mw)} Ω")
        if not math.isnan(headphone.asr_94db_voltage):
            if not math.isnan(headphone.asr_impedance):
                print(f"ASR efficiency: {calculate_asr_db_mw(
                    headphone.asr_94db_voltage, headphone.asr_impedance)} dB/mW")
            elif not math.isnan(headphone.official_impedance):
                print(f"ASR efficiency (calculated with official impedance): {calculate_asr_db_mw(
                    headphone.asr_94db_voltage, headphone.official_impedance)} dB/mW")
            print(f"ASR sensitivity: {calculate_asr_db_vrms(
                headphone.asr_94db_voltage)} dB/Vrms")
            if not math.isnan(headphone.asr_impedance):
                print(f"ASR impedance: {headphone.asr_impedance} Ω")
        print(f"Allow balanced input: {
              "yes" if headphone.balance == "yes" else "no"}")
        print(f"{headphone.back}-back design")
        print(f"Production status: {headphone.production}")
        official_note = headphone.official_note
        if isinstance(official_note, str):
            print(f"Official note: {headphone.official_note}")
        asr_note = headphone.asr_note
        if isinstance(asr_note, str):
            print(f"ASR note: {headphone.asr_note}")
        print(f"Record date: {headphone.date.strftime('%Y-%m-%d')}\n")


def find_headphones(headphones_list):
    found_headphones = []
    for brand in headphones_list:
        for headphone in headphones:
            if (
                headphone.brand == brand
                and headphone.model in headphones_list[brand]
            ):
                found_headphones.append(headphone)
    return found_headphones


def official_sensitivity_distribution(official):

    # Create a copy of the dataframe to avoid modifying the original
    df = official.copy()

    # Fill in missing values using the formula: efficiency = sensitivity + 10*log10(impedance) - 30
    # Fill missing efficiency (db/mw) values
    mask_missing_efficiency = df['db/mw'].isna(
    ) & ~df['db/vrms'].isna() & ~df['impedance'].isna()
    df.loc[mask_missing_efficiency, 'db/mw'] = df.loc[mask_missing_efficiency,
                                                      'db/vrms'] + 10 * np.log10(df.loc[mask_missing_efficiency, 'impedance']) - 30

    # Fill missing sensitivity (db/vrms) values
    mask_missing_sensitivity = ~df['db/mw'].isna(
    ) & df['db/vrms'].isna() & ~df['impedance'].isna()
    df.loc[mask_missing_sensitivity, 'db/vrms'] = df.loc[mask_missing_sensitivity,
                                                         'db/mw'] - 10 * np.log10(df.loc[mask_missing_sensitivity, 'impedance']) + 30

    # Fill missing impedance values
    mask_missing_impedance = ~df['db/mw'].isna(
    ) & ~df['db/vrms'].isna() & df['impedance'].isna()
    df.loc[mask_missing_impedance, 'impedance'] = 10 ** (
        (df.loc[mask_missing_impedance, 'db/mw'] - df.loc[mask_missing_impedance, 'db/vrms'] + 30) / 10)

    # 打印sensitivity最高和最低的十款耳机的"brand"+"model"+"driver"
    # 打印efficiency最高和最低的十款耳机的"brand"+"model"+"driver"
    # 打印impedance最高和最低的十款耳机的"brand"+"model"+"driver"

    # Focus on the three main driver types
    # driver_types = ["AMT", "dynamic", "planar"]
    driver_types = ["dynamic", "planar"]

    # Store statistics for reporting
    stats = {}

    # Create separate plots for each metric
    for metric in ['db/mw', 'db/vrms', 'impedance']:
        # plt.figure(figsize=(10, 6))

        # Collect data for each driver type
        data = []
        labels = []

        for driver in driver_types:
            values = df[df['driver'] == driver][metric].dropna()
            if len(values) > 0:
                data.append(values)
                labels.append(driver)

                # Store statistics
                if driver not in stats:
                    stats[driver] = {}
                stats[driver][metric] = {
                    'median': values.median(),
                    'count': len(values)
                }

        # Create boxplot
        if data:
            if metric == 'db/mw':
                current_whis = 1.5
                plt.ylim(75, 115)
                plt.title('Efficiency (dB/mW) whis='+str(current_whis))
                plt.ylabel('dB/mW')
                fig_name = 'efficiency distribution.png'
            elif metric == 'db/vrms':
                current_whis = 1.5
                plt.ylim(90, 130)
                plt.title('Sensitivity (dB/Vrms) whis='+str(current_whis))
                plt.ylabel('dB/Vrms')
                fig_name = 'sensitivity distribution.png'
            elif metric == 'impedance':
                current_whis = 2.5
                plt.ylim(4, 375)
                plt.title('Impedance (Ω) whis='+str(current_whis))
                plt.ylabel('Ω (log scale)')
                plt.yscale('log')
                plt.yticks([16, 32, 64, 128, 256, 512], [
                           '16', '32', '64', '128', '256', '512'])
                fig_name = 'impedance distribution.png'
            else:
                print("ERROR")
                return

            plt.boxplot(data, tick_labels=labels,
                        patch_artist=True, whis=current_whis, widths=0.6)

            for i, values in enumerate(data):
                # 计算统计量
                median = np.median(values)
                q1 = np.percentile(values, 25)
                q3 = np.percentile(values, 75)

                # 设置文本位置和格式
                x_pos = i + 1  # 箱线图的x坐标

                # 添加标签(根据是否为对数刻度调整格式)
                if metric == 'impedance':
                    plt.text(x_pos + 0.3, median, f"{median:.1f}Ω",
                             verticalalignment='center', fontsize=8)
                    plt.text(x_pos + 0.3, q1, f"{q1:.1f}Ω",
                             verticalalignment='center', fontsize=8)
                    plt.text(x_pos + 0.3, q3, f"{q3:.1f}Ω",
                             verticalalignment='center', fontsize=8)
                else:
                    plt.text(x_pos + 0.3, median, f"{median:.1f}",
                             verticalalignment='center', fontsize=8)
                    plt.text(x_pos + 0.3, q1, f"{q1:.1f}",
                             verticalalignment='center', fontsize=8)
                    plt.text(x_pos + 0.3, q3, f"{q3:.1f}",
                             verticalalignment='center', fontsize=8)

            # Add grid lines for better readability
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            # Set title and labels

            plt.gcf().set_size_inches(4, 4)
            plt.tight_layout()
            # plt.show()
            plt.savefig('./analysis results/'+fig_name, dpi=400)
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
    parse_dates=["date"]
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
            data["note"],
            data["date"]
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
        print("Error! ASR has "+data['brand']+" " +
              data['model']+" but official data does not")
        sys.exit(1)

# inquire_headphones_list = dict(
#     {
#         "aune": ["ar5000", "sr7000"],
#         "akg": ["k701"]
#     }
# )
# inquire(inquire_headphones_list)

# reference_headphones_list = dict(
#     {
#         "sennheiser": ["hd800s", "hd600"],
#         "dca": ["expanse"],
#         "fiio": ["jt1", "ft1", "ft1 pro"],
#         "akg": ["k701"],
#         "audeze": ["lcd-5"],
#         "sony": ["mdr-m1"],
#         "beyer": ["dt880 250", "dt900 prox", "dt880 600"],
#         "philips": ["shp9500"],
#         "focal": ["utopia 2022"],
#         "hifiman": ["susvara", "he400se stealth", "susvara unveiled", "ananda nano"],
#         "zmf": ["caldera"],
#         "abyss": ["1266 phi tc"],
#         "anan audio": ["nan-7"],
#         "moondrop": ["cosmo", "para"],
#         "ath": ["adx5000", "r70x"],
#         "xk audio": ["serene"],
#         "aune": ["ar5000"]
#     }
# )


# plot(
#     headphones_list=reference_headphones_list,
#     indicator="voltage",
#     title="Voltage Requirements of Some Headphones to Reach 96 dB",
#     xlabel="Voltage (mV)",
#     save_path="./analysis results/",
# )

# plot(
#     headphones_list=reference_headphones_list,
#     indicator="power",
#     title="Power Requirements of Some Headphones to Reach 96 dB",
#     xlabel="Power (mW)",
#     save_path="./analysis results/",
# )

# plot(
#     headphones_list=reference_headphones_list,
#     indicator="current",
#     title="Current Requirements of Some Headphones to Reach 96 dB",
#     xlabel="Current (mA)",
#     save_path="./analysis results/",
# )

official_sensitivity_distribution(official)
