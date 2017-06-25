Chapter 4 – Lists  
https://automatetheboringstuff.com/chapter4/

# リスト
ここでは、リストとタプルについて学びます。  
リストとタプルには複数の値を入れることができるので、大量のデータを扱うプログラムの作成が容易になります。  
リスト自体に他のリストを含めることができるので、データを階層構造に配置することができます。  


## リストデータ型
下記のようなデータを「リスト」と呼びます。`['cat', 'bat', 'rat', 'elephant']` このひとかたまりが、リストです。    
リスト内の各値は「アイテム」と呼ばれます。`'cat'` `'bat'` `'rat'` `'elephant'` のそれぞれが、アイテムです。  
リスト内に文字列を入れる場合は `''` でくくります。  

```python
# リストの例
>>> [1, 2, 3]
[1, 2, 3]

>>> ['cat', 'bat', 'rat', 'elephant']
['cat', 'bat', 'rat', 'elephant']

>>> ['hello', 3.1415, True, None, 42]
['hello', 3.1415, True, None, 42]

>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam
['cat', 'bat', 'rat', 'elephant']
```

## リスト内のアイテムの取得方法いろいろ

### インデックス
リスト内の各アイテムの値は、**インデックス** を使用して取得します。  
1番目のアイテムは `[0]` インデックスで取得することに注意してください。  
インデックスに使用できるのは整数値だけです。整数値以外を指定するとエラーになります。
```python
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam
['cat', 'bat', 'rat', 'elephant']   # spam変数に格納されたリストデータの値
>>>
>>> spam[0]
'cat'
>>> spam[1]
'bat'
>>> spam[2]
'rat'
>>> spam[3]
'elephant'

# インデックスを超える範囲を指定するとエラーになる
>>> spam[4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range

# インデックスに整数値以外を指定するとエラーになる
>>> spam[1.0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list indices must be integers or slices, not float
```

リストには、下記のように他のリスト値を含めることができます。  
これらのリストのアイテムには、複数のインデックスを使用してアクセスします。  
1つのインデックスのみを使用する場合、プログラムはそのインデックスのリストに設定されているすべての値を出力します。
```python
>>> spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
>>> spam
[['cat', 'bat'], [10, 20, 30, 40, 50]]
>>> spam[0]
['cat', 'bat']
>>> spam[1]
[10, 20, 30, 40, 50]
>>> spam[0][1]
'bat'
>>> spam[1][1]
20
```

### ネガティブインデックス
インデックスに負の整数(**ネガティブインデックス**)を使用することもできます。  
`[-1]` はリスト内の最後のインデックスを参照し、`[-n]` はリスト内の最後からn番目のインデックスを参照します。  
```python
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam[-1]
'elephant'
>>> spam[-3]
'bat'
```

### スライス
2つの整数をコロンで区切り、リスト内の「n番目～m番目」の値を取得することができます(**スライス**) 。  
スライスは、より短く書くこともできます。  
- `[0:n]` = `[:]`
- `[0:2]` = `[:2]`
- `[1:n]` = `[1:]`

```python
>>> spam = ['cat', 'bat', 'rat', 'elephant']

# スライスで値を取得する
>>> spam[0:0]
[]
>>> spam[0:1]
['cat']
>>> spam[0:2]
['cat', 'bat']
>>> spam[0:3]
['cat', 'bat', 'rat']
>>> spam[0:4]
['cat', 'bat', 'rat', 'elephant']
>>> spam[0:5]  # アイテム数以上の値を指定してもエラーにならない。
['cat', 'bat', 'rat', 'elephant']

# 同じ
>>> spam[0:4]
['cat', 'bat', 'rat', 'elephant']
>>> spam[:]
['cat', 'bat', 'rat', 'elephant']

# 同じ
>>> spam[0:2]
['cat', 'bat']
>>> spam[:2]
['cat', 'bat']

# 同じ
>>> spam[1:4]
['bat', 'rat', 'elephant']
>>> spam[1:]
['bat', 'rat', 'elephant']
```

