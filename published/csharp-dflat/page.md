---
published: true
publishedAt: 2024-06-28
tags:
  - ネタ
  - プログラミング
created: 2024-06-26 17:15:54+09:00
modified: 2024-06-26 22:58:52+09:00
---

# C#があるなら、D♭もあるんじゃね？と思ったら”C#”が「シーハッシュ」だった話

```table-of-contents
minLevel: 2
```

## はじめに

みなさんは **C#** という言語をご存知でしょうか？プログラミングに馴染みのある人なら一度は聞いたことがあるのではないでしょうか？逆にプログラミングを知らない人はなんのことやらといった感じでしょう。

かくいう私もC#という言語が存在することは知っていますが、何が得意な言語で、どういった文法を持っているのかは全く知りません。

唯一知っていることといえば、C#は「**シーシャープ**」と読むことぐらいです。

今回の記事を読む上でプログラミングの知識は一切必要ないのでご安心ください。

ある日、お風呂に入っているときに天からあるお告げがあったのです。

```callout
----
icon: 💡
title: C#があるなら、D♭もあるんじゃね？
----
```

神というものはなんといたずら好きなのでしょうか。この疑問が興味深すぎるあまり、私は夜も眠れませんでした。

ならば調べるしかない。

## その前に

調べる前に、音楽にあまり詳しくない人はC#とかD♭とか言われてもなんのことやらだと思うのでそこから整理しましょう。

とは言っても私も音楽なんて素人中の素人なのでざっくりとしか説明できません。

音楽では「ドレミファソラシド」の音階を「**CDEFGABC**」で表すことがあります。ラがAでそこからアルファベット順に進み、G（ソ）「まで行くとまたA（ラ）に戻ってきます。

また、音階には**半音**という概念が存在します。D♭ならD（レ）の半音下という感じです。半音上とか下とかを表すときに登場する記号が、”♯”や”♭”です。**♯（シャープ）は半音上**を、**♭（フラット）は半音下**を表す記号です。

なので、CとDのちょうど中間の音を表す方法が2つあることがわかります。1つ目が**C♯**（Cの半音上）、2つ目が**D♭**（Dの半音下）です。

もっと詳しく知りたい人はWikipediaの記事を参考にしてください。

[音名・階名表記](https://ja.wikipedia.org/wiki/音名・階名表記)

つまりこの記事で言いたいことは「C#というプログラミング言語が存在するならば、それと同じ音階のD♭という言語は存在するのかどうか気になる〜」ということです。

前置きが長くなりましたが検索してみましょう。

## Googleで検索してみた

まずは手始めにGoogleで検索をかけてみました。検索ワードは次のとおりです。

- 「D♭ プログラミング」
- 「Dフラット プログラミング」

検索してみたところ、検索結果にプログラミング言語D♭は存在しませんでした。

ただ、ひとつだけ面白い発見があったので共有しておきます。それは次のサイトに書いてありました。

[プログラム言語を確実に習得する4つのステップ](http://blogs.bizmakoto.jp/yokoyamat/entry/17387.html)

これは2014年に書かれたエンジニアのブログなのですが、興味深い記述がありました。

> C#の設計はアンダース・ヘルスバーグが行なった。彼は8ビットパソコン後期から16ビットパソコン初期の時代に人気があったTurbo Pascalの作者であり、後にDelphi(デルファイ)という言語設計に関わる。口の悪い人は「C♯はD♭だ」という。Cシャープ(ドの半音上)とDフラット(レの半音下)が同じ音階になることを揶揄して「C#の本質はDelphi(D)より格下だ」と言うわけだ。

なんとC#をディスる悪口としてD♭が使用されていた用例があったのです。悪口が大好きな私としては良い収穫になりました。

## ちょっとまてよ、、、

お分かりいただけたでしょうか。

C#を「シーシャープ」と読むのってなんか変じゃないですか？

おかしくない？じゃあInstagramの投稿で「#Dフラットなんて言語はなかったんや」というときの”#”はなんと読みますか？「シャープ」じゃないですよね？「**ハッシュ**（タグ）」ですよね。

そうです、”#”という記号は「シャープ」ではなく、「ハッシュ」なのです。

```callout
----
icon: 💡
title: C#（シーシャープ）の「シャープ」は「ハッシュ」だった
----
```

スマホやパソコンの自動変換で試してみてほしいのですが、「しゃーぷ」と入力してみてください。そうすると、”**♯**”が出てくると思います。これはハッシュ（#）とは違う記号です。

ちなみにハッシュは日本語で「**井桁**」と呼ぶこともあるらしいです。なので「いげた」と入力すると”#”や”＃”が出てくると思います。前者と後者は半角か全角かの違いです。

わけわかんなくなった人のための整理表

- \#： ハッシュ＝井桁
    - C#の「シャープ」はハッシュ
- ♯： シャープ
- 丼： どん

## まとめ

それではまとめに入ります。

今回の記事で得られた教訓は以下のとおりです。

```callout
----
icon: 💡
title: D♭という言語はないし、C#の”#”はシャープじゃない
----
```

来年のエイプリルフールには、D♭というジョーク言語を作ってみてはいかがでしょうか。あとはC#をディスりたいときに「それD♭やん」って言うとウケます（たぶん）。

「目のつけどころがシャープだね」と思った人は友人たちにこの記事をシェアしてください！

ここまでお読みいただきありがとうございました。
