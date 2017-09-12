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

# HTML
Webページを選ぶ前に、いくつかのHTMLの基本を学びます。   
また、Webブラウザの強力な開発者ツールにアクセスする方法もわかります。  
これにより、Webから情報を簡単に取り出せるようになります。

## HTMLを学習するためのリソース

HTMLの基本的な使い方を前提としていますが、初心者のチュートリアルが必要な場合は、次のサイトのいずれかをお勧めします。
- http://htmldog.com/guides/html/beginner/
- http://www.codecademy.com/tracks/web/
- https://developer.mozilla.org/en-US/learn/html/

## クイックリフレッシャー

HTMLを見てからしばらく時間があった場合は、ここで基本の概要を簡単に説明します。   
HTMLファイルは.htmlファイル拡張子を持つプレーンテキストファイルです。   
これらのファイルのテキストは、山括弧で囲まれたタグで囲まれています。   
このタグは、ブラウザにウェブページのフォーマット方法を指示します。   
開始タグと終了タグは、テキストを囲んで要素を形成することができます。   
テキスト（または内部HTML）は開始タグと終了タグの間の内容です。   

たとえば、次のHTMLはHello worldを表示します。   
ブラウザでHelloを太字で表示します。
```html
<strong>Hello</strong> world!
```

開始<strong>タグは、囲まれたテキストが太字で表示されることを示します。   
閉じる</strong>タグは、太字のテキストの終わりがブラウザに表示されます。

HTMLにはさまざまなタグがあります。   
これらのタグの中には、角括弧内の属性の形式で追加のプロパティを持つものがあります。   
たとえば、<a>タグはリンクであるテキストを囲みます。   
テキストリンク先のURLは、href属性によって決まります。   
ここに例があります：
```html
Al's free <a href="http://inventwithpython.com">Python books</a>.
```

一部の要素には、ページ内の要素を一意に識別するために使用されるid属性があります。   
id属性で要素を探し出すようにプログラムに指示することが多いので、ブラウザの開発者ツールを使用して要素のid属性を調べることは、Webスクレイピングプログラムを書く際の一般的な作業です。

## WebページのソースHTMLの表示

あなたのプログラムが動作するWebページのHTMLソースを調べる必要があります。   
これを行うには、Webブラウザで任意のWebページを右クリック（またはOS XでCTRL-クリック）し、ソースの表示またはページソースの表示を選択して、ページのHTMLテキストを表示します。   
これはブラウザが実際に受け取るテキストです。   
ブラウザは、このHTMLからWebページを表示またはレンダリングする方法を知っています。

お気に入りのサイトのソースHTMLを表示することを強くお勧めします。   
あなたがソースを見るときにあなたが見ているものを完全に理解していないのであれば問題ありません。   
シンプルなWebスクレイピングプログラムを書くためにHTMLの知識は必要ありません。  
結局のところ、あなた自身のウェブサイトを書くことはありません。   
既存のサイトからデータを取り出すには、十分な知識が必要です。

## ブラウザの開発者ツールを開く

Webページのソースを表示するだけでなく、ブラウザの開発者ツールを使用してページのHTMLを見ることもできます。  
ChromeとInternet Explorer for Windowsでは、開発者ツールは既にインストールされており、F12キーを押すと表示されます。   
F12をもう一度押すと、デベロッパーツールが消えます。   
Chromeでは、[表示] - [デベロッパ] - [デベロッパーツール]を選択してデベロッパーツールを表示することもできます。   
OS Xでは、 [command + OPTION + I] を押すと、Chromeの開発者ツールが開きます。

Firefoxでは、WindowsとLinuxでCTRL-SHIFT-Cを押すか、OS Xで⌘-OPTION-Cを押してWeb Developer Tools Inspectorを起動できます。  
レイアウトはChromeの開発ツールとほぼ同じです。

SafariでPreferencesウィンドウを開き、AdvancedペインでメニューバーオプションのShow Developメニューをチェックします。   
これを有効にした後、 - OPTION-Iを押して開発者ツールを起動することができます。

ブラウザに開発ツールを有効またはインストールしたら、Webページの任意の部分を右クリックし、コンテキストメニューから「要素の検査」を選択して、ページのその部分を担当するHTMLを表示することができます。   
これは、Webスクレイピングプログラム用にHTMLを解析するときに役立ちます。

### 正規表現を使用してHTMLを解析しない

文字列内のHTMLの特定の部分を見つけることは、正規表現の完璧なケースのように思えます。   
しかし、私はそれに対してあなたに助言します。   
HTMLをフォーマットしても有効なHTMLと見なすことができるさまざまな方法がありますが、これらの可能なバリエーションをすべて正規表現でキャプチャしようとすると、面倒でエラーが発生しやすくなります。   
Beautiful SoupのようなHTMLを解析するために特別に開発されたモジュールは、バグの原因となる可能性が低くなります。

