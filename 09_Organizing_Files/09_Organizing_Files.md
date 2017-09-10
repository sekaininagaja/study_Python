Chapter 9 – Organizing Files  
https://automatetheboringstuff.com/chapter9/

# ファイルの整理

前の章では、Pythonで新しいファイルを作成して書き込む方法を学びました。   
お使いのプログラムは、既存のファイルをハードドライブに整理することもできます。   
おそらく、数十、数百、または数千のファイルで構成されたフォルダーを通過し、手作業でそれらのファイルをコピー、名前変更、移動、または圧縮するという経験がありました。   
または、次のようなタスクを検討してください。

- フォルダのすべてのサブフォルダにすべてのPDFファイル（およびPDFファイルのみ）のコピーを作成する
- フォルダ内の spam001.txt, spam002.txt, spam003.txt などの何百ものすべてのファイルのファイル名の先頭のゼロを削除する
- いくつかのフォルダの内容を1つのZIPファイルに圧縮する（簡単なバックアップシステム）

この退屈なものはすべて、Pythonで自動化されているように頼んでいます。   
これらのタスクを実行するようにコンピュータをプログラミングすることで、決して間違いのないクイックワーキングファイルクラッカーに変換することができます。

# シャッターモジュール

shutil モジュールには、Pythonプログラムのファイルのコピー、移動、名前の変更、および削除を可能にする関数があります。   
shutil関数を使用するには、まず `import shutil` を使用する必要があります。

shutil モジュールは、ファイルとフォルダ全体のコピー機能を提供します。
shutil.copy(source, destination) を呼び出すと、パス元のファイルがパス先のフォルダにコピーされます。
destinationがファイル名の場合、コピーされたファイルの新しい名前として使用されます。   
この関数は、コピーされたファイルのパスの文字列を返します。  

```python
>>> import shutil, os

# コピー先としてフォルダを指定。-> 同じ名前のファイルがコピーされる
>>> os.chdir('C:\\')
>>> shutil.copy('C:\\spam.txt', 'C:\\delicious')
'C:\\delicious\\spam.txt'

# リネームしてコピーする
>>> shutil.copy('eggs.txt', 'C:\\delicious\\eggs2.txt')
'C:\\delicious\\eggs2.txt'
```

最初のshutil.copy() は、C:\spam.txt のファイルをC:\delicious フォルダにコピーします。   
戻り値は、新しくコピーされたファイルのパスです。   
コピー先としてフォルダが指定されているため、元のspam.txtファイル名はコピーされた新しいファイルのファイル名に使用されます。   
2番目のshutil.copy() は、C:\eggs.txt にあるファイルを C:\delicious にコピーしますが、コピーしたファイルにはeggs2.txtという名前を付けます。

shutil.copy() は1つのファイルをコピーしますが、shutil.copytree() はフォルダ全体とそこに含まれるすべてのフォルダとファイルをコピーします。   
shutil.copytree(source, destination) を呼び出すと、パスソースのフォルダとそのすべてのファイルとサブフォルダがパス先のフォルダにコピーされます。   
sourceパラメータとdestinationパラメータは両方とも文字列です。   
この関数は、コピーしたフォルダのパスの文字列を返します。

```python
# ディレクトリのコピー
>>> import shutil, os
>>> os.chdir('C:\\')
>>> shutil.copytree('C:\\bacon', 'C:\\bacon_backup')
'C:\\bacon_backup'
```

shutil.copytree() を呼び出すと、オリジナルのbaconフォルダと同じ内容のbacon_backupという名前の新しいフォルダが作成されます。   
貴重な貴重なベーコンを安全にバックアップしました。

## ファイルとフォルダの移動と名前の変更

shutil.move(source, destination) を呼び出すと、パス元のファイルまたはフォルダがパス先に移動し、新しい場所の絶対パスの文字列が返されます。  
宛先がフォルダを指す場合、ソースファイルは宛先に移動し、現在のファイル名を保持します。   

```python
>>> import shutil
>>> shutil.move('C:\\bacon.txt', 'C:\\eggs')
'C:\\eggs\\bacon.txt'
```

C:\\eggs というディレクトリが存在する場合、このshutil.move()呼び出しでは、C:\\bacon.txt を C:\\eggs\ 以下に移動します。  

すでに C:\eggs に bacon.txt ファイルがあった場合は、上書きされていました。  
この方法でファイルを誤って上書きするのは簡単なので、move() を使用するときは注意が必要です。