## リストのアイテム数を `len()関数` で取得する
`len()関数` を使用して、リストのアイテム数を取得します。
```python
>>> spam = ['cat', 'dog', 'moose']
>>> len(spam)
3
```

## リスト内の値の更新
リストのインデックスを使用して、そのインデックス内の値を変更します。  

```python
>>> spam = ['cat', 'bat', 'rat', 'elephant']

>>> spam[1] = 'apple'
>>> spam
['cat', 'apple', 'rat', 'elephant']

>>> spam[2] = spam[1]
>>> spam
['cat', 'apple', 'apple', 'elephant']

>>> spam[-1] = 12345
>>> spam
['cat', 'apple', 'apple', 12345]
```

## リスト連結とリスト複製
`+` を使うと、2つのリストを組み合わせて新しいリストを作ることができます。  
`[リスト] * n(整数)` とすると、リストの中身を複製します。  

```python
# リスト連結
>>> [1, 2, 3] + ['A', 'B', 'C']
[1, 2, 3, 'A', 'B', 'C']

# リスト複製
>>> ['X', 'Y', 'Z'] * 3
['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']

# 変数に入れたリストも連結できる
>>> spam = [1, 2, 3]
>>> spam = spam + ['A', 'B', 'C']
>>> spam
[1, 2, 3, 'A', 'B', 'C']
```

## リストから値を削除する
`del` を使用してリスト内の値を削除します。削除する値は、リストのインデックスを使用して指定します。  

```python
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam
['cat', 'bat', 'rat', 'elephant']

>>> del spam[2]
>>> spam
['cat', 'bat', 'elephant']

>>> del spam[2]
>>> spam
['cat', 'bat']

# 存在しないインデックスはエラーになる
>>> del spam[2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list assignment index out of range

# 変数spamを削除してから実施すると、「NameError」になる
>>> del spam
>>> del spam[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
>>>
```

## リストを使うとうれしいこと
例えば、下記のように catName1～catName6 という6個の変数を使って「猫の名前」を登録しようとしているとします。  
これだと、猫が6匹以上になったときにスクリプトを修正する必要がでてしまいます。
```python
# allMyCats1.py 抜粋
print('Enter the name of cat 1:')
catName1 = input()
print('Enter the name of cat 2:')
catName2 = input()
print('Enter the name of cat 3:')
catName3 = input()
print('Enter the name of cat 4:')
catName4 = input()
print('Enter the name of cat 5:')
catName5 = input()
print('Enter the name of cat 6:')
catName6 = input()
```

下記のように、リストを使って登録するようにすれば、猫の数が変動した場合でもスクリプトを修正する必要がありません。  
それぞれの変数に入力していた上記の場合よりも柔軟性をもたせることができます。
```python
# allMyCats2.py 抜粋
catNames = []
while True:
    # n番目の猫の名前を入力。何も入力せずにエンターを押せば入力を終える。
    print('Enter the name of cat ' +
           str(len(catNames) + 1) +
          ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # list concatenation
```

## for文でリストを使う

以前、こんなかんじでfor文を書きました。
```python
for i in range(4): # i が4になるまで(0～3の間)繰り返し
    print(i)

# 結果
0
1
2
3
```

リストを使うとこんなかんじで書けます。
```python
for i in [0, 1, 2, 10]:
    print(i)

# 結果
0
1
2
10
```

さらに、for文の条件に `range(len(supplies))` を使うと、リストのアイテム数をそのまま設定できます。  
もしリストのアイテム数が変更されても、スクリプトを修正しなくて済みます。

```python
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('index ' + str(i) + ' in supplies is: ' + supplies[i])

# 結果
index 0 in supplies is: pens
index 1 in supplies is: staplers
index 2 in supplies is: flame-throwers
index 3 in supplies is: binders
```

## `in` と `not in` 演算子

`in` と `not in` 演算子を使用して、リスト内に値があるかどうかを判断できます。  
`in` と `not in` はブール値で評価されます。

```python
>>> 'howdy' in ['hello', 'hi', 'howdy', 'heyas']
True

>>> spam = ['hello', 'hi', 'howdy', 'heyas']
>>> 'cat' in spam
False
>>> 'howdy' not in spam
False
>>> 'cat' not in spam
True
```

