#! .venv/bin/python

"""
Google Cloud Storage にファイルを同期するスクリプト
"""

import os
import glob
from datetime import datetime
from zoneinfo import ZoneInfo
from lib.storage import GCS
import asyncio
import update_page_info


async def main() -> None:
    os.chdir(os.path.dirname(__file__))

    # ページ情報を更新
    print("ページ情報を更新します...")
    update_page_info.main()
    print("ページ情報の更新が完了しました")

    # 対象となるファイル
    target_patterns = [
        "*.md",
        "assets/*.*",
        "page-info.json",
    ]

    try:
        with open("./last-sync.txt", "r") as f:
            last_sync = datetime.fromisoformat(f.read().strip())
    except FileNotFoundError:
        print("last-sync.txt が存在しないため、初回同期とみなします。")
        # 非常に過去の日時を設定して、すべてのファイルをアップロード対象とする
        last_sync = datetime(1970, 1, 1, tzinfo=ZoneInfo("Asia/Tokyo"))

    gcs = GCS()

    local_files = []
    for pattern in target_patterns:
        local_files.extend(glob.glob(pattern))

    gcs_files = await gcs.list_files("")

    local_files_set = set(local_files)
    gcs_files_set = set(gcs_files)

    files_to_delete = gcs_files_set - local_files_set

    print("削除処理を開始します...")
    delete_tasks = []
    for file in files_to_delete:
        print(f"  {file} を削除します")
        delete_tasks.append(gcs.delete(file))
    await asyncio.gather(*delete_tasks)
    print(f"削除処理が完了しました。削除ファイル数: {len(files_to_delete)}")

    files_to_upload = local_files

    print("アップロード処理を開始します...")
    upload_tasks = []
    uploaded_count = 0
    content_type_map = {
        ".jpeg": "image/jpeg",
        ".jpg": "image/jpeg",
        ".png": "image/png",
        ".webp": "image/webp",
        ".svg": "image/svg+xml",
        ".md": "text/markdown",
        ".json": "application/json",
        ".txt": "text/plain",
    }
    for file in files_to_upload:
        # ファイルの更新日時を取得
        modified_time = datetime.fromtimestamp(
            os.path.getmtime(file), tz=ZoneInfo("Asia/Tokyo")
        )
        if modified_time > last_sync:
            print(f"  {file} をアップロードします")
            with open(file, "rb") as f:
                content = f.read()
            extension = os.path.splitext(file)[1].lower()
            content_type = content_type_map.get(extension)
            upload_tasks.append(gcs.write(file, content, content_type=content_type))
            uploaded_count += 1
    await asyncio.gather(*upload_tasks)
    print(f"アップロード処理が完了しました。アップロードファイル数: {uploaded_count}")

    # 最終同期時刻を更新
    with open("./last-sync.txt", "w") as f:
        f.write(datetime.now(tz=ZoneInfo("Asia/Tokyo")).isoformat())

    print("同期が完了しました")


if __name__ == "__main__":
    asyncio.run(main())
