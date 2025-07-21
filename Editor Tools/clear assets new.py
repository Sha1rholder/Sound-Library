import os
import re
from pathlib import Path
from urllib.parse import unquote
from typing import Set, List, Tuple

dry_run_global = True  # 是否为预览模式，True表示只预览不实际删除


class AssetAnalyzer:
    def __init__(self, project_root: str):
        self.project_root = Path(project_root).resolve()
        self.assets_dirs = [
            self.project_root / "assets",
            self.project_root / "zh-CN" / "assets",
        ]

    def find_all_markdown_files(self) -> List[Path]:
        """递归查找所有.md文件"""
        md_files = []
        for root, dirs, files in os.walk(self.project_root):
            for file in files:
                if file.endswith(".md"):
                    md_files.append(Path(root) / file)
        return md_files

    def extract_asset_references(self, md_file: Path) -> Set[str]:
        """从markdown文件中提取所有assets引用"""
        try:
            with open(md_file, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            print(f"读取文件 {md_file} 失败: {e}")
            return set()

        # 正则表达式匹配markdown图片语法
        # 支持 ![alt](path) 和 ![alt](<path>) 两种格式
        patterns = [
            # 标准格式：![alt](path)
            r"!\[([^\]]*)\]\(([^)]+)\)",
            # 尖括号格式：![alt](<path>)
            r"!\[([^\]]*)\]\(<([^>]+)>\)",
        ]

        asset_refs = set()

        for pattern in patterns:
            matches = re.findall(pattern, content)
            for match in matches:
                # match[1] 是路径
                path = match[1]

                # 检查是否是assets引用
                if "/assets/" in path or "\\assets\\" in path:
                    # 处理URL编码（如%20表示空格）
                    path = unquote(path)

                    # 将路径转换为相对于markdown文件的绝对路径
                    if path.startswith(("/", "\\")):
                        # 绝对路径（相对于项目根目录）
                        full_path = self.project_root / path.lstrip("/\\")
                    else:
                        # 相对路径
                        full_path = (md_file.parent / path).resolve()

                    # 只保留在assets目录下的引用
                    try:
                        for assets_dir in self.assets_dirs:
                            if (
                                assets_dir in full_path.parents
                                or full_path.parent == assets_dir
                            ):
                                asset_refs.add(full_path)
                                break
                    except:
                        pass

        return asset_refs

    def get_all_asset_files(self) -> Set[Path]:
        """获取所有assets目录下的文件"""
        asset_files = set()
        for assets_dir in self.assets_dirs:
            if assets_dir.exists():
                for root, dirs, files in os.walk(assets_dir):
                    for file in files:
                        asset_files.add(Path(root) / file)
        return asset_files

    def analyze(self) -> Tuple[Set[Path], Set[Path], Set[Path]]:
        """
        分析assets引用情况
        返回：(引用但不存在的文件, 引用且存在的文件, 未被引用但存在的文件)
        """
        # 获取所有markdown文件
        md_files = self.find_all_markdown_files()
        print(f"找到 {len(md_files)} 个markdown文件")

        # 提取所有assets引用
        all_references = set()
        for md_file in md_files:
            refs = self.extract_asset_references(md_file)
            all_references.update(refs)

        print(f"找到 {len(all_references)} 个assets引用")

        # 获取所有实际存在的asset文件
        all_asset_files = self.get_all_asset_files()
        print(f"找到 {len(all_asset_files)} 个实际存在的asset文件")

        # 分类
        referenced_but_not_exist = set()
        referenced_and_exist = set()

        for ref in all_references:
            if ref.exists():
                referenced_and_exist.add(ref)
            else:
                referenced_but_not_exist.add(ref)

        # 未被引用但存在的文件
        not_referenced_but_exist = all_asset_files - referenced_and_exist

        return referenced_but_not_exist, referenced_and_exist, not_referenced_but_exist

    def delete_unreferenced_assets(
        self, unreferenced_files: Set[Path], dry_run: bool = False
    ):
        """
        删除未被引用的asset文件
        dry_run: 如果为True，只显示将要删除的文件，不实际删除
        """
        if dry_run:
            print("\n[预览模式] 以下文件将被删除：")
        else:
            print("\n正在删除未被引用的文件：")

        deleted_count = 0
        for file_path in unreferenced_files:
            if file_path.exists():
                try:
                    relative_path = file_path.relative_to(self.project_root)
                    print(f"  - {relative_path}")

                    if not dry_run:
                        os.remove(file_path)
                        deleted_count += 1
                except Exception as e:
                    print(f"  ! 删除失败 {file_path}: {e}")

        if dry_run:
            print(f"\n预览完成，共 {len(unreferenced_files)} 个文件将被删除")
            print("如需实际删除，请设置 dry_run=False")
        else:
            print(f"\n删除完成，共删除 {deleted_count} 个文件")


def main():
    # 设置项目根目录
    project_root = "./"  # 请根据实际情况调整路径

    analyzer = AssetAnalyzer(project_root)

    # 执行分析
    referenced_but_not_exist, referenced_and_exist, not_referenced_but_exist = (
        analyzer.analyze()
    )

    # 打印结果
    print("\n" + "=" * 50)
    print("分析结果：")
    print("=" * 50)

    print(
        f"\n1. Markdown文件引用了，但实际上不存在的文件路径 ({len(referenced_but_not_exist)} 个):"
    )
    if referenced_but_not_exist:
        for file_path in sorted(referenced_but_not_exist):
            try:
                relative_path = file_path.relative_to(analyzer.project_root)
                print(f"  - {relative_path}")
            except:
                print(f"  - {file_path}")
    else:
        print("  无")

    print(
        f"\n2. Markdown文件引用了，且找得到的assets引用文件路径 ({len(referenced_and_exist)} 个):"
    )
    if referenced_and_exist:
        for file_path in sorted(referenced_and_exist):
            relative_path = file_path.relative_to(analyzer.project_root)
            print(f"  - {relative_path}")
    else:
        print("  无")

    print(
        f"\n3. Markdown文件都没有引用过，但在assets中存在的文件路径 ({len(not_referenced_but_exist)} 个):"
    )
    if not_referenced_but_exist:
        for file_path in sorted(not_referenced_but_exist):
            relative_path = file_path.relative_to(analyzer.project_root)
            print(f"  - {relative_path}")
    else:
        print("  无")

    # 询问是否删除未引用的文件
    if not_referenced_but_exist:
        print("\n" + "-" * 50)
        analyzer.delete_unreferenced_assets(
            not_referenced_but_exist, dry_run=dry_run_global
        )


if __name__ == "__main__":
    main()
