Chapter 6 – Manipulating Strings  
https://automatetheboringstuff.com/chapter6/

# 概要
テキストはプログラムで扱うデータ形式の最も一般的な形式のひとつです。  
あなたはすでに「2つの値を一緒にするには + 演算子を使う」ことを知っていますが、それ以上のことができます。  
文書から任意の文字列を抽出したり、スペースを消したり、小文字を大文字に変更したり、文書のフォーマットが正しいかをチェックすることもできます。  
クリップボードにアクセスしてテキストをコピーして貼り付けるためのPythonコードを書くことだってできます。  

この章では、上記のすべてとさらにプラスアルファを下記の例題をとおして学習します。  
プログラム例「シンプルなパスワードマネージャー」と、「テキストの書式設定の退屈な作業を自動化するプログラム」

# 文字列操作

Pythonでコード内の文字列を書いたり、印刷したり、アクセスしたりする方法をいくつか見てみましょう。  

## 文字列リテラル

文字列の値をPythonコードで入力するの簡単です。`'` で始まり、`'`  で終わりにすればOKです。
しかし、下記のような場合はどうしたらいいでしょうか。  
```
'That is Alice's cat.'
```

シングルクオート `''` でくくると、うまくいかないのです。

```python
# エラー！
>>> spam = 'That is Alice's cat.'
  File "<stdin>", line 1
    spam = 'That is Alice's cat.'
                          ^
SyntaxError: invalid syntax
```

ではどうやって `Alice's` を表現すればいいのでしょうか。  
幸い、文字列を入力するには複数の方法があります。  

### ダブルクオート `""` でくくる
- かんたん
- 文字列に `'` と '"' の両方を使用する必要がある場合は、エスケープ文字を使用する必要がある。

```
>>> spam = "That is Alice's cat."
>>> spam
"That is Alice's cat."
>>>
```

### エスケープ(\)する
- バックスラッシュ(\) でエスケープする
- 単独では文字列に入れることが不可能な文字(`'`, `"` など)を使えるようになる

```python
>>> spam = 'Say hi to Bob\'s mother'
>>> spam
"Say hi to Bob's mother"
>>>
```

```
#エスケープする必要がある文字  

\` シングルクオート
\" ダブルクオート
\t タブ
\n 開業
\\ バックスラッシュ
```

```python
>>> print("Hello there!\nHow are you?\nI\'m doing fine.")
Hello there!
How are you?
I'm doing fine.
>>>
```
```python
>>> print('Dear Alice,\n\nEve\'s cat has been arrested for catnapping, cat burglary, and extortion.\n\nSincerely,\nBob')
Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob
>>>
```

### 生文字列
- 文字列の最初の引用符の前にrを置く
- 生文字列はすべてのエスケープ文字を完全に無視する(バックスラッシュはバックスラッシュとして出力する)
- 正規表現を表すのに便利

```python
>>> print(r'That is Carol\'s cat.')
That is Carol\'s cat.
>>>
```

### 三重引用符
- printするときに3つのシングルクォーテーションまたは3つのダブルクォートでくくる(`'''`, `"""`)
- 三重引用符の間の引用符、タブ、または改行は、文字列の一部とみなされる
- Pythonブロックの字下げ規則は、複数行の文字列内の行には適用されない

```python
>>> print('''Dear Alice,
...
... Eve's cat has been arrested for catnapping, cat burglary, and extortion.
...
... Sincerely,
... Bob''')
Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob
>>>
```

### 複数行コメント
- 3つのダブルクオートでくくる

```python
"""
コメントコメント
コメントコメントコメントコメントコメントコメント
"""
```

## インデックスおよび文字列のスライス
文字列は、リストと同じ方法でインデックスとスライスを使用します。  
文字列 `Hello world！` を例に考えてみます。  
文字列内の各文字をリストとして、対応する索引を持つ項目として指定します。  
スペースと感嘆符は文字数に含まれているので、 `Hello world！` はインデックス0(H)からインデックス11(!)までの、12文字の長さです。  

