import os
import re


def replace_resource_with_assets(directory):
    # 定义正则表达式
    pattern = re.compile(r"(\[[^\]]*\]\([^\)]*\/)resource(\/[^\)]*\))")

    # 遍历文件夹及其子文件夹
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # 替换匹配的部分
                new_content = pattern.sub(r'\1assets\2', content)

                # 写回文件
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Processed file: {file_path}")


# 使用示例
directory_path = './'  # 替换为你的文件夹路径
replace_resource_with_assets(directory_path)
