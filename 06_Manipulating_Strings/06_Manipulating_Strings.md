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

## その他の isX 文字列メソッド

islower() と isupper() に加えて、「is」で始まる名前を持ついくつかの文字列メソッドがあります。
これらのメソッドは、文字列の性質を記述するブール値を返します。

- isalpha() : 文字列が **文字のみ** の場合「True」
- isalnum() : 文字列が **文字と数字のみ** の場合に「True」 ★英数字であるかをテスト
- isdecimal() : 文字列が **数字のみ** の場合「True」 ★10進数であるかのテスト
- isspace() : 文字列が **空白、タブ、改行のみ** の場合「True」
- istitle() : 文字列の **最初の1文字が大文字であと全部小文字** (例.Hello) の場合「True」

```python
>>> 'hello'.isalpha()
True
>>> 'hello123'.isalpha()
False
>>> 'hello123'.isalnum()
True
>>> 'hello'.isalnum()
True
>>> '123'.isdecimal()
True
>>> '      '.isspace()
True
>>> 'This Is Title Cace'.istitle()
True
>>> 'This Is Title Cace 123'.istitle()
True
>>> 'This Is not Title Cace'.istitle()
False
>>> 'This Is NOT Title Cace Either'.istitle()
False
```

isX 文字列メソッドは、ユーザー入力を検証する必要がある場合に役立ちます。
たとえば、次のプログラムは、有効な入力を提供するまで、ユーザーに年齢とパスワードを繰り返し尋ねます。  

```python
# validateInput.py

Enter your age:
forty two
Please enter a number for your age.
Enter your age:
42
Select a new password (letters and numbers only):
test!!
Passwords can only have letters and numbers.
Select a new password (letters and numbers only):
test
```

## startswith(), endswith()

- startswith() : 呼び出された文字列値がメソッドに渡された文字列で開始している場合「True」
- endswith() : 呼び出された文字列値がメソッドに渡された文字列で終わっている場合「True」

```python
>>> 'Hello world!'.startswith('Hello')
True
>>> 'Hello world!'.endswith('world!')
True
>>> 'abc123'.startswith('abcdef')
False
>>> 'abc123'.endswith('12')
False
>>> 'Hello world!'.startswith('Hello world!')
True
>>> 'Hello world!'.endswith('Hello world!')
True
```

これらのメソッドは、全体ではなく文字列の **最初** または **最後** の部分が判定する文字列と等しいかどうかだけをチェックする必要がある場合、「== equals演算子」に変わる便利な方法です。  


## join(), split()

- join() : 文字列のリストに対して呼び出すと、1つの文字列値に結合する。  
  `'デリミタ'.join(['A', 'B', 'C'])` とすると、指定したデリミタで区切って出力する。
- split() : それは文字列値に対して呼び出すと、文字列のリストを返す。  
  `'aaa,bbb,ccc'.split('デリミタ')` とすると、指定したデリミタの位置で区切って出力する(通常のデリミタはスペースかタブ)。  
  split()の一般的な使い方は、複数行の文字列を改行文字に沿って分割すること。

```python
# join()

# デリミタはカンマ(,)
>>> ', '.join(['cats', 'rats', 'bats'])
'cats, rats, bats'

# デリミタはスペース
>>> ' '.join(['My', 'name', 'is', 'Simon'])
'My name is Simon'

# デリミタはABC
>>> 'ABC'.join(['My', 'name', 'is', 'Simon'])
'MyABCnameABCisABCSimon'
```

```python
# split()

# デリミタ指定なし(デフォルトのスペースで区切る)
>>> 'My name is Simon'.split()
['My', 'name', 'is', 'Simon']

# デリミタは「ABC」
>>> 'MyABCnameABCisABCSimon'.split('ABC')
['My', 'name', 'is', 'Simon']

# デリミタは「m」
>>> 'My name is Simon'.split('m')
['My na', 'e is Si', 'on']
```

split() を使用して、改行に沿って分割する。  
改行文字`\n` を引数として、`split('\n')` のようにsplitメソッドに渡す。  
すると、改行に沿ってスパムに格納されている複数行の文字列を分割し、各項目が文字列の1行に対応するリストを返すことができます。

