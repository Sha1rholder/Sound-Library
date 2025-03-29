import os
import shutil
from PIL import Image, UnidentifiedImageError
import pillow_avif  # 这句不能删
import re


def clear_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder created: {folder_path}")
    else:
        shutil.rmtree(folder_path)
        os.makedirs(folder_path)
        print(f"Folder erased: {folder_path}")


def copy_img(file_path, output_path, file_index):
    file_extension = os.path.splitext(file_path)[1]
    shutil.copy(file_path, os.path.join(
        output_path, f"{file_index}{file_extension}"))


def compress_jpg(jpg_path, max_kb=0):
    if max_kb != 0:
        jpg = Image.open(jpg_path)
        quality = 95
        while os.path.getsize(jpg_path) > max_kb * 1024 and quality > 0:
            jpg.save(jpg_path, quality=quality)
            quality -= 1


def convert_and_compress(file_path, output_path, file_index, max_kb=0):
    try:
        img = Image.open(file_path)
        img = img.convert('RGB')
        jpg_path = os.path.join(output_path, f'{file_index}.jpg')
        img.save(jpg_path, 'JPEG', quality=95)
        compress_jpg(jpg_path, max_kb=max_kb)
    except UnidentifiedImageError:
        print(f"Cannot identify image file: {file_path}")


def find_and_process(article_path, output_path, allowed_extensions, max_kb=0):
    clear_folder(output_path)
    md_pattern = re.compile(r'!\[.*?\]\((.*?)\)')
    md_pattern_special = re.compile(r'!\[.*?\]\(<(.*?)>\)')
    img_paths = []
    with open(article_path, 'r', encoding='utf-8') as file:
        content = file.read()
        matches = md_pattern.findall(content)
        matches_special = md_pattern_special.findall(content)
        for match in matches:
            if not match.startswith('<'):
                img_path = os.path.normpath(os.path.join(
                    os.path.dirname(article_path), match))
                img_paths.append(img_path)
        for match in matches_special:
            img_path = os.path.normpath(os.path.join(
                os.path.dirname(article_path), match))
            img_paths.append(img_path)
    file_index = 1
    for img_path in img_paths:
        img_path = img_path.replace('\\', '\\\\').replace('%20', ' ')
        if img_path.endswith('.jpg'):
            copy_img(img_path, output_path, file_index)
            compress_jpg(f"{output_path}\\{file_index}.jpg", max_kb)
        else:
            extension_allowed = False
            for extension in allowed_extensions:
                if img_path.endswith(extension):
                    extension_allowed = True
                    if os.path.getsize(img_path) <= max_kb * 1024 or max_kb == 0:
                        copy_img(img_path, output_path, file_index)
                    else:
                        convert_and_compress(
                            img_path, output_path, file_index, max_kb)
            if not extension_allowed:
                convert_and_compress(
                    img_path, output_path, file_index, max_kb)
        file_index += 1
    print(f"{file_index-1} images processed to {output_path}")


def independize_document(article_path, target_folder, format="md"):
    """实现文档独立化功能"""
    # 清空并创建目标文件夹
    clear_folder(target_folder)

    # 克隆原文档
    cloned_doc_name = os.path.basename(article_path)
    cloned_doc_path = os.path.join(target_folder, cloned_doc_name)
    shutil.copy(article_path, cloned_doc_path)

    # 创建assets子文件夹
    assets_dir = os.path.join(target_folder, 'assets')
    os.makedirs(assets_dir, exist_ok=True)

    # 匹配所有图片引用（包含普通和带<>的格式）
    combined_pattern = re.compile(r'!\[(.*?)\]\(<?(.*?)>?\)')
    img_paths = []

    with open(article_path, 'r', encoding='utf-8') as f:
        content = f.read()
        matches = combined_pattern.findall(content)
        for desc, path in matches:
            # 处理路径中的特殊字符和空格
            clean_path = path.replace('%20', ' ').replace('\\', '/')
            img_paths.append(clean_path)

    # 处理每个图片文件
    for rel_path in img_paths:
        # 转换为绝对路径
        abs_path = os.path.normpath(os.path.join(
            os.path.dirname(article_path), rel_path))

        if not os.path.exists(abs_path):
            print(f"图片不存在: {abs_path}")
            continue

        # 获取文件名并复制到assets目录
        filename = os.path.basename(abs_path)
        target_path = os.path.join(assets_dir, filename)
        shutil.copy(abs_path, target_path)

    # 修改克隆文档中的图片引用
    with open(cloned_doc_path, 'r', encoding='utf-8') as f:
        content = f.read()

    def replace_image_link(match):
        desc = match.group(1)
        old_path = match.group(2)
        # 获取实际的文件名
        abs_old_path = os.path.normpath(os.path.join(
            os.path.dirname(article_path),
            old_path.replace('%20', ' ').replace('\\', '/')))
        return f'![{desc}](<./assets/{os.path.basename(abs_old_path)}>)'

    new_content = combined_pattern.sub(replace_image_link, content)

    with open(cloned_doc_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"文档已独立化保存在: {target_folder}")


# 使用示例保持不变
user_name = "sha1r"
output_path = f"C:\\Users\\{user_name}\\Pictures\\assets"
independent_folder = f"C:\\Users\\{user_name}\\Pictures\\independent_assets"
article_path = "./zh-CN/Knowledge/初识数字音频.md"
independize_document(article_path, independent_folder, format="md")


# 文档资产全压缩功能示例
# article_path = "./en-US/Knowledge/Design Philosophy of Planar Magnetic Headphones.md"
# allowed_extensions = ['.jpg', '.png', '.gif', '.webp', '.avif']
# find_and_process(article_path, output_path, allowed_extensions)
