#! /usr/bin/env python
import glob
import json
import os
import re
from datetime import date, datetime

import yaml
from pydantic import BaseModel

from util.validate import validate_callout


IGNORE_SLUGS = {
    "template",
    "AGENTS",
    # "test",
}


def is_target(slug: str) -> bool:
    if slug in IGNORE_SLUGS:
        return False
    return True


def validate(slug: str) -> None:
    filepath = f"{slug}.md"
    with open(filepath, "r") as f:
        lines = f.read().splitlines()
    res = validate_callout(lines)
    if res is not None:
        raise ValueError(f"Validation failed for {filepath}: {res}")


# date, datetimeの変換関数
def json_serial(obj: object) -> str:
    # 日付型の場合には、文字列に変換します
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    # 上記以外はサポート対象外.
    raise TypeError("Type %s not serializable" % type(obj))


def get_json(slug: str) -> dict[str, object]:
    with open(f"{slug}.md", "r") as f:
        lines = f.read().splitlines()
    yaml_flag = False
    yaml_lines = []
    headings = []
    thumbnail = None  # サムネイルの初期値をNoneに設定
    for line in lines:
        if line == "---" and not yaml_flag:
            yaml_flag = True
            continue
        if line == "---" and yaml_flag:
            yaml_flag = False
            break
        if yaml_flag:
            yaml_lines.append(line)
    for line in lines:
        if thumbnail is None:  # 最初の画像が見つかるまで
            image_match = re.search(r"^!\[.*?\]\((.*?\.webp)\)", line)
            if image_match:
                image_path = image_match.group(1)
                thumbnail = os.path.basename(image_path)  # ファイル名のみ抽出

    dic: dict[str, object] = yaml.safe_load("\n".join(yaml_lines))  # yamlから辞書を作成
    for line in lines:
        if line.startswith("# "):
            # タイトルを取得
            dic["title"] = line[2:]
        heading_match = re.match(r"^(##+) (.*)", line)
        if heading_match:
            # 見出しを取得
            level = len(heading_match.group(1))
            title = heading_match.group(2)
            headings.append(
                {
                    "level": level,
                    "title": title,
                }
            )
    dic["headings"] = headings
    dic["slug"] = slug
    dic["thumbnail"] = thumbnail
    return dic


def main() -> None:
    os.chdir(os.path.dirname(__file__))

    page_info = {}

    for md_path in glob.glob("*.md"):
        slug = os.path.splitext(md_path)[0]
        validate(slug)
        dic = get_json(slug)
        page_info[slug] = dic
    json.dump(page_info, open("page-info.json", "w"), default=json_serial, indent=4)


if __name__ == "__main__":
    main()