-> [メモ] あれー？？  `already exists` って出るな。
```
shutil.Error: Destination path '/Users/pat/to/dir/hoge.txt' already exists
```

宛先パスは、ファイル名を指定することもできます。 次の例では、ソースファイルが移動され、名前が変更されます。
```python
>>> shutil.move('C:\\bacon.txt', 'C:\\eggs\\new_bacon.txt')
'C:\\eggs\\new_bacon.txt'
```

前の両方の例は、C:\\eggs\ ディレクトリが存在することを前提として動作していました。   
しかし、eggsフォルダがない場合、move() はbacon.txtの名前を eggs という名前に変更します。

```python
# bacon.txt が eggs という名前になる
>>> shutil.move('C:\\bacon.txt', 'C:\\eggs')
'C:\\eggs'
```

ここでは、move() は C:\\eggs フォルダを見つけることができないので、2番目の引数はフォルダではなくファイル名であると想定します。   
したがって、bacon.txtのテキストファイルは、eggsというファイル（.txtファイル拡張子のないテキストファイル）に変更されました。  
おそらくあなたが望むものではありません。 move()コールは、あなたが期待していたものとはかなり異なるものを喜んで行うことができるので、あなたのプログラムでは難しいバグかもしれません。   
これは、move()を使用するときに注意するもう一つの理由です。

最後に、デスティネーションを構成するフォルダが既に存在していなければなりません。  
そうしないと、Pythonは例外をスローします。

```python
>>> shutil.move('spam.txt', 'c:\\does_not_exist\\eggs\\ham')
Traceback (most recent call last):
  File "C:\Python34\lib\shutil.py", line 521, in move
    os.rename(src, real_dst)
FileNotFoundError: [WinError 3] The system cannot find the path specified:
'spam.txt' -> 'c:\\does_not_exist\\eggs\\ham'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    shutil.move('spam.txt', 'c:\\does_not_exist\\eggs\\ham')
  File "C:\Python34\lib\shutil.py", line 533, in move
    copy2(src, real_dst)
  File "C:\Python34\lib\shutil.py", line 244, in copy2
    copyfile(src, dst, follow_symlinks=follow_symlinks)
  File "C:\Python34\lib\shutil.py", line 108, in copyfile
    with open(dst, 'wb') as fdst:
FileNotFoundError: [Errno 2] No such file or directory: 'c:\\does_not_exist\\
eggs\\ham'
```

Pythonは、ディレクトリ does_not_exist の中で eggs と ham を探します。   
存在しないディレクトリが見つからないため、指定したパスにspam.txtを移動することはできません。

## ファイルとフォルダを永久に削除する

osモジュール内の関数を持つ単一のファイルまたは空の単一のフォルダを削除できますが、フォルダとそのすべての内容を削除するには、shutilモジュールを使用します。  

- os.unlink(path) を呼び出すと、pathにあるファイルが削除されます。
- os.rmdir(path) を呼び出すと、pathのフォルダが削除されます。 このフォルダは、ファイルまたはフォルダが空である必要があります。
- shutil.rmtree(path) を呼び出すと、パスにあるフォルダが削除され、そこに含まれるすべてのファイルとフォルダも削除されます。 **危険取扱い注意**

あなたのプログラムでこれらの関数を使うときは注意してください！   
これらの呼び出しがコメントアウトされた状態でプログラムを実行し、削除されるファイルを表示するprint()呼び出しを追加することは、しばしば良い考えです。   
以下は.txtファイル拡張子を持つファイルを削除することを目的としたPythonプログラムですが、代わりに.rxtファイルを削除するようなタイプミス（太字で強調表示）があります：

```python
import os
for filename in os.listdir():
    if filename.endswith('.rxt'):
        os.unlink(filename)
```

.rxtで終わる重要なファイルがあった場合、それらは誤って永久に削除されてしまいます。   
代わりに、まず次のようにプログラムを実行する必要があります。

```python
import os
for filename in os.listdir():
    if filename.endswith('.rxt'):
        #os.unlink(filename)
        print(filename)
```

今os.unlink()呼び出しはコメントされているので、Pythonはそれを無視します。   
代わりに、削除されるファイルのファイル名が表示されます。   
最初にこのバージョンのプログラムを実行すると、間違って.txtファイルの代わりに.rxtファイルを削除するようプログラムに指示したことが示されます。

