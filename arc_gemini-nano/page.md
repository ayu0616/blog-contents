---
published: true
publishedAt: 2024-08-27
tags:
  - Web
  - AI
created: 2024-06-26 17:15:54+09:00
modified: 2024-08-27 10:27:11+09:00
---

# ArcブラウザでローカルLLM（Gemini Nano）を利用する方法

```table-of-contents
minLevel: 2
```

## 結論

- ArcでもGemini Nanoを利用できそう
- だが、出力はまったく役に立たない

## 手順

ArcはChromiumをベースに作られているため、Chromeと同様の機能を使用することができます。したがってGemini NanoもChromeと同じような設定で使用することができるようです。
手順は以下の記事のいずれかを参考にしてください。

- [Chrome の Gemini Nano を試す｜npaka](https://note.com/npaka/n/n17176250330e)
- [Chrome内蔵LLM Gemini Nanoを使ってみた](https://zenn.dev/the_exile/articles/chrome-gemini-nano)
- [【KARAKURI LM 10本ノック】番外編： Chrome内蔵のローカルLLM (Gemini Nano)で「どこでもCopilot」を作ってみた | by Yuki Yoshida | KARAKURI Techblog | Aug, 2024 | Medium](https://medium.com/karakuri/karakuri-lm-10%E6%9C%AC%E3%83%8E%E3%83%83%E3%82%AF-%E7%95%AA%E5%A4%96%E7%B7%A8-chrome%E5%86%85%E8%94%B5%E3%81%AE%E3%83%AD%E3%83%BC%E3%82%AB%E3%83%ABllm%E3%81%A7-%E3%81%A9%E3%81%93%E3%81%A7%E3%82%82copilot-%E3%82%92%E4%BD%9C%E3%81%A3%E3%81%A6%E3%81%BF%E3%81%9F-384da92c6080)

Arcのバージョンなどの情報はこんな感じです。ベータ版などではなく、通常のリリース版を利用しています。

```
Based on Chromium version 128.0.6613.85 (Official Build) （arm64）
```

## やってみた

先ほど紹介した手順を完了したら、Arcのデベロッパーツールを開きましょう。

コンソールにこんな感じのプログラムを貼り付けてみます。

```js
// 生成AI機能が利用可能かどうか確認
const canCreate = await window.ai.canCreateTextSession();

if (canCreate !== "no") {
  // セッションを作成
  const session = await window.ai.createTextSession();

  // 質問してみる：
  const result1 = await session.prompt("日本の首都はどこですか？");
  console.log(result1);
  
  const result2 = await session.prompt("ハンバーグの作り方を説明してください");
  console.log(result2);
}
```

![](スクリーンショット%202024-08-27%2010.21.47.png)

すると、こんな感じに出力されてしまいます。
どうしてなのでしょうか？ やはりChromeから利用しないといけないのでしょうか？

Arcでも生成AI機能を利用することができるとワクワクしていたのでこれは残念でした。
言ったことをそのまま返してくれるので、オウムを飼いたいけど躊躇している方はぜひGemini Nanoを飼って日々の疲れを癒やしてもらってくださいね。
