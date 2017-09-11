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


# ロギング

プログラムの実行中にprint()ステートメントをコードに出力して変数の値を出力したことがある場合は、コードのデバッグにロギングのフォームを使用しています。   
ロギングは、プログラム内で何が起きているのか、起きている順番を理解するのに最適です。   
Pythonのロギングモジュールを使用すると、作成するカスタムメッセージのレコードを簡単に作成できます。   
これらのログメッセージは、プログラムの実行がロギング機能コールに達した時点を記述し、その時点で指定した変数をリストします。   
一方、欠落したログメッセージは、コードの一部がスキップされて実行されなかったことを示します。

## ロギングモジュールの使用

プログラムの実行中にロギングモジュールが画面にログメッセージを表示できるようにするには、プログラムの先頭に次の行をコピーします（**#!python シバン行の直下**）。

```
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s
- %(message)s')
```

どのように動作するか心配する必要はありませんが、基本的に、Pythonがイベントを記録するとき、そのイベントに関する情報を保持するLogRecordオブジェクトを作成します。   
ロギングモジュールのbasicConfig（）関数を使用すると、表示するLogRecordオブジェクトの詳細とその詳細をどのように表示するかを指定できます。

数値の階乗を計算する関数を書いたとします。   
数学では、階乗4 は 1×2×3×4、つまり24です。  
階数7は1×2×3×4×5×6×7、つまり5,040です。   

新しいファイルエディタウィンドウを開き、次のコードを入力します。   
それにはバグがありますが、間違っていることを理解するのに役立ついくつかのログメッセージも入力します。  

ここでは、ログ情報を出力するときにlogging.debug（）関数を使用します。   
このdebug（）関数はbasicConfig（）を呼び出し、一連の情報が出力されます。   
この情報は、basicConfig（）で指定したフォーマットであり、debug（）に渡したメッセージを含みます。   
print（factorial（5））呼び出しは元のプログラムの一部であるため、ロギングメッセージが無効になっていても結果が表示されます。

このプログラムの出力は次のようになります。

```python
2017-09-11 17:06:13,236 - DEBUG - Start of program
2017-09-11 17:06:13,237 - DEBUG - Start of dactorial(5)
2017-09-11 17:06:13,237 - DEBUG - i is 0, total is 0
2017-09-11 17:06:13,248 - DEBUG - i is 1, total is 0
2017-09-11 17:06:13,250 - DEBUG - i is 2, total is 0
2017-09-11 17:06:13,252 - DEBUG - i is 3, total is 0
2017-09-11 17:06:13,256 - DEBUG - i is 4, total is 0
2017-09-11 17:06:13,258 - DEBUG - i is 5, total is 0
2017-09-11 17:06:13,262 - DEBUG - End of factorial(5)
0
2017-09-11 17:06:13,267 - DEBUG - End of program
```

factorial（）関数は5の階乗として0を返しますが、これは正しくありません。   
forループは、合計値に1から5までの数字を掛けなければなりません。しかし、logging.debug（）によって表示されるログメッセージは、i変数が1ではなく0から始まっていることを示しています。   
反復の残りの部分もまた、合計のために間違った値を持つ。   
ログメッセージには、いつブレッドクラムがあるのかが分かります。

範囲（n + 1）内のfor iを範囲（1, n + 1）内のiに対して変更して実行する。  

```python
2017-09-11 17:09:34,592 - DEBUG - Start of program
2017-09-11 17:09:34,592 - DEBUG - Start of dactorial(5)
2017-09-11 17:09:34,593 - DEBUG - i is 1, total is 1
2017-09-11 17:09:34,598 - DEBUG - i is 2, total is 2
2017-09-11 17:09:34,600 - DEBUG - i is 3, total is 6
2017-09-11 17:09:34,605 - DEBUG - i is 4, total is 24
2017-09-11 17:09:34,607 - DEBUG - i is 5, total is 120
2017-09-11 17:09:34,612 - DEBUG - End of factorial(5)
120
2017-09-11 17:09:34,616 - DEBUG - End of program
```

factorial(5) 呼び出しは正しい値(120)を返します。  
ログメッセージはループ内で何が起こっているのかを示し、これはバグに直結しています。
logging.debug（）呼び出しは、渡された文字列だけでなく、タイムスタンプとDEBUGという単語も出力することがわかります。

## print() でデバッグしないでください

