"""
- ブログコンテンツのディレクトリ構成を変更しよう
    - 現在
        - `/[slug]/page.md`
        - `/[slug]/assets/***.webp`
    - 現在の構成の問題点
        - 記事が増えるとObsidianで編集する際にファイルを見つけるのが困難になる
          Obsidianではフォルダ名でソートすることが不可能だから
        - 編集することが少ない公開済みの記事を`/published`ディレクトリに格納しているが、これではGCSと同期する際に面倒
          ディレクトリが変わるため、旧ディレクトリのファイルを一度削除してから`/published`にアップロードしないといけない
    - 変更後
        - `/[slug].md`
        - `/assets/***.webp`
    - 変更のポイント
        - 記事のファイルをルートディレクトリに直接配置
        - そうすることで最後に編集した記事を並び順上位に持ってくることができる
        - assetsはルートディレクトリに配置してごちゃまぜにする
          →特定の画像を探したいときに不便になる可能性があるが仕方がない
"""

import os
import glob
import shutil

article_dirs = [os.path.dirname(p) for p in glob.glob("*/page.md")]

for article_dir in article_dirs:
    article_slug = os.path.basename(article_dir)
    article_md = os.path.join(article_dir, "page.md")
    article_assets = os.path.join(article_dir, "assets")
    new_article_md = f"{article_slug}.md"

    shutil.move(article_md, new_article_md)
    if os.path.exists(article_assets):
        for asset in os.listdir(article_assets):
            shutil.move(os.path.join(article_assets, asset), "assets")
    shutil.rmtree(article_dir)
