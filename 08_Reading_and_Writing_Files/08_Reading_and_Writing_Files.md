Chapter 8 – Reading and Writing Files
https://automatetheboringstuff.com/chapter8/

# ファイルの読み書き

変数は、プログラムの実行中にデータを保存するうえで便利ですが、プログラムが終了してもデータを保持したい場合は、ファイルに保存する必要があります。  
ファイルの内容は、1ギガバイトのサイズの単一文字列値と考えることができます。  
この章では、Pythonを使用してハードドライブ上のファイルを作成、読み込み、保存する方法を学習します。

# ファイルとファイルパス

ファイルには、ファイル名（通常は1つの単語として書かれます）とパスという2つの重要なプロパティがあります。  
パスは、コンピュータ上のファイルの場所を指定します。  
たとえば、C:\Users\asweigart\Documents というパスに project.docx というファイル名の Windows7ノートパソコンのファイルがあります。  
最後のピリオドの後のファイル名の部分は、ファイルの拡張子と呼ばれ、ファイルの種類を示します。  
project.docx はWord文書で、Users、asweigart、およびDocumentsはすべてフォルダ（ディレクトリとも呼ばれます）を参照します。  
フォルダには、ファイルやその他のフォルダを含めることができます。  
たとえば、project.docxはDocumentsフォルダにあります。
これはasweigartフォルダ内にあり、Usersフォルダ内にあります。

パスの C:\ 部分は、他のすべてのフォルダを含むルートフォルダです。   
Windowsでは、ルートフォルダの名前は C:\ で、Cドライブとも呼ばれます。  
OS XおよびLinuxでは、ルートフォルダは / です。  
この本では、Windows形式のルートフォルダ C:\ を使用します。  
OS XまたはLinuxでインタラクティブシェルの例を入力する場合は、 / を入力します。

DVDドライブやUSBサムドライブなどの追加のボリュームは、異なるオペレーティングシステムでは別々に表示されます。  
Windowsでは、D:\ や E:\ などの新しい文字ドライブとして表示されます。  
OS Xでは、 / Volumesフォルダの下に新しいフォルダとして表示されます。  
Linuxでは、/ mnt（ "mount"）フォルダの下に新しいフォルダとして表示されます。  
また、フォルダ名とファイル名はWindowsとOS Xでは大文字と小文字は区別されませんが、Linuxでは大文字と小文字が区別されます。

## WindowsのバックスラッシュとOS XおよびLinuxのフォワードスラッシュ

Windowsでは、フォルダ名の区切り文字としてバックスラッシュ（\）を使用してパスが書き込まれます。  
ただし、OS XおよびLinuxでは、パス区切り文字としてスラッシュ（/）を使用します。  
すべてのオペレーティングシステムでプログラムを動作させたい場合は、両方の場合を処理するためにPythonスクリプトを作成する必要があります。

幸いにも、これは `os.path.join()`関数を使って簡単に行うことができます。  
パスに個々のファイル名とフォルダ名の文字列値を渡すと、 `os.path.join()`は正しいパス区切り文字を使ってファイルパスの文字列を返します。

```python
>>> import os
>>> os.path.join('usr','bin','spam')
'usr/bin/spam'
```

私はこれらの対話型シェルの例をWindows上で実行していますので、`os.path.join('usr', 'bin', 'spam')` は `'usr\\bin\\spam'` を返しました。  
（各バックスラッシュを別のバックスラッシュ文字でエスケープする必要があるため、バックスラッシュは2倍になります）。  
この関数をOS XまたはLinuxで呼び出した場合、文字列は 'usr/bin/spam'になります。

`os.path.join()`関数は、ファイル名の文字列を作成する必要がある場合に役立ちます。  
これらの文字列は、この章で紹介したいくつかのファイル関連関数に渡されます。  
たとえば、次の例では、ファイル名のリストからフォルダ名の末尾に名前を結合します。

```
>>> for filename in myFiles: \
... print(os.path.join('C:\\Users\\asweight',filename))
...
C:\Users\asweight/accounts.txt
C:\Users\asweight/details.cvs
C:\Users\asweight/invite.docx
```

## 現在の作業ディレクトリ

あなたのコンピュータ上で動作するすべてのプログラムは、現在の作業ディレクトリまたはcwdを持っています。  
ルートフォルダで始まらないファイル名またはパスは、現在の作業ディレクトリの下にあるとみなされます。   
現在の作業ディレクトリを `os.getcwd()` 関数で文字列値として取得し、`os.chdir()` で変更することができます。

```python
>>> import os
>>> os.getcwd()
'/Users/hoge/path/to/dir'
>>> os.chdir('/home')
>>> os.getcwd()
'/home'
```

ここで、現在の作業ディレクトリは C:\Python34 に設定されているので、project.docxというファイル名は C:\Python34\ project.docxを参照しています。  
現在の作業ディレクトリを C:\Windows に変更すると、project.docxは C:\Windows\project.docx と解釈されます。

Pythonは、存在しないディレクトリに変更しようとするとエラーを表示します。

```python
>>> os.chdir('/home/tekitou/dir')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: '/home/tekitou/dir'
```

folderはディレクトリのより現代的な名前ですが、現在の作業ディレクトリ（または単に作業ディレクトリ）は現在の作業フォルダではなく標準用語であることに注意してください。  


## 絶対パスをと相対パス

ファイルパスを指定する方法は2つあります。
- 絶対パス: 常にルートフォルダで始まります
- 相対パス: プログラムの現在の作業ディレクトリを基準とします

