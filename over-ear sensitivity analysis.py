import csv
import math
import matplotlib.pyplot as plt


def plot_power_needed(
    data,
    title="Power Requirement of Headphones to ",
    target_db=94,
    beginner=0,
    stopper=0,
    order=True,
):

    power_data = []

    for row in data:
        if row["mw"]:
            power = 10 ** ((target_db - row["mw"]) / 10)
            power_data.append((f'{row["brand"]} {row["model"]}', power))

    power_data.sort(key=lambda x: x[1], reverse=not order)

    print(power_data)

    if stopper:
        power_data = power_data[-stopper:-beginner]
    else:
        power_data = power_data[:-beginner]

    headphones, power = zip(*power_data)

    plt.barh(headphones, power)
    plt.xlabel("Power (mW)")
    plt.ylabel("Headphones")
    plt.title(title + str(target_db) + " dB")
    plt.show()


def plot_voltage_needed(
    data,
    title="Voltage Requirement of Headphones to ",
    target_db=94,
    beginner=0,
    stopper=0,
    order=True,
):

    voltage_data = []

    for row in data:
        if row["v"]:
            voltage = 10 ** ((target_db - row["v"]) / 20)
            voltage_data.append((f'{row["brand"]} {row["model"]}', voltage))

    voltage_data.sort(key=lambda x: x[1], reverse=not order)

    if stopper:
        voltage_data = voltage_data[-stopper:-beginner]
    else:
        voltage_data = voltage_data[:-beginner]

    headphones, voltage = zip(*voltage_data)

    plt.barh(headphones, voltage)
    plt.xlabel("Voltage (Vrms)")
    plt.ylabel("Headphones")
    plt.title(title + str(target_db) + " dB")
    plt.show()


data = []

with open("./resource/over-ear sensitivity.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    headers = next(reader)
    for row in reader:
        row_dict = {headers[i]: value for i, value in enumerate(row)}
        row_dict["relation"] = ""
        if row_dict["impedance"]:
            row_dict["impedance"] = float(row_dict["impedance"])
        else:
            row_dict["impedance"] = None
        if row_dict["mw"]:
            row_dict["mw"] = float(row_dict["mw"])
        else:
            row_dict["mw"] = None
        if row_dict["v"]:
            row_dict["v"] = float(row_dict["v"])
        else:
            row_dict["v"] = None
        if row_dict["impedance"]:
            if row_dict["mw"]:
                if row_dict["v"]:
                    row_dict["relation"] = (
                        "know everything about both sensitivities and impedance"
                    )
                else:
                    row_dict["v"] = (
                        row_dict["mw"] + 30 - 10 * math.log10(row_dict["impedance"])
                    )
                    row_dict["relation"] = (
                        "calculate db/vrms though impedance and db/mw"
                    )
            elif row_dict["v"]:
                row_dict["mw"] = (
                    row_dict["v"] - 30 + 10 * math.log10(row_dict["impedance"])
                )
                row_dict["relation"] = "calculate db/mw though impedance and db/vrms"
            else:
                row_dict["relation"] = "only know impedance"
        elif row_dict["mw"]:
            if row_dict["v"]:
                row_dict["impedance"] = 10 ** (
                    row_dict["mw"] / 10 - row_dict["v"] / 10 + 3
                )
                row_dict["relation"] = "calculate impedance though db/mw and db/vrms"
            else:
                row_dict["relation"] = "only know db/mw"
        elif row_dict["v"]:
            row_dict["relation"] = "only know db/vrms"
        else:
            row_dict["relation"] = "know nothing about sensitivities and impedance"
        data.append(row_dict)

plot_power_needed(
    data,
    title="Power Requirement of Headphones to ",
    beginner=1,
    stopper=31,
    order=True,
)

plot_power_needed(
    [row for row in data if row["back"] == "open"],
    title="Power Requirement of Open-back Headphones to ",
    beginner=1,
    stopper=31,
    order=True,
)

plot_power_needed(
    [row for row in data if row["back"] != "open"],
    title="Power Requirement of Closed-back Headphones to ",
    beginner=0,
    stopper=31,
    order=True,
)

plot_voltage_needed(
    data,
    title="Voltage Requirement of Headphones to ",
    beginner=1,
    stopper=31,
    order=True,
)

plot_voltage_needed(
    [row for row in data if row["back"] == "open"],
    title="Voltage Requirement of Open-back Headphones to ",
    beginner=1,
    stopper=31,
    order=True,
)

plot_voltage_needed(
    [row for row in data if row["back"] != "open"],
    title="Voltage Requirement of Closed-back Headphones to ",
    beginner=0,
    stopper=31,
    order=True,
)