たとえば、以下のようなプログラムで使用します。  
- ペットの名前を入力させる
- ペットのリスト内に、入力した名前があった場合は「わたしのペットです」と表示
- ペットのリスト内に、入力した名前がなかった場合は「わたしのペットじゃありません」と表示

```python
# myPets.py 抜粋
if name not in myPets:
  print('I do not have a pet named ' + name)
else:
  print(name + 'is my pet.')
```


## 多重代入
**多重代入** を使うと、下記のような内容を簡単に書けます。  
値の数と、リストの長さは同じである必要があります。同じじゃない場合はエラーになります。

```python
# 多重代入を使わない書き方
>> cat = ['fat', 'orange', 'loud']
>>> size = cat[0]
>>> color = cat[1]
>>> disposition = cat[2]

# 多重代入を使った書き方
>>> cat = ['fat', 'orange', 'loud']
>>> size, color, disposition = cat

# どちらも結果は同じ
>>> size
'fat'
>>> color
'orange'
>>> disposition
'loud'
>>>
```

2つの値を入れ替えるときにも、多重代入が使われます。
```python
>>> a,b = 'Alice','Bob'
>>> a,b = b,a
>>> print(a)
Bob
>>> print(b)
Alice
```

## 累算代入演算子

累算代入演算子というとスゲー難しい感じがする・・・。  
要は「変数spamには、元々42という値が入っていました。これにプラス1して、43にしたい。」というやつです。  

```python
# 累算代入演算を使わないで +1 する書き方
>>> spam = 42
>>> spam = spam + 1
>>> spam
43

# 累算代入演算を使って +1 する書き方
>>> spam = 42
>>> spam += 1
>>> spam
43
>>>
```

累算代入演算は、`+`, `-`, `*`, `/`, `%` でおこなうことができます。  
それぞれどんな意味になるかを、下記に記載します。
```python
spam += 1  # spam = spam + 1
spam -= 1  # spam = spam - 1
spam *= 1  # spam = spam * 1
spam /= 1  # spam = spam / 1
spam %= 1  # spam = spam % 1
```

ちなみに `+=` は文字列とリストの連結にも使えます。  
それから `*=` は文字列とリストの複製にも使えます。
```python
>>> spam = 'Hello'
>>> spam += ' world!'
>>> spam
'Hello world!'

>>> spam = ['hoge']
>>> spam += ['fuga']
>>> spam
['hoge', 'fuga']

>>> bacon = 'Hello'
>>> bacon *= 3
>>> bacon
'HelloHelloHello'

>>> bacon = ['Zophie']
>>> bacon *= 3
>>> bacon
['Zophie', 'Zophie', 'Zophie']
>>>
```

# メソッド

メソッドとは、関数みたいなものです。値とメソッドを `.` でつないで使います。  
たとえば下記のようなメソッドがあります。

### index() メソッド
- リスト内に値が存在していたら、その値のインデックス値を取得する
- 値が存在していなかったらエラーになる
- 値が重複していたら、最初の値のインデックスを返す

```python
>>> spam = ['hello', 'hi', 'howdy', 'heyas']
>>> spam.index('hello')
0
>>> spam.index('heyas')
3

# 値が存在していなかったらエラーになる
>>> spam.index('howdyhowdyhowdy')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 'howdyhowdyhowdy' is not in list
>>>

# 値が重複していたら、最初の値のインデックスを返す
>>> spam = ['namake', 'tamao', 'masubuchi', 'tamao']
>>> spam.index('tamao')
1
```

### append() メソッド
リストの最後に値を追加します。

```python
>>> spam = ['cat', 'dog', 'bad']
>>> spam.append('moose')
>>> spam
['cat', 'dog', 'bad', 'moose']
>>>
```

### insert() メソッド
insert() メソッドは、リスト内の任意の位置に値を追加します。  
最初の引数でインデックスを指定し、2番めの引数でそこに入れる値を指定します。  
こんなかんじになります。

```python
>>> spam = ['cat', 'dog', 'bat']
>>> spam.insert(1, 'chiken')
>>> spam
['cat', 'chiken', 'dog', 'bat']
```