ドット（.）とドットドット（..）フォルダもあります。  
これらは実際のフォルダではなく、パスで使用できる特別な名前です。  
フォルダ名の単一のピリオド（.）は、 "this directory"の略語です。  
ピリオド（..）は、 "親フォルダ" を意味します。

相対パスの先頭にある .\ はオプションです。   
たとえば、 .\spam.txt と spam.txt は同じファイルを参照します。

## os.makedirs() で 新しいフォルダをつくる

あなたのプログラムは、`os.makedirs()`関数を使って新しいフォルダ（ディレクトリ）を作成することができます。

```python
>>> import os
>>> os.makedirs('/var/tmp/gomi/sugukeshitene/aaa/bbb/ccc')
```

```python
# 作成前
$ ls -la /var/tmp/gomi/
total 0
drwxr-xr-x  2 hoge  wheel   68  9  2 03:18 .
drwxrwxrwt  8 root  wheel  272  9  2 03:18 ..

# 作成後
$ ls -lR /var/tmp/gomi/
total 0
drwxr-xr-x  3 hoge  wheel  102  9  2 03:21 sugukeshitene

/var/tmp/gomi//sugukeshitene:
total 0
drwxr-xr-x  3 hoge  wheel  102  9  2 03:21 aaa

/var/tmp/gomi//sugukeshitene/aaa:
total 0
drwxr-xr-x  3 hoge  wheel  102  9  2 03:21 bbb

/var/tmp/gomi//sugukeshitene/aaa/bbb:
total 0
drwxr-xr-x  2 hoge  wheel  68  9  2 03:21 ccc

/var/tmp/gomi//sugukeshitene/aaa/bbb/ccc:
```

# os.path モジュール

os.pathモジュールには、ファイル名やファイルパスに関連する多くの便利な機能が含まれています。  
たとえば、 `os.path.join()` を使用して、すべてのオペレーティングシステムで動作する方法でパスを構築したとします。   os.path はosモジュール内のモジュールなので、import osを実行するだけでインポートできます。  
プログラムがファイル、フォルダ、またはファイルパスを処理する必要がある場合は、このセクションの短い例を参照してください。   os.pathモジュールの完全なドキュメントは、PythonのWebサイト（http://docs.python.org/3/library/os.path.html）にあります。

このセクションで続く例のほとんどはosモジュールを必要とするので、あなたが書き込むスクリプトの始めとIDLEを再起動するときはいつもそれをインポートしてください。   
さもなければ、あなたはNameErrorを得るでしょう `NameError: name 'os' is not defined`

## 絶対パスと相対パスの処理

os.pathモジュールは、相対パスの絶対パスを返す関数と、指定されたパスが絶対パスかどうかをチェックする関数を提供します。  

- `os.path.abspath(path)` を呼び出すと、引数の絶対パスの文字列が返されます。  
  これは、相対パスを絶対パスに変換する簡単な方法です。
- `os.path.isabs(path)` を呼び出すと、引数が絶対パスの場合はTrueを返し、相対パスの場合はFalseを返します。
- `os.path.relpath(path, start)` を呼び出すと、開始パスからパスまでの相対パスの文字列が返されます。  
  startが指定されていない場合は、現在の作業ディレクトリが開始パスとして使用されます。

```python
>>> os.path.abspath('.')
'/Users/hoge/path/to/dir'

>>> os.path.abspath('../')
'/Users/hoge/path/to'

>>> os.path.isabs('.')
False

>>> os.path.isabs(os.path.abspath('.'))
True

>>> os.path.relpath('/var/tmp/', '/')
'var/tmp'
>>>
>>> os.path.relpath('/var/tmp/', '/etc')
'../var/tmp'
```

`os.path.dirname(path) `を呼び出すと、path引数の最後のスラッシュの前に来るすべての文字列が返されます。  
`os.path.basename(path)` を呼び出すと、path引数の最後のスラッシュの後に来るすべての文字列が返されます。

```python
>>> path = '/Users/hoge/path/to/dir/hoge.md'

>>> os.path.basename(path)
'hoge.md'

>>> os.path.dirname(path)
'/Users/hoge/path/to/dir'
```

パスのディレクトリ名とベース名が必要な場合は、os.path.split() を呼び出して、次のように2つの文字列でタプル値を取得できます。
`os.path.dirname()` と `os.path.basename()` を呼び出して戻り値をタプルに入れて、同じタプルを作成できることに注意してください。  
しかし、両方の値が必要な場合は、 `os.path.split()` は素敵なショートカットです。

```python
>>> calcFilePath = '/Users/hoge/path/to/dir/hoge.md'

# os.path.split
>>> os.path.split(calcFilePath)
('/Users/hoge/path/to/dir', 'hoge.md')

# os.path.dirname と os.path.basename
>>> (os.path.dirname(calcFilePath), os.path.basename(calcFilePath))
('/Users/hoge/path/to/dir', 'hoge.md')
```

また、`os.path.split()` はファイルパスを取らず、各フォルダの文字列のリストを返します。  
そのためには、`split()` 文字列メソッドを使用し、os.sepの文字列を分割します。  
以前のバージョンから、プログラムを実行するコンピュータのos.sep変数が正しいフォルダ区切りに設定されていることを思い出してください。
OS XおよびLinuxシステムでは、返されるリストの先頭に空白の文字列があります。

```python
# windows
>>> calcFilePath.split(os.path.sep)
['C:', 'Windows', 'System32', 'calc.exe']

# mac, linux
>>> '/usr/bin'.split(os.path.sep)
['', 'usr', 'bin']
```

