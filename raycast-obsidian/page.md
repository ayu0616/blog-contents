---
published: true
publishedAt: 2024-07-15
tags:
  - 備忘録
created: 2024-06-26 17:15:54+09:00
modified: 2024-07-15 01:50:28+09:00
---

# ObsidianのVaultをRaycastで一発で開く方法

```table-of-contents
minLevel: 2
```

## 結論

```callout
----
title: Quicklinksを使う
icon: 💡
----
Quicklinksに`obsidian://open?vault={vaultName}`を設定してやる
```

## 背景

私は、Obsidianで日記を書いているのですが、わざわざアプリを開くのが面倒だと感じていました。vaultを4つぐらい使い分けていて、アプリを開いた際には最後に開いていたvaultが開く仕組みになっているようで、別のvaultから日記に変更するのも手間でした。

RaycastというMacの便利ランチャーアプリにObsidian用のプラグイン（[Raycast Store: Obsidian - overview](https://www.raycast.com/KevinBatdorf/obsidian)）があることは知っていて絶賛利用しているし便利なのですが、それでもやはり`"Open Vault" -> "{vaultName}"`という2ステップを踏む必要がありました。

1ステップ目
![](スクリーンショット%202024-07-15%201.45.49.png)
2ステップ目
![](スクリーンショット%202024-07-15%201.46.07.png)

## 対策

Raycastにデフォルトで入っている`Quicklink`を使用すれば良いことがわかりました。

QuicklinksのURLに`obsidian://open`と指定するとObsidianが開くリンクを作成することが出来ます。

![](スクリーンショット%202024-07-15%201.47.22.png)
詳しい仕様については[Obsidian URI - Obsidian Help](https://help.obsidian.md/Extending+Obsidian/Obsidian+URI)をご参照ください。
