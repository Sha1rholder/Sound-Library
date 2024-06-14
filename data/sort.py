import csv

file_paths = ["./data/over-ear sensitivity official.csv"]

for file_path in file_paths:
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        # 跳过标题行（如果有的话），并将数据存储在列表中
        # header = next(reader)  # 如果文件有标题行，取消注释这行
        data = list(reader)

    # 根据品牌和型号排序
    sorted_data = sorted(data, key=lambda x: (x[0].lower(), x[1].lower()))

    # 写入新的CSV文件
    with open(file_path, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        # writer.writerow(header)  # 如果需要写入标题行，取消注释这行
        writer.writerows(sorted_data)