split()文字列メソッドは、パスの各部分のリストを返すように動作します。  
os.path.sepを渡すと、どのオペレーティングシステムでも動作します。

## ファイルサイズとフォルダの内容の検索

ファイルパスを処理する方法があれば、特定のファイルとフォルダに関する情報の収集を開始できます。  
os.pathモジュールは、バイト単位のファイルのサイズと、指定されたフォルダ内のファイルとフォルダを見つけるための関数を提供します。

- os.path.getsize(path) を呼び出すと、path引数のファイルのサイズがバイト単位で返されます。
- os.listdir(path) を呼び出すと、path引数の各ファイルのファイル名文字列のリストが返されます。  
 （この関数はos.pathにではなく、osモジュールにあることに注意してください。）

```python
>>> os.path.getsize('C:\\Windows\\System32\\calc.exe')
776192
>>> os.listdir('C:\\Windows\\System32')
['0409', '12520437.cpx', '12520850.cpx', '5U877.ax', 'aaclient.dll',
--snip--
'xwtpdui.dll', 'xwtpw32.dll', 'zh-CN', 'zh-HK', 'zh-TW', 'zipfldr.dll']
```

このディレクトリ内のすべてのファイルの合計サイズを調べたい場合は、os.path.getsize() と os.listdir() を一緒に使用できます。

```python
>>> totalSize = 0
>>> for filename in os.listdir('C:\\Windows\\System32'):
      totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))

>>> print(totalSize)
1117846456
```

lsでみたファイルサイズを取ってくるっぽい(?) 実際のファイルサイズとは違いそうだけど・・

```python
>>> os.path.getsize('../.git')
510

# ls
drwxr-xr-x  15 hoge  staff  510  9  2 03:26 .git  <-- ls結果

# duで見たときとちがう
$ du -cs ../.git/
808     ../.git/
```

C:\Windows\System32 フォルダ内の各ファイル名をループすると、totalSize変数は各ファイルのサイズによって増分されます。   
os.path.getsize() を呼び出すと、os.path.join()を使用してフォルダ名を現在のファイル名に結合する方法に注目してください。  
os.path.getsize() が返す整数が totalSizeの値に加算されます。  
すべてのファイルをループした後、totalSizeを表示して、C:\Windows\System32 フォルダの合計サイズを確認します。

## パスの有効性の確認

存在しないパスを指定すると、多くのPython関数がクラッシュし、エラーが発生します。   
os.pathモジュールは、指定されたパスが存在するかどうか、そしてそれがファイルかフォルダかをチェックする関数を提供します。

- `os.path.exists(path)` を呼び出すと、引数で参照されているファイルまたはフォルダが存在する場合はTrueを返し、存在しない場合はFalseを返します。
- `os.path.isfile(path)` を呼び出すと、path引数が存在し、ファイルであればTrueを返し、それ以外の場合はFalseを返します。
- `os.path.isdir(path)` を呼び出すと、path引数が存在し、フォルダであればTrueを返し、それ以外の場合はFalseを返します。

```python
>>> os.path.exists('/var/tmp')
True

>>> os.path.exists('/var/tmp/hoge')
False

>>> os.path.isdir('/var/tmp')
True

>>> os.path.isdir('/etc/hosts')
False

>>> os.path.isfile('/etc/hosts')
True
```

`os.path.exists()` 関数を使用してチェックすることによって、現在コンピュータに接続されているDVDまたはフラッシュドライブがあるかどうかを判断できます。   
たとえば、Windowsコンピュータで D:\ という名前のボリュームでフラッシュドライブを確認する場合は、次のようにして実行できます。

```python
>>> os.path.exists('D:\\')
False
```

おっとっと！ 私は私のフラッシュドライブを接続するのを忘れたように見えます。


# ファイルの読み書きプロセス

フォルダと相対パスを扱うことができれば、読み書きするファイルの場所を指定することができます。  
次のいくつかのセクションで説明する関数は、平文ファイルに適用されます。  
プレーンテキストファイルには、基本的なテキスト文字のみが含まれ、フォント、サイズ、または色情報は含まれません。  
拡張子が .txt のテキストファイルまたは拡張子が .py のPythonスクリプトファイルは、プレーンテキストファイルの例です。  
これらは、Windowsのメモ帳やOS XのTextEditアプリケーションで開くことができます。  
あなたのプログラムは、平文ファイルの内容を簡単に読み取って、普通の文字列値として扱うことができます。

バイナリファイルは、ワープロ文書、PDF、画像、スプレッドシート、実行可能プログラムなどの他のすべてのファイルタイプです。   
メモ帳やテキストエディットでバイナリファイルを開くと、ぐちゃぐちゃなかんじで見えます。

異なる種類のバイナリファイルはすべて独自の方法で処理する必要があるため、このマニュアルでは、生のバイナリファイルを直接読み書きすることはありません。  
幸いにも、多くのモジュールがバイナリファイルを扱いやすくしています。  
この章の後半では、shelveモジュールの1つを調べます。

Pythonでファイルを読み書きするには、3つのステップがあります。

- `open()` 関数を呼び出してFileオブジェクトを返します。
- Fileオブジェクトの `read()` メソッドまたは `write()` メソッドを呼び出します。
- Fileオブジェクトの `close()` メソッドを呼び出して、ファイルを閉じます。

## open() でファイルを開く

open（）関数でファイルを開くには、開くファイルを示す文字列パスを渡します。   
絶対パスまたは相対パスのいずれかになります。 open（）関数はFileオブジェクトを返します。  

メモ帳やテキストエディットを使ってhello.txtという名前のテキストファイルを作成してみてください。   
このテキストファイルの内容として保存し、ユーザーのホームフォルダに保存します。   

