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
リスト内に文字列を入れる場合は '' でくくります。  

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

リスト内の各アイテムの値は、インデックスを使用して取得します。  
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
