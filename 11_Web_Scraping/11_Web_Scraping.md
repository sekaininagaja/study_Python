Chapter 11 – Web Scraping  
https://automatetheboringstuff.com/chapter11/

# WEBスクレイピング

私がWi-Fiを使用していない稀少な恐ろしい瞬間では、私がコンピュータ上で行っていることのどれがインターネット上で実際に何をしているのかが分かります。   
私は自分の電子メールをチェックしたり、友人のTwitterフィードを読んだり、「1985年のRobocopに登場する前に、Kurtwood Smithが大きな役割を果たしていたのですか？」という質問に答えようとしています。

コンピュータ上での多くの作業はインターネット上で行われるため、プログラムがオンラインになることができれば幸いです。   Webスクレイピングとは、プログラムを使用してWebからコンテンツをダウンロードして処理するための用語です。   
たとえば、Googleは検索エンジン用のWebページにインデックスを付けるために、多くのWebスクレイピングプログラムを実行しています。   
この章では、PythonでWebページを簡単にスクラップするためのいくつかのモジュールについて学びます。

- webbrowser: Pythonに付属し、特定のページへのブラウザを開きます。
- Requests: インターネットからファイルやWebページをダウンロードします。
- Beautiful Soup: Webページが書かれている書式であるHTMLを解析します。
- Selenium: Webブラウザを起動して制御します。 Seleniumはフォームを記入し、このブラウザでマウスクリックをシミュレートすることができます。

# プロジェクト：webbrowserモジュールを使用したmapit.py

webbrowserモジュールのopen()関数は、指定されたURLに新しいブラウザを起動できます。  

```python
>>> import webbrowser
>>> webbrowser.open('http://inventwithpython.com/')
```

Webブラウザのタブで http://inventwithpython.com/ のURLを開きます。   
これは、webbrowserモジュールが実行できる唯一のことです。   
それでも、open()関数はいくつか興味深いことを可能にします。   
たとえば、ストリートアドレスをクリップボードにコピーしてGoogleマップ上に地図を表示するのは面倒です。   
この作業では、クリップボードの内容を使用してブラウザで地図を自動的に起動する簡単なスクリプトを作成することで、いくつかのステップを実行できます。   
この方法では、アドレスをクリップボードにコピーしてスクリプトを実行すれば、マップが自動的に読み込まれます。

あなたのプログラムが下記を行います。
- コマンドライン引数またはクリップボードから住所を取得します。
- ウェブブラウザを開き、アドレスのGoogleマップページに移動します。

つまり、コードでは次のことを行う必要があります。
- sys.argvのコマンドライン引数を読んでください。
- クリップボードの内容を読んでください。
- webbrowser.open()関数を呼び出してWebブラウザを開きます。

## ステップ1：URLを把握する

付録Bの手順に基づいて、コマンドラインからコマンドラインを実行するようにmapIt.pyを設定します。  

...スクリプトは、クリップボードの代わりにコマンドライン引数を使用します。   
コマンドライン引数がない場合、プログラムはクリップボードの内容を使用することを認識します。

まず、特定の住所に使用するURLを特定する必要があります。   
ブラウザに http://maps.google.com/ をロードしてアドレスを検索すると、アドレスバーのURLは次のようになります。
```   
https://www.google.co.jp/maps/place/%E7%9A%87%E5%B1%85/@35.6851793,139.7506108,17z/data=!3m1!4b1!4m5!3m4!1s0x60188c0d02d8064d:0xd11a5f0b379e6db7!8m2!3d35.685175!4d139.7527995?hl=ja
```

アドレスはURLにありますが、そこにはさらに多くのテキストがあります。   
ウェブサイトでは、訪問者の追跡やサイトのカスタマイズに役立つように、URLに余分なデータを追加することがよくあります。   
しかし、https://www.google.com/maps/place/870+Valencia+St+San+Francisco+CA/  にアクセスすると、正しいページが表示されます。   
したがって、プログラムを設定してウェブブラウザを開き、「https://www.google.com/maps/place/your_address_string」（your_address_stringはマップしたいアドレス）に移動します。


## ステップ2：コマンドライン引数を処理する

シバン、プログラムのメモを書きます。  
必要モジュールをインポートします。  
sys.argv変数には、プログラムのファイル名とコマンドライン引数のリストが格納されます。   
このリストに単なるファイル名以上のものがある場合、len（sys.argv）は1より大きい整数に評価されます。  
つまり、コマンドライン引数の存在をチェックします。