```python
# windows
>>> helloFile = open('C:\\Users\\your_home_folder\\hello.txt')

# mac
>>> helloFile = open('/Users/your_home_folder/hello.txt')
```

これらのコマンドはどちらも、ファイルを「読み込み平文」モードで、または読み込みモードを省略して開きます。   
ファイルが読み込みモードで開かれると、Pythonではファイルからのみデータを読み込むことができます。   
どのような方法でも書いたり変更することはできません。   
読み取りモードは、Pythonで開いたファイルのデフォルトモードです。   
しかし、Pythonのデフォルトに依存したくない場合は、文字列値 'r'を第2引数としてopen（）に渡すことで明示的にモードを指定できます。
`open('/Users/asweigart/ hello.txt', 'r') ` と `open('/Users/asweigart/hello.txt')` は同じことをします。

open（）を呼び出すと、Fileオブジェクトが返されます。   
Fileオブジェクトは、コンピュータ上のファイルを表します。   
すでに慣れ親しんでいるリストや辞書と同じように、Pythonの単なる別の型の値です。   
前の例では、変数helloFileにFileオブジェクトを格納していました。   
これで、ファイルを読み書きするときはいつでも、helloFileのFileオブジェクトのメソッドを呼び出すことでファイルを読み書きできます。

## ファイルの内容を読む

Fileオブジェクトを作成したので、Fileオブジェクトから読み込みを開始できます。   
ファイルの内容全体を文字列値として読み取る場合は、Fileオブジェクトのread（）メソッドを使用します。   
helloFileに保存したhello.txtファイルオブジェクトを続けてみましょう。

```python
>>> helloContent = helloFile.read()
>>> helloContent
'Hello World!\n'
```

ファイルの内容を単一の大きな文字列値と考える場合、read（）メソッドはファイルに格納されている文字列を返します。

あるいは、readlines（）メソッドを使用して、ファイルから文字列値のリストを取得することもできます。  
文字列の各行に対して1つの文字列を取得できます。   
たとえば、hello.txtと同じディレクトリにsonnet29.txtという名前のファイルを作成し、次のテキストを書き込みます。

```python
>>> sonnetFile = open('/Users/hoge/sonnet29.txt')
>>> sonnetFile.readlines()
["When, in disgrace with fortune and men's eyes,\n", 'I all alone beweep my outcast state,\n', 'And trouble deaf heaven with my bootless cries,\n', 'And look upon myself and curse my fate,\n']
```

各文字列値はファイルの最後の行を除いて改行文字\ nで終わることに注意してください。   
文字列のリストは、単一の大きな文字列値よりも扱いやすいことがよくあります。

## ファイルへの書き込み

Pythonでは、print（）関数が文字列を画面に書き込む方法と同様に、コンテンツをファイルに書き込むことができます。   
読み込みモードで開いたファイルに書き込むことはできません。   
代わりに、 "平文の書き込み"モードまたは "平文の追加"モードで開くか、書き込みモードと追加モードを省略して開く必要があります。

書き込みモードでは、変数の値を新しい値で上書きするときと同じように、既存のファイルを上書きして最初から開始します。   
書き込みモードでファイルを開くには、open（）の第2引数として 'w'を渡します。   
一方、Appendモードでは、既存のファイルの最後にテキストを追加します。   
変数を上書きするのではなく、変数内のリストに追加すると考えることができます。   
追加モードでファイルを開くには、open（）の第2引数として 'a'を渡します。

open（）に渡されたファイル名が存在しない場合、書き込みモードと追加モードの両方で新しい空のファイルが作成されます。   
ファイルを読み書きした後、ファイルを開く前にclose（）メソッドを呼び出します。

```python
# 読み込みモードでファイル作成、書き込み、閉じる
>>> baconFile = open('bacon.txt','w')
>>> baconFile.write('Hello world!\n')
13
>>> baconFile.close()

# 追記モードで開く、書き込み(追記)、閉じる
>>> baconFile = open('bacon.txt', 'a')
>>> baconFile.write('Bacon is not a vegetable.')
25
>>> baconFile.close()

# 開く、内容をcontentに代入、ファイル閉じる、内容をprint
>>> baconFile = open('bacon.txt')
>>> content = baconFile.read()
>>> baconFile.close()
>>> print(content)
Hello world!
Bacon is not a vegetable.
```

まず、bacon.txtを書き込みモードで開きます。   
まだbacon.txtがないので、Pythonはbacon.txtを作成します。   
開いたファイルに対してwrite（）を呼び出し、write（）に文字列引数 'Hello world！ \n'を渡します。   
ファイルに文字列を書き込み、改行を含めて書き込まれた文字数を返します。 その後、ファイルを閉じます。  

先ほど書き込んだ文字列を置き換えるのではなく、ファイルの既存の内容にテキストを追加するには、ファイルを追加モードで開きます。   
私たちは「ベーコンは野菜ではありません」と書いています。   
ファイルに保存して閉じます。   

最後に、ファイルの内容を画面に表示するために、デフォルトの読み取りモードでファイルを開き、read（）を呼び出して、結果のFileオブジェクトをコンテンツに格納し、ファイルを閉じてコンテンツを印刷します。  

write（）メソッドは、print（）関数のように文字列の末尾に改行文字を自動的に追加しないことに注意してください。   
このキャラクターを自分で追加する必要があります。


# shelveモジュールで変数を保存する