```python
spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".

Please do not drink it.
Sincerely,
Bob'''

print(spam.split('\n'))

# 結果
['Dear Alice,', 'How have you been? I am fine.', 'There is a container in the fridge', 'that is labeled "Milk Experiment".', '', 'Please do not drink it.', 'Sincerely,', 'Bob']
```


## rjust(), ljust(), center()

- rjust() : 文字列にスペース(または任意の文字)を挿入して、引数で指定した文字数となるようにテキストを整形する(右寄せ)。
- ljust() : 文字列にスペース(または任意の文字)を挿入して、引数で指定した文字数となるようにテキストを整形する(左寄せ)
- center() : 文字列にスペース(または任意の文字)を挿入して、引数で指定した文字数となるようにテキストを整形する(中央揃え)

```python
# 文字長が「10文字」になるようにスペースを挿入
>>> 'Hello'.rjust(10) # 右寄せ
'     Hello'
>>> 'Hello'.ljust(10) # 左寄せ
'Hello     '

# 文字長が「20文字」になるようにスペースを挿入
>>> 'Hello'.rjust(20)
'               Hello'
>>> 'Hello World'.rjust(20)
'         Hello World'

# スペーサーを指定する場合は、第2引数で指定する
>>> 'Hello'.rjust(20, '*')
'***************Hello'
>>> 'Hello'.ljust(20, '-')
'Hello---------------'

# 中央寄せ
>>> 'Hello'.center(20)
'       Hello        '
>>> 'Hello'.center(20, '=')
'=======Hello========'
```

これらの方法は、適切な間隔を持つ表形式のデータを印刷する必要がある場合に特に便利です。  
文字列の長さが何文字であるかわからなくても、文字列がきちんと整列されるようにすることができます。  

```python
# picnicTable.py
def print_picnic(items_dict, left_width, right_width):
    print('PICNIC ITEMS'.center(left_width + right_width, '-'))
    for k, v in items_dict.items():
        print(k.ljust(left_width, '.') + str(v).rjust(right_width))

picnic_items = {'sandwitches': 4, 'apples': 12, 'cookies': 8000}
print_picnic(picnic_items, 12, 5)  #第2, 第3引数として、左右の列をどれだけ広げたいかを指定する
print_picnic(picnic_items, 20, 6)

# 結果
---PICNIC ITEMS--
sandwitches.    4
apples......   12
cookies..... 8000
-------PICNIC ITEMS-------
sandwitches.........     4
apples..............    12
cookies.............  8000
```

## strip(), rstrip(), lstrip()

下記のメソッドは、文字列に含まれる空白(または任意の文字)を取り除く場合に使います。  

- strip() : 先頭または末尾に空白(または任意の文字)を含まない新しい文字列を返す
- rstrip() : 右端から空白(または任意の文字)を削除
- lstrip() : 左端から空白(または任意の文字)を削除

```python
>>> spam = '     Hello World     '

>>> spam.strip()
'Hello World'

>>> spam.lstrip()
'Hello World     '

>>> spam.rstrip()
'     Hello World'
```

```python
# 両端から任意の文字を取り除く場合
>>> spam = 'SpamSpamBaconSpamEggsSpamSpam'

# 「文字」として認識されるっぽい(文字列じゃなく順番関係ないみたい)。'ampS' でも 'mapS'でも 'Spam' でも結果は同じ
>>> spam.strip('ampS')
'BaconSpamEggs'
>>> spam.strip('Spam')
'BaconSpamEggs'
```

## pyperclipモジュールによる文字列のコピーと貼り付け

pyperclipモジュールには、コンピュータのクリップボードとの間でテキストを送受信できるcopy()関数とpaste()関数があります。  
プログラムの出力をクリップボードに送信すると、その他のソフトウェアに簡単に貼り付けることができます。  

### pyperclipモジュールのインストール