以下で、正規表現を使用してHTMLを解析しないようにすべき理由の拡張引数を見つけることができます。  
http://stackoverflow.com/a/1732454/1893164/  

## 開発者ツールを使用したHTML要素の検索

プログラムがリクエストモジュールを使用してWebページをダウンロードすると、そのページのHTMLコンテンツが単一の文字列値になります。   
ここで、HTMLのどの部分が興味のあるWebページの情報に対応しているかを理解する必要があります。

これは、ブラウザのデベロッパーツールが役立つところです。   
http://weather.gov/ から天気予報データを取得するプログラムを作成したいとします。   
コードを書く前に、少し研究をしてください。   
あなたがサイトにアクセスして郵便番号(94105)を検索すると、サイトはそのエリアの予測を示すページに移動します。

その郵便番号の温度情報を掻き集めることに興味があればどうですか？   
ページ上の位置を右クリック（またはOS X上でCONTROLクリック）し、表示されるコンテキストメニューから「要素を検査」を選択します。   
これにより、Developer Toolsウィンドウが表示され、Webページのこの特定の部分を生成するHTMLが表示されます。   

開発者ツールから、Webページの温度部分を担当するHTMLが `<p class="myforecast-current-lrg">59°F</p>` であることがわかります。   
これはまさにあなたが探していたものです！   
温度情報は、myforecast-current-lrgクラスの<p>要素内に含まれているようです。   
これで、あなたが探しているものが分かったので、BeautifulSoupモジュールは文字列内でそれを見つけるのに役立ちます。


## BeautifulSoupモジュールでのHTMLの解析

Beautiful Soupは、HTMLページから情報を抽出するためのモジュールです（正規表現よりもはるかに優れています）。   
BeautifulSoupモジュールの名前は bs4 です（Beautiful Soup、version 4用）。   
インストールするには、コマンドラインからpip install beautifulsoup4を実行する必要があります。   
（サードパーティ製モジュールのインストール方法については付録Aを参照してください。）  
beautifulsoup4がインストールに使用される名前ですが、Beautiful Soupをインポートするには `import bs4` を実行します。

この章では、Beautiful Soupの例では、ハードドライブ上のHTMLファイルを解析（つまり、その部分を分析して識別する）します。   
IDLEで新しいファイルエディタウィンドウを開き、次のように入力してexample.htmlとして保存します。   
または、http://nostarch.com/automatestuff/ からダウンロードしてください。

```html
<!-- This is the example.html example file. -->

<html><head><title>The Website Title</title></head>
<body>
<p>Download my <strong>Python</strong> book from <a href="http://
inventwithpython.com">my website</a>.</p>
<p class="slogan">Learn Python the easy way!</p>
<p>By <span id="author">Al Sweigart</span></p>
</body></html>
```

ご覧のとおり、単純なHTMLファイルでもさまざまなタグや属性が使用されています。  
複雑なWebサイトでは、すぐに問題が混乱します。   
ありがたいことに、Beautiful SoupはHTMLでの作業をはるかに簡単にします。

## HTMLからBeautifulSoupオブジェクトを作成する

bs4.BeautifulSoup()関数は、解析するHTMLを含む文字列で呼び出す必要があります。   
bs4.BeautifulSoup()関数はBeautifulSoupオブジェクトを返します。   
コンピュータがインターネットに接続されている間は、対話型シェルに次のように入力します。

```python
>>> import requests, bs4
>>> res = requests.get('http://nostarch.com')
>>> res.raise_for_status()
>>> noStarchSoup = bs4.BeautifulSoup(res.text)
>>> type(noStarchSoup)
<class 'bs4.BeautifulSoup'>
```

このコードでは、requests.get()を使用してNo Starch PressのWebサイトからメインページをダウンロードし、応答のテキスト属性をbs4.BeautifulSoup()に渡します。   
返されるBeautifulSoupオブジェクトは、noStarchSoupという名前の変数に格納されます。

bs4.BeautifulSoup()にFileオブジェクトを渡すことで、ハードドライブからHTMLファイルを読み込むこともできます。   
インタラクティブシェルに次のように入力します（example.htmlファイルが作業ディレクトリにあることを確認してください）。

```python
>>> exampleFile = open('example.html')
>>> exampleSoup = bs4.BeautifulSoup(exampleFile)
>>> type(exampleSoup)
<class 'bs4.BeautifulSoup'>
```

BeautifulSoupオブジェクトを取得したら、そのメソッドを使用してHTMLドキュメントの特定の部分を見つけることができます。

## select()メソッドでの要素の検索

BeautifulSoupオブジェクトからWebページ要素を取得するには、select()メソッドを呼び出して、探している要素のCSSセレクタの文字列を渡します。   
セレクタは正規表現に似ています。一般的なテキスト文字列ではなくHTMLページで検索するパターンを指定します。

