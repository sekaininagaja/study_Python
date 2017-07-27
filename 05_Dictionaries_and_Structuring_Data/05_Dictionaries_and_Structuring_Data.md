Chapter 5 – Dictionaries and Structuring Data  
https://automatetheboringstuff.com/chapter5/

# 概要
この章では、データにアクセスして整理するための柔軟な方法を提供する **辞書型** について説明します。  
前の章のリストの知識と辞書を組み合わせて、チック・タック・トゥ・ボードをモデル化するデータ構造を作成する方法を学びます。


# 辞書型
リスト型のように、辞書型はいくつかの値の集合です。しかし、インデックスに関してはリスト型とは違います。  
リスト型ではインデックスに整数しか使えませんが、辞書型のインデックスはいくつかの異なるデータ型を扱えます。  
辞書型のインデックスは **キー** と呼ばれ、キーは **キーバリュー** と呼ばれる関連する値とペアになっています。   

以下のコードのとおり、辞書型は **{}** で表します。  

```python
>>> myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud' }
>>> myCat['size']
'fat'
>>> 'My cat has ' + myCat['color'] + ' fur.'
'My cat has gray fur.'
```

辞書型は、整数型もキーとして使えます。  
リスト型のインデックスのようなかんじですが、0からスタートする必要はなくて任意の値を使用できます。  
```python
>>> spam = {12345: 'Luggage Combination', 42: 'The Answer'}
>>> spam[12345]
'Luggage Combination'
>>> spam[42]
'The Answer'
```

## 辞書型 VS リスト型

リストとは違って、辞書型のアイテムは順序づけられていません。  
「spam」リストの最初のアイテムは「spam[0]」です。しかし、これは辞書型では最初のアイテムになりません。  
2つのリストが同じかどうかを判断するには項目の順序が重要ですが、辞書型の key-value ペアではどのような順序で入力されるかは関係ありません。  
辞書型は順序づけされていないので、リスト型のようにスライスすることはできません。  

```python
# リストは、内包するアイテムが同じでも、格納する順番が異なると同じリストとみなされない
>>> spam = ['cats', 'dogs', 'moose']
>>> bacon = ['dogs', 'moose', 'cats']
>>> spam == bacon
False

# 辞書は、内包するアイテムが同じなら、格納する順番が違っても同じ辞書とみなされる
>>> eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
>>> ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
>>> eggs == ham
True
```

辞書型で、存在しないキーを参照しようとすると KeyError になります。リスト形でいう “out-of-range” IndexError みたいなものです。  

```python
>>> spam = {'name': 'Zophie', 'age': '7'}
>>> spam['color']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'color'
```

辞書は順序付けされていませんが、キーに任意の値を設定できるため、データを強力な方法で整理できます。  
友人の誕生日データを保存するプログラムを作成したいとき、キーを「名前」、値を「誕生日」とする辞書を使用するといいかんじです。  

```python
# birthdays.py 実行結果
Enter a name: (blank to quit)
Alice
Apr 1 is the birthday of Alice
Enter a name: (blank to quit)
Masubuchi
I do not have birthday information for Masubuchi
What is their birthday?
July 3
Birthday database updated.
Enter a name: (blank to quit)
Masubuchi
July 3 is the birthday of Masubuchi
Enter a name: (blank to quit)
```

## keys(), values(), items() メソッド

下記の通り、3つの辞書型をあつかうためのメソッドがあります。  
- keys() … 辞書のキーを返す
- values() … 辞書の値を返す
- items() … キーと値を返す
リストに似ていますが、これらのメソッドで返される値は真ではありません。変更もできないし、append()メソッドもありません。  

しかし、これらのデータ型(dict_keys, dict_values, dict_items)はfor文の中で使えます。  
これらのメソッドを使用して、for文内でそれぞれ辞書内のキー、値、またはキーと値のペアを反復処理できます。  
items()メソッドによって返されるdict_itemsの値は、キーと値のタプルであることに注意してください。  

