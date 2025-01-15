import os
from PIL import Image


def compress_image(input_path, output_path, max_kb):
    img = Image.open(input_path)
    img.save(output_path, 'JPEG', quality=85)
    while os.path.getsize(output_path) > max_kb * 1024:
        img = Image.open(output_path)
        img.save(output_path, 'JPEG', quality=img.info['quality'] - 5)


def convert_and_compress_png(source_folder, output_folder, max_kb):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for root, _, files in os.walk(source_folder):
        for file in files:
            if file.endswith('.png'):
                file_path = os.path.join(root, file)
                if os.path.getsize(file_path) > max_kb * 1024:
                    output_path = os.path.join(
                        output_folder, os.path.splitext(file)[0] + '.jpg')
                    compress_image(file_path, output_path, max_kb)


def convert_and_compress_avif_webp(source_folder, output_folder, max_kb):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for root, _, files in os.walk(source_folder):
        for file in files:
            if file.endswith('.avif') or file.endswith('.webp'):
                file_path = os.path.join(root, file)
                output_path = os.path.join(
                    output_folder, os.path.splitext(file)[0] + '.jpg')
                compress_image(file_path, output_path, max_kb)

convert_and_compress_png('./assets', 'C:/Users/sha1r/Pictures', 999)
convert_and_compress_avif_webp('./assets', 'C:/Users/sha1r/Pictures', 999)