コマンドラインの引数は通常スペースで区切りますが、この場合はすべての引数を単一の文字列として解釈したいとします。  
sys.argvは文字列のリストなので、join（）メソッドに渡すことができます。  
このメソッドは単一の文字列値を返します。   
この文字列にプログラム名は必要ないので、sys.argvの代わりにsys.argv[1:]を渡して配列の最初の要素を切り捨てる必要があります。   
この式が評価する最後の文字列は、address変数に格納されます。

これをコマンドラインに入力してプログラムを実行すると...   
`mapit 870 Valencia St, San Francisco, CA 94110`

... sys.argv変数にはこのリスト値が含まれます。  
`['mapIt.py', '870', 'Valencia', 'St, ', 'San', 'Francisco, ', 'CA', '94110']`

アドレス変数には文字列 `'870 Valencia St, San Francisco, CA 94110'` が含まれます。

#＃ 手順3：クリップボードのコンテンツを処理してブラウザを起動する

コマンドライン引数がない場合、プログラムはアドレスがクリップボードに格納されているとみなします。   
pyperclip.paste（）でクリップボードの内容を取得し、addressという名前の変数に格納することができます。   
最後に、Google Maps URLを使用してWebブラウザを起動するには、webbrowser.open（）を呼び出します。

あなたが書いたプログラムの中には、時間を節約する巨大なタスクを実行するものもありますが、アドレスのマップを取得するなど、一般的なタスクを実行するたびに数秒で便利にプログラムを使用するだけで十分です。   
以下は、手動でやるのとスクリプトにやらせるの、それぞれの手順を比較しています。

### 手動で地図を取得する手順
- アドレスを強調表示する
- アドレスをコピーする
- Webブラウザを開く
- http://maps.google.com/ にアクセスする
- ブラウザのアドレスフィールドをクリックする
- アドレスを貼り付ける
- エンターを押す

### スクリプトを使用した手順
- アドレスを強調表示する
- アドレスをコピーする
- スクリプトを実行する

## 類似のアイデア
あなたがURLを持っている限り、webbrowserモジュールでは、ブラウザを開いて自分自身をウェブサイトに誘導するステップを省略できます。   
他のプログラムは、この機能を使用して次のことを行うことができます。

- 別のブラウザタブでページ上のすべてのリンクを開く
- ブラウザで地元の天気のURLを開く
- 定期的にチェックするいくつかのソーシャルネットワークサイトを開く

# requestsモジュールを使用して、Webからファイルをダウンロード

要求モジュールを使用すると、ネットワークエラー、接続の問題、データ圧縮などの複雑な問題を心配することなく、Webからファイルを簡単にダウンロードできます。   
要求モジュールにはPythonが付属していないので、最初にインストールする必要があります。   
コマンドラインからpipインストール要求を実行します。
（付録Aにサードパーティのモジュールをインストールする方法の詳細があります）。

requests モジュールは、Pythonのurllib2モジュールが使いすぎるため記述されています。   
実際には、恒久的なマーカーを持ち、この段落全体を黒く塗ります。   
私は今までurllib2について言及しています。   
Webからダウンロードする必要がある場合は、requests モジュールを使用してください。

次に、requests モジュールが正しくインストールされていることを確認する簡単なテストを行います。   
対話型シェルに次のように入力します。
エラーメッセージが表示されない場合、要求モジュールは正常にインストールされています。

```python
>>> import requests
```

## requests.get()関数を使用したWebページのダウンロード

requests.get() 関数はダウンロードするURLの文字列を受け取ります。   
requests.get()の戻り値でtype()を呼び出すと、リクエストに応じてWebサーバーから渡されたレスポンスを含むResponseオブジェクトが返されることがわかります。   
レスポンスオブジェクトについては後で詳しく説明しますが、今のところコンピュータがインターネットに接続されている間は、対話型シェルに次のように入力します。

```python
>>> import requests
>>> res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
>>> type(res)
<class 'requests.models.Response'>
❶ >>> res.status_code == requests.codes.ok
True
>>> len(res.text)
178981
>>> print(res.text[:250])
The Project Gutenberg EBook of Romeo and Juliet, by William Shakespeare

This eBook is for the use of anyone anywhere at no cost and with
almost no restrictions whatsoever. You may copy it, give it away or
re-use it under the terms of the Proje
```

URLは、ロメオとジュリエットの全プレイのテキストWebページに移動します。   
Responseオブジェクトのstatus_code属性をチェックすることによって、このWebページのリクエストが成功したことがわかります。   
それがrequests.codes.okの値と等しい場合は、すべてがうまくいった。   
（ちなみに、HTTPプロトコルの「OK」のステータスコードは200です。「Not Found」の404ステータスコードにはすでに慣れているかもしれません）  

## エラーのチェック