CSSセレクタ構文の詳細は、このマニュアルの範囲を超えています（http://nostarch.com/automatestuff/ のリソースにセレクタチュートリアルがあります）が、セレクタの簡単な紹介があります。   
以下に、最も一般的なCSSセレクタパターンの例を示します。  

- soup.select('div')
  - すべての `<div>` 要素
- soup.select('#author')
  - `id="author"` な要素
- soup.select('.notice')
  - `class="notice"` な要素
- soup.select('div span')
  - `<div>` 要素内にある `<span>` 要素
- soup.select('div > span')
  - `<div>` 直下にある `<span>` 要素で
- soup.select('input[name]')
  - 任意の値を持つname属性を持つ `<input>` 要素
- soup.select('input[type="button"]')
  - `type="button"` 属性を持つ `<input>` 要素

様々なセレクタパターンを組み合わせて洗練されたマッチを作ることができます。   
たとえば、 `soup.select('p #author')` は、<p>内の、`id="author"` なすべての要素に一致します。  

select()メソッドは、Beautiful SoupがHTML要素を表す方法であるTagオブジェクトのリストを返します。   
このリストには、BeautifulSoupオブジェクトのHTML内のすべての一致に対して1つのTagオブジェクトが含まれます。   
タグ値はstr()関数に渡して、それらが表すHTMLタグを表示することができます。   
タグ値には、タグのすべてのHTML属性を辞書として示すattrs属性もあります。   
前述のexample.htmlファイルを使用して、対話型シェルに次のように入力します。

```python
>>> import bs4
>>> exampleFile = open('example.html')
>>> exampleSoup = bs4.BeautifulSoup(exampleFile.read())
>>> elems = exampleSoup.select('#author')
>>> type(elems)
<class 'list'>
>>> len(elems)
1
>>> type(elems[0])
<class 'bs4.element.Tag'>
>>> elems[0].getText()
'Al Sweigart'
>>> str(elems[0])
'<span id="author">Al Sweigart</span>'
>>> elems[0].attrs
{'id': 'author'}
```

このコードは、例のHTMLから `id="author"` の要素を引き出します。   
`select('#author')` を使用して、`id="author"`のすべての要素のリストを返します。   
このタグオブジェクトのリストを変数elemsに格納し、len（elems）はリストに1つのTagオブジェクトがあることを示します。よって、1つのマッチがあったことを示します。   

要素の getText（）を呼び出すと、要素のテキストまたは内部HTMLが返されます。   
要素のテキストは、開始タグと終了タグの間の内容です。  
この場合、 'Al Sweigart'です。   
要素をstr（）に渡すと、開始タグと終了タグ、および要素のテキストを含む文字列が返されます。   
最後に、attrsは要素の属性 'id'とid属性の値 'author'を持つ辞書を返します。  

また、すべての<p>要素をBeautifulSoupオブジェクトから取得することもできます。   
これをインタラクティブシェルに入力します：

```python
>>> pElems = exampleSoup.select('p')
>>> str(pElems[0])
'<p>Download my <strong>Python</strong> book from <a href="http://
inventwithpython.com">my website</a>.</p>'
>>> pElems[0].getText()
'Download my Python book from my website.'
>>> str(pElems[1])
'<p class="slogan">Learn Python the easy way!</p>'
>>> pElems[1].getText()
'Learn Python the easy way!'
>>> str(pElems[2])
'<p>By <span id="author">Al Sweigart</span></p>'
>>> pElems[2].getText()
'By Al Sweigart'
```

今回は、select（）は3つの一致のリストをpElemsに格納します。   
pElems[0], pElems[1], pElems[2] にstr()を使用すると、各要素が文字列として表示され、各要素でgetText()を使用すると、そのテキストが表示されます。

## 要素の属性からのデータの取得

Tagオブジェクトのget（）メソッドは、要素の属性値に簡単にアクセスできるようにします。   
このメソッドには、属性名の文字列が渡され、その属性の値が返されます。   
example.htmlを使用して、インタラクティブシェルに次のように入力します。

```python
>>> import bs4
>>> soup = bs4.BeautifulSoup(open('example.html'))
>>> spanElem = soup.select('span')[0]
>>> str(spanElem)
'<span id="author">Al Sweigart</span>'
>>> spanElem.get('id')
'author'
>>> spanElem.get('some_nonexistent_addr') == None
True
>>> spanElem.attrs
{'id': 'author'}
```

ここでは、select（）を使用して任意の<span>要素を見つけ、最初に一致した要素をspanElemに格納します。   
get（）に属性名 'id'を渡すと、属性の値 'author'が返されます。

# プロジェクト：「I'm Feeling Lucky」Google検索

