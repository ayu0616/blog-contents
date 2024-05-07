#! /usr/bin/env python
import json
import os
import re
from datetime import date, datetime

import yaml

os.chdir(os.path.dirname(__file__))

IGNORE_SLUGS = {
    "template",
    # "test",
}


def is_target(slug: str):
    if not os.path.isdir(slug):
        return False
    if slug.startswith("."):
        return False
    if slug in IGNORE_SLUGS:
        return False
    return True


# date, datetimeの変換関数
def json_serial(obj):
    # 日付型の場合には、文字列に変換します
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    # 上記以外はサポート対象外.
    raise TypeError("Type %s not serializable" % type(obj))


def get_json(slug: str):
    with open(os.path.join(slug, "page.md"), "r") as f:
        lines = f.read().splitlines()
    yaml_flag = False
    yaml_lines = []
    headings = []
    for line in lines:
        if line == "---" and not yaml_flag:
            yaml_flag = True
            continue
        if line == "---" and yaml_flag:
            yaml_flag = False
            break
        if yaml_flag:
            yaml_lines.append(line)
    dic = yaml.safe_load("\n".join(yaml_lines))  # yamlから辞書を作成
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
    return dic


def main():
    slugs = [slug for slug in os.listdir() if is_target(slug)]
    page_info = {}
    for slug in slugs:
        dic = get_json(slug)
        page_info[slug] = dic
    json.dump(page_info, open("page-info.json", "w"), default=json_serial, indent=4)


if __name__ == "__main__":
    main()