```python
# インストール
[root]# pip3 install pyperclip
Collecting pyperclip
  Downloading pyperclip-1.5.27.zip
Installing collected packages: pyperclip
  Running setup.py install for pyperclip ... done
Successfully installed pyperclip-1.5.27

# 確認
[root]# pip list --format=columns
Package    Version
---------- -------
pip        9.0.1
pyperclip  1.5.27
setuptools 28.8.0
```

Linux(CUI)で実施した場合エラーになっちゃった。 -> `Pyperclip could not find a copy/paste mechanism for your system.`
```python
>>> import pyperclip
>>> pyperclip.copy('Hello world!')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/root/.pyenv/versions/3.6.1/lib/python3.6/site-packages/pyperclip/clipboards.py", line 125, in __call__
    raise PyperclipException(EXCEPT_MSG)
pyperclip.exceptions.PyperclipException:
    Pyperclip could not find a copy/paste mechanism for your system.
    For more information, please visit https://pyperclip.readthedocs.org
```

WindowsのPythonで試した結果。  
クリップボードの中身を操れてちょっと感動。
```python
>>> import pyperclip
>>> pyperclip.copy('Hello world!')
>>> pyperclip.paste()
'Hello world!'
>>> pyperclip.paste()
'ああああああああ'
>>> pyperclip.copy('nonoonno')
>>> pyperclip.paste()
'nonoonno'
```


# Project: Password Locker

あなたはおそらく多くの異なるウェブサイトにアカウントを持っています。  
これらのサイトのいずれかにセキュリティ違反があると、ハッカーは他のすべてのアカウントのパスワードを知るため、それぞれに同じパスワードを使用することは悪い習慣です。  
1つのマスターパスワードを使用してパスワードマネージャのロックを解除するコンピュータ上のパスワードマネージャソフトウェアを使用することをお勧めします。  
その後、アカウントのパスワードをクリップボードにコピーし、Webサイトのパスワードフィールドに貼り付けることができます。  

この例で作成するパスワードマネージャプログラムは安全ではありませんが、そのようなプログラムの仕組みの基本的なデモンストレーションを提供しています。  

### Step 1: Program Design and Data Structures

アカウントの名前であるコマンドライン引数（電子メールやブログなど）でこのプログラムを実行できるようにします。  
そのアカウントのパスワードはクリップボードにコピーされ、ユーザーはこれをパスワードフィールドに貼り付けることができます。  
このようにして、ユーザーは長く複雑なパスワードを覚えることなくそのパスワードを保持することができます。  

まず書くこと

- シバン
- プログラムを簡単に説明するコメント
- アカウントとパスワードで構成された辞書データ

### Step 2: Handle Command Line Arguments

- コマンドライン引数を変数 sys.argv に格納
- sys.argv リストの最初の項目は、常にプログラムのファイル名('pw.py')を含む文字列でなければなりません。
- また、2番目の項目は、 最初のコマンドラインの引数になります。
  このプログラムでは、この引数はパスワードが必要なアカウントの名前です。
  コマンドライン引数は必須。
- 追加するのを忘れた場合（つまり、sys.argvリストに値が2つ未満の場合）、ユーザーに使用方法メッセージを表示します

### Step 3: Copy the Right Password

- 変数アカウントに文字列として格納されたアカウント名が、PASSWORDS辞書データ内に存在するかどうか確認する。  
  - pyperclipモジュールのインポート
  - pyperclip.copy() を使用してキーの値をクリップボードにコピーす
- account変数の用意
  - sys.argv[1] を使用することでこのプログラムでどこでもアカウントを使用することができるが、変数に入れることでプログラムの可読性が良くなる

コマンドラインプログラムを簡単に起動するための付録Bの手順を使用すると、アカウントパスワードをクリップボードにすばやくコピーできます。  
新しいパスワードでプログラムを更新する場合はいつでも、ソースのPASSWORDS辞書の値を変更する必要があります。  
もちろん、誰でも簡単にコピーできる場所にすべてのパスワードを保存したくないと思うかもしれませんが練習なので（；^ω^）

