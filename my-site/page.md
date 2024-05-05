---
published: true
publishedAt: 2024-05-05
tags:
created: 2024-05-05 16:07:02+09:00
modified: 2024-05-06 01:16:17+09:00
---

# 自分のサイトを作ってみた

```table-of-contents
minLevel: 2
```

## リポジトリ

- [フロントエンド](https://github.com/ayu0616/ayu0616.github.io)
- [ブログのコンテンツ](https://github.com/ayu0616/blog-contents)

## 使用した技術

### フロントエンド

- Next.js
    - 今見ているページのフロントエンド
    - SSGでビルドしてGitHub Pagesで配信している
- Tailwind CSS
- react-markdown
    - Markdownで書いたブログ記事をjsx要素に変換する

### CMS（コンテンツ管理システム）

- Obsidian
    - CMSではないが、ここでブログ用のMarkdownを編集する
    - フロントとは別のリポジトリでアップロードして、それをフロントのビルド時に参照する