Googleでトピックを検索するたびに、一度に1つの検索結果しか表示されません。   
検索結果のリンクを中クリックする（またはCTRLを押しながらクリックする）ことで、後で読むために新しいタブの束の最初のいくつかのリンクを開きます。   
私は、ブラウザを開いたり、トピックを検索したり、いくつかのリンクを1つずつ途中でクリックしたりするこのワークフローが面倒なので、Googleを頻繁に検索します。   
コマンドラインで検索用語を入力するだけで、すべての検索結果が新しいタブでブラウザーを自動的に開くようにすればいいです。 これを行うためのスクリプトを書きましょう。

あなたのプログラムがこれを行います：
- コマンドライン引数から検索キーワードを取得します。
- 検索結果ページを取得します。
- 結果ごとにブラウザタブを開きます。

つまり、コードでは次のことを行う必要があります。

- sys.argvのコマンドライン引数を読んでください。
- リクエストモジュールで検索結果ページを取得します。
- 各検索結果へのリンクを検索します。
- webbrowser.open()関数を呼び出してWebブラウザを開きます。

## ステップ1：コマンドライン引数を取得し、検索ページを要求する

何かをコーディングする前に、まず検索結果ページのURLを知る必要があります。    
Google検索後にブラウザのアドレスバーを見ると、結果ページに https://www.google.com/search?q=SEARCH_TERM_HERE のようなURLがあることがわかります。   
リクエストモジュールはこのページをダウンロードしてから、BeautifulSoup を使用してHTML内の検索結果リンクを見つけることができます。   
最後に、webbrowserモジュールを使用してブラウザタブでそれらのリンクを開きます。

ユーザーは、プログラムを起動するときにコマンドライン引数を使用して検索条件を指定します。   
これらの引数は、sys.argvのリストに文字列として格納されます。

## ステップ2：すべての結果を検索する

ダウンロードしたHTMLからトップ検索結果リンクを抽出するには、Beautiful Soupを使用する必要があります。   
しかし、あなたはどのようにして仕事のための正しいセレクターを見つけますか？   
たとえば、HTML内で気にしないリンクがたくさんあるので、すべての `<a>` タグだけを検索することはできません。   
その代わりに、ブラウザの開発者ツールを使用して検索結果ページを調べ、必要なリンクだけを選択するセレクタを見つけようとする必要があります。

Beautiful SoupのGoogle検索を行った後、ブラウザの開発者ツールを開いて、ページのリンク要素の一部を調べることができます。   
彼らは信じられないほど複雑に見えます。
```html
<a href="/url?sa =t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8& amp;ved=0CCgQFjAA&url=http%3A%2F%2Fwww.crummy.com%2Fsoftware%2FBeautifulSoup %2F&ei=LHBVU_XDD9KVyAShmYDwCw&usg=AFQjCNHAxwplurFOBqg5cehWQEVKi-TuLQ&a mp;sig2=sdZu6WVlBlVSDrwhtworMA" onmousedown="return rwt(this,'','','','1','AFQ jCNHAxwplurFOBqg5cehWQEVKi-TuLQ','sdZu6WVlBlVSDrwhtworMA','0CCgQFjAA','','',ev ent)" data-href="http://www.crummy.com/software/BeautifulSoup/"><em>Beautiful Soup</em>: We called him Tortoise because he taught us.</a>
```

要素が非常に複雑に見えることは重要ではありません。   
あなたは、すべての検索結果リンクが持つパターンを見つける必要があります。   
しかし、この `<a>`要素には、ページ上の非検索結果`<a>`要素と簡単に区別できるものはありません。

`<a>`要素から少し調べると、`<h3 class="r">` のような要素があります。   
残りのHTMLソースを調べると、rクラスは検索結果リンクにのみ使用されるように見えます。   
CSSクラスrが何であるか、それが何であるかを知る必要はありません。   
探している `<a>` 要素のマーカーとして使用するだけです。   
ダウンロードしたページのHTMLテキストからBeautifulSoupオブジェクトを作成し、セレクタ `'.r a'` を使用して、CSSクラス "r" を持つ要素内の<a>要素をすべて見つけることができます。


## ステップ3：各結果のWebブラウザを開く

最後に、結果を得るためにWebブラウザのタブを開くようにプログラムに指示します。

デフォルトでは、webbrowserモジュールを使用して、最初の5つの検索結果を新しいタブで開きます。   
ただし、ユーザーが5つ以下の結果を表示したものを検索した可能性があります。   
soup.select（）呼び出しは、 `'.r a'` セレクタに一致するすべての要素のリストを返します。  
開こうとするタブの数は5か、このリストの長さのいずれか小さい方です。   

組み込みのPython関数min（）は、渡された整数または浮動小数点引数の中で最小のものを返します。   
（渡される最大の引数を返す組み込みのmax（）関数もあります）  
min（）を使用すると、リストに5つ以下のリンクがあるかどうかを調べ、開いているリンクの数を格納できます。  
numOpenという名前の変数 次に、range（numOpen）を呼び出してforループを実行することができます。

