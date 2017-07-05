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