これまで見てきたように、Responseオブジェクトには、ダウンロードが成功したかどうかを確認するために、requests.codes.okに対して確認できるstatus_code属性があります。   
成功を確認する簡単な方法は、Responseオブジェクトに対してraise_for_status（）メソッドを呼び出すことです。   
これは、ファイルのダウンロード中にエラーが発生した場合に例外を発生させ、ダウンロードが成功した場合は何も行いません。 対話型シェルに次のように入力します。

```python
>>> res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
>>> res.raise_for_status()
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    res.raise_for_status()
  File "C:\Python34\lib\site-packages\requests\models.py", line 773, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 404 Client Error: Not Found
```

raise_for_status（）メソッドは、悪いダウンロードが発生した場合にプログラムが停止するのを防ぐための良い方法です。   
これは良いことです：予期せぬエラーが発生するとすぐにプログラムを停止させたい。   
失敗したダウンロードがプログラムのディール・ブレーカー(合意を壊すもの？)でない場合、raise_for_status（）行をtryおよびexceptステートメントでラップして、クラッシュすることなくこのエラー・ケースを処理できます。

```python
import requests
res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status()
except Exception as exc:  # exceptによって、エラーメッセージが出力される
    print('There was a problem: %s' % (exc))

# エラーメッセージ内容
There was a problem: 404 Client Error: Not Found for url: http://inventwithpython.com/page_that_does_not_exist
```

requests.get（）を呼び出した後、常にraise_for_status（）を呼び出します。   
プログラムが続行される前にダウンロードが実際に機能していることを確認する必要があります。

# ダウンロードしたファイルをハードドライブに保存する

ここから、標準のopen（）関数とwrite（）メソッドを使用して、Webページをハードドライブ上のファイルに保存できます。   
しかし、若干の違いがあります。   
まず、文字列 'wb'を2番目の引数としてopen（）に渡すことで、ファイルをバイナリ書き込みモードで開く必要があります。   
ページが平文であっても（前にダウンロードしたロミオとジュリエットのテキストなど）、テキストのUnicodeエンコーディングを維持するために、テキストデータではなくバイナリデータを書き込む必要があります。

### Unicodeエンコーディング
Unicodeエンコーディングについては、この本の範囲を超えていますが、これらのWebページから詳細を知ることができます。  

- Joel on Software: The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets (No Excuses!): http://www.joelonsoftware.com/articles/Unicode.html
- Pragmatic Unicode: http://nedbatchelder.com/text/unipain.html

Webページをファイルに書き込むには、forループをResponseオブジェクトのiter_content（）メソッドとともに使用します。  

```python
>>> import requests
>>> res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
>>> res.raise_for_status()
>>> playFile = open('RomeoAndJuliet.txt', 'wb')
>>> for chunk in res.iter_content(100000):
        playFile.write(chunk)

100000
78981
>>> playFile.close()
```

iter_content（）メソッドは、ループを介して各繰り返しでコンテンツの「チャンク」を返します。   
各チャンクはバイトデータ型であり、各チャンクに含めるバイト数を指定できます。   
一般的には100,000バイトが良いサイズなので、iter_content（）の引数として100000を渡します。

ファイルRomeoAndJuliet.txtは現在の作業ディレクトリに存在します。   
ウェブサイトのファイル名はrj.txtでしたが、ハードドライブ上のファイルのファイル名は異なります。   
要求モジュールは、単にWebページのコンテンツのダウンロードを処理します。   
ページがダウンロードされると、それは単にプログラム内のデータです。   
ウェブページをダウンロードした後にインターネット接続を失ったとしても、すべてのページデータはあなたのコンピュータに残ります。

write()メソッドは、ファイルに書き込まれたバイト数を返します。   
前の例では、最初のチャンクに100,000バイトがあり、ファイルの残りの部分には78,981バイトしか必要ありませんでした。

ファイルをダウンロードして保存するための完全なプロセスを次に示します。
- ファイルをダウンロードするには `requests.get()` を呼び出します。
- writeバイナリモードで新しいファイルを作成するには、`open()` を **'wb'** で呼び出します。
- Responseオブジェクトの `iter_content()` メソッドをループします。
- 各繰り返しで `write()` を呼び出して、コンテンツをファイルに書き込みます。
- `close()` を呼び出してファイルを閉じます。

リクエストモジュールにはこれだけです！   
forループとiter_content() は、テキストファイルの書き込みに使用していた open() / write() / close() ワークフローと比べて複雑に思えるかもしれませんが、リクエストモジュールが大量のファイルをダウンロードした場合大量のメモリが必要になります。   
リクエストモジュールのその他の機能については、http：//requests.readthedocs.org/から参照できます。
