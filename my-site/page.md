---
published: true
publishedAt: 2024-05-05
tags:
  - Web
  - プログラミング
created: 2024-05-05 16:07:02+09:00
modified: 2024-06-17 00:53:18+09:00
---

# 自分のサイトを作ってみた

```table-of-contents
minLevel: 2
```

## リポジトリ

GitHubのリポジトリを置いときます

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

### コンテンツ管理

ブログ記事を書くためのシステムやツール

- Obsidian
    - ここでブログ用のMarkdownを編集する
    - フロントとは別のリポジトリでアップロードして、それをフロントのビルド時に参照する

## 掲載するコンテンツ

- `/`
    - トップページ
    - プロフィールやSNSのリンクを配置する
- `/skill`
    - 技術スタックの一覧ををグラフの形で表示する
    - `/skill/[id]`
        - 各技術要素の詳細を解説する
        - 現在制作中
- `/work`
    - これまで作ってきた作品の一覧を表示する
    - `/work/[slug]`
        - 作品の詳細を解説する
        - 現在制作中
- `/blog`
    - ブログの一覧
    - `/blog/[slug]`
        - ブログの記事
    - `/blog/tag/[tag]`
        - タグ別の記事一覧

## ビルド・デプロイ

ビルドとデプロイはGitHub Actionsを用いて行いました。
このサイトはGitHub Pages上で配信されています。

基本的には[nextjs.yml](https://github.com/actions/starter-workflows/blob/main/pages/nextjs.yml)を用いればよいですが、いくつか設定事項があります。

- `next.config.js`に`output: 'export'`の設定を追加して`out`ディレクトリにビルド後のコードが出力されるように設定する必要がある
- 当プロジェクトではpnpmを利用しているため、そのための設定を追記
- 別リポジトリで管理しているブログ記事のデータを引っ張ってくる処理の追加

[設定事項を追記したあとのファイル](https://github.com/ayu0616/ayu0616.github.io/blob/develop/.github/workflows/nextjs.yml)

参考にしたサイト： [2023年8月版: Next.jsをGitHub ActionsでGitHub Pagesにデプロイする方法](https://zenn.dev/pino0701/articles/nextjs_github_pages)

## これから

これからやりたいことを書いて今回の記事を終えたいと思います。

- `/skill/[id]`, `/work/[slug]`を実装する
- ブログ記事を充実させる
