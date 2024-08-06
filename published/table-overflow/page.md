---
published: true
publishedAt: 2024-06-30
tags:
  - Web
  - プログラミング
  - 備忘録
created: 2024-06-26 17:15:54+09:00
modified: 2024-06-30 02:11:42+09:00
---

# 横スクロール対応のテーブルで画面全体がスクロール可能になってしまう不具合が起こった【HTML・CSS】

```table-of-contents
minLevel: 2
```

```callout
----
icon: ❗
title: 前提
----
- Next.js, Tailwind CSSで開発している
```

## 起こった事象

```tsx
<div className="w-full overflow-x-auto">
    <table className="min-w-full table-auto whitespace-nowrap">
        ...
    </table>
</div>
```

横スクロール対応のテーブルを作成したいと思い、上記のようにスタイルを指定した

- できたこと
    - テーブルの横スクロール対応
- 不具合
    - `<html>`や`<body>`などの横幅は画面横幅通りなのに、なぜか画面全体が横スクロール可能になる
    - 横スクロールできる長さはテーブルがオーバーフローして隠れた部分の長さと同じと思われる

![](スクリーンショット%202024-06-30%202.01.32.png)

## 解決方法

```callout
----
icon: 💡
title: "`<div>`タグの`className`に`relative`を追加するだけ"
----
```

理由はよくわかりませんが、上記の対応を行うと解決できます。
`relative`にすると親や先祖の要素の幅の計算に入らないとかそんな感じだと思います。
詳しい人、教えて下さい！
