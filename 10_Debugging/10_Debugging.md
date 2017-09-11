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

# アサーション

アサーションは、あなたのコードが間違って何かを間違って実行していないことを確認する健全性チェックです。   
これらのサニティ(正常性)チェックは、アサート文によって実行されます。   
サニティチェックが失敗すると、AssertionError例外が発生します。   
コードでは、assert文は次の要素で構成されます。

- assertキーワード
- 条件（TrueまたはFalseで評価される式）
- コンマ
- 条件がFalseの場合に表示する文字列

```python
>>> podBayDoorStatus = 'open'
>>> assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
>>> podBayDoorStatus = 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'
>>> assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
AssertionError: The pod bay doors need to be "open".
```

ここでは podBayDoorStatusを 'open'に設定しました。  
これからは、この変数の値が 'open'になることを完全に期待しています。   
この変数を使用するプログラムでは、期待どおりに動作するためには、その値が「開かれている」ことに依存する「開かれた」コードであるという前提で、多くのコードを書いているかもしれません。   
そこで、podBayDoorStatusが 'open'であると仮定するようにアサーションを追加します。   
ここでは、「ポッドベイのドアを開く必要があります」というメッセージが含まれています。   
アサーションが失敗した場合、何が間違っているかを簡単に確認できます。

後で、podBayDoorStatusに別の値を割り当てる間違いを間違えているが、多くのコード行には気づかないと言う。   
アサーションはこのミスをキャッチし、何が間違っているかを明確に伝えます。

普通の英語では、assertステートメントは「この条件が成り立つと主張し、そうでなければプログラムのどこかにバグがあります」と述べています。  
例外とは異なり、tryやexceptを使ってアサートステートメントを処理するべきではありません。   
アサーションが失敗した場合、プログラムはクラッシュするはずです。   
このように速く失敗することで、バグの元の原因と最初にバグに気付く時期との間の時間が短くなります。   
これにより、バグの原因となっているコードを見つける前にチェックする必要があるコードの量が減ります。

アサーションはプログラマのエラーであり、ユーザのエラーではありません。   
復旧可能なエラー（ファイルが見つからない、またはユーザーが無効なデータを入力するなど）に対しては、assert文で検出するのではなく、例外を発生させます。

## 信号機シミュレーションでのアサーションの使用

交通信号シミュレーションプログラムを構築しているとします。   
交差点のストップライトを表すデータ構造は、南北に面したストップライトと東西に面したキーである 'ns'と 'ew'を持つ辞書です。   
これらのキーの値は、 'green', ' yellow', 'red' のいずれかになります。   
コードは次のようになります。

これらの2つの変数は、Market Streetと2nd Street、Mission Streetと16th Streetの交差点をあらわします。  
プロジェクトを開始するには、switchLights()関数を記述します。  
この関数は、交差点辞書を引数として取り、ライトを切り替えます。

最初は、switchLights（）は、各ライトをシーケンス内の次の色に切り替える必要があると考えるかもしれません。  
「緑」の値は「黄」に、「黄」の値は「赤」に、 値は「緑色」に変わります。   
このアイデアを実装するコードは次のようになります。

```python
market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}

def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'

switchLights(market_2nd)
```

このコードではすでに問題が発生しているかもしれませんが、数千行の長いシミュレーションコードを気付かずに書いたふりをしましょう。   
最終的にシミュレーションを実行すると、プログラムはクラッシュしませんが、あなたのバーチャルカーは大破します！

既にプログラムの残りの部分を書いているので、バグがどこにあるのか分かりません。   
たぶんそれは、車をシミュレートするコードまたは仮想ドライバをシミュレートするコードにあります。   
バグをswitchLights（）関数にトレースするのに数時間かかることがあります。

しかし、switchLights（）を書くときに、少なくとも1つのライトが常に赤であることを確認するアサーションを関数の一番下に追加してあった場合・・・

```
assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)
```

このアサーションが適切に設定されていると、プログラムがクラッシュし、次のエラーメッセージが表示されます。

```python
Traceback (most recent call last):
  File "carSim.py", line 14, in <module>
    switchLights(market_2nd)
  File "carSim.py", line 13, in switchLights
    assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)
❶ AssertionError: Neither light is red! {'ns': 'yellow', 'ew': 'green'}
```

ここで重要なのはAssertionError❶です。   
あなたのプログラムがクラッシュするのは理想的ではありませんが、ただちに健全性チェックが失敗したことを指摘します。  
どちらの方向も赤信号ではありません。   
プログラムの実行の早い段階で失敗することで、将来の多くのデバッグ作業を自分で省くことができます。


## アサーションの無効化

アサーションは、Pythonの実行時に  `-O` オプションを渡すことで無効にすることができます。   
これは、プログラムの作成とテストが終了し、サニティチェックを実行して速度を落とさないようにしたい場合に便利です（ほとんどの場合、assert文は速度の差が目立たない）。   
アサーションは開発用であり、最終製品用ではありません。   
プログラムを他の人に渡して実行するまでには、バグがなく、正当性チェックを必要としません。   
`-O` オプションを使用して、おそらくあまり意味のないプログラムを起動する方法の詳細については、付録Bを参照してください。