`import logging` と `logging.basicConfig(level=logging.DEBUG, format= '%(asctime)s - %(levelname)s - %(message)s')` を入力するのはやや面倒です。   
代わりにprint（）を使用したいかもしれませんが、この誘惑には気をつけてください！   
デバッグが完了すると、各ログメッセージのコードからprint（）呼び出しを削除するのに多くの時間を費やします。   
必要なprint（）呼び出しを誤って削除することさえあります。   
ログメッセージについての良い点は、あなたが好きなだけ多くのプログラムを自由に書き込めることです。  
また、1つの `logging.disable(logging.CRITICAL)` コールを追加することで、いつでも無効にすることができます。   
print（）とは異なり、ログモジュールはログメッセージの表示と非表示を簡単に切り替えることができます。

ログメッセージは、ユーザではなくプログラマを対象としています。   
ユーザーは、デバッグに役立ついくつかの辞書値の内容を気にしません。   
そのようなもののためにログメッセージを使用してください。   
File not found や Invalid input のように、ユーザが見たいと思うメッセージについては、あなたはprint（）コールを使うべきです。    
ログメッセージを無効にした後に、有用な情報をユーザーに提供したくないことは避けてください。


## ロギングレベル

ロギングレベルは、重要度別にログメッセージを分類する方法を提供します。   
下記のとおり、5つのログレベルがあります。   
メッセージは、異なるロギング機能を使用して各レベルでログに記録できます。

- DEBUG : logging.debug()
  - 最低レベル。 小さな細部に使用されます。 通常は、問題を診断する場合にのみこれらのメッセージを気にします。
- INFO : logging.info()
  - プログラムの一般的な出来事に関する情報を記録したり、プログラム内のその時点で動作していることを確認するために使用されます。
- WARNING : logging.warning()
  - プログラムの動作を妨げない潜在的な問題を示すために使用されますが、将来的にはそうする可能性があります。
- ERROR : logging.error()
  - プログラムが何かをしなかった原因となったエラーを記録するために使用されます。
- CRITICAL : logging.critical()
  - 最高レベル。 プログラムの実行を完全に停止させる原因となった、またはその原因となる致命的なエラーを示すために使用されます。

  ロギングメッセージは、これらの関数に文字列として渡されます。   
  ログレベルは推奨値です。   
  結局のところ、あなたのログメッセージがどのカテゴリーに入るかはあなた次第です。

```python
>>> import logging
>>> logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -
%(levelname)s - %(message)s')
>>> logging.debug('Some debugging details.')
2015-05-18 19:04:26,901 - DEBUG - Some debugging details.
>>> logging.info('The logging module is working.')
2015-05-18 19:04:35,569 - INFO - The logging module is working.
>>> logging.warning('An error message is about to be logged.')
2015-05-18 19:04:56,843 - WARNING - An error message is about to be logged.
>>> logging.error('An error has occurred.')
2015-05-18 19:05:07,737 - ERROR - An error has occurred.
>>> logging.critical('The program is unable to recover!')
2015-05-18 19:05:45,794 - CRITICAL - The program is unable to recover!
```

ロギングレベルの利点は、表示するロギングメッセージの優先順位を変更できることです。   
basicConfig（）関数のlevelキーワード引数にlogging.DEBUGを渡すと、すべてのログレベル（DEBUGが最低レベル）からのメッセージが表示されます。   
しかし、プログラムをもう少し開発した後は、エラーだけに興味があるかもしれません。   
その場合、basicConfig（）のレベル引数をlogging.ERRORに設定できます。   
これにより、ERRORおよびCRITICALメッセージのみが表示され、DEBUG、INFO、およびWARNINGメッセージはスキップされます。

## ロギングの無効化

あなたのプログラムをデバッグした後は、おそらく、これらのログメッセージがすべてスクリーンに乱雑にならないようにする必要があります。   
logging.disable（）関数はこれらを無効にするので、プログラムに入ってすべてのログ呼び出しを手作業で削除する必要はありません。   
単にlogging.disable（）にログレベルを渡すと、そのレベル以下のすべてのログメッセージが表示されなくなります。 したがって、ロギングを完全に無効にしたい場合は、logging.disable（logging.CRITICAL）をプログラムに追加してください。   
たとえば、対話型シェルに次のように入力します。