shelveモジュールを使用して、Pythonプログラムの変数をバイナリシェルフファイルに保存することができます。   
これにより、プログラムはハードドライブから変数にデータを復元できます。   
shelveモジュールを使用すると、プログラムに保存機能と開く機能を追加できます。   
たとえば、プログラムを実行していくつかの構成設定を入力した場合、それらの設定をシェルフファイルに保存して、次回の実行時にプログラムにロードさせることができます。

```python
>>> import shelve
>>> shelfFile = shelve.open('mydata')
>>> cats = ['Zophie', 'Pooka', 'Simon']
>>> shelfFile['cats'] = cats
>>> shelfFile.close()
```

shelveモジュールを使用してデータを読み書きするには、まずshelveをインポートします。   
shelve.open（）を呼び出してファイル名を渡し、返されたシェルフ値を変数に格納します。   
シェルフ値を辞書のように変更することができます。   
完了したら、シェルフ値でclose（）を呼び出します。   
ここでは、シェルフ値はshelfFileに格納されます。   
リストcatsを作成し、shelfFile ['cats'] = catsと書いてshelfFileのリストをキー 'cats'に関連付けられた値（辞書のように）として保存します。   
次に、shelfFileでclose（）を呼び出します。

前のコードをWindowsで実行すると、現在の作業ディレクトリにmydata.bak、mydata.dat、およびmydata.dirの3つの新しいファイルが表示されます。   
xOS Xでは、1つのmydata.dbファイルのみが作成されます。

これらのバイナリファイルには、シェルフに保存したデータが含まれています。   
これらのバイナリファイルの形式は重要ではありません。   
あなたは棚モジュールが何をしているかを知る必要があります。   
このモジュールを使用すると、プログラムのデータをファイルに格納する方法を気にする必要がなくなります。

プログラムは、shelveモジュールを使用して、後でこれらのシェルフ・ファイルからデータを再オープンして取り出すことができます。   
シェルフの値は、読み書きモードで開く必要はありません。  
一度開かれると両方のモードを実行できます。

```python
>>> shelfFile = shelve.open('mydata')
>>> type(shelfFile)
<class 'shelve.DbfilenameShelf'>
>>> shelfFile['cats']
['Zophie', 'Pooka', 'Simon']
>>> shelfFile.close()
```

ここでは、データが正しく保存されたことを確認するためにシェルフファイルを開きます。   
shelfFile ['cats']を入力すると、先ほど保存したのと同じリストが返されるので、リストが正しく格納されていることがわかり、close（）を呼び出します。

シェルフ値には辞書と同様にkeys（）とvalues（）メソッドがあり、シェルフのキーと値のリストのような値が返されます。   
これらのメソッドは真のリストの代わりにリストのような値を返すので、list（）関数に渡してリスト形式で取得する必要があります。

```python
>>> shelfFile = shelve.open('mydata')
>>> list(shelfFile.keys())
['cats']
>>> list(shelfFile.values())
[['Zophie', 'Pooka', 'Simon']]
>>> shelfFile.close()
```

プレーンテキストは、メモ帳やテキストエディットなどのテキストエディタで読み込むファイルを作成するのに便利ですが、Pythonプログラムからデータを保存する場合は、shelveモジュールを使用してください。


# pprint.pformat()関数による変数の保存

pprint.printat（）関数はリストやディクショナリの内容を画面に表示するのに対し、pprint.print（）関数は文字列としてこのテキストを返します。   
この文字列は読みやすいようにフォーマットされているだけでなく、構文的に正しいPythonコードでもあります。   
変数に辞書が格納されていて、この変数とその内容を将来の使用のために保存したいとします。   
pprint.pformat（）を使用すると、.pyファイルに書き込むことができる文字列が得られます。   
このファイルは、それに格納されている変数を使用するたびにインポートできる独自のモジュールになります。

```python
>>> import pprint
>>> cats = [{'name':'Zophie','desc':'chubby'},{'name':'Pooka','desc':'fluffy'}]
>>> pprint.pformat(cats)
"[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]"
>>> fileObj = open('myCats.py','w')
>>> fileObj.write('cats =' + pprint.pformat(cats) + '\n')
82
>>> fileObj.close()
```

ここでは、pprintをインポートしてpprint.pformat（）を使用します。   
変数catに格納されている辞書のリストがあります。   
シェルを閉じた後でもネコのリストを利用できるようにするため、pprint.pformat（）を使用して文字列として返します。   
catのデータを文字列として取得したら、文字列をファイルに書き込むのは簡単です。これはmyCats.pyと呼ばれます。

importステートメントがインポートするモジュールは、それ自体が単なるPythonスクリプトです。   
pprint.pformat（）の文字列が.pyファイルに保存されると、ファイルは他のファイルと同じようにインポートできるモジュールになります。

また、Pythonスクリプト自体は.pyファイル拡張子を持つテキストファイルなので、Pythonプログラムは他のPythonプログラムを生成することさえできます。   
これらのファイルをスクリプトにインポートすることができます。

```python
>>> import myCats
>>> myCats.cats
[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]
>>> myCats.cats[0]
{'desc': 'chubby', 'name': 'Zophie'}
>>> myCats.cats[0]['name']
'Zophie'
```

.pyファイルを作成する利点（シェルブモジュールで変数を保存するのではなく）は、テキストファイルであるため、単純なテキストエディタを使用すると誰でもファイルの内容を読み込んで変更することができます。   
ただし、ほとんどのアプリケーションでは、変数をファイルに保存するには、shelveモジュールを使用してデータを保存することをお勧めします。   
整数、浮動小数点数、文字列、リスト、辞書などの基本データ型のみを単純なテキストとしてファイルに書き込むことができます。   
たとえば、ファイルオブジェクトはテキストとしてエンコードすることはできません。