ループを繰り返すたびに、webbrowser.open（）を使用してWebブラウザで新しいタブを開きます。   
返される`<a>`要素のhref属性の値には、最初のhttp://google.com の部分が含まれていないため、href属性の文字列値に連結する必要があります。

これで、コマンドラインでPythonプログラミングチュートリアルを実行することで、Pythonプログラミングチュートリアルの最初の5つのGoogle結果を即座に開くことができます。   
（オペレーティングシステムでプログラムを簡単に実行する方法については、付録Bを参照してください）。

## 類似のアイデア

タブブラウズのメリットは、新しいタブで簡単にリンクを開いて後で読むことができることです。   
一度に複数のリンクを自動的に開くプログラムは、以下を行うための素早いショートカットになります。

- Amazonなどのショッピングサイトを検索した後、すべての商品ページを開きます
- 1つの製品のレビューへのリンクをすべて開きます
- FlickrやImgurなどの写真サイトで検索を実行した後、結果リンクを写真に開く

# プロジェクト：すべてのXKCDコミックをダウンロードする

ブログや定期的に更新されているウェブサイトには、通常、最新の投稿が表示されているフロントページと、以前の投稿に移動するためのページ上の[戻る]ボタンがあります。   
そのポストには[前へ]ボタンなどがあり、最新のページからサイトの最初のポストまでの軌跡が作成されます。   
オンラインでないときにサイトのコンテンツのコピーを読みたい場合は、手動で各ページをナビゲートし、それぞれを保存することができます。   
しかし、これはかなり退屈な作業なので、代わりにそれを行うプログラムを作成しましょう。

XKCDは、この構造に適合するウェブサイトを持つ人気のあるオタクWebコムです。   
一番上のページ http://xkcd.com/ には、前の漫画に戻るように案内するPrevボタンがあります。   
手で各コミックをダウンロードするのは永遠になりますが、数分でこれを行うスクリプトを書くことができます。

あなたのプログラムは次のようになります：
- XKCDホームページを読み込みます。
- そのページに漫画の画像を保存します。
- 以前のコミックリンクに従います。
- それが最初の漫画に達するまで繰り返す。

つまり、コードでは次のことを行う必要があります。

- リクエストモジュールを含むページをダウンロードします。
- Beautiful Soupを使ってページの漫画イメージのURLを探します。
- iter_content（）を使用して、コミックイメージをダウンロードしてハードドライブに保存します。
- 前のコミックリンクのURLを見つけ、繰り返します。


## ステップ1：プログラムを設計する

ブラウザのデベロッパーツールを開いてページの要素を調べると、次のようになります：
- コミックのイメージファイルのURLは、`<img>` 要素のhref属性で与えられます。
- `<img>` 要素は `<div id="comic">` 要素の内部にあります。
- Prevボタンにはprevの値を持つ rel HTML属性があります。
- 最初の漫画の前のボタンは http://xkcd.com/# のURLにリンクしており、これ以上前のページがないことを示しています。

値 'http://xkcd.com' で始まり、現在のページの前のリンクのURLで繰り返しforループを更新するurl変数があります。   
ループのすべてのステップで、あなたはURLでコミックをダウンロードします。   
urlが '＃'で終了するときにループを終了することがわかります。

イメージファイルは、xkcdという名前の現在の作業ディレクトリにあるフォルダにダウンロードされます。   os.makedirs()を呼び出すと、このフォルダが存在することが確認され、exist_ok=Trueキーワード引数は、このフォルダがすでに存在する場合に関数が例外をスローするのを防ぎます。   
残りのコードは、プログラムの残りの部分を概説するコメントに過ぎません。

## ステップ2：Webページをダウンロードする

ページをダウンロードするためのコードを実装しましょう。

まず、プログラムがダウンロードしようとしているURLをユーザが知るように、urlを出力します。   
要求モジュールのrequest.get（）関数を使用してダウンロードします。   
いつものように、レスポンスオブジェクトのraise_for_status（）メソッドを呼び出すと、例外がスローされ、ダウンロードに何か問題があった場合にはプログラムを終了します。   
それ以外の場合は、ダウンロードしたページのテキストからBeautifulSoupオブジェクトを作成します。

## ステップ3：漫画イメージを見つけてダウンロードする

コードを次のようにします。

あなたの開発者ツールでXKCDホームページを調べると、漫画画像の `<img>` 要素は、`<div id="comic">` 要素内にあることがわかります。  
セレクタ '#comic img' は、 BeautifulSoupオブジェクトから`<img>`要素を修正してください。