プログラムが意図したとおりに動作したら、print(filename)行を削除し、os.unlink(filename)行のコメントを外します。  
次に、プログラムを再度実行して、ファイルを実際に削除します。

## send2trashモジュールによる安全な削除

Pythonに組み込まれているshutil.rmtree()関数は、ファイルやフォルダを不可逆的に削除するので、危険です。   
サードパーティのsend2trashモジュールを使用すると、ファイルやフォルダを削除する方がはるかに優れています。   
このモジュールは、ターミナルウィンドウから `pip install send2trash` を実行することでインストールできます。   
サードパーティのモジュールをインストールする方法の詳細については、付録Aを参照してください。

send2trashを使用すると、Pythonの通常の削除機能よりも安全です。  
フォルダやファイルをコンピュータのごみ箱やごみ箱に永久に削除する代わりに送信するからです。   
あなたのプログラムのバグがあなたが削除しようとしていなかったsend2trashで何かを削除した場合、後でそれをごみ箱から復元することができます。

```python
>>> import send2trash
>>> baconFile = open('bacon.txt', 'a') # creates the file
>>> baconFile.write('Bacon is not a vegetable.')
25
>>> baconFile.close()
>>> send2trash.send2trash('bacon.txt')
```

一般に、ファイルとフォルダを削除するには、常にsend2trash.send2trash()関数を使用する必要があります。   
しかし、ごみ箱にファイルを送信すると後で復元することができますが、永久に削除するようなディスク容量を解放することはありません。  
プログラムでディスク領域を解放するには、osおよびshutil関数を使用してファイルとフォルダを削除します。  
send2trash()関数はごみ箱にのみファイルを送信できることに注意してください。   
ファイルをそこから引き出すことはできません。

## ディレクトリツリーのあるきかた

あるフォルダ内のすべてのファイルと、そのフォルダのすべてのサブフォルダ内のすべてのファイルの名前を変更したいとします。   
つまり、ディレクトリツリー全体を歩き回りながら、各ファイルに触れたいとします。   
これを行うためのプログラムを書くことは難しいかもしれません。   
幸いにも、Pythonはこのプロセスを処理する関数を提供します。

os.walk()関数を使用するプログラムの例を次に示します。

```python
import os

for folderName, subfolders, filenames in os.walk('C:\\delicious'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)

    print('')
```

os.walk()関数には、単一の文字列値、つまりフォルダのパスが渡されます。   
forループステートメントでos.walk()を使用すると、range()関数を使用してある範囲の数値をどのように扱うかと同じように、ディレクトリツリーを歩くことができます。   
range()とは異なり、os.walk()関数は、ループを通る各繰り返しで3つの値を返します。  

- 現在のフォルダ名
- 現在のフォルダ内にあるフォルダのリスト
- 現在のフォルダ内にあるファイルのリスト

現在のフォルダでは、forループの現在の繰り返しのフォルダを意味します。    
プログラムの現在の作業ディレクトリはos.walk()によって変更されません。

`for i in range(10):` で変数名iを選択できるのと同様に、前述の3つの値の変数名を選択することもできます。   
私は通常、foldername, subfolders, filenames という名前を使用します。  
このプログラムを実行すると、次のように出力されます。

```python
The current folder is C:\delicious
SUBFOLDER OF C:\delicious: cats
SUBFOLDER OF C:\delicious: walnut
FILE INSIDE C:\delicious: spam.txt

The current folder is C:\delicious\cats
FILE INSIDE C:\delicious\cats: catnames.txt
FILE INSIDE C:\delicious\cats: zophie.jpg

The current folder is C:\delicious\walnut
SUBFOLDER OF C:\delicious\walnut: waffles

The current folder is C:\delicious\walnut\waffles
FILE INSIDE C:\delicious\walnut\waffles: butter.txt.
```

os.walk()は、サブフォルダとファイル名変数の文字列のリストを返すので、これらのリストを独自のforループで使用することができます。   
print()関数呼び出しを独自のカスタムコードで置き換えます。   
（またはどちらか一方または両方が必要ない場合は、forループを削除してください）。

# zipfileモジュールによるファイルの圧縮