# プロジェクト：ランダムクイズファイルの生成

あなたがクラスの35人の生徒を持つ地理先生で、米国の州都でポップクイズをしたいとします。   
悲しいかな、クラスにはいくつかの悪い卵があり、学生は不正行為をしないように信じることはできません。   
質問の順序をランダムにして、各クイズがユニークなものになるようにして、他の誰かからのベビーベッドの回答を誰にも不可能にします。   
もちろん、これを手作業で行うのは時間がかかり退屈なことになります。   
幸いにも、あなたはPythonを知っています。

プログラムの動作を以下に示します。

- 35の異なるクイズを作成します。
- クイズごとに50の多肢選択問題をランダムな順序で作成します。
- 正解と3つのランダムな間違った答えをランダムな順序で各質問に提供します。
- 35のテキストファイルにクイズを書き込む。
- 35のテキストファイルに解答キーを書き込む。

つまり、コードでは次のことを行う必要があります。

- 州とその首都を辞書に格納する。
- クイズと答えのテキストファイルのopen（）、write（）、close（）を呼び出します。
- random.shuffle（）を使用して、質問の順序と複数選択肢のオプションをランダム化します。

## 手順1：クイズデータを辞書に格納する

最初のステップでは、スケルトンスクリプトを作成し、クイズデータを入力します。   
randomQuizGenerator.pyという名前のファイルを作成ます。

このプログラムではランダムに質問と回答を注文するので、その機能を利用するにはランダムモジュールをインポートする必要があります。   
首都変数には、米国の州をキーとし、その資本を値として持つ辞書が含まれています。   
35個のクイズを作成したいので、クイズと答えのキーファイル（TODOコメントでマークされています）を実際に生成するコードは、forループを35回繰り返すループに入ります。  
（この番号は任意の数のクイズファイルを生成するように変更できます）。

## ステップ2：クイズファイルを作成し、質問の順序をシャッフルする

ループ内のコードは、各クイズごとに1回ずつ35回繰り返されるため、ループ内のクイズは一度に1つだけ心配する必要があります。   
まず、実際のクイズファイルを作成します。   
それは一意のファイル名を持つ必要があり、名前、日付、およびクラス期間を記入するための場所で、標準ヘッダーのいくつかの種類を持っている必要があります。   
次に、状態のリストを無作為の順序で取得する必要があります。  
これは後でクイズの質問と回答を作成するために使用できます。

クイズのファイル名はcapitalsquiz <N> .txtになります。  
ここで<N>はforループのカウンタであるquizNumから来るクイズの一意の番号です。   
capitalsquiz <N> .txtの解答キーは、capitalsquiz_answers <N> .txtというテキストファイルに格納されます。   
ループを通過するたびに、 'capitalsquiz％s.txt'と 'capitalsquiz_answers％s.txt'の％sプレースホルダは（quizNum + 1）に置き換えられるので、作成された最初のクイズとanswerキーはcapitalsquiz1.txtになります。  
capitalsquiz_answers1.txt。   
これらのファイルは、open（）関数を呼び出し、書き込みモードで開くために第2引数として 'w'を使用して作成されます。

quiz_file の write（）ステートメントは、学生が記入するクイズヘッダーを作成します。   
最後に、米国の状態のランダム化されたリストはrandom.shuffle（）関数の助けを借りて作成されます。  
この関数は渡されたリストの値をランダムに並べ替えます。

## ステップ3：回答オプションを作成する

今度は、各質問の回答オプションを生成する必要があります。  
これはAからDまでの複数の選択肢になります。  
もう1つのforループを作成する必要があります。  
これは、クイズの50の質問のそれぞれについてコンテンツを生成するものです。  
そして、各質問に対して複数の選択肢のオプションを生成するために内部にネストされた3番目のforループがあります。 コードを次のようにします。

正解は簡単に入手できます。  
これは大文字辞書の値として格納されています。   
このループは、状態[0]から状態[49]のシャッフル状態リストの状態をループし、各状態を大文字で検索し、その状態の対応する大文字をcorrectAnswerに格納します。

考えられる間違った回答のリストは扱いにくいです。   
大文字辞書のすべての値を複製し、正しい答えを削除して、このリストから3つのランダムな値を選択することによって得ることができます。   
random.sample（）関数を使用すると、この選択を簡単に行うことができます。   
最初の引数は、選択したいリストです。   
2番目の引数は、選択したい値の数です。   
回答オプションの全リストは、これら3つの誤答と正しい回答の組み合わせです。   
最後に、正しい回答が必ずしも選択肢Dではないように、回答を無作為化する必要がある。

## 手順4：クイズと回答キーファイルに内容を書き込む

残されているのは、質問をクイズファイルに書き込むことと、回答キーファイルに答えることだけです。   
コードを次のようにします。

forループは整数0から3を通り、answerOptionsリストに回答オプションを書きます。   
'ABCD' [i]という表現は、文字列 'ABCD'を配列として扱い、ループを通じたそれぞれの反復で 'A'、 'B'、 'C'、そして 'D'を評価します。

最後の行では、answerOptions.index（correctAnswer）という式は、ランダムに順序付けされた回答オプションで正解の整数インデックスを検索し、 'ABCD' [answerOptions.index（correctAnswer）]は、 応答キーファイルに書き込まれます。

プログラムを実行すると、capitalsquiz1.txtファイルがどのように表示されるのですか？  
random.shuffle（）呼び出しの結果に応じて、質問と回答のオプションはここに示されているものと異なる場合があります。