このプログラムを修正して、通常のテキストをクリップボードにすばやくコピーするプログラムを作成できます。  
同じ株式段落の多くが共通する複数のメールを送信しているとします。  
各段落をPASSWORDSディクショナリの値として置くこともできます（この時点で辞書の名前を変更したいと思うでしょう）。  
そして、多くの標準テキストを素早く選択してクリップボードにコピーする方法があります。

Windowsでは、WIN-R Runウィンドウでこのプログラムを実行するバッチファイルを作成できます。 （バッチファイルの詳細については、付録Bを参照してください。）  
ファイルエディタに次のように入力し、ファイルをpw.batとしてC：¥Windowsフォルダに保存します。
```
@py.exe C:\Python34\pw.py %*
@pause
```
このバッチファイルを作成すると、Windows上でパスワード保護されたプログラムを実行することは、WIN-Rを押してpw <account name>と入力するだけです。


# Project: Adding Bullets to Wiki Markup

Wikipediaの記事を編集するとき、箇条書きリストを作成するには、各リスト項目は下記のように表記します。  
```
* 項目1
* 項目2
* 項目3
```  
しかし、非常に大きなリストの場合手動で `*` を先頭に置いていくのは大変です。
短いPythonスクリプトでこの作業を自動化することもできます。  

bulletPointAdder.pyスクリプトは、クリップボードからテキストを取得し、各行の先頭に星とスペースを追加し、この新しいテキストをクリップボードに貼り付けます。  
たとえば下記のようなリストの場合。  
```
Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars
```

プログラムを実行すると、クリップボードには次の内容が入ることになります。
```
* Lists of animals
* Lists of aquarium life
* Lists of biologists by author abbreviation
* Lists of cultivars
```

### Step 1: Copy and Paste from the Clipboard

bulletPointAdder.py の処理

1. クリップボードからテキストを貼り付ける
  - pyperclip.paste() を使う
1. 何らかの変換をする
1. 新しいテキストをクリップボードにコピーする
  - pyperclip.copy() を使う

### Step 2: Separate the Lines of Text and Add the Star

pyperclip.paste()を呼び出すと、クリップボード上のすべてのテキストが大きな文字列として返されます。
"List of Lists"の例を使用すると、テキストに格納された文字列は次のようになります。

```
'Lists of animals\nLists of aquarium life\nLists of biologists by author
abbreviation\nLists of cultivars'
```

この文字列の `\n` 改行文字は、クリップボードから印刷または貼り付けられたときに複数行で表示されます。
この1文字列の値には多くの「行」があります。これらの行の先頭にスターを追加したいとします。  

「文字列の `\n` 改行文字をそれぞれ検索し、その直後に星を追加するコードを書く」
・・・でも良いんですが、  
**「split()メソッドを使用して元の文字列の各行に1つの文字列のリストを返し、リスト内の各文字列の先頭に星を追加する」**   
・・・のほうが簡単です。

- テキストを改行に沿って分割し、各項目がテキストの1行であるリストを取得する
- リストを lines変数に格納し、行数分ループする
- 各行について、行の先頭に * とスペースを追加する
- 行の各文字列は * から始まる

### Step 3: Join the Modified Lines

行リストに、* で始まる変更された行が追加されました。
しかし、pyperclip.copy() に入るものは、文字列値のリストではなく、単一の文字列値を期待しています。  
この単一文字列値を作成するには、行をjoin()メソッドに渡して、リストの文字列から結合された単一の文字列を取得します。

このプログラムを参考にして
- 行末から末尾の空白を削除
- テキストを大文字または小文字に変換
など、他の種類のテキスト操作を自動化したい場合に応用できます。


# まとめ

テキストは一般的なデータ形式であり、Pythonには文字列値に格納されたテキストを処理するための多くの有用な文字列メソッドが付属しています。  
ほとんどのPythonプログラムでは、索引付け、スライシング、および文字列メソッドを使用します。  