### [Note] append() と insert() メソッド について

append() と insert() メソッドは、list()メソッドもしくはただのリストから使います。  
文字列や整数値が入るふつうの変数では使えません。

**下記は同じ意味にはならないので注意してください。**
- `spam.append('moose')` は `spam = spam.append('moose')` と同じではない
- `spam.insert(1, 'chiken')` は `spam = spam.insert(1, 'chiken')` と同じではない

```python
# ふつうの変数に対して append() と insert() を使うとエラーになる
>>> eggs = 'hello'
>>> eggs.append('world')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'append'

>>> bacon = 42
>>> bacon.insert(1, 'world')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'int' object has no attribute 'insert'
>>>
```

## remove() メソッド
remove() は、リスト内の値を削除します。  
存在しない値を消そうとすると、エラーになります。  
値が重複している場合は、最初のインデックスの値だけが削除されます。

```python
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam.remove('bat')
>>> spam
['cat', 'rat', 'elephant']

# 存在しない 'chicken' を消そうとしているため、エラーになる
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam.remove('chicken')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list

# 'cat' が重複している。最初の 'cat' だけが削除される
>>> spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
>>> spam.remove('cat')
>>> spam
['bat', 'rat', 'cat', 'hat', 'cat']
```

### del VS remove() メソッド
`del` は、**削除するインデックスの値** がわかっている場合に使うと良いです。  
`remove() メソッド` は **削除する値** がわかっている場合に使うと良いです。


## sort() メソッド
数値や文字列のリストは `sort()` メソッドでソートすることができます。  
`reverse` 変数に `True` を与えると、降順にソートすることができます。  

```python
>>> spam = [2, 5, 3.14, 1, -7]
>>> spam.sort()
>>> spam
[-7, 1, 2, 3.14, 5]

>>> spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
>>> spam.sort()
>>> spam
['ants', 'badgers', 'cats', 'dogs', 'elephants']

# 降順にソート
>>> spam.sort(reverse=True)
>>> spam
['elephants', 'dogs', 'cats', 'badgers', 'ants']
```

`sort()` メソッドを使う時の3つの注意点があります。  
1. `sort()`メソッドはリストのみで使える。
1. 数値と文字列が混ざったリストでは使えない。
1. ソートメソッドはデフォルトで「ASCIIbetical order」を使用する。  
   そのため、大文字の方が小文字よりも先にソートされる(`a` は `Z` の次)。  

   「regular alphabetical order」を使用したい場合は、`key` 変数に `str.lower` を設定する。  
   `str.lower` を使用すると、実際の値ではなく、すべて小文字としてソートする。

```python
# 数値と文字列が混在するリストをソートしようとすると、エラーになる
>>> spam = [1, 3, 2, 4, 'Alice', 'Bob']
>>> spam.sort()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'str' and 'int'


# 大文字が先にソートされる
>>> spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
>>> spam.sort()
>>> spam
['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats']

# すべて小文字としてソートする(Alice -> alice、 Bob ー> bob、 Carol -> carol)
>>> spam.sort(key=str.lower)
>>> spam
['Alice', 'ants', 'badgers', 'Bob', 'Carol', 'cats']
```

# コードを読みやすくするためのTips

## インデントとコードブロック

Pythonは、インデントでコードブロックをあらわしますが、いくつかの例外があります。  
たとえば、リストはソースコード内の複数行にわたることがあります。  
Pythonは、`]` を見つけるまでリストは終わっていないと判断します。  
長いリストなど、適宜インデントしてコードがきれいに見えるように整形するといいです。  

また、1行で書くとちょっと長くて可読性が悪くなるようなコードは、`\` を使って複数行に分割することができます。  
`\` は「この命令は次の行に続きがありますよ」ということをあらわします。  
`\` につづくインデントは特に意味を持たないので、コードの見栄えを良くするために適宜インデントしてください。

```
print('Four score and seven' + \
      'years ago ...')