```python
Name:

Date:

Period:

                    State Capitals Quiz (Form 1)

1. What is the capital of West Virginia?
    A. Hartford
    B. Santa Fe
    C. Harrisburg
    D. Charleston

2. What is the capital of Colorado?
    A. Raleigh
    B. Harrisburg
    C. Denver
    D. Lincoln
```

対応するcapitalsquiz_answers1.txtテキストファイルは次のようになります。

```python
1. D
2. C
3. A
4. C
```

-> 下記部分のインデントがずれていたせいでエラーになっていた・・・・・・・
```python
quizFile.close()
answerKeyFile.close()
```
```
Traceback (most recent call last):
  File "randomQuizGenerator.py", line 55, in <module>
    quiz_file.write('%s. What is the capital of %s?\n' % (question_num + 1, states[question_num]))
ValueError: I/O operation on closed file.
```

# プロジェクト：マルチクリップボード

いくつかのテキストフィールドを持つWebページやソフトウェアの多くのフォームに記入するという退屈な作業があるとします。   
クリップボードを使用すると、同じテキストを何度も繰り返し入力する必要がなくなります。   
しかし、クリップボードには一度に1つのことしかできません。   
コピーして貼り付ける必要のあるテキストが複数ある場合は、同じいくつかの項目を繰り返し強調表示してコピーする必要があります。

複数のテキストを追跡するPythonプログラムを書くことができます。   
この "multiclipboard"の名前はmcb.pywとなります（ "multiclipboard"よりも "mcb"の方が短いので）。   
拡張子.pywは、Pythonがこのプログラムを実行するときにターミナルウィンドウを表示しないことを意味します。   
（詳細は、付録Bを参照してください）。

プログラムは、各クリップボードテキストをキーワードの下に保存します。   
たとえば、py mcb.pywを実行してスパムを保存すると、現在のクリップボードの内容はspamというキーワードで保存されます。   
このテキストは、後でpy mcb.pyw spamを実行することで、クリップボードに再度ロードすることができます。   
また、ユーザーが持っているキーワードを忘れた場合は、py mcb.pyw listを実行して、すべてのキーワードのリストをクリップボードにコピーすることができます。

プログラムの内容は次のとおりです。

- キーワードのコマンドライン引数がチェックされます。
- 引数がsaveの場合、クリップボードの内容はキーワードに保存されます。
- 引数がlistの場合、すべてのキーワードがクリップボードにコピーされます。
- それ以外の場合は、キーワードのテキストがクリップボードにコピーされます。

つまり、コードでは次のことを行う必要があります。

- sys.argvのコマンドライン引数を読んでください。
- クリップボードを読み書きします。
- 保存してシェルフファイルに読み込みます。

Windowsを使用している場合は、次の内容のmcb.batという名前のバッチファイルを作成して、このスクリプトを[実行...]ウィンドウから簡単に実行できます。

```python
@pyw.exe C:\Python34\mcb.pyw %*
```

## ステップ1：コメントとシェルフの設定

いくつかのコメントと基本的な設定でスケルトンスクリプトを作ってみましょう。

ファイルの上部に一般的な使用方法の情報をコメントに入れるのが一般的です。   
スクリプトの実行方法を忘れてしまった場合は、これらのコメントを常に確認して通知することができます。   

次にモジュールをインポートします。   
コピー＆ペーストにはpyperclipモジュールが必要です。  
コマンドライン引数を読むにはsysモジュールが必要です。   
シェルブモジュールも便利です：新しいクリップボードテキストを保存するときはいつでも、それをシェルフファイルに保存します。   
次に、ユーザーがテキストをクリップボードに貼り付けたい場合は、シェルフファイルを開いてプログラムにロードし直します。   
シェルフファイルには、接頭辞mcbが付けられます。

## 手順2：クリップボードコンテンツをキーワードで保存する

プログラムは、ユーザーがテキストをキーワードに保存するか、クリップボードにテキストをロードするか、または既存のキーワードをすべて一覧表示するかによって、異なる処理を行います。   
その最初のケースに対処しましょう。

最初のコマンドライン引数（常にsys.argvリストのインデックス1にある）が 'save'の場合、2番目のコマンドライン引数はクリップボードの現在のコンテンツのキーワードです。   
キーワードはmcbShelfのキーとして使用され、値は現在クリップボードにあるテキストになります。  
コマンドライン引数が1つしかない場合は、クリップボードにコンテンツをロードするために、それが 'list'かキーワードのいずれかとみなされます。

## ステップ3：キーワードのリストとキーワードのコンテンツの読み込み

最後に、残りの2つのケースを実装しましょう。  
ユーザーは、キーワードからクリップボードテキストをロードするか、使用可能なすべてのキーワードのリストが必要です。

コマンドライン引数が1つしかない場合は、最初にそれが 'list'であるかどうかチェックしてみましょう。   
その場合、シェルフキーのリストの文字列表現がクリップボードにコピーされます。  
ユーザはこのリストをオープンテキストエディタに貼り付けて読むことができます。

それ以外の場合は、コマンドライン引数がキーワードであると仮定できます。   
このキーワードがキーとしてmcbShelfシェルフに存在する場合は、その値をクリップボードに読み込むことができます。

以上です！ このプログラムを起動するには、コンピュータが使用するオペレーティングシステムによって異なるステップがあります。   
お使いのオペレーティングシステムの詳細については、付録Bを参照してください。