いくつかのXKCDページには、単純なイメージファイルではない特別なコンテンツがあります。   
あなたはそれらをスキップします。   
セレクタが要素を見つけられない場合、soup.select('#comic img') は空白のリストを返します。   
それが起こると、プログラムはエラーメッセージを出力し、画像をダウンロードすることなく移動することができます。

それ以外の場合、セレクタは1つの `<img>` 要素を含むリストを返します。   
この `<img>` 要素からsrc属性を取得し、それをrequests.get()に渡して、漫画の画像ファイルをダウンロードすることができます。

# ステップ4：画像を保存し、以前の漫画を見つける

この時点で、コミックの画像ファイルはres変数に格納されます。   
このイメージデータをハードドライブ上のファイルに書き込む必要があります。

open（）に渡すローカルイメージファイルのファイル名が必要です。   
comicUrlには、 'http://imgs.xkcd.com/comics/heartbleed_explanation.png' のような値があります。  
ファイルパスのように見えるかもしれません。   
実際、comicUrlでos.path.basename（）を呼び出すと、URLの最後の部分である 'heartbleed_explanation.png'が返されます。   
イメージをハードドライブに保存するときにファイル名として使用できます。   
この名前をos.path.join（）を使用してxkcdフォルダの名前に結合すると、プログラムでWindowsでは円記号（¥）、OS XおよびLinuxではスラッシュ（/）が使用されます。   
最終的にファイル名を持つようになったので、open（）を呼び出して新しいファイルを 'wb' "バイナリ書き込み"モードで開くことができます。

この章の前半から、リクエストを使用してダウンロードしたファイルを保存するには、iter_content（）メソッドの戻り値をループする必要があります。   
forループのコードは、イメージデータのチャンク（それぞれ最大100,000バイト）をファイルに書き出し、ファイルを閉じます。   
イメージがハードドライブに保存されるようになりました。

その後セレクタ 'a[rel="prev"]' はrel属性がprevに設定された `<a>` 要素を識別し、この `<a>` 要素のhref属性を使用して以前のコミックのURLを取得できます。   
その後、whileループはこのコミックのダウンロードプロセス全体を再び開始します。

このプログラムを実行するとこんな感じになります。  

```python
Downloading page http://xkcd.com...
Downloading image http://imgs.xkcd.com/comics/phone_alarm.png...
Downloading page http://xkcd.com/1358/...
Downloading image http://imgs.xkcd.com/comics/nro.png...
Downloading page http://xkcd.com/1357/...
Downloading image http://imgs.xkcd.com/comics/free_speech.png...
Downloading page http://xkcd.com/1356/...
Downloading image http://imgs.xkcd.com/comics/orbital_mechanics.png...
Downloading page http://xkcd.com/1355/...
Downloading image http://imgs.xkcd.com/comics/airplane_message.png...
Downloading page http://xkcd.com/1354/...
Downloading image http://imgs.xkcd.com/comics/heartbleed_explanation.png...
--snip--
```

このプロジェクトは、Webから大量のデータを削るためにリンクを自動的にたどるプログラムの良い例です。   
Beautiful Soupのその他の機能については、 http://www.crummy.com/software/BeautifulSoup/bs4/doc/ のドキュメントを参照してください。

## 類似のアイデア
ページをダウンロードしてリンクをたどることは、多くのWebクローリングプログラムの基礎となります。 同様のプログラムでは、次のことも可能です。

- すべてのリンクをたどってサイト全体をバックアップします。
- すべてのメッセージをWebフォーラムからコピーしてください。
- オンラインストアで販売するアイテムのカタログを複製します。

リクエストとBeautifulSoupモジュールは、requests.get（）に渡す必要があるURLを把握できる限り、素晴らしいものです。   
しかし、時々、これは見つけるのが簡単ではない。 あるいは、あなたのプログラムがナビゲートするウェブサイトには、まずログインする必要があります。   
seleniumモジュールは、あなたのプログラムにそのような洗練されたタスクを実行する力を与えます。

# seleniumモジュールでブラウザを制御する

セレンモジュールを使うと、プログラマチックにリンクをクリックしてログイン情報を入力することで、Pythonがブラウザを直接制御できるようになります。  
人間のユーザがページとやりとりしているかのようです。   
Seleniumでは、Requests and Beautiful Soupよりはるかに高度な方法でWebページとやり取りできます。   
しかし、Webブラウザを起動するので、Webからいくつかのファイルをダウンロードするだけで、バックグラウンドで実行するのが少し遅くて難しくなります。

## selenium制御ブラウザの起動

これらの例では、FirefoxのWebブラウザが必要です。   
これはあなたがコントロールするブラウザになります。   
まだFirefoxをお持ちでない場合は、http：//getfirefox.com/から無料でダウンロードできます。

Selenium用のモジュールをインポートするのはややこしいことです。   
`import selenium` の代わりに、`from selenium import webdriver` から実行する必要があります。   
（セレンモジュールがこのように設定されている正確な理由は、この本の範囲を超えています）。  
その後、SeleniumでFirefoxブラウザを起動できます。 対話型シェルに次のように入力します。