# 結果
Four score and sevenyears ago ...
```

## random() 関数

「0 〜 リストのインデックス数-1」の範囲でランダムな数を生成したいとき、以下のように書くことができます。  
リストの値が増減しても、コードを変更することなく、「0 〜 リストのインデックス数-1」の範囲でランダムな数を生成できるところがミソです。  
あとでコードを修正するとき、修正すべき箇所が少ないとバグ混入の可能性も少なくなります。

```python
# magic8Ball.py抜粋
random.randint(0, len(messages) - 1)
```

# 文字列とタプル

文字列もほぼ「リスト」と見なすことができます。  
リストと同じように、インデックスやスライスを使った表現、ループでの使用、`in` や `not in` の判定ができます。  

```python
>>> name = "Zophie"

>>> name[0]
'Z'
>>> name[-2]
'i'
>>> name[0:4]
'Zoph'

>>> 'Zo' in name
True
>>> 'z' in name
False
>>> 'p' not in name
False

>>> for i in name: \
... print('***' + i + '***')
...
***Z***
***o***
***p***
***h***
***i***
***e***
>>>
>>>
```

## ミュータブル(可変)データとイミュータブル(不可変)データ

文字列とリストは似ているけれど、ある重要な点が異なります。  
リストは、値の追加・変更・削除がおこなえます。  
でも、文字列は内容を変更することはできません。やってみると、エラーになります。  

文字列の内容を変更するには、古い文字列の内容をスライスで切り出して、変更したい部分をくっつけて、それを新しい変数に入れるようなかたちで実現します。  
こうすることで、古い文字列に手を加えずに、新しい文字列を作ることができます。  

ミュータブルタイプとイミュータブルタイプは無意味な区別のように見えるかもしれませんが、ミュータブルタイプとイミュータブルタイプを持つ関数を呼び出すときに、タイプによって異なる動作をします。

```python
# 代入で変更しようとするとエラーになる
>>> name = 'Zophie a cat'
>>> name[7]
'a'
>>> name[7] = 'the'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment

# 新しい変数に、新たに組み立てた文字列を値として入れる
>>> name = 'Zophie a cat'
>>> newName = name[0:7] + 'the' + name[8:12]
>>> name
'Zophie a cat'
>>> newName
'Zophie the cat'
```

リストの値は変更可能なのですが、下記の場合は「変更」じゃなくて「上書き」になります。  
`eggs` を外箱、`[]` を内箱とすると、`[1,2,3]` の内箱をとりだして、新しく `[4,5,6]` の内箱に入れ替えるイメージです。  
変更は、2番めのように `[1,2,3]` のうちばこから `1,2,3` を消して `4,5,6` の値だけを元々の `[]` に入れる場合のことをいいます。

```python
# 上書き
>>> eggs = [1,2,3]
>>> eggs = [4,5,6] # [1,2,3] を取り出し [4,5,6]を入れる
>>> eggs
[4, 5, 6]

# 変更
>>> eggs = [1,2,3]
>>> del eggs[2]    # [1,3]
>>> del eggs[1]    # [3]
>>> del eggs[0]    # []
>>> eggs.append(4) # [4]
>>> eggs.append(5) # [4,5]
>>> eggs.append(6) # [4,5,6]
>>> eggs
[4, 5, 6]
```

## タプル

タプルはリストにすごく似ています。2つの点をのぞいて。  
1つめ。タプルは `[]` ではなく、 `()` を使います。  
2つめ。タプルはイミュータブル(不可変)データです。

```python
# タプルは()であらわす。リストのようにインデックスやスライスなどが使える
>>> eggs = ('hello', 42, 0.5)
>>> eggs[0]
'hello'
>>> eggs[1:3]
(42, 0.5)
>>> len(eggs)
3

# 内容を変えることはできない
>>> eggs = ('hello', 42, 0.5)
>>> eggs[1] = 99
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

1つの値しかないけど、タプル型にしたいときは、カンマを使います。  
Pythonは、最後のアイテムの後にカンマがあるか無いかで、リストとタプルを判別しています。  
**type関数** を使うと、データ型を判別できます。  


```python
# カンマがないと、文字列
>>> type(('hello'))
<class 'str'>

# カンマがあると、タプル
>>> type(('hello',))
<class 'tuple'>
```