他の多くのファイルの圧縮された内容を保持できるZIPファイル（拡張子が.zipのファイル）に精通しているかもしれません。   
ファイルを圧縮するとサイズが小さくなり、インターネット経由で転送するときに便利です。   
また、ZIPファイルには複数のファイルとサブフォルダも含めることができるので、複数のファイルを1つにまとめる便利な方法です。   
アーカイブファイルと呼ばれるこの1つのファイルは、例えば、電子メールに添付することができます。  
あなたのPythonプログラムは、zipfileモジュール内の関数を使ってZIPファイルを作成したり開いたりすることができます。  

## ZIPファイルの読み取り

ZIPファイルの内容を読み込むには、まずZipFileオブジェクトを作成する必要があります（大文字のZとFに注意してください）。   
ZipFileオブジェクトは、前章のopen()関数によって返されたFileオブジェクトと概念的に似ています。  
これらは、プログラムがファイルとやり取りするときの値です。   
ZipFileオブジェクトを作成するには、zipfile.ZipFile()関数を呼び出して、.zipファイルのファイル名の文字列を渡します。   
zipfileはPythonモジュールの名前で、ZipFile()は関数の名前です。

```python
>>> import zipfile, os
>>> os.chdir('C:\\')    # move to the folder with example.zip
>>> exampleZip = zipfile.ZipFile('example.zip')
>>> exampleZip.namelist()
['spam.txt', 'cats/', 'cats/catnames.txt', 'cats/zophie.jpg']
>>> spamInfo = exampleZip.getinfo('spam.txt')
>>> spamInfo.file_size
13908
>>> spamInfo.compress_size
3828

# 元のファイルサイズを圧縮ファイルサイズで割ってexample.zipを圧縮する効率を計算し、％sでフォーマットされた文字列を使用してこの情報を出力する
>>> 'Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo
.compress_size, 2))
'Compressed file is 3.63x smaller!'
>>> exampleZip.close()
```

ZipFileオブジェクトには、ZIPファイルに含まれるすべてのファイルとフォルダの文字列のリストを返すnamelist()メソッドがあります。   
これらの文字列は、getinfo()ZipFile メソッドに渡して、その特定のファイルに関するZipInfoオブジェクトを返すことができます。   
ZipInfoオブジェクトには、それぞれ元のファイルサイズと圧縮ファイルサイズの整数を保持する file_sizeや compress_size などの独自の属性があります。   
ZipFileオブジェクトはアーカイブファイル全体を表しますが、ZipInfoオブジェクトはアーカイブ内の単一ファイルに関する有益な情報を保持します。

## ZIPファイルからの抽出

ZipFileオブジェクトの extractall()メソッドは、すべてのファイルとフォルダをZIPファイルから現在の作業ディレクトリに抽出します。  

このコードを実行すると、example.zip の内容が C:\ に抽出されます。   
オプションで、現在の作業ディレクトリ以外のフォルダにファイルを展開するために、extractall() にフォルダ名を渡すことができます。  
extractall()メソッドに渡されたフォルダが存在しない場合は作成されます。   
たとえば、呼び出しを `exampleZip.extractall('C:\\delicious')` に置き換えた場合、コードは example.zip から新しく作成された C:\delicious フォルダにファイルを抽出します。

ZipFileオブジェクトのextract()メソッドは、ZIPファイルから単一のファイルを抽出します。   
インタラクティブシェルの例を続けます。

```python
>>> exampleZip.extract('spam.txt')
'C:\\spam.txt'
>>> exampleZip.extract('spam.txt', 'C:\\some\\new\\folders')
'C:\\some\\new\\folders\\spam.txt'
>>> exampleZip.close()
```

extract()に渡す文字列は、namelist()によって返されたリスト内の文字列のいずれかと一致しなければなりません。   
必要に応じて、extract()に2番目の引数を渡して、ファイルを現在の作業ディレクトリ以外のフォルダに抽出することができます。   
この2番目の引数がまだ存在しない場合、Pythonはそのフォルダを作成します。   
extract()が返す値は、ファイルが抽出された絶対パスです。

## ZIPファイルの作成と追加

独自の圧縮ZIPファイルを作成するには、第2引数として 'w'を渡して、書き込みモードでZipFileオブジェクトを開く必要があります。   
（これは、open（）関数に 'w'を渡してテキストファイルを書込みモードで開くのと同じです。）

