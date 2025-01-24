#! /usr/bin/env python3

"""
assetsの中にある使用されていないファイルを削除する
"""


import os


def main(directory: str):
    if not os.path.isdir(directory):
        print(f"{directory} is not a directory")
        return

    assets = os.path.join(directory, "assets")
    if not os.path.isdir(assets):
        print(f"{assets} is not a directory")
        return
    assets_files = set(os.listdir(assets))

    md_path = os.path.join(directory, "page.md")
    if not os.path.isfile(md_path):
        print(f"{md_path} is not a file")
        return
    md_text = open(os.path.join(directory, "page.md")).read()

    for file in assets_files:
        basename = os.path.basename(file)
        if basename not in md_text:
            os.remove(os.path.join(assets, file))
            print(f"removed {file}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python3 clean_assets.py ...[directory]")
        sys.exit(1)

    for dir in sys.argv[1:]:
        main(dir)