### リストのかわりにタプルを使う場面は？

- コード内でタプルが使われていれば、「この値は変更することを意図していないんだな」ということが暗黙で伝わる
- タプルを使うと、リスト使用時とくらべてほんの少し実行が早くなる

### list()関数と tuple()関数 で「リスト⇔タプル」変換する

タプルからリスト(リストからタプル)に簡単に変換できます。  

```python
>>> tuple(['cat','dag',5])
('cat', 'dag', 5)
>>> list(('cat','dag',5))
['cat', 'dag', 5]
>>> list('hello')
['h', 'e', 'l', 'l', 'o']
```


# 参照(リファレンス)

cheeseはspamを複製して作った変数です。  
複製後、spamの値を変更しても、cheeseの値には影響しません。  
spam と cheese は別々の変数だからです。  

```python
>>> spam = 42       # spamという変数に 42 を設定
>>> cheese = spam   # spamを複製して、cheeseを作成
>>> spam = 100      # spamに 100 を設定
>>> spam
100
>>> cheese  # spamへの変更は、cheeseには影響しない。
42
```

しかし、リストの場合は上記のような動作にはなりません。  
あなたが変数にリストにを設定するとき、実際に変数に割り当てられるのは **リスト参照** です。  
参照は、あるビットのデータを指し示す値であり、リスト参照はリストを指す値です。  

下記のコードを見るとこの内容が分かりやすいかも。  
spamというリストを作ったとき、実際の値は **spam変数のリスト参照** に設定されます。  
cheese に spam をコピーしましたが、この時コピーされたのは変数(外箱)だけで、リスト参照先はspamと同じところを向いています。  
なので、cheeseリストの内容を変更すると、spamリストも同じところを参照しているので、こちらの内容も変更されるのです。  

```python
# cheseしか変更していないのに、spamの内容まで変更されている件
>>> spam = [0,1,2,3,4,5]  # spamというリストを作成。値はリストリファレンスに設定される
>>> cheese = spam         # cheese に spam をコピー。でも、リストリファレンスはspamと同じ場所を指したまま
>>> cheese[1] = 'Hello!'  # cheseの内容を変更
>>> spam                  # cheseしか変更していないのに、spamの内容まで変更されている！
[0, 'Hello!', 2, 3, 4, 5]
>>> cheese
[0, 'Hello!', 2, 3, 4, 5]
```

変数は箱のようなもので、その中身が値だということを覚えておきましょう。  
リスト型の場合、変数には、リストの値自体ではなく、リスト値への参照がはいります。  
整数型や文字列型の場合は、箱の中身は単に整数や文字列です。  

Pythonは、変数の型が可変な場合はいつも **参照** を使用します。  
変数の型が不変な場合は、値そのものが入ります。  

- ミュータブル型(可変)
  - リスト / 辞書

- イミュータブル型(不可変)
  - 文字列 / 整数 / タプル

## 参照渡し

参照は、引数が関数にどのように渡されるかを理解するために特に重要です。  
関数が呼び出されると、引数の値が変数のパラメータにコピーされます。  
リストや辞書では、参照のコピーがパラメータに使用されます。  

下記のコードを見てください。  
eggs()関数が呼び出されると、リストをその場で直接編集しています。  
(返り値はspamに新しい値を代入してはいません。)

ですが、spam と someParameter の参照先は別個であるにもかかわらずどちらも同じリストを参照しています。  
これが、関数内のappend('Hello')メソッドが、関数呼び出しが返った後でもリストに影響している理由です。  

**この動作を覚えておいてください。**  
Pythonがリストと辞書の変数を操作するときは、こういう動作をするということを忘れると、混乱するバグにつながります。  

```python
# passingReference.py
def eggs(someParameter):
  someParameter.append('Hello')

spam = [1,2,3]
eggs(spam)
print(spam)

# 結果
[1, 2, 3, 'Hello']
```

## copyモジュール (copy(), deepcopy())

参照渡しは、リストと辞書をあつかう際にしばしば使われる手っ取り早い方法ですが、
関数が渡されるリストや辞書を変更すると、オリジナルのリストや辞書の値を変更してしまうので、変更したくないときがあるかもしれません。    