ZipFileオブジェクトの write（）メソッドにパスを渡すと、Pythonはそのパスのファイルを圧縮し、ZIPファイルに追加します。   
write（）メソッドの最初の引数は、追加するファイル名の文字列です。   
2番目の引数は圧縮タイプのパラメータで、ファイルを圧縮するためにどのアルゴリズムを使うべきかをコンピュータに指示します。   
この値を常にzipfile.ZIP_DEFLATEDに設定することができます。   
（これは、すべてのタイプのデータでうまく動作するデフレート圧縮アルゴリズムを指定します。）

```python
>>> import zipfile
>>> newZip = zipfile.ZipFile('new.zip', 'w')
>>> newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
>>> newZip.close()
```

このコードはspam.txtの圧縮された内容を持つnew.zipという名前の新しいZIPファイルを作成します。  
ファイルへの書き込みと同様に、書き込みモードはZIPファイルの既存の内容をすべて消去します。   
既存のZIPファイルにファイルを追加するだけの場合は、zipfile.ZipFile() に2番目の引数として 'a'を渡して、追加モードでZIPファイルを開きます。

# プロジェクト：アメリカスタイルの日付からヨーロッパスタイルの日付にファイルの名前を変更する

あなたの上司がアメリカンスタイルの日付（MM-DD-YYYY）の名前のファイルを何千もの電子メールで送信し、ヨーロッパスタイルの日付（DD-MM-YYYY）に名前を変更する必要があるとします。   
この退屈な仕事は一日中手で行うことができます！   
その代わりにそれを行うプログラムを書こう。

プログラムの内容は次のとおりです。
- 現在の作業ディレクトリ内のすべてのファイル名をアメリカスタイルの日付で検索します。
- ファイルが見つかると、月と日をスワップしてファイルの名前を変更し、ヨーロッパ風にします。

つまり、コードでは次のことを行う必要があります。
- アメリカ式の日付のテキストパターンを識別できる正規表現を作成します。
- os.listdir() を呼び出すと、作業ディレクトリ内のすべてのファイルが検索されます。
- 正規表現を使って日付があるかどうかを確認するために、各ファイル名をループします。
- 日付がある場合は、ファイルの名前をshutil.move()に変更します。

## ステップ1：アメリカ式日付の正規表現を作成する

プログラムの最初の部分では、必要なモジュールをインポートし、MM-DD-YYYYの日付を識別できる正規表現を作成する必要があります。   
TODOのコメントは、このプログラムに書き込むために残されていることを思い出させます。   
TODOと入力すると、IDLEのCTRL-F検索機能を使用して簡単に見つけることができます。

この章では、ファイルの名前を変更するためにshutil.move() 関数を使用することができます。  
引数は、名前を変更するファイルの名前と新しいファイル名です。   
この機能はshutilモジュールに存在するため、そのモジュールをインポートする必要があります。

しかし、ファイルの名前を変更する前に、名前を変更するファイルを特定する必要があります。   
spam4-4-1984.txt や 01-03-2014eggs.zip などの日付のファイル名は、名前を変更する必要がありますが、littlebrother.epub などの日付のないファイル名は無視してください。

正規表現を使用してこのパターンを識別できます。   
reモジュールを一番上にインポートした後、re.compile（）を呼び出してRegexオブジェクトを作成します。   re.VERBOSEを2番目の引数に渡すと、正規表現文字列の空白とコメントが読みやすくなります。

この正規表現では、4-31-2014, 2-29-2013、0-15-2014 などの無効な日付を受け取ります。  
日付は見逃しやすい特殊なケースがたくさんありますが、簡単なケースでこのプログラムの正規表現は十分に機能するので今回はこれでいく。  

1885年は有効な年ですが、20年または21世紀には何年も探しているだけです。   
これにより、あなたのプログラムは、非日付のファイル名と日付のような形式（10-10-1000.txtなど）との間違いを防ぐことができます。

## 手順2：ファイル名から日付部分を特定する

次に、プログラムは os.listdir（）から返されたファイル名の文字列のリストをループし、それらを正規表現と照合する必要があります。   
日付が付いていないファイルはスキップする必要があります。   
日付を持つファイル名の場合、一致するテキストは複数の変数に格納されます。   
次のコードを使用して、プログラムの最初の3つのTODOを入力します。

search（）メソッドから返されたMatchオブジェクトがNone❶の場合、amerFilenameのファイル名は正規表現と一致しません。   
continueステートメント❷は、残りのループをスキップし、次のファイル名に移動します。

