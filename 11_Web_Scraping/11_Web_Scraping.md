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
  - すべての <div> 要素
- soup.select('#author')
  - `id="author"` な要素
- soup.select('.notice')
  - `class="notice"` な要素
- soup.select('div span')
  - <div> 要素内にある <span> 要素
- soup.select('div > span')
  - <div> 直下にある <span> 要素で
- soup.select('input[name]')
  - 任意の値を持つname属性を持つ <input> 要素
- soup.select('input[type="button"]')
  - `type="button"` 属性を持つ <input> 要素

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