パスワードを辞書に保存した第6章で作成したパスワードロッカープログラムを思い出してください。   
パスワードを更新するには、プログラムのソースコードを変更する必要がありました。   
これは理想的ではありません。平均的なユーザーは、ソフトウェアを更新するためにソースコードを変更するのが快適ではないと感じるからです。   
また、ソースコードをプログラムに変更するたびに、誤って新しいバグが導入される危険性があります。   
プログラムのデータをコードとは別の場所に格納することで、プログラムを他の人が使用しやすくし、バグに強いようにすることができます。

## 悩み

-> 写経してみたが実行の方法がわからない＼(^o^)／   
mcb.bak, mcb.dat, mcb.dir の3ファイルは作成される(サイズ0KB)のだけど、下記のようにしても動かない・・・・・・・・
```
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
```

-> 直接pythonスクリプトを実行する方法だと実行できた。(付録Bのmcb.bat作成する方法でなく)  
mcb.bak, mcb.dat, mcb.dir の3ファイルは「実行する場所」に作成されるみたい。  

```
# コマンドプロンプトにて
> C:\Users\hoge\bin\python_scripts\mcb.bat save aaa
-> "aaa" にクリップボードの内容が保存される。  
カレントディレクトリ以下に、mcb.bak, mcb.dat, mcb.dirの3ファイルが作成される。

> C:\Users\hoge\bin\python_scripts\mcb.bat aaa
-> "aaa" で保存した内容がクリップボードにロードされる

> C:\Users\hoge\bin\python_scripts\mcb.bat list
-> ['aaa', 'bbb', 'ccc'] のかたちで、今までsaveしたキーワードがクリップボードにロードされる
```


# まとめ

ファイルはフォルダ（ディレクトリとも呼ばれます）に編成され、パスはファイルの場所を示します。   
コンピュータ上で実行されているすべてのプログラムには、現在の作業ディレクトリがあります。  
これにより、完全（または絶対）パスを入力するのではなく、現在の場所を基準にファイルパスを指定できます。   os.pathモジュールには、ファイルパスを操作するための多くの関数があります。

あなたのプログラムは、テキストファイルの内容と直接対話することもできます。   
open（）関数は、これらのファイルを開いて内容を大きな文字列（read（）メソッドを使用）として読み取るか、文字列のリスト（readlines（）メソッドを使用）として読み取ることができます。   
open（）関数は、ファイルを書き込みモードまたは追加モードで開いて、新しいテキストファイルを作成したり、既存のテキストファイルに追加したりすることができます。

これまでの章では、クリップボードを使用して、プログラムに大量のテキストを入力するのではなく、すべてを入力していました。  
プログラムでハードドライブから直接ファイルを読み込むことができます。   
クリップボードよりもはるかに揮発性が低い。

次の章では、ファイルをコピーし、削除したり、名前を変更したり、移動したりすることによって、ファイル自体を処理する方法について学習します。

# 練習問題

1. What is a relative path relative to?
- 対象ディレクトリを、今いるディレクトリを基準として指定する

2. What does an absolute path start with?
- 対象ディレクトリを、ルートディレクトリを基準として指定する

3. What do the os.getcwd() and os.chdir() functions do?
- os.getcwd() : 現在の作業ディレクトリを文字列として取得
- os.chdir() : 現在の作業ディレクトリを変更する

4. What are the . and .. folders?
- .: カレントディレクトリ
- ..: 親ディレクトリ

5. In C:\bacon\eggs\spam.txt, which part is the dir name, and which part is the base name?
- dir name: C:\bacon\eggs\
- base name: spam.txt

6. What are the three “mode” arguments that can be passed to the open() function?
- r: 読み込みモード
- w: 書き込みモード
- a: 追記モード

7. What happens if an existing file is opened in write mode?
- 既存のファイルは上書きされる

8. What is the difference between the read() and readlines() methods?
- read(): ファイルの内容を単一の大きな文字列としてとらえる
- readlines(): 文字列の各行に対して1つの文字列を取得する

9. What data structure does a shelf value resemble?
- 辞書データ(key と value がある)

# 練習プロジェクト

## マルチクリップボードの拡張

この章のmultlipboardプログラムを拡張し、delete <keyword>コマンドライン引数を使用して、シェルフからキーワードを削除します。   
次に、すべてのキーワードを削除するdeleteコマンドライン引数を追加します。

-> 下記を追記。  
```python
if sys.argv[1].lower() == 'delete':
    mcb_shelf.clear()
```
mcb.bak, mcb.dir のファイルサイズは0KBになった。mcb.dat は0KB以上でまだ何か入ってるかんじ([]かな？)
```
C:\Users\hoge\bin\python_scripts\mcb.bat list
-> クリップボードに空のリスト [] がロードされる
```

## Mad Libs

テキストファイルを読み込んで、ADJECTIVE、NOUN、ADVERB、またはVERBという単語がテキストファイルに表示されている場所で、ユーザーが自分のテキストを追加できるようにするMad Libsプログラムを作成します。   
たとえば、テキストファイルは次のようになります。

```
The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.
```

プログラムは、これらの出現を見つけ、それらを置き換えるようにユーザに促す。

```
Enter an adjective:
silly
Enter a noun:
chandelier
Enter a verb:
screamed
Enter a noun:
pickup truck
```

次のテキストファイルが作成されます。

```
The silly panda walked to the chandelier and then screamed. A nearby pickup
truck was unaffected by these events.
```

結果は画面に表示され、新しいテキストファイルに保存されます。

## 正規表現の検索

フォルダ内のすべての.txtファイルを開き、ユーザー指定の正規表現に一致する行を検索するプログラムを作成します。   
結果はスクリーンに印刷する必要があります。