それ以外の場合は、正規表現グループに一致するさまざまな文字列がbeforePart、monthPart、dayPart、yearPart、およびafterPart❸という名前の変数に格納されます。   
これらの変数の文字列は、次のステップでヨーロッパスタイルのファイル名を形成するために使用されます。

グループ番号をまっすぐに保つには、最初から正規表現を読み、開きかっこが出現するたびにカウントアップしてください。   
コードを考えずに、正規表現の概要を書くだけです。   
これは、グループを視覚化するのに役立ちます。

```python
# グループNoの対応
date_pattern = re.compile(r"""^(.*?) # 「日付」前のすべてのテキスト
    ((0|1)?\d)-     # "01～09月" or "10～12月"
    ((0|1|2|3)?\d)- # "01～09日" or "10～19日" or "20～29日" or "30～31日"
    ((19|20)\d\d)   # "19XX年" or "20XX年"
    (.*?)$          # 「日付」後のすべてのテキスト
    """, re.VERBOSE)

datePattern = re.compile(r"""^(グループ1) # all text before the date
    (グループ2 (グループ3) )-                     # one or two digits for the month
    (グループ4 (グループ5) )-                     # one or two digits for the day
    (グループ6 (グループ7) )                      # four digits for the year
    (グループ8)$                          # all text after the date
    """, re.VERBOSE)
```

ここで、番号1〜8は、作成した正規表現のグループを表します。   
カッコとグループ番号だけで正規表現の概要を作ることで、プログラムの残りの部分に進む前に、あなたの正規表現をはっきりと理解することができます。

## 手順3：新しいファイル名を作成してファイル名を変更する

最後のステップとして、前のステップで作成した変数の文字列をヨーロッパスタイルの日付に連結します。  
日付は月の前に来ます。

連結された文字列をeuroFilenameという名前の変数に格納します。   
次に、amerFilenameの元のファイル名と新しいeuroFilename変数をshutil.move()関数に渡して、ファイル名を❸に変更します。

このプログラムでは、shutil.move（）呼び出しがコメントアウトされ、代わりにファイル名が変更されます。   
最初にこのようなプログラムを実行すると、ファイルの名前が正しく変更されたかどうかを再確認できます。  
次に、shutil.move（）の呼び出しをコメント解除し、プログラムを再度実行してファイルの実際の名前を変更することができます。

## 類似のアイデア

多数のファイルの名前を変更する理由は他にもたくさんあります。

- ファイル名の先頭にプレフィックスを追加するには (eggs.txt の名前を spam_eggs.txt に変更するために spam_ を追加するなど)
- ヨーロッパスタイルの日付をアメリカスタイルの日付に変更する
- spam0042.txt などのファイルからゼロを削除する

# プロジェクト：ZIPファイルへのフォルダのバックアップ

ファイルを C:\AlsPythonBook という名前のフォルダに保存しているプロジェクトで作業しているとします。   
作業を失うことに心配しているので、フォルダ全体のZIPファイル「スナップショット」を作成したいと考えています。   
異なるバージョンを使用したいので、ZIPファイルのファイル名を増分する必要があります。   
たとえば、AlsPythonBook_1.zip、AlsPythonBook_2.zip、AlsPythonBook_3.zipなどがあります。   
あなたは手でこれを行うことができますが、それはむしろ迷惑であり、誤ってZIPファイルの名前を誤って数えてしまうかもしれません。   
この退屈な仕事をするプログラムを実行する方がずっと簡単です。

## ステップ1：ZIPファイルの名前を調べる

このプログラムのコードは、backupToZip() という名前の関数に配置されます。   
これにより、この機能を必要とする他のPythonプログラムに関数をコピー＆ペーストするのが簡単になります。   
プログラムの最後に、関数を呼び出してバックアップを実行します。

1つのパラメータfolderのみを使用する backup_to_zip()関数を定義します。   
このパラメータは、内容をバックアップするフォルダへの文字列パスです。   
この関数は、作成するZIPファイルに使用するファイル名を決定します。   
この関数はファイルを作成し、フォルダフォルダを歩み、各サブフォルダとファイルをZIPファイルに追加します。   
これらのステップのTODOコメントをソースコードに書き込んで、後でそれを思い出させる❹。

最初の部分は、ZIPファイルの名前で、フォルダの絶対パスのベース名を使用します。   
バックアップするフォルダが C:\delicious の場合、ZIPファイルの名前は delicious_N.zip でなければなりません。  
N = 1はプログラムを初めて実行し、N = 2は2回目のように続きます。

