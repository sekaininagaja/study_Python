Appendix B. Running Programs   
https://automatetheboringstuff.com/appendixb/

IDLEのファイルエディタでプログラムを開いている場合は、F5キーを押すか、Run Run Moduleメニュー項目を選択するだけです。   
これは、プログラムの作成中にプログラムを実行する簡単な方法ですが、終了したプログラムを実行するためにIDLEを開くことは負担になります。    
Pythonスクリプトを実行するより便利な方法があります。

# シバンライン

あなたのすべてのPythonプログラムの最初の行はシバン行でなければなりません。  
この行はPythonにこのプログラムを実行させたいことをコンピュータに伝えます。   
シバン行は＃！で始まりますが、残りはオペレーティングシステムによって異なります。

- On Windows, the shebang line is #! python3.
- On OS X, the shebang line is #! /usr/bin/env python3.
- On Linux, the shebang line is #! /usr/bin/python3.

shebang行なしでIDLEからPythonスクリプトを実行できますが、コマンドラインから実行するにはその行が必要です。

## WindowsでのPythonプログラムの実行

Windowsでは、Python 3.4インタプリタは C：\ Python34 \ python.exeにあります。   
あるいは、便利なpy.exeプログラムは、.pyファイルのソースコードの先頭にあるシバン行を読み込み、そのスクリプトの適切なバージョンのPythonを実行します。   
py.exeプログラムは、コンピュータに複数のバージョンがインストールされている場合、Pythonの正しいバージョンでPythonプログラムを実行するようにします。

Pythonプログラムを実行するのに便利なように、py.exeでPythonプログラムを実行するための.batバッチファイルを作成します。   
バッチファイルを作成するには、次のような1行の新しいテキストファイルを作成します。

```python
@py.exe C:\path\to\your\pythonScript.py %*
```

このパスを独自のプログラムの絶対パスに置き換え、.batファイル拡張子（たとえば、pythonScript.bat）でこのファイルを保存します。   
このバッチファイルを使用すると、実行するたびにPythonプログラムの完全な絶対パスを入力する必要がなくなります。   
すべてのバッチファイルと.pyファイルをC：\ MyPythonScriptsやC：\ Users \ YourName \ PythonScriptsのような単一のフォルダに配置することをお勧めします。

実行ダイアログからバッチファイルを実行できるように、C：\ MyPythonScriptsフォルダをWindowsのシステムパスに追加する必要があります。   
これを行うには、PATH環境変数を変更します。   
[スタート]ボタンをクリックし、アカウントの環境変数の編集を入力します。   
このオプションは、入力を開始した後で自動的に完了します。   
表示される環境変数ウィンドウは、図B-1のようになります。

「システム変数」から「パス」変数を選択し、「編集」をクリックします。   
値のテキストフィールドにセミコロンを追加し、C：\ MyPythonScriptsと入力して、[OK]をクリックします。   
これで、C：\ MyPythonScriptsフォルダ内の任意のPythonスクリプトを、WIN-Rを押してスクリプト名を入力するだけで実行できます。   
たとえば、pythonScriptを実行すると、pythonScript.batが実行され、実行ダイアログからpy.exe C：\ MyPythonScripts \ pythonScript.pyというコマンド全体を実行する必要がなくなります。