このため、Pythonは copyモジュールを提供します。  
copyモジュールは、`copy()` と `deepcopy()` 関数を提供します。  

`copy.copy()` は、辞書やリストのような変更可能な値を複製コピーします。ただの参照先のコピーではありません。  
下記のコードを見てください。  
spam と cheese が別々のリストを参照していることがわかります。  
もはや、これらの変数のリファレンスIDナンバーは同じではありません。  
なぜなら、これらの変数の参照先は独立したリストだからです。  

```python
>>> import copy
>>> spam = ['A', 'B', 'C', 'D']
>>> cheese = copy.copy(spam)
>>> cheese[1] = 42

# spam と cheese で内容が変わった！
>>> spam
['A', 'B', 'C', 'D']
>>> cheese
['A', 42, 'C', 'D']
```

コピーする必要のあるリストにさらにリストが含まれている場合は、copy.deepcopy() 関数を使用します。  
このdeepcopy()関数は、内部リストもコピーします。


## まとめ
- リストは、1つの変数に変更可能な値を記述できる、有用なデータ型です。  
  リストなしでは困難または不可能なこともあります。
- **リスト** は変更可能です。そのため、内容が変更される可能性があります。  
  (`append()` や `remove()`)   
  **タプル** と **文字列** は、リストに似ていますが、内容を変更することはできません。  
  たとえば、タプルまたは文字列値を含む変数は、新しいタプルや文字列値で上書きすることはできます。  
- 変数はリスト値を直接格納しません。リストへの参照を格納します。  
  これは、変数をコピーしたり、関数呼び出しで引数としてリストを渡すときに重要となる違いです。  
  コピーされる値はリスト参照であるため、リストに加えた変更がプログラムの別の変数に影響する可能性があります。  
  元のリストを変更せず、ある変数のみでリスト内容を変更したい場合は `copy()` や `deepcopy()` を使用します。

# 練習問題
1. What is []?  
  - リスト

2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam?(Assume spam contains [2, 4, 6, 8, 10].)  
  - `spam[2] = 'hello'`

For the following three questions, let’s say spam contains the list ['a', 'b', 'c', 'd'].  
3. What does spam[int(int('3' * 2) // 11)] evaluate to?

  ```python
  # メモ
  '3' * 2  # '33'
  int('33') // 11 # 3
  int(3) # 3
  spam[3]

  # 結果
  >>> spam = ['a', 'b', 'c', 'd']
  >>> spam[int(int('3' * 2) // 11)]
  'd'
  ```

4. What does spam[-1] evaluate to?
  - ['d']

5. What does spam[:2] evaluate to?
  - ['a', 'b']

For the following three questions, let’s say bacon contains the list [3.14, 'cat', 11, 'cat', True].  
6. What does bacon.index('cat') evaluate to?
  - 1

7. What does bacon.append(99) make the list value in bacon look like?
  - baconリストの値の最後に 99 が追加される

8. What does bacon.remove('cat') make the list value in bacon look like?
  - [3.14, 11, 'cat', True, 99]

9. What are the operators for list concatenation and list replication?  
  - concatenation: `+`
  - replication:  `*`

10. What is the difference between the append() and insert() list methods?  
  - append(): リストの最後に値を追加する
  - insert(): リストのインデックスで、値を挿入する場所を決められる

11. What are two ways to remove values from a list?  
  - del
  - remove()

12. Name a few ways that list values are similar to string values.  
  -

13. What is the difference between lists and tuples?
  - list: 値の変更が可能
  - tuple: 値の変更はできない

14. How do you type the tuple value that has just the integer value 42 in it?
  - (42,) <-- 最後にカンマをうつ

15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?
  - list()
  - tuple()
  ```python
  >>> list((42,))
  [42]
  >>> tuple([42])
  (42,)
  ```
16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?
  - リストのリファレンスID

17. What is the difference between copy.copy() and copy.deepcopy()?
  - copy.copy(): リストにリストが含まれて居ない場合の複製コピー
  - copy.deepcopy(): リストにリストが含まれている場合の複製コピー