delicious_1.zip がすでに存在するかどうかを確認し、delicious_2.zip がすでに存在するかどうかを確認するなどして、Nが何であるべきかを判断できます。   
N にはnumberという名前の変数を使用し、os.path.exists() を呼び出すループ内でインクリメントして、ファイルが存在するかどうかをチェックします。   
最初に存在しないファイル名が見つかると、新しいzipのファイル名が見つかるため、ループが中断されます。


## 手順2：新しいZIPファイルを作成する

次に、ZIPファイルを作成しましょう。

新しいZIPファイルの名前がzipFilename変数に格納されたので、zipfile.ZipFile()を呼び出して実際にZIPファイルを作成することができます。   
ZIPファイルが書き込みモードで開かれるように、第2引数として 'w'を渡してください。

## 手順3：ディレクトリツリーを移動してZIPファイルに追加する

これで、os.walk()関数を使用して、フォルダ内のすべてのファイルとそのサブフォルダをリストする作業を行う必要があります。

forループの中で os.walk（）を使うことができます。  
そして、各反復で、反復の現在のフォルダ名、そのフォルダ内のサブフォルダ、およびそのフォルダ内のファイル名を返します。

forループでは、フォルダがZIPファイルに追加されます。   
ネストされたforループは、ファイル名リストの各ファイル名を通過できます。   
以前に作成されたバックアップZIPを除いて、それぞれがZIPファイルに追加されます。

このプログラムを実行すると、次のような出力が生成されます。

```
Creating delicious_1.zip...
Adding files in C:\delicious...
Adding files in C:\delicious\cats...
Adding files in C:\delicious\waffles...
Adding files in C:\delicious\walnut...
Adding files in C:\delicious\walnut\waffles...
Done.
```

2回目に実行すると、C:\delicious のすべてのファイルが delicious_2.zip という名前のZIPファイルに格納されます。

## 類似のアイデア

ディレクトリツリーを歩いて、いくつかの他のプログラムで圧縮ZIPアーカイブにファイルを追加することができます。   
たとえば、次のようなプログラムを記述することができます。

- ディレクトリツリーを走査して .txt や .py などの特定の拡張子を持つファイルだけをアーカイブする
- ディレクトリツリーを走査して .txt と .py 以外のすべてのファイルをアーカイブする
- ディレクトリツリー内で、最も多くのファイルを持つフォルダ、または最も多くのディスクスペースを使用するフォルダを探す

# まとめ

経験豊かなコンピュータユーザーであっても、マウスやキーボードを使用して手動でファイルを処理することがあります。   
現代のファイルエクスプローラでは、いくつかのファイルで簡単に作業できます。   
しかし、コンピュータのファイルエクスプローラを使って何時間もかかる作業を実行する必要があることがあります。

osおよびshutilモジュールは、ファイルのコピー、移動、名前の変更、および削除のための機能を提供します。   
ファイルを削除するときはファイルを永久に削除するのではなく、send2trashモジュールを使用してごみ箱に移動するのがベター。   
また、ファイルを扱うプログラムを書くときは、実際のコピー/移動/名前の変更/削除を行うコードをコメントアウトしてprint()であらかじめ確認しておくのがおすすめ。

これらの操作は、あるフォルダ内のファイルだけでなく、そのフォルダ内のすべてのフォルダ、それらのフォルダ内のすべてのフォルダなどでも実行する必要があります。   
os.walk()関数は、このトレックをフォルダ間で処理します。  
そのため、プログラムがファイル内のファイルで行う必要があることに集中することができます。  

zipfileモジュールは、Pythonを介して.zipアーカイブ内のファイルを圧縮および抽出する方法を提供します。   
osとshutilのファイル処理機能と組み合わせることで、zipfileはハードドライブのどこからでも複数のファイルを簡単にパッケージ化することができます。   
これらの.zipファイルは、多くの別々のファイルよりもWebサイトへのアップロードや電子メールの添付ファイルとしての送信がはるかに簡単です。

この本の前の章では、コピーするためのソースコードを提供しています。   
しかし、あなた自身のプログラムを書くとき、彼らはおそらく初めて完全には出てこないでしょう。   
次の章では、プログラムを分析してデバッグするのに役立ついくつかのPythonモジュールに焦点を当て、プログラムをすばやく正しく実行できるようにします。