```python
>>> spam = {'color': 'red', 'age': '42'}

# spam辞書の値を表示
>>> for v in spam.values(): \
... print(v)
red
42

# spam辞書のキーを表示
>>> for k in spam.keys(): \
... print(k)
...
color
age

# spam辞書のキーと値の両方を表示 (キーと値のタプルが返る)
>>> for i in spam.items(): \
... print(i)
...
('color', 'red')
('age', '42')
```

これらのメソッドの真のリストが必要な場合は、戻り値をlist()関数に渡します。  

```python
>>> spam = {'color': 'red', 'age': 42}
>>> spam.keys()
dict_keys(['color', 'age'])
>>> list(spam.keys())
['color', 'age']
```

forループ内で複数の割り当てトリックを使用して、別々の変数にキーと値を割り当てることができます。  

```python
>>> spam = {'color': 'red', 'age': 42}
>>> for k, v in spam.items(): \
... print('Key: ' + k + ' Value: ' + str(v))
...
Key: color Value: red
Key: age Value: 42
```

## 辞書内の存在確認(Key, Value)

"in" と "not in" を使用して、ある値がリスト内に存在するかどうかを確認しました。  
これらの演算子を使用して、辞書でも同じように存在確認することができます。  

```python
>>> spam = {'name': 'Zophie', 'age': 7}

>>> 'name' in spam.values()
False

>>> 'name' in spam.keys()
True

>>> 'Zophie' in spam.values()
True

>>> 'color' in spam.keys()
False

>>> 'color' not in spam.keys()
True

# 'color' in spam.keys() の短縮した書き方
>>> 'color' in spam
False
```

## get() メソッド

そのキーの値にアクセスする前に、キーが辞書に存在するかどうかをチェックするのは面倒です。  
そんなときに get() メソッドを使います。  
get() メソッドでは、2つの引数(取り出す値のキーと、そのキーが存在しない場合に返すフォールバック値)を指定します。  

```python
>>> picnicItems = {'apples': 5, 'cups': 2}

# picnicItems に cups はある。cups の値を返す。
>>> 'I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.'
'I am bringing 2 cups.'

# picnicItems に eggs はない。get()メソッドで指定したフォールバック値を返す。
>>> 'I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.'
'I am bringing 0 eggs.'

# get()メソッドを使用しない場合、picnicItems に存在しない eggs を指定するをエラーになる
>>> 'I am bringing ' + str(picnicItems['eggs']) + ' eggs.'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'eggs'
```

## setdefault() メソッド

あるキーの辞書に値を設定しなければならない場合があります。  
以下は、if文で実現する方法です。

```python
>>> spam = {'name': 'Pooka', 'age': 5}
>>> if 'color' not in spam: \
... spam['color'] = 'black'

# 'color': 'black' が登録された！
>>> spam
{'name': 'Pooka', 'age': 5, 'color': 'black'}
```

setdefault() メソッドを使うと、上記のif文と同じことを1行でおこなえます。  
最初の引数にチェックするキーを指定し、2番目の引数にデフォルト値を設定します。  
キーが存在しない場合は、デフォルトの値がそのキーの値として設定されます。  
キーが存在する場合は、setdefault() メソッドはキーの値を返します。  
setdefault() メソッドを使用すると、辞書内に値が存在することを保証できます。  

```python
>>> spam = {'name': 'Pooka', 'age': 5}

# 'color' キーがないので、デフォルト値の 'black' を設定
>>> spam.setdefault('color', 'black')
'black'
>>> spam
{'name': 'Pooka', 'age': 5, 'color': 'black'}

# 'color': 'black' がすでに設定されているので、'white' にはならない。
>>> spam.setdefault('color', 'white')
'black'
>>> spam
{'name': 'Pooka', 'age': 5, 'color': 'black'}
```

## Pretty Printing (pprint() と pformat())