```python
>>> import logging
>>> logging.basicConfig(level=logging.INFO, format=' %(asctime)s -
%(levelname)s - %(message)s')

# disableにする前
>>> logging.critical('Critical error! Critical error!')
2015-05-22 11:10:48,054 - CRITICAL - Critical error! Critical error!

# disableにする
>>> logging.disable(logging.CRITICAL)

# disableにしたあと。メッセージは出なくなった。
>>> logging.critical('Critical error! Critical error!')
>>> logging.error('Error! Error!')
```

logging.disable（）はそれ以降のすべてのメッセージを無効にするので、`import logging` 行の近くにそれを追加するといいかんじです。  
必要に応じてロギングメッセージを有効または無効にするために、その呼び出しをコメントアウトまたはコメント解除することが容易にわかります。

## ファイルへのロギング

ログメッセージを画面に表示する代わりに、テキストファイルに書き込むことができます。   
logging.basicConfig（）関数はfilenameキーワード引数をとります：

```python
import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='
%(asctime)s - %(levelname)s - %(message)s')
```

ログメッセージはmyProgramLog.txtに保存されます。   
ロギングメッセージは役立ちますが、画面が乱雑になり、プログラムの出力を読みにくくなる可能性があります。   
ロギングメッセージをファイルに書き込むと、画面をクリアしたままにしておき、プログラムを実行した後で読むことができます。   
このテキストファイルは、メモ帳やテキストエディットなどのテキストエディタで開くことができます。

# IDLEデバッガ

デバッガはIDLEの機能で、一度に1行ずつプログラムを実行できます。   
デバッガは1行のコードを実行し、次に続行するように指示します。   
このようにプログラムを「デバッガの下で」実行することで、プログラムの存続期間中の任意の時点で変数の値を検査するのに必要な時間を長く取ることができます。   
これは、バグを追跡するための貴重なツールです。

IDLEのデバッガを有効にするには、対話型シェルウィンドウで[デバッグ] [デバッガ]をクリックします。   

Debug Controlウィンドウが表示されたら、 **Stack、Locals、Source、Globalsの4つのチェックボックスをすべてオン** にして、ウィンドウにデバッグ情報の完全なセットが表示されるようにします。   
デバッグ制御ウィンドウが表示されている間は、ファイルエディタからプログラムを実行するたびに、デバッガは最初の命令の前に実行を一時停止し、次を表示します。  

- 実行しようとしているコード行
- すべてのローカル変数とその値のリスト
- すべてのグローバル変数とその値のリスト

グローバル変数のリストには、定義されていない__builtins__、__doc__、__file__などの変数がいくつかあります。   
これらはPythonがプログラムを実行するたびに自動的に設定する変数です。   
これらの変数の意味はこの本の範囲を超えており、あなたはそれらを無理なく無視することができます。

Debug ControlウィンドウのGo、Step、Over、Out、Quitの5つのボタンのいずれかを押すまで、プログラムは一時停止したままになります。

## Go(実行)

[Go]ボタンをクリックすると、プログラムが終了するか、ブレークポイントに達するまでプログラムが正常に実行されます。   
ブレークポイントについては、この章の後半で説明します。  
デバッグが終了してプログラムを正常に続行させたい場合は、[Go]ボタンをクリックします。

## Step

[Step]ボタンをクリックすると、デバッガは次のコード行を実行してから再び一時停止します。   
Debug Controlウィンドウのグローバル変数とローカル変数のリストは、値が変更された場合に更新されます。   
次のコード行が関数呼び出しである場合、デバッガはその関数に「ステップイン」し、その関数のコードの最初の行にジャンプします。

## Over

[Over]ボタンをクリックすると、[Step]ボタンと同様に次のコード行が実行されます。   
ただし、次のコード行が関数呼び出しである場合、オーバーボタンは関数内のコードを「ステップオーバー」します。   
関数のコードは最高速度で実行され、関数呼び出しが返されるとすぐにデバッガが一時停止します。   
たとえば、次のコード行がprint（）呼び出しである場合、組み込みprint（）関数内のコードは実際には気にしません。   
あなたはそれを渡す文字列をスクリーンに印刷したいだけです。   
このため、ステップボタンよりもオーバーボタンを使用する方が一般的です。

## Out

[Out]ボタンをクリックすると、デバッガは現在の関数から復帰するまで、コードの行を最高速度で実行します。   
[Step]ボタンを使用して関数呼び出しに入った後、戻ってくるまで指示を実行し続けたい場合は、[Out]ボタンをクリックして現在の関数呼び出しから抜け出します。

## Quit

