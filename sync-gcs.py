#! .venv/bin/python

"""
Google Cloud Storage にファイルを同期するスクリプト
"""

import os
import glob
from datetime import datetime
from zoneinfo import ZoneInfo
from lib.storage import GCS

os.chdir(os.path.dirname(__file__))

# 対象となるファイル
target_patterns = [
    "*.md",
    "assets/*.*",
    "page-info.json",
]

with open("./last-sync.txt", "r") as f:
    last_sync = datetime.fromisoformat(f.read().strip())

gcs = GCS()

local_files = []
for pattern in target_patterns:
    local_files.extend(glob.glob(pattern))

gcs_files = gcs.list_files("")

local_files_set = set(local_files)
gcs_files_set = set(gcs_files)

files_to_delete = gcs_files_set - local_files_set

for file in files_to_delete:
    print(f"{file} を削除します")
    gcs.delete(file)

files_to_upload = local_files

for file in files_to_upload:
    # ファイルの更新日時を取得
    modified_time = datetime.fromtimestamp(os.path.getmtime(file), tz=ZoneInfo("Asia/Tokyo"))
    if modified_time > last_sync:
        print(f"{file} をアップロードします")
        with open(file, "rb") as f:
            content = f.read()
        gcs.write(file, content)


# 最終同期時刻を更新
with open("./last-sync.txt", "w") as f:
    f.write(datetime.now(tz=ZoneInfo("Asia/Tokyo")).isoformat())

print("同期が完了しました")