pprintモジュールをプログラムにインポートすると、pprint() と pformat() 関数にアクセスして、辞書の値を「きれいに」表示します。  
print() が提供するものよりも、辞書内の項目をいいかんじに表示できます。  
pprint.pprint() 関数は、辞書にネストされたリストや辞書が含まれている場合に特に役立ちます。  

```python
# characterCount.py 結果
{'I': 1, 't': 6, ' ': 13, 'w': 2, 'a': 4, 's': 3, 'b': 1, 'r': 5, 'i': 6, 'g': 2, 'h': 3, 'c': 3, 'o': 2, 'l': 3, 'd': 3, 'y': 1, 'n': 4, 'A': 1, 'p': 1, ',': 1, 'e': 5, 'k': 2, '.': 1}

# prettyCharacterCount.py 結果

{' ': 13,
 ',': 1,
 '.': 1,
 'A': 1,
 'I': 1,
 'a': 4,
 'b': 1,
 'c': 3,
 'd': 3,
 'e': 5,
 'g': 2,
 'h': 3,
 'i': 6,
 'k': 2,
 'l': 3,
 'n': 4,
 'o': 2,
 'p': 1,
 'r': 5,
 's': 3,
 't': 6,
 'w': 2,
 'y': 1}
```

装飾テキストを画面に表示する代わりに文字列値として取得する場合は、代わりにpprint.pformat()を呼び出します。

```python
# 以下の2つはどちらも同じ意味
pprint.pprint(someDictionaryValue)
print(pprint.pformat(someDictionaryValue))
```

# 辞書とリストのネスト

複雑なもののモデリングには、辞書内にリストや辞書のネストが必要になることがあります。  
リストは順序付けられた一連の値を格納する場合に使用し、辞書はキーを値に関連付けるのに使用します。  

たとえば、ピクニックに誰が何を持って来るのかを確認するために、他の辞書を含む辞書を使用するプログラムがあります。  
totalBrought()関数は、このデータ構造を読み込み、すべてのゲストが持っているアイテムの総数を計算します。  

```python
allGuests = {'Allice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

# totalBrought()関数の中で、ゲストごとのキーと値を繰り返し処理する。
# k... ゲスト名
# v... ピクニックアイテムの辞書
def totalBrought(guests, item):
    newBrought = 0
    for k, v in guests.items():
        # アイテムがキーとして存在する場合、その数値が newBrought に追加される
        # 存在しない場合、get()メソッドは 0 を返す
        newBrought = newBrought + v.get(item, 0)
    return newBrought

print('Number og things being broughe:')
print(' - Apples          ' + str(totalBrought(allGuests, 'apple')))
print(' - Cups            ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes           ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches  ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies      ' + str(totalBrought(allGuests, 'apple pies')))
```

```python
# 結果
Number og things being broughe:
 - Apples          7
 - Cups            3
 - Cakes           0
 - Ham Sandwiches  3
 - Apple Pies      1
```

最初はモデル化なんて必要ないような気がするかもしれませんが、そのうち数千のアイテムを処理するようになってくると利便性がわかってくると思います。  
最初にプログラミングを始めるときは、データをモデル化する「正しい」方法について心配する必要はありません。   
より多くの経験を積むにつれ、より効率的なモデルを考え出すことができますが、重要な点は、データモデルがプログラムのニーズに対応していることです。  


# まとめ
- リストと辞書は、他のリストや辞書を含む複数の値をネストできる。
- 辞書は、ある項目（キー）を別のもの（値）にマッピングできる。
- 辞書内の値にアクセスする場合は、大括弧で囲む(リストと同様)。
- 辞書のインデックスは整数ではない。整数、浮動小数点数、文字列、またはタプルなどのさまざまなデータ型のキーを辞書に含めることができる。
- プログラムの値をデータ構造に編成することで、実世界のオブジェクトの表現を作成できる。

# 練習問題

Q:1. What does the code for an empty dictionary look like?  
`{}`

