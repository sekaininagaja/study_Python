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
現在の作業ディレクトリを `os.getcw()` 関数で文字列値として取得し、`os.chdir()` で変更することができます。

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