```python
>>> from selenium import webdriver
>>> browser = webdriver.Firefox()
>>> type(browser)
<class 'selenium.webdriver.firefox.webdriver.WebDriver'>
>>> browser.get('http://inventwithpython.com')
```

-> Firefox 55.0.3 だと、「geckodriverがない」というエラーになった。  
```
>>> browser = webdriver.Firefox()
〜略〜
selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable needs to be in PATH.
>>>
```
https://github.com/mozilla/geckodriver/releases/tag/v0.18.0  からダウンロードしてきて `/usr/local/bin/` 以下に設置。うごくようになった。  
- 参考: Selenium 3 をPythonで使う http://pc.atsuhiro-me.net/entry/2017/01/15/124308


webdriver.Firefox() が呼び出されると、Firefox Webブラウザが起動します。   
webdriver.Firefox() のtypeをみてみると、WebDriverのデータ型であることがわかります。   
browser.get('http://inventwithpython.com') を呼び出すと、ブラウザは http://inventwithpython.com/ に移動します。

## ページ上の要素の検索

WebDriverオブジェクトには、ページ上の要素を見つけるためのかなりのメソッドがあります。   
それらは、`find_element_*` メソッドと `find_elements_*` メソッドに分かれています。   
find_element_*メソッドは、WebElementオブジェクトを1つ返します。  
このオブジェクトは、クエリと一致するページの最初の要素を表します。   
find_elements_*メソッドは、ページ上の一致するすべての要素のWebElement_*オブジェクトのリストを返します。

下記に、変数ブラウザに格納されているWebDriverオブジェクトで呼び出されるfind_element_*メソッドとfind_elements_*メソッドのいくつかの例を示します。  

- CSSクラス名を使用する要素
  - browser.find_element_by_class_name(name)
  - browser.find_elements_by_class_name(name)

- CSSセレクタに一致する要素
  - browser.find_element_by_css_selector(selector)
  - browser.find_elements_by_css_selector(selector)

- id属性値に一致する要素
  - browser.find_element_by_id(id)
  - browser.find_elements_by_id(id)

- 提供されたテキストと完全に一致する`<a>`要素
  - browser.find_element_by_link_text(text)
  - browser.find_elements_by_link_text(text)

- 提供されたテキストを含む`<a>`要素
  - browser.find_element_by_partial_link_text(text)
  - browser.find_elements_by_partial_link_text(text)

- name属性値に一致する要素
  - browser.find_element_by_name(name)
  - browser.find_elements_by_name(name)

- タグ名が一致する要素（大文字と小文字は区別されず、`<a>` も `<A>` もマッチ）
  - browser.find_element_by_tag_name(name)
  - browser.find_elements_by_tag_name(name)

`*_by_tag_name()`メソッドを除いて、すべてのメソッドの引数は大文字と小文字を区別します。   
メソッドが探しているものと一致する要素がページ上に存在しない場合、セレンモジュールは NoSuchElement 例外を発生させます。   
この例外でプログラムをクラッシュさせたくない場合は、tryとexcept文をコードに追加してください。

WebElementオブジェクトを取得したら、その属性を読んだり、下記のメソッドを呼び出すことで、WebElementオブジェクトについて詳しく知ることができます。  

- tag_name
  - `<a>`要素の 'a'などのタグ名
- get_attribute(name)
  - 要素のname属性の値
- text
  - `<span>hello</span>` の 'hello'のような要素内のテキスト
- clear()
  - テキストフィールドまたはテキストエリアの要素に対しては、入力されたテキストをクリアします
- is_displayed()
  - 要素が表示されている場合はTrueを返します。 それ以外の場合はFalseを返します。
- is_enabled()
  - 入力要素の場合、要素が有効な場合はTrueを返します。 それ以外の場合はFalseを返します。
- is_selected()
  - チェックボックスまたはラジオボタンの要素の場合、要素が選択されている場合はTrueを返します。それ以外の場はFalseを返します。
- location
  - ページ内の要素の位置を示すキー「x」と「y」を持つ辞書

たとえばこんなプログラム。

```python
from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')
try:
    elem = browser.find_element_by_class_name('bookcover')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')
```

ここではFirefoxを開いてURLに転送します。   
このページでは、クラス名が 'bookcover' の要素を見つけようとします。  
そのような要素が見つかった場合は、tag_name属性を使用してタグ名を出力します。   
そのような要素が見つからなければ、別のメッセージを出力します。  

クラス名が「ブックカバー」、タグ名が「img」の要素が見つかりましたので、このプログラムは以下を出力します。
```
Found <img> element with that class name!
```

## ページをクリックする