Q:2. What does a dictionary value with a key 'foo' and a value 42 look like?  
`{'foo': 42}`

Q:3. What is the main difference between a dictionary and a list?  
リストは、整数のインデックスを持ち、順序だったデータを格納する。  
辞書のインデックスは整数以外も使える(整数、浮動小数点数、文字列、またはタプルなど)。  
辞書は、キーを値にマッピングする場合に便利。

Q:4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?  
KeyError になる。  

```python
>>> spam = {'bar': 100}
>>> spam['foo']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'foo'
```

Q:5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?  
spam['cat'] は、catという「キー」に対応する「値」をあらわす。  
spam.keys() は、spam という辞書内の「キー」すべてをあらわす。

Q:6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
spam['cat'] は、catという「キー」に対応する「値」をあらわす。  
spam.values() は、spam という辞書内の「値」すべてをあらわす。

Q:7. What is a shortcut for the following code?

```python
if 'color' not in spam:
    spam['color'] = 'black'
```

`spam.get('color', 'black')`


Q:8. What module and function can be used to “pretty print” dictionary values?  
pprintモジュールと、pprint(), pformat()関数  


# 練習プロジェクト

### ファンタジーゲームインベントリ

あなたはファンタジービデオゲームを作成しています。   
プレーヤーの所持品をモデル化するためのデータ構造は、キーがインベントリ内のアイテムを説明する文字列値であり、値がそのアイテムがプレーヤーの持つアイテムの数を示す整数値である辞書である。   
たとえば、「rope」：1、「torch」：6、「gold coin」：42、「dagger」：1、「arrow」：12 は、ロープ1本、トーチ6本、金42 コインなど。  

displayInventory() という名前の関数を作成し、可能な「インベントリ」を取り出し、次のように表示します。   
```python
Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62
```

### 解答
inventory.py

### ファンタジーゲームインベントリの辞書機能へのリスト

ドラゴンを倒すと戦利品がもらえます。  
戦利品は、下記のように文字列のリストとして表されます。  
`dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']`

これを、プレーヤーの所持品リストに加えるスクリプトを作成します。  
プログラムの結果は下記のようになるはずです。  

```python
Inventory:
45 gold coin
1 rope
1 ruby
1 dagger

Total number of items: 48
```

### 解答
dragonInventory.py

```python
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = {'gold coin': 42, 'rope': 1}

# 各パラメータに入るもの
# inventory <-- inv辞書
# added_items <-- dragon_lootリスト
def add_to_inventory(inventory, added_items):

    # added_items(dragon_lootリスト)のアイテム数とおなじ回数(len(added_items))だけ精査する。
    for i in range(len(added_items)):
        item_name = added_items[i]   # 精査するアイテム名
        item_total = 0               # 精査するアイテムの所持数の一時的に記憶するところ(初期化)

        # アイテムがinventory(inv辞書)内に存在する場合
        if item_name in inventory:
            item_total = int(inventory[item_name]) + 1  # 所持数+1する。辞書内の値はint型にしてから計算する。
            inventory[item_name] = item_total           # 辞書内の値を、item_totalの値に更新。(inventory[item_name] = int(inventory[item_name]) + 1 でも良さそう)

        # アイテムがinventory(inv辞書)内に存在しない場合
        else:
            inventory[item_name] = 1 # アイテムを辞書に追加する(値1)
            #inventory.setdefault(item_name, 1)  <-- setdefaultで登録しようとしてたときの名残
    i = i+1
    return inventory  # ★内容が更新された辞書を返す

def display_inventory(inventory):
    print("Inventry:")
    item_total = 0
    for k, v in inventory.items():
        print(str(inventory[k]) + '  ' + k )
        item_total = item_total + v
    print("Total number if items: " + str(item_total) )

# for debug
# コメントを外して使う。デバッグしたい関数が出現する前あたりにおいてやるとよさげ。
#import pdb;pdb.set_trace()

inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)
```

