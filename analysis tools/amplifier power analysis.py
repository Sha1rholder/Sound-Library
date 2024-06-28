import math
import matplotlib.pyplot as plt
import pandas as pd


class Amp:
    def __init__(
        self,
        brand,
        model,
        class_="",
        type="",
        power_se=[],
        power_bal=[],
        output_level_se=math.nan,
        output_level_bal=math.nan,
        impedance_se=math.nan,
        impedance_bal=math.nan,
    ):
        self.brand = brand
        self.model = model
        self.class_ = class_
        self.type = type
        self.power_se = power_se
        self.power_bal = power_bal
        self.output_level_se = output_level_se
        self.output_level_bal = output_level_bal
        self.impedance_se = impedance_se
        self.impedance_bal = impedance_bal

    def print_info(self):
        for attr, value in self.__dict__.items():
            print(f"{attr}: {value}")

    def max_voltage_se(self):
        if not math.isnan(self.output_level_se):
            if self.power_se:
                return max(
                    self.output_level_se,
                    math.sqrt(self.power_se[-1][1] / 1000 * self.power_se[-1][0]),
                )  # 如果压摆“反向虚标”，则取实际输出功率计算的最大压摆
            else:
                return self.output_level_se
        elif self.power_se:
            return math.sqrt(self.power_se[-1][1] / 1000 * self.power_se[-1][0])

    def max_voltage_bal(self):
        if not math.isnan(self.output_level_bal):
            if self.power_bal:
                return max(
                    self.output_level_bal,
                    math.sqrt(self.power_bal[-1][1] / 1000 * self.power_bal[-1][0]),
                )
            else:
                return self.output_level_bal
        elif self.power_bal:
            return math.sqrt(self.power_bal[-1][1] / 1000 * self.power_bal[-1][0])

    def min_current_load_se(self):  # 最低“电流负载能力”
        if self.power_se:
            return math.sqrt(self.power_se[0][1] / 1000 / self.power_se[0][0])

    def min_current_load_bal(self):
        if self.power_bal:
            return math.sqrt(self.power_bal[0][1] / 1000 / self.power_bal[0][0])

    def sweet_point_se(self):
        u = self.max_voltage_se()
        i = self.min_current_load_se()
        return u / i, u * i * 1000

    def sweet_point_bal(self):
        u = self.max_voltage_bal()
        i = self.min_current_load_bal()
        return u / i, u * i * 1000


# def plot_amp(amp):


official = pd.read_csv(
    "./data/amplifier power.csv",
    dtype={
        "brand": str,
        "model": str,
        "class": str,
        "type": str,
        "power se": str,
        "power bal": str,
        "output level se": float,
        "output level bal": float,
        "imdedance se": str,
        "imdedance bal": str,
    },
)
amps = []
for index, data in official.iterrows():
    amps.append(
        Amp(
            data["brand"],
            data["model"],
            data["class"],
            data["type"],
            tuple(
                [
                    tuple(map(int, item.split(";")))
                    for item in data["power se"].split(" ")
                ]
            ),
            tuple(
                [
                    tuple(map(int, item.split(";")))
                    for item in data["power bal"].split(" ")
                ]
            ),
            data["output level se"],
            data["output level bal"],
            data["impedance se"],
            data["impedance bal"],
        )
    )

for amp in amps:
    # amp.print_info()
    print(amp.sweet_point_se())
    print(amp.sweet_point_bal())

# 有严重错误