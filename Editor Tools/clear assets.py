# Warning: This script will delete all unreferenced images in the assets folder.

import os
import re


def find_image_paths(directory):
    image_paths = set()
    md_pattern = re.compile(r'!\[.*?\]\((.*?)\)')
    md_pattern_special = re.compile(r'!\[.*?\]\(<(.*?)>\)')

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                    matches = md_pattern.findall(content)
                    matches_special = md_pattern_special.findall(content)
                    for match in matches:
                        if not match.startswith('<'):
                            image_paths.add(os.path.normpath(
                                os.path.join(root, match)))
                    for match in matches_special:
                        image_paths.add(os.path.normpath(
                            os.path.join(root, match)))
    # for image_path in image_paths:
    #     print(image_path)
    return image_paths


def find_unreferenced_images(directory):
    referenced_images = find_image_paths(directory)
    assets_dirs = [os.path.join(directory, 'assets'), os.path.join(
        directory, 'zh-CN', 'assets')]
    unreferenced_images = []

    for assets_dir in assets_dirs:
        for root, _, files in os.walk(assets_dir):
            for file in files:
                file_path = os.path.normpath(os.path.join(root, file))
                file_path_normalized = file_path.replace(' ', '%20')
                if file_path_normalized not in referenced_images:
                    unreferenced_images.append(file_path)
                    # print(file_path)
    for image in unreferenced_images:
        try:
            os.remove(image)
            print(f'Deleted: {image}')
        except OSError as e:
            print(f'Error deleting {image}: {e}')
            return False
    return True


directory = '.'
# find_image_paths(directory)
find_unreferenced_images(directory)
