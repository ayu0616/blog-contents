---
published: false
publishedAt: 
tags:
  - 備忘録
  - Obsidian
created: 2025-02-04 17:08:55+09:00
modified: 2025-02-04 17:46:16+09:00
---

# Obsidianで表のセルに入力したテキストを折り返さないで表示する方法

```table-of-contents
title: 
style: nestedList # TOC style (nestedList|nestedOrderedList|inlineFirstLevel)
minLevel: 2 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
includeLinks: true # Make headings clickable
hideWhenEmpty: false # Hide TOC if no headings are found
debugInConsole: false # Print debug info in Obsidian console
```

## やりたいこと

Obsidianでテーブルを作成したときに、カラムの数が多くなってくると表示がやや崩れ気味になることが気になっている。
そのため、カラム数が多くなってもテキストを折り返さず表示する方法はないか試してみた。

【現状】
- Obsidianのテーブルはテーブル全体の幅が画面の横幅を超えないように調整される
- そのため、カラムが多くなると1つのセルの幅が小さくなり、長いテキストが折り返されて読みづらい

![セルのテキストが折り返されている](テーブルスタイル適用前.webp)

【目標】
- テキストが折り返されずに表示される
- テーブル全体を横スクロールすることで後ろの方のカラムを閲覧することができる
- （デザイン面なので好みだが）
    - ヘッダ行に背景色を加える
    - セルの上下左右の余白をそれぞれ増やす

![セルのテキストが折り返されず、テーブル全体が横スクロール可能](テーブルスタイル適用後.webp)

## CSSで指定すれば良い

```css
th > div.table-cell-wrapper {
    background-color: #f8fafc !important; /* ヘッダの背景色（任意） */
}

th > div.table-cell-wrapper,
td > div.table-cell-wrapper {
    padding: 0.5em 1em !important; /* 余白調整（任意） */

    white-space: nowrap !important; /* テキスト折り返し防止 */
}
```