# 練習問題

1. What is the difference between shutil.copy() and shutil.copytree()?
- shutil.copy() : 単体のファイルをコピーする
- shutil.copytree() : ディレクトリとディレクトリに含まれるすべてをコピーする

2. What function is used to rename files?
- shutil.move('変更前ファイル名', '変更後ファイル名')

3. What is the difference between the delete functions in the send2trash and shutil modules?
- shutil.rmtree(path) : パスにあるフォルダが削除され、そこに含まれるすべてのファイルとフォルダも消える。消したらもとに戻せない。
- send2trash : ゴミ箱に入れる。戻すときはゴミ箱から戻せる。

4. ZipFile objects have a close() method just like File objects’ close() method. What ZipFile method is equivalent to File objects’ open() method?
- zipfile.ZipFile('hoge.zip')

# 練習プロジェクト

## 選択コピー
フォルダツリーを走査して特定のファイル拡張子（.pdfや.jpgなど）を持つファイルを検索するプログラムを作成します。   
これらのファイルを、それらが入っている場所から新しいフォルダにコピーします。

-> choice_copy.py  
拡張子を扱える `endswith` メソッドを知った。   
`for filename in filenames:` で全ファイル精査していくとき、対象ディレクトリ以下が含まれるようなディレクトリ構成の場合うまくいかないので対象ディレクトリをはずすような条件をつけた。

```python
# /path/to/source_dir 以下の特定ファイルを
# /path/to/source_dir/target_dir にコピーするようなディレクトリ構成の場合、target_dirを除外する

for filename in filenames:
    if filename.endswith(extension) and folder_name != target_dir:
```

## 不要なファイルの削除
フォルダツリーを通って非常に大きなファイルやフォルダ（ファイルサイズが100MBを超えるものなど）を検索するプログラムを作成します。   
（ファイルのサイズを取得するには、osモジュールのos.path.getsize（）を使用することを忘れないでください）。  
これらのファイルは絶対パスで画面に表示してください。

-> du.py  
バイト数で指定している。KBとかGBで指定したい。  
表示もKBとかGBとかわかりやすくやりたい。これだったらduコマンド使ってしまうよ・・・  
```python
size = 10000 <-- 数値で指定する

filesize = os.path.getsize(filepath)
    if size < filesize:  <-- sizeを数値で指定していないとここの比較でエラーになる
```

## ギャップを埋める

spam001.txt、spam002.txtなどの特定の接頭辞を持つすべてのファイルを1つのフォルダに格納し、番号の隙間を見つけ出すプログラムを作成します。  
（spam001.txt と spam003.txt があるけど spam002.txt はない場合など）
このギャップを閉じるために、後のすべてのファイルの名前をプログラムに変更させます。
追加の課題として、番号の付いたファイルにギャップを挿入して新しいファイルを追加できる別のプログラムを作成します。

-> 3-1: このギャップを閉じるために、後のすべてのファイルの名前をプログラムに変更させます

```bash
# スクリプト実行前
$ ls -la /tmp/test/
total 16
drwxr-xr-x  5 eri   wheel  170  9 10 22:28 .
drwxrwxrwt  8 root  wheel  272  9 10 22:28 ..
-rw-r--r--  1 eri   wheel    0  9 10 22:28 sample000.txt
-rw-r--r--  1 eri   wheel   48  9 10 22:28 sample002.txt
-rw-r--r--  1 eri   wheel   48  9 10 22:28 sample005.txt

# スクリプト実行
$ python gap_rename.py
===sample001.txt===
リネームする対象: /tmp/test/sample000.txt
リネーム後の名称: /tmp/test/sample001.txt
===sample002.txt===
すでに存在しています
===sample003.txt===
リネームする対象: /tmp/test/sample005.txt
リネーム後の名称: /tmp/test/sample003.txt

# スクリプト実行後
$ ls -la /tmp/test/
total 16
drwxr-xr-x  5 eri   wheel  170  9 10 22:29 .
drwxrwxrwt  8 root  wheel  272  9 10 22:28 ..
-rw-r--r--  1 eri   wheel    0  9 10 22:28 sample001.txt
-rw-r--r--  1 eri   wheel   48  9 10 22:28 sample002.txt
-rw-r--r--  1 eri   wheel   48  9 10 22:28 sample003.txt
```