今作成しているプログラムは、あまり洗練されていないように見えます。  
画像やカラフルなテキストのグラフィカルユーザーインターフェイスはありません。   
これまでは、print()でテキストを表示していて、ユーザがinput()でテキストを入力できるようにしています。  
しかしながら、ユーザは、クリップボードを通して大量のテキストを素早く入力することができる。
この能力は、膨大な量のテキストを操作するプログラムを作成するための便利な方法を提供します。   
これらのテキストベースのプログラムでは、派手なウィンドウやグラフィックスがないかもしれませんが、すばやく多くの有益な作業を行うことができます。  

大量のテキストを操作する別の方法は、ハードドライブからファイルを直接読み書きすることです。  
次の章でPythonでこれを行う方法を学びます。

Pythonプログラミングのすべての基本的な概念をカバーしています。  
この本の残りの部分では、引き続き新しい概念を学びますが、タスクを自動化できる便利なプログラムを書くのに十分な知識があります。  
Webページをダウンロードしたり、スプレッドシートを更新したり、テキストメッセージを送るなど、Pythonの知識が十分にあるとは思えないかもしれませんが、Pythonモジュールがそこに入ります！  
他のプログラマーによって書かれたこれらのモジュールは、これらすべてのことを簡単に行うための機能を提供します。  
そこで、役に立つ自動化されたタスクを行うための実際のプログラムを書く方法を学びましょう。  


# Practice Questions

1. What are escape characters?
バックスラッシュ(\)

2. What do the \n and \t escape characters represent?
- \n : 改行
- \t : タブ

3. How can you put a \ backslash character in a string?
こんなかんじで、エスケープしたい文字の直前に置く。
```
spam = 'Say hi to Bob\'s mother'
```

4. The string value "Howl's Moving Castle" is a valid string. Why isn’t it a problem that the single quote character in the word Howl's isn’t escaped?  
ダブルクオートで囲っている。かつ、中に含むシングルクオートが1個だけ。なので、エスケープは不要。

5. If you don’t want to put \n in your string, how can you write a string with newlines in it?
三重引用符(`"""` もしくは `'''`) でかく。

6. What do the following expressions evaluate to?
```
1. 'Hello world!'[1]
2. 'Hello world!'[0:5]
3. 'Hello world!'[:5]
4. 'Hello world!'[3:]
```
1.`e`   /   2.`Hello`   /   3.`Hello`  /   4.`lo world!`

7. What do the following expressions evaluate to?
```
1. 'Hello'.upper()
2. 'Hello'.upper().isupper()
3. 'Hello'.upper().lower()
```
1.`HELLO`  /  2.`True`  /  3.`hello`

8. What do the following expressions evaluate to?
```
1. 'Remember, remember, the fifth of November.'.split()
2. '-'.join('There can be only one.'.split())
```
1.`['Remember,', 'remember,', 'the', 'fifth', 'of', 'November.']`  
2.`'There-can-be-only-one.'`

9. What string methods can you use to right-justify, left-justify, and center a string?  
rjust(), ljust(), center()

10. How can you trim whitespace characters from the beginning or end of a string?  
strip(), rstrip(), lstrip()


# Practice Project

## Table Printer

print_table() という名前の関数を記述します。  
この関数は、文字列のリストを取得し、適切に整理された表に各列を右詰めで表示します。  
すべての内部リストに同じ数の文字列が含まれるとします。  

```python
# 例
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
```

下記の出力が得られる print_table()関数を記述してください。  
・3行*4列 の表形式で出力  
・各リストで最も長い文字列に合わせて右端揃え
```
  apples Alice  dogs
 oranges   Bob  cats
cherries Carol moose
  banana David goose
```

ヒント：  
コードでは、内部の各リストで最も長い文字列を最初に見つけて、列全体がすべての文字列に収まるようにする必要があります。  
各列の最大幅を整数のリストとして格納できます。
print_table()関数は、col_widths = [0] * len(tableData) で始めます。  
これは、table_dataの内部リストの数と同じ数の0値を含むリストを作成します。
こうすることで、col_widths[0] は table_data[0] に最長文字列の幅を格納し、col_widths[1] は table_data[1] に最長文字列の幅を格納することができます。
col_widthsリストの中で最大の値を見つけて、rjust()文字列メソッドに渡す整数幅を調べます。