デバッグを完全に停止し、残りのプログラムの実行を続行しない場合は、[Quit]ボタンをクリックします。   
終了ボタンはすぐにプログラムを終了します。 通常どおりにプログラムを実行したい場合は、デバッガを無効にするためにデバッグ・デバッガを再度選択してください。

## プログラムを追加する数値のデバッグ

```
# buggyAddingProgram.py
print('Enter the first number to add:')
first = input()
print('Enter the second number to add:')
second = input()
print('Enter the third number to add:')
third = input()
print('The sum is ' + first + second + third)
```

デバッガを有効にしない状態で実施。

```python
Enter the first number to add:
5
Enter the second number to add:
3
Enter the third number to add:
42
The sum is 5342
```

プログラムはクラッシュしていませんが、その合計は明らかに間違っています。   
Debug Controlウィンドウを有効にして、今度はデバッガの下で再度実行してみましょう。

F5キーを押すか、RunRunモジュールを選択すると（DebugDebuggerが有効で、Debug Controlウィンドウの4つすべてのチェックボックスがオンになっています）、プログラムは1行目で一時停止状態になります。  
デバッガは常にコード行 実行しようとしています。

Overボタンを1回クリックすると、最初のprint（）コールが実行されます。   
print（）関数のコードにステップインしたくないので、ここで[ステップ]ではなく[オーバー]を使用してください。   
Debug Controlウィンドウは2行目に更新され、ファイルエディタウィンドウの2行目が強調表示されます。   
これは、プログラムの実行が現在どこにあるかを示します。

Overボタンをもう一度クリックすると、input（）関数呼び出しが実行され、IDLEが対話型シェルウィンドウへのinput（）呼び出しのための何かを入力するのを待っている間、Debug Controlウィンドウのボタンが無効になります。   
5と入力してReturnキーを押します。   
Debug Controlウィンドウのボタンが再度有効になります。

デバッガが7行目になるまで、次の2つの数字として3と42を入力し、プログラムの最後のprint（）コールをクリックして、Overをクリックし続けます。   
Globalsセクションで、第1、第2、第3の変数が整数値5,3、および42の代わりに文字列値 '5'、 '3'、および '42'に設定されていることがわかります。  
最後の行が実行されると これらの文字列は、一緒に追加される代わりに連結され、バグが発生します。

デバッガでプログラムをステップ実行すると便利ですが、遅くなることもあります。   
通常は、プログラムが特定のコード行に達するまで正常に実行されるようにします。   
ブレークポイントでこれを行うようにデバッガを構成できます。

## ブレークポイント

特定のコード行にブレークポイントを設定し、プログラムの実行がその行に到達するたびにデバッガを強制的に一時停止させることができます。   
新しいファイルエディタウィンドウを開き、以下のプログラムを入力して、コインを1,000回フリップするようにシミュレートします。

```python
# coinFlip.py
import random
heads = 0
for i in range(1, 1001):
❶     if random.randint(0, 1) == 1:
        heads = heads + 1
    if i == 500:
❷         print('Halfway done!')
print('Heads came up ' + str(heads) + ' times.')
```

random.randint(0,1) コールは、時間の半分を0で返し、もう半分は1を返します。   
これは「50/50コインフリップ」をシミュレートするために使用でき、1はヘッドを表します。   
デバッガなしでこのプログラムを実行すると、次のような出力がすぐに出力されます。

```
Halfway done!
Heads came up 490 times.
```

デバッガの下でこのプログラムを実行した場合は、プログラムが終了する前に何千回もオーバーボタンをクリックする必要があります。   
プログラム実行の途中でヘッドの価値に興味があった場合、1000個のコインフリップが500個完成したら、ラインプリントにブレークポイントを設定するだけです（ 'Halfway done！'）❷。   
ブレークポイントを設定するには、ファイルエディタでその行を右クリックして[Set Breakpoint]を選択します。  
-> (ブレークポイントを設定したラインは黄色くなる)

ifステートメントはループを介したすべての繰り返しで実行されるため、ifステートメント行にブレークポイントを設定したくない場合。   
ifステートメント内のコードにブレークポイントを設定することにより、デバッガは実行がif句に入るときにのみブレークします。  

ブレークポイントのある行は、ファイルエディタで黄色で強調表示されます。   
デバッガの下でプログラムを実行すると、通常どおり、最初の行で一時停止状態で開始します。   
しかし、[Go]をクリックすると、ブレークポイントが設定された行に到達するまで、プログラムは最高速度で実行されます。   
Go、Over、Step、またはOutをクリックすると、通常通り続行できます。

