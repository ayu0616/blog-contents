#! /usr/bin/env python
import os
import shutil

os.chdir(os.path.dirname(__file__))


def check_exists(slug: str):
    return os.path.exists(slug)


def new_page(slug: str):
    # テンプレートディレクトリをコピーする
    shutil.copytree("template", slug)


def main(slugs: list[str]):
    for slug in slugs:
        if check_exists(slug):
            print(f'"{slug}" already exists.')
        else:
            new_page(slug)


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        slugs = [input("Enter the slug: ")]
    else:
        slugs = sys.argv[1:]

    main(slugs)
