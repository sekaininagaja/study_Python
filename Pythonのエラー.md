

```python
# カンマのとじ忘れ
>>> 'Hello world!
SyntaxError: EOL while scanning string literal
```

```python
# 型がちがうもの同士はエラー
>>> 'Alice' + 42
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: must be str, not int
```

```python
# 文字列 * 文字列 というPythonさんが理解できない式はエラー
>>> 'Alice' * 'Bob'
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    'Alice' * 'Bob'
TypeError: can't multiply sequence by non-int of type 'str'
```

```python
# 文字列 * 浮動小数点 はエラー
>>> 'Alice' * 5.0
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    'Alice' * 5.0
TypeError: can't multiply sequence by non-int of type 'float'
```

```python
# 型がちがう
>>> int('99.99')
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    int('99.99')
ValueError: invalid literal for int() with base 10: '99.99'
```