#### はまったところ
- 全然理解してないのに getメソッドや、setdefaultメソッドを使ってやってみようと色気をだしてしまった。愚直にif文、代入方式に変えた。
- 関数のパラメータの意味をいまいちよくわかっていない
- add_to_inventory関数の最後で return しなかったせいで、inv変数に更新した辞書を設定できなかった。  
  `inv = add_to_inventory(inv, dragon_loot)` <-- ここ  
- そのせいで、`display_inventory(inv)` がずっとエラーになるしまつ。  
  `AttributeError: 'NoneType' object has no attribute 'items'` `AttributeError: 'int' object has no attribute 'items'` など。(invに変な値がはいっている)
- Pythonデバッグの方法  
  参考: 【Python】いつまでprintデバッグで消耗してるの？
  http://racchai.hatenablog.com/entry/2016/05/30/070000  
  すばらしい記事。

#### デバッグしながら実行する様子
詳しくは上記の参考サイトを見る。  

- l(ist)	現在行の前後のソースコードを表示
- a(rgs)	現在いる関数の引数を表示
- p	プリント
- c(ont(inue))	次のブレイクポイントまで実行

```python
# python dragonInventory.py
> /root/work/study_Python/05_Dictionaries_and_Structuring_Data/dragonInventory.py(29)<module>()
-> inv = add_to_inventory(inv, dragon_loot)
(Pdb) l
 24         print("Total number if items: " + str(item_total) )
 25
 26     # for debug
 27     import pdb;pdb.set_trace()
 28
 29  -> inv = add_to_inventory(inv, dragon_loot)
 30     display_inventory(inv)
[EOF]
(Pdb) s
--Call--
> /root/work/study_Python/05_Dictionaries_and_Structuring_Data/dragonInventory.py(5)add_to_inventory()
-> def add_to_inventory(inventory, added_items):
(Pdb) l
  1     dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
  2     inv = {'gold coin': 42, 'rope': 1}
  3
  4     # dragon_loot のアイテムがinv内に存在するか確認し、存在していたら+1する
  5  -> def add_to_inventory(inventory, added_items):
  6         for i in range(len(added_items)):
  7             item_name = added_items[i]
  8             item_total = 0
  9             if item_name in inventory:
 10                 item_total = int(inventory[item_name]) + 1
 11                 inventory[item_name] = item_total
(Pdb) a
inventory = {'gold coin': 42, 'rope': 1}
added_items = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
(Pdb) s
> /root/work/study_Python/05_Dictionaries_and_Structuring_Data/dragonInventory.py(6)add_to_inventory()
-> for i in range(len(added_items)):
(Pdb) p type(inventory)
<class 'dict'>
(Pdb) p type(added_items)
<class 'list'>
(Pdb) s
> /root/work/study_Python/05_Dictionaries_and_Structuring_Data/dragonInventory.py(7)add_to_inventory()
-> item_name = added_items[i]
(Pdb) l
  2     inv = {'gold coin': 42, 'rope': 1}
  3
  4     # dragon_loot のアイテムがinv内に存在するか確認し、存在していたら+1する
  5     def add_to_inventory(inventory, added_items):
  6         for i in range(len(added_items)):
  7  ->         item_name = added_items[i]
  8             item_total = 0
  9             if item_name in inventory:
 10                 item_total = int(inventory[item_name]) + 1
 11                 inventory[item_name] = item_total
 12             else:
(Pdb) s
> /root/work/study_Python/05_Dictionaries_and_Structuring_Data/dragonInventory.py(8)add_to_inventory()
-> item_total = 0
(Pdb) s
> /root/work/study_Python/05_Dictionaries_and_Structuring_Data/dragonInventory.py(9)add_to_inventory()
-> if item_name in inventory:
(Pdb) s
> /root/work/study_Python/05_Dictionaries_and_Structuring_Data/dragonInventory.py(10)add_to_inventory()
-> item_total = int(inventory[item_name]) + 1
(Pdb) l
  5     def add_to_inventory(inventory, added_items):
  6         for i in range(len(added_items)):
  7             item_name = added_items[i]
  8             item_total = 0
  9             if item_name in inventory:
 10  ->             item_total = int(inventory[item_name]) + 1
 11                 inventory[item_name] = item_total
 12             else:
 13                 inventory[item_name] = 1
 14                 #inventory.setdefault(item_name, 1)
 15         i = i+1
(Pdb) s
> /root/work/study_Python/05_Dictionaries_and_Structuring_Data/dragonInventory.py(11)add_to_inventory()
-> inventory[item_name] = item_total
(Pdb) l
  6         for i in range(len(added_items)):
  7             item_name = added_items[i]
  8             item_total = 0
  9             if item_name in inventory:
 10                 item_total = int(inventory[item_name]) + 1
 11  ->             inventory[item_name] = item_total
 12             else:
 13                 inventory[item_name] = 1
 14                 #inventory.setdefault(item_name, 1)
 15         i = i+1
 16         return inventory
(Pdb) p inventory[item_name]
42
(Pdb) s
> /root/work/study_Python/05_Dictionaries_and_Structuring_Data/dragonInventory.py(6)add_to_inventory()
-> for i in range(len(added_items)):
(Pdb) p inventory[item_name]
43
(Pdb) a
inventory = {'gold coin': 43, 'rope': 1}
added_items = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
(Pdb) s
> /root/work/study_Python/05_Dictionaries_and_Structuring_Data/dragonInventory.py(7)add_to_inventory()
-> item_name = added_items[i]
(Pdb) s
> /root/work/study_Python/05_Dictionaries_and_Structuring_Data/dragonInventory.py(8)add_to_inventory()
-> item_total = 0
(Pdb) s
> /root/work/study_Python/05_Dictionaries_and_Structuring_Data/dragonInventory.py(9)add_to_inventory()
-> if item_name in inventory:
(Pdb) s
> /root/work/study_Python/05_Dictionaries_and_Structuring_Data/dragonInventory.py(13)add_to_inventory()
-> inventory[item_name] = 1
(Pdb) l
  8             item_total = 0
  9             if item_name in inventory:
 10                 item_total = int(inventory[item_name]) + 1
 11                 inventory[item_name] = item_total
 12             else:
 13  ->             inventory[item_name] = 1
 14                 #inventory.setdefault(item_name, 1)
 15         i = i+1
 16         return inventory
 17
 18     def display_inventory(inventory):
(Pdb) p  inventory[item_name]
*** KeyError: 'dagger'
(Pdb) s
> /root/work/study_Python/05_Dictionaries_and_Structuring_Data/dragonInventory.py(6)add_to_inventory()
-> for i in range(len(added_items)):
(Pdb) l
  1     dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
  2     inv = {'gold coin': 42, 'rope': 1}
  3
  4     # dragon_loot のアイテムがinv内に存在するか確認し、存在していたら+1する
  5     def add_to_inventory(inventory, added_items):
  6  ->     for i in range(len(added_items)):
  7             item_name = added_items[i]
  8             item_total = 0
  9             if item_name in inventory:
 10                 item_total = int(inventory[item_name]) + 1
 11                 inventory[item_name] = item_total
(Pdb) p  inventory[item_name]
1
(Pdb) a
inventory = {'gold coin': 43, 'rope': 1, 'dagger': 1}
added_items = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
(Pdb) s
> /root/work/study_Python/05_Dictionaries_and_Structuring_Data/dragonInventory.py(7)add_to_inventory()
-> item_name = added_items[i]
(Pdb) s
> /root/work/study_Python/05_Dictionaries_and_Structuring_Data/dragonInventory.py(8)add_to_inventory()
-> item_total = 0
(Pdb) s
> /root/work/study_Python/05_Dictionaries_and_Structuring_Data/dragonInventory.py(9)add_to_inventory()
-> if item_name in inventory:
(Pdb) s
> /root/work/study_Python/05_Dictionaries_and_Structuring_Data/dragonInventory.py(10)add_to_inventory()
-> item_total = int(inventory[item_name]) + 1
(Pdb) s
> /root/work/study_Python/05_Dictionaries_and_Structuring_Data/dragonInventory.py(11)add_to_inventory()
-> inventory[item_name] = item_total
(Pdb) s
> /root/work/study_Python/05_Dictionaries_and_Structuring_Data/dragonInventory.py(6)add_to_inventory()
-> for i in range(len(added_items)):
(Pdb) s
> /root/work/study_Python/05_Dictionaries_and_Structuring_Data/dragonInventory.py(7)add_to_inventory()
-> item_name = added_items[i]
(Pdb) s
> /root/work/study_Python/05_Dictionaries_and_Structuring_Data/dragonInventory.py(8)add_to_inventory()
-> item_total = 0
(Pdb) s
> /root/work/study_Python/05_Dictionaries_and_Structuring_Data/dragonInventory.py(9)add_to_inventory()
-> if item_name in inventory:
(Pdb) s
> /root/work/study_Python/05_Dictionaries_and_Structuring_Data/dragonInventory.py(10)add_to_inventory()
-> item_total = int(inventory[item_name]) + 1
(Pdb) s
> /root/work/study_Python/05_Dictionaries_and_Structuring_Data/dragonInventory.py(11)add_to_inventory()
-> inventory[item_name] = item_total
(Pdb) s
> /root/work/study_Python/05_Dictionaries_and_Structuring_Data/dragonInventory.py(6)add_to_inventory()
-> for i in range(len(added_items)):
(Pdb) s
> /root/work/study_Python/05_Dictionaries_and_Structuring_Data/dragonInventory.py(7)add_to_inventory()
-> item_name = added_items[i]
(Pdb) s
> /root/work/study_Python/05_Dictionaries_and_Structuring_Data/dragonInventory.py(8)add_to_inventory()
-> item_total = 0
(Pdb) s
> /root/work/study_Python/05_Dictionaries_and_Structuring_Data/dragonInventory.py(9)add_to_inventory()
-> if item_name in inventory:
(Pdb) s
> /root/work/study_Python/05_Dictionaries_and_Structuring_Data/dragonInventory.py(13)add_to_inventory()
-> inventory[item_name] = 1
(Pdb) s
> /root/work/study_Python/05_Dictionaries_and_Structuring_Data/dragonInventory.py(6)add_to_inventory()
-> for i in range(len(added_items)):
(Pdb) s
> /root/work/study_Python/05_Dictionaries_and_Structuring_Data/dragonInventory.py(15)add_to_inventory()
-> i = i+1
(Pdb) s
> /root/work/study_Python/05_Dictionaries_and_Structuring_Data/dragonInventory.py(16)add_to_inventory()
-> return inventory
(Pdb) s
--Return--
> /root/work/study_Python/05_Dictionaries_and_Structuring_Data/dragonInventory.py(16)add_to_inventory()->{'dagger': 1, 'gold coin': 45, 'rope': 1, 'ruby': 1}
-> return inventory
(Pdb) a
inventory = {'gold coin': 45, 'rope': 1, 'dagger': 1, 'ruby': 1}
added_items = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
(Pdb) l
 11                 inventory[item_name] = item_total
 12             else:
 13                 inventory[item_name] = 1
 14                 #inventory.setdefault(item_name, 1)
 15         i = i+1
 16  ->     return inventory
 17
 18     def display_inventory(inventory):
 19         print("Inventry:")
 20         item_total = 0
 21         for k, v in inventory.items():
(Pdb) s
> /root/work/study_Python/05_Dictionaries_and_Structuring_Data/dragonInventory.py(30)<module>()
-> display_inventory(inv)

～略～

(Pdb) c
Inventry:
45  gold coin
1  rope
1  dagger
1  ruby
Total number if items: 48
```
