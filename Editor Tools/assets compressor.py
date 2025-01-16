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


def find_and_process(article_path, output_path, max_kb=0):
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


user_name = "sha1r"
output_path = f"C:\\Users\\{user_name}\\Pictures\\assets"

# article_path = "./zh-CN/Knowledge/平面磁耳机的设计逻辑.md"
# allowed_extensions = ['.jpg', '.png', '.gif']
# find_and_process(article_path, output_path, 999)

article_path = "./en-US/Knowledge/Design Philosophy of Planar Magnetic Headphones.md"
allowed_extensions = ['.jpg', '.png', '.gif', '.webp', '.avif']
find_and_process(article_path, output_path)
