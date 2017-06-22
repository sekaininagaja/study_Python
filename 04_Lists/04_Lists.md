Chapter 4 – Lists  
https://automatetheboringstuff.com/chapter4/

# リスト
ここでは、リストとタプルについて学びます。  
リストとタプルには複数の値を入れることができるので、大量のデータを扱うプログラムの作成が容易になります。  
リスト自体に他のリストを含めることができるので、データを階層構造に配置することができます。  

また、メソッドについても学びます。  
メソッドとは、あるデータ型の値に関連付けられた関数のことです。  


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