```
' 文字列:  H   e   l   l   o       w   o   r   l   d    !   '
  Index :  0   1   2   3   4   5   6   7   8   9   10   11
```

あるインデックスから別のインデックスまでの範囲を指定すると、**開始インデックスが含まれ、終了インデックスは含まれません。**

```python
>>> spam = 'Hello world!'
>>> spam[0]
'H'
>>> spam[4]
'o'
>>> spam[-1]
'!'
>>> spam[0:5] <-- インデックス0(H)は含む。インデックス5( )は含まない。
'Hello'
>>> spam[6:]
'world!'
>>>
```

下記は変数のスライスを別の変数に取り込む方法です。  
文字列をスライスして部分文字列として別の変数に格納することで、文字列全体と部分文字列の両方を手軽に利用できます。

```python
>>> spam = 'Hello world!'  <-- 文字列全体
>>> fizz = spam[0:5]       <-- 部分文字列
>>> fizz
'Hello'
>>>
```

## in や not in 演算子を文字列に対して使う

`in` および `not in` 演算子は、リスト値とまったく同じように文字列でも使用できます。  
`in` または `not in` を使用して結合された2つの文字列を持つ式は、真または偽のブール値で評価されます。  
これらの式は、最初の文字列(大文字と小文字を区別する)が、2番目の文字列内にあるかどうかをテストします。  

```python
>>> 'Hello' in 'Hello World'
True

>>> 'Hello' in 'Hello'
True

>>> 'HELLO' in 'Hello World'
False

>>> '' in 'spam'  # この結果は意外だった！
True

>>> 'cats' not in 'cats and dogs'
False
```


# 便利な文字列メソッド

文字列メソッドは文字列を分析したり、変換された文字列値を作成したりします。  
このセクションでは、いくつかのよく使われる方法について説明します。  

## upper(), lower(), isupper(), islower()

### upper(), lower()

- upper() : 小文字を大文字に変換
- lower() : 大文字を小文字に変換

```python
>>> spam = 'Hello world!'

# 大文字に変換
>>> spam = spam.upper()
>>> spam
'HELLO WORLD!'

# 小文字に変換
>>> spam = spam.lower()
>>> spam
'hello world!'
```
これらのメソッドは文字列自体を変更するのではなく、新しい文字列値を返すだけなので、元の文字列を変更する場合は元の文字列が格納されている変数に新しい文字列を割り当てる必要があります。  
このため、`spam = spam.upper()` のようにしてspam文字列を変更しています。  

大文字小文字を区別しない比較を行う必要がある場合は、upper() と lower() が役立ちます。
ユーザーが実際には `Great`, `great`, `GREAT`, または `grEAT` と入力したとしても、すべて「great (またはGREAT)」として処理できるようになります。

### isupper(), islower()

- isupper() : 文字列内のすべての文字が大文字である場合「True」、それ以外の場合「False」
- islower() : 文字列内のすべての文字が小文字である場合「True」、それ以外の場合「False」

```python
>>> spam = 'Hello world!'
>>> spam.islower()
False
>>> spam.isupper()
False

>>> 'HELLO'.isupper()
True
>>> 'abc12345'.islower()
True

# 文字列に「文字」が1文字も含まれていない場合
>>> '12345'.islower()
False
>>> '12345'.isupper()
False
```

upper() と lower() の文字列メソッド自体は文字列を返すので、返された文字列の値についても文字列メソッドを呼び出すことができます。  
これを行う式は、一連のメソッド呼び出しのように見えます。  

```python
>>> 'Hello'.upper()
'HELLO'
>>> 'Hello'.upper().lower()
'hello'
>>> 'Hello'.upper().lower().upper()
'HELLO'

>>> 'HELLO'.lower()
'hello'
>>> 'HELLO'.lower().islower()
True
```
