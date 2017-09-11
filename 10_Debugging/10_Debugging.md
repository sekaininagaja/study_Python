Chapter 10 – Debugging
https://automatetheboringstuff.com/chapter10/

# デバッグ

より複雑なプログラムを書くのに十分な知識があるので、単純ではないバグを見つけることができます。   
この章では、プログラム内のバグの根本的な原因を突き止めるためのツールやテクニックについて説明します。  

プログラマーの間で古いジョークを言い換えると、「コードを書くことはプログラミングの90％を占めます。 デバッグコードは他の90％を占めています。」  

あなたのコンピュータはあなたの言うことだけを行います。   
あなたの心を読んで、あなたが意図したことをすることはありません。   
プロのプログラマーでもバグが常に発生するので、プログラムに問題がある場合は落胆しないでください。  

幸いにも、コードが正確に何をしているのか、どこが間違っているのかを特定するためのいくつかのツールとテクニックがあります。   
まず、ロギングとアサーションを見ていきます。  
これは、バグを早期に発見するのに役立つ2つの機能です。   
一般的に、バグを早く発見すればするほど修正が容易になります。

次に、デバッガの使い方を見ていきます。   
デバッガはIDLEの機能であり、一度に1命令ずつプログラムを実行するので、コード実行中に変数の値を検査したり、プログラムの途中で値がどのように変化するかを追跡したりすることができます。   
プログラムをフルスピードで実行するよりもはるかに時間がかかりますが、実行中のプログラムの実際の値をソースコードから推測するのではなく、実際の値を調べると便利です。

# 例外の発生

Pythonは、無効なコードを実行しようとするたびに例外を発生させます。   
第3章では、tryやexcept文でPythonの例外を処理する方法について説明しました。  
これにより、プログラムは予期した例外から回復することができます。   
しかし、コード内で独自の例外を発生させることもできます。   
例外を発生させる方法は、「この関数でコードを実行しないで、プログラムの実行をexceptステートメントに移す」という方法です。

raise文で例外が発生します。 コードでは、raise文は次の要素で構成されます。
- raiseキーワード
- exception()関数の呼び出し
- exception()関数に渡される有用なエラーメッセージを含む文字列

```python
>>> raise Exception('This is the error message.')
Traceback (most recent call last):
  File "<pyshell#191>", line 1, in <module>
    raise Exception('This is the error message.')
Exception: This is the error message.
```

tryおよびexceptステートメントがない場合、raiseステートメントで例外を発生させるとプログラムは単にクラッシュし、例外のエラーメッセージを表示します。  

多くの場合、関数を呼び出すコードであり、関数自体ではなく、expectionを処理する方法を知っています。   
したがって、関数内でraise文が一般的に表示され、関数を呼び出すコード内でtry文とexcept文が表示されます。

ここでは、文字、幅、高さを取るboxPrint（）関数を定義し、その幅と高さの箱を少し描写するために文字を使用します。   
このボックス形状はスクリーンに印刷されます。  

文字を1文字にし、幅と高さを2より大きくしたいとしましょう。  
これらの要件が満たされない場合、例外を発生させるif文を追加します。   
後で、さまざまな引数を指定してboxPrint（）を呼び出すと、try / exceptは無効な引数を処理します。

このプログラムは、exceptステートメントの例外としてerr以外の例外を使用します。   
例外オブジェクトがboxPrint（）から返された場合、このexcept文はerrという名前の変数に格納します。   
次に、Exceptionオブジェクトをstr（）に渡して文字列に変換し、ユーザーフレンドリーなエラーメッセージを生成することができます。   
このboxPrint.pyを実行すると、出力は次のようになります。

```
****
*  *
*  *
****
OOOOOOOOOOOOOOOOOOOO
O                  O
O                  O
O                  O
OOOOOOOOOOOOOOOOOOOO
An exception happened: Width must be greater than 2.
An exception happened: Symbol must be a single character string.
```

tryおよびexceptステートメントを使用すると、プログラム全体がクラッシュするのではなく、エラーをより適切に処理できます。


# トレースバックを文字列として取得する

Pythonがエラーに遭遇すると、トレースバックと呼ばれる宝くじ情報が生成されます。   
トレースバックには、エラーメッセージ、エラーの原因となった行の行番号、およびエラーを引き起こした関数呼び出しのシーケンスが含まれます。   
この一連の呼び出しは呼び出しスタックと呼ばれます。

```python
# errorExample.py
def spam():
    bacon()
def bacon():
    raise Exception('This is the error message.')

spam()
```

errorExample.pyを実行すると、出力は次のようになります。

```python
Traceback (most recent call last):
  File "errorExample.py", line 7, in <module>
    spam()
  File "errorExample.py", line 2, in spam
    bacon()
  File "errorExample.py", line 5, in bacon
    raise Exception('This is the error message.')
Exception: This is the error message.
```

トレースバックをたどると、エラーが 5行目のbacon()関数の中で、に起こったことがわかります。   
この特定のbacon()呼び出しは、2行目のspam()関数から呼び出され、7行目で呼び出されました。  
複数の場所から関数を呼び出すことができるプログラムでは、コールスタックは、どのコールがエラーにつながったかを判断するのに役立ちます。

```
(1) 7行目 spam() でエラー
(2) 2行目 bacon() でエラー
(3) 5行目 「raise Exception('This is the error message.')」  <-- これが呼び出されたから！
```

トレースバックは、発生した例外が処理されなくなるたびにPythonによって表示されます。   
しかし、traceback.format_exc()を呼び出すことで文字列として取得することもできます。   
この関数は、例外のトレースバックから情報を取得するだけでなく、例外を正常に処理するためにexceptステートメントを使用する場合に便利です。   
この関数を呼び出す前に、Pythonのトレースバックモジュールをインポートする必要があります。

たとえば、例外が発生したときにプログラムをクラッシュさせる代わりに、トレースバック情報をログファイルに書き込んでプログラムを実行し続けることができます。   
プログラムをデバッグする準備ができたら、後でログファイルを見ることができます。   

```python
>>> import traceback
>>> try:
         raise Exception('This is the error message.')
except:
         errorFile = open('errorInfo.txt', 'w')
         errorFile.write(traceback.format_exc())
         errorFile.close()
         print('The traceback info was written to errorInfo.txt.')

116
The traceback info was written to errorInfo.txt.
```

116は、ファイルに116文字が書き込まれたため、write（）メソッドからの戻り値です。   
トレースバックテキストはerrorInfo.txtに書き込まれました。

```
Traceback (most recent call last):
  File "<pyshell#28>", line 2, in <module>
Exception: This is the error message.
```
