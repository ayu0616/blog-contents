---
published: true
publishedAt: 2024-07-04
tags:
  - プログラミング
  - Python
created: 2024-06-26 17:15:54+09:00
modified: 2024-07-04 14:41:27+09:00
---

# Pythonのmatch-caseで困ったところ

```table-of-contents
minLevel: 2
```

## やりたかったこと

```python
val: int | float | bool | str = ...

if (type(val) is int) or (type(val) is float):
    ...
elif type(val) is bool:
    ...
else:
    ...
```

if-elseで書いた上のような処理をmatch-caseを用いてやりたいと思いました。

- やりたかったこと
    - 型によって処理を分ける
    - 複数条件で同じ処理を実行
        - 上の例なら、`val`の型が`int`と`float`で同じ処理を行う

やりたかった動機は、`type(val)`をいたるところに書く必要があり、コードが読みにくかったからです。

## やろうとしてダメだったコード

```callout
----
icon: ⚠
title: 下のコードを実行するとエラーが発生します
----
```

```python
val: int | float | bool | str = ...

match type(val):
    case int:
    case float:
        ...
    case bool:
        ...
    case _:
        ...
```

JavaScriptとかだったらこんな感じの書き方をしたはずですが、Pythonではダメでした。

## 成功するコード

```python
val: int | float | bool | str = ...

match val:
    case int() | float():
        ...
    case bool():
        ...
    case _:
        ...
```

個人的には失敗したコードのほうが自然なんですけど、Pythonではこちらのコードが正しいらしいです。

pythonで普通に`int()`を実行すると`0`と出力されるので、`val == 0`でなければ中の処理が実行されなさそうですが、そんなことはなく、たとえば`val == 1`でも`case int():`の処理が実行されます。不思議ですね。
[クラスパターン](https://docs.python.org/ja/3/reference/compound_stmts.html#class-patterns)というPythonの仕様だそうですが、うーんと思ってしまいました。

## まとめ

```callout
----
icon: 💡
title: `val`がある型`Class`のインスタンスかどうか判定したい
----
- `match val`とする
- `case Class():`とする
```

```callout
----
icon: 💡
title: `val`がある値`a`または`b`であることを判定したい
----
- `case a | b:`とする
```
