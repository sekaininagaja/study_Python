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