find_element_*メソッドと find_elements_*メソッドから返されるWebElementオブジェクトには、その要素のマウスクリックをシミュレートするclick（）メソッドがあります。   
このメソッドは、リンクをたどる、ラジオボタンを選択する、送信ボタンをクリックする、または要素がマウスでクリックされたときに発生する可能性のあるその他のものをトリガするために使用できます。   
たとえば、対話型シェルに次のように入力します。

```python
>>> from selenium import webdriver
>>> browser = webdriver.Firefox()
>>> browser.get('http://inventwithpython.com')
>>> linkElem = browser.find_element_by_link_text('Read It Online')
>>> type(linkElem)
<class 'selenium.webdriver.remote.webelement.WebElement'>
>>> linkElem.click() # follows the "Read It Online" link
```

Firefoxがhttp://inventwithpython.com/ を開き、"Read It Online"のテキストを持つ`<a>`要素のWebElementオブジェクトを取得し、その`<a>`要素をクリックすることをシミュレートします。   
あなたが自分でリンクをクリックした場合と同じです。 ブラウザはそのリンクに従います。

## フォームの記入と送信

Webページのテキストフィールドにキーストロークを送信するには、そのテキストフィールドの `<input>` または `<textarea>` 要素を見つけてからsend_keys()メソッドを呼び出します。   
たとえば、対話型シェルに次のように入力します。

```
>>> from selenium import webdriver
>>> browser = webdriver.Firefox()
>>> browser.get('https://mail.yahoo.com')
>>> emailElem = browser.find_element_by_id('login-username')
>>> emailElem.send_keys('not_my_real_email')
>>> passwordElem = browser.find_element_by_id('login-passwd')
>>> passwordElem.send_keys('12345')
>>> passwordElem.submit()
```

この本が公開されて以来、Gmailでユーザー名とパスワードのテキストフィールドのIDが変更されていない限り、前のコードではこれらのテキストフィールドに入力したテキストが入力されます。   
（あなたはいつでもブラウザのインスペクタを使ってidを確認できます）。  
要素のsubmit() メソッドを呼び出すと、要素が入っているフォームのSubmitボタンをクリックしたのと同じ結果になります（emailElem.submit()、そしてコードは同じことをしていました）。

## 特殊キーの送信

Seleniumには、エスケープ文字によく似た、文字列値には入力できないキーボードキー用のモジュールがあります。   
これらの値は、selenium.webdriver.common.keysモジュールの属性に格納されます。   
これは長いモジュール名なので、`from selenium.webdriver.common.keys import Keys` から実行する方がはるかに簡単です。  
そうした場合、通常はselenium.webdriver.common.keysを書く必要がある場所であればどこでもKeysを書くことができます。

以下に、よく使用されるKeys変数を示します。

- Keys.DOWN, Keys.UP, Keys.LEFT, Keys.RIGHT
  - キーボードの矢印キー
- Keys.ENTER, Keys.RETURN
  - ENTERキーとRETURNキー
- Keys.HOME, Keys.END, Keys.PAGE_DOWN, Keys.PAGE_UP
  - homeキー, endキー, pagedownキー, pageupキー
- Keys.ESCAPE, Keys.BACK_SPACE, Keys.DELETE
  - ESCキー, BACKSPACEキー, DELETEキー
- Keys.F1, Keys.F2,..., Keys.F12
  - F1 〜 F12 キー
- Keys.TAB
  - TABキー

たとえば、カーソルが現在テキストフィールドにない場合、HOMEキーとENDキーを押すと、ブラウザがページの上部と下部にそれぞれスクロールします。   
インタラクティブシェルに次のように入力し、send_keys（）がページをスクロールする方法に注意してください。

```python
>>> from selenium import webdriver
>>> from selenium.webdriver.common.keys import Keys
>>> browser = webdriver.Firefox()
>>> browser.get('http://nostarch.com')
>>> htmlElem = browser.find_element_by_tag_name('html')
>>> htmlElem.send_keys(Keys.END)     # scrolls to bottom
>>> htmlElem.send_keys(Keys.HOME)    # scrolls to top
```

`<html>`タグはHTMLファイルのベースタグです。
.HTMLファイルの完全な内容は`<html>`タグと`</html>`タグで囲まれています。   
browser.find_element_by_tag_name('html')を呼び出すと、一般的なWebページにキーを送信するのに適しています。   
たとえば、ページの一番下までスクロールした後に新しいコンテンツが読み込まれた場合などに便利です。

-> うごきませんなあ・・・？

## ブラウザボタンをクリックする

Seleniumは、さまざまなブラウザボタンのクリックを次の方法でシミュレートすることもできます。

- browser.back() : 戻るボタンをクリック
- browser.forward() : 進むボタンをクリック
- browser.refresh() : 再読込ボタンをクリック
- browser.quit() : windowを閉じるボタンをクリック