ブレークポイントを削除するには、ファイルエディタでその行を右クリックし、メニューから[ブレークポイントのクリア]を選択します。   
黄色の強調表示が消えて、デバッガは将来その行を中断しません。

# まとめ

アサーション、例外、ロギング、およびデバッガは、プログラム内のバグを見つけて防ぐための貴重なツールです。   
アサーションはPythonのassert文を使用して、必要な条件が満たされない場合に早期警告を与える「健全性チェック」を実装するのに適しています。   
アサーションは、プログラムが回復しようとしてはならないエラーのためだけであり、速く失敗するはずです。   
それ以外の場合は、例外を発生させる必要があります。

例外は、tryおよびexceptステートメントによって捕捉され、処理されます。   

ロギングモジュールは、実行中にコードを調べるための良い方法です。  
異なるロギングレベルとテキストファイルへのログ機能のために、print（）関数よりもはるかに便利です。  

デバッガを使用すると、一度に1行ずつプログラムをステップ実行できます。   
あるいは、通常の速度でプログラムを実行し、ブレークポイントが設定された行に到達するたびにデバッガを実行して一時停止させることもできます。   
デバッガを使用すると、プログラムの存続期間中の任意の時点で変数の値の状態を確認できます。

これらのデバッグツールとテクニックは、動作するプログラムを書くのに役立ちます。   
誤ってコードにバグを導入することは、何年ものコーディング経験を持っていても、事実です。

# 練習問題

1. Write an assert statement that triggers an AssertionError if the variable spam is an integer less than 10.
- 10より小さい場合はNG => 10以上ならTrue
- assert spam >= 10, 'spam が 10 より小さい値です。'

```
# OK
>>> spam = 12
>>> assert spam >= 10, 'spam が 10 より小さい値です。'
>>> spam = 10
>>> assert spam >= 10, 'spam が 10 より小さい値です。'

# NG
>>> spam = 9
>>> assert spam >= 10, 'spam が 10 より小さい値です。'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError: spam が 10 より小さい値です。
```

2. Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the same as each other, even if their cases are different (that is, 'hello' and 'hello' are considered the same, and 'goodbye' and 'GOODbye' are also considered the same).
- 大文字小文字に関わらず中身が同じならTrue。
- assert egg.upper() == bacon.upper(), 'egg と bacon の中身がちがいます'

```python
# OK
>>> egg = 'hello'
>>> bacon = 'HELLO'
>>> assert egg.upper() == bacon.upper(), 'egg と bacon の中身がちがいます'

# NG
>>> egg = 'bye'
>>> assert egg.upper() == bacon.upper(), 'egg と bacon の中身がちがいます'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError: egg と bacon の中身がちがいます
```
3. Write an assert statement that always triggers an AssertionError.
- 永遠に True にならなければいいってこと？？
- assert False, 'EROOOOOOOOOOR!!!'

```
>>> assert False, 'EROOOOOOOOOOR!!!'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError: EROOOOOOOOOOR!!!
```

4. What are the two lines that your program must have in order to be able to call logging.debug()?
```
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
```

5. What are the two lines that your program must have in order to have logging.debug() send a logging message to a file named programLog.txt?
```
import logging
logging.basicConfig(filename='programLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
```

6. What are the five logging levels?
- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

7. What line of code can you add to disable all logging messages in your program?
- logging.disable(logging.CRITICAL)

8. Why is using logging messages better than using print() to display the same message?
- print() によるデバッグだと必要なくなったときに手動で消していかないといけない。
- loggingモジュールを使うと、簡単にログの有効化・無効化が可能

9. What are the differences between the Step, Over, and Out buttons in the Debug Control window?
- Step: コードを1行ずつ実行していく。コード行が関数呼び出しの場合はその関数の一番始めの行に「ステップイン」する（関数も1行ずつ実行していく）
- Over: Stepと同様にコードを1行ずつ実行していくが、コード行が関数呼び出しの場合は「ステップオーバー」する（関数は1行ずつ実行していかない）

10. After you click Go in the Debug Control window, when will the debugger stop?
- プログラムが終了するか、ブレークポイントに到達したら止まる

11. What is a breakpoint?
- 特定のコード行にブレークポイントを設定し、コードがその行に到達するとデバッガーは処理を一時停止する

12. How do you set a breakpoint on a line of code in IDLE?
- ブレークポイントを設定したいコード行で右クリックし、[Set Breakpoint]する
