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
