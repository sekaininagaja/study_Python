Chapter 12 – Working with Excel Spreadsheets
https://automatetheboringstuff.com/chapter12/

# Excelスプレッドシートの操作

Excelは、Windows用の一般的で強力なスプレッドシートアプリケーションです。   
openpyxlモジュールを使用すると、PythonプログラムでExcelスプレッドシートファイルを読み取り、変更することができます。   
たとえば、あるスプレッドシートの特定のデータをコピーして別のスプレッドシートに貼り付けるという退屈な作業があります。   
または、何千もの行を通過し、いくつかの基準に基づいて小さな編集を行うためにそれらのうちのほんの一握りを選ぶ必要があるかもしれません。   
あるいは、数百の部門予算のスプレッドシートを見て、赤字のものを探しなければならないかもしれません。   
これはまさに、Pythonがあなたのためにできる退屈で、愚かなスプレッドシートタスクの一種です。

ExcelはMicrosoftの独占的なソフトウェアですが、Windows、OS X、およびLinux上で動作する無料の代替製品があります。   
LibreOffice CalcとOpenOffice Calcは、スプレッドシート用のExcelの.xlsxファイル形式で動作します。  
つまり、openpyxlモジュールはこれらのアプリケーションのスプレッドシートでも動作します。   
ソフトウェアは、それぞれ https://www.libreoffice.org/ および http://www.openoffice.org/ からダウンロードできます。   
既にExcelがコンピュータにインストールされている場合でも、これらのプログラムを使いやすくすることができます。   
ただし、この章のスクリーンショットはすべてWindows 7上のExcel 2010のものです。

# Excelドキュメント

まず、いくつかの基本的な定義を見てみましょう。  
Excelスプレッドシート文書はブックと呼ばれます。   
1つのブックは、拡張子が.xlsxのファイルに保存されます。   
各ワークブックには、複数のシート（ワークシートとも呼ばれます）を含めることができます。   
ユーザーが現在表示しているシート（またはExcelを閉じる前に最後に表示されたシート）をアクティブシートといいます。

各シートには列（Aから始まる文字でアドレス指定）と行（1から始まる数字でアドレス指定）があります。   
特定の列と行のボックスはセルと呼ばれます。   
各セルには、数値またはテキスト値を含めることができます。   
データを含むセルのグリッドがシートを構成します。

# openpyxlモジュールのインストール

PythonにはOpenPyXLが付属していないため、インストールする必要があります。   
付録Aのサードパーティモジュールのインストール手順に従ってください。   
モジュールの名前はopenpyxlです。   
正しくインストールされているかどうかをテストするには、対話型シェルに次のように入力します。

```
>>> import openpyxl
```

モジュールが正しくインストールされていれば、エラーメッセージは表示されません。   
この章の対話的なシェルの例を実行する前にopenpyxlモジュールをインポートすることを忘れないようにしないと、エラーになります: `NameError: name 'openpyxl' is not defined`

この本はOpenPyXLのバージョン2.3.3をカバーしていますが、OpenPyXLチームによって定期的に新しいバージョンがリリースされています。   
しかし、心配する必要はありません。新しいバージョンは、この書籍の説明書との互換性を保ち続けるべきです。   
新しいバージョンをお持ちで、利用可能な追加機能を確認したい場合は、http://openpyxl.readthedocs.org/ にあるOpenPyXLの全マニュアルをご覧ください。  

# Excel文書を読む

この章の例では、ルートフォルダに格納されているexample.xlsxというスプレッドシートを使用します。   
スプレッドシートを自分で作成するか、http://nostarch.com/automatestuff/ からダウンロードすることができます。   

ブックのシートのタブは、Excelの左下隅にあります。
openpyxlモジュールでどのように操作できるかを見てみましょう。

## OpenPyXLでExcel文書を開く

openpyxlモジュールをインポートすると、openpyxl.load_workbook（）関数を使用することができます。   
対話型シェルに次のように入力します。

```python
>>> import openpyxl
>>> wb = openpyxl.load_workbook('example.xlsx')
>>> type(wb)
<class 'openpyxl.workbook.workbook.Workbook'>
```

openpyxl.load_workbook（）関数は、ファイル名を取り込み、ワークブックデータ型の値を返します。   
このWorkbookオブジェクトはExcelファイルを表し、Fileオブジェクトが開いているテキストファイルをどのように表現しているかのようです。

example.xlsxは作業のために現在の作業ディレクトリに存在する必要があることに注意してください。   
現在の作業ディレクトリは、osをインポートしてos.getcwd（）を使用して調べることができ、os.chdir（）を使用して現在の作業ディレクトリを変更できます。

## ワークブックからのシートの取得

ブックのすべてのシート名のリストを取得するには、get_sheet_names（）メソッドを呼び出します。   
対話型シェルに次のように入力します。

```python
>>> import openpyxl
>>> wb = openpyxl.load_workbook('example.xlsx')
>>> wb.get_sheet_names()
['Sheet1', 'Sheet2', 'Sheet3']
>>> sheet = wb.get_sheet_by_name('Sheet3')
>>> sheet
<Worksheet "Sheet3">
>>> type(sheet) <class 'openpyxl.worksheet.worksheet.Worksheet'>
>>> sheet.title
'Sheet3'
>>> anotherSheet = wb.active
>>> anotherSheet
<Worksheet "Sheet1">
```

各シートはワークシート・オブジェクトで表され、シート名文字列をget_sheet_by_name（）ワークブック・メソッドに渡すことで取得できます。   
最後に、ワークブック・オブジェクトのアクティブ・メンバー変数を読み取って、ワークブックのアクティブ・シートを取得することができます。   
アクティブなシートは、Excelでブックを開いたときに上部にあるシートです。   
Worksheetオブジェクトを取得したら、title属性からその名前を取得できます。

## シートからセルを取得

ワークシートオブジェクトを取得したら、その名前でCellオブジェクトにアクセスできます。

```python
>>> import openpyxl
>>> wb = openpyxl.load_workbook('example.xlsx')
>>> sheet = wb.get_sheet_by_name('Sheet1')
>>> sheet['A1']
<Cell Sheet1.A1>
>>> sheet['A1'].value
datetime.datetime(2015, 4, 5, 13, 34, 2)
>>> c = sheet['B1']
>>> c.value
'Apples'
>>> 'Row ' + str(c.row) + ', Column ' + c.column + ' is ' + c.value
'Row 1, Column B is Apples'
>>> 'Cell ' + c.coordinate + ' is ' + c.value
'Cell B1 is Apples'
>>> sheet['C1'].value
73
```

Cellオブジェクトには、意外にも、そのセルに格納されている値が含まれているvalue属性があります。   
セルオブジェクトには、セルの位置情報を提供する行、列、および座標属性もあります。

ここで、セルB1のCellオブジェクトのvalue属性にアクセスすると、文字列 'Apples'が返されます。   
行属性は整数1を与え、列属性は私たちに 'B'を与え、座標属性は私たちに 'B1'を与えます。

OpenPyXLは列Aの日付を自動的に解釈し、文字列ではなくdatetime値として返します。   
datetimeデータ型については、第16章で詳しく説明します。

文字列で指定するのは難しいかもしれません。  
特に、列Zの後で列が2つの文字（AA、AB、ACなど）を使用して開始するためです。   
代わりに、シートのcell（）メソッドを使用してセルを取得し、その行と列のキーワード引数に整数を渡すこともできます。   
最初の行または列の整数は0ではなく1です。次のように入力して対話型シェルの例を続行します。

```python
>>> sheet.cell(row=1, column=2)
<Cell Sheet1.B1>
>>> sheet.cell(row=1, column=2).value
'Apples'
>>> for i in range(1, 8, 2):
        print(i, sheet.cell(row=i, column=2).value)

1 Apples
3 Pears
5 Apples
7 Strawberries
```

ご覧のとおり、シートのcell（）メソッドを使ってrow = 1とcolumn = 2を渡すと、シート['B1']の指定と同様に、セルB1のCellオブジェクトが得られます。   
次に、cell（）メソッドとキーワード引数を使用して、一連のセルの値を出力するforループを記述できます。

列Bを降りて奇数の行番号を持つすべてのセルに値を印刷したいとします。   
range（）関数の "step"パラメータに2を渡すことで、1行おきにセルを得ることができます（この場合、すべての奇数行）。   
forループのi変数はrowキーワード引数にcell（）メソッドに渡され、2は常にcolumnキーワード引数に渡されます。   
文字列 'B'ではなく、整数2が渡されることに注意してください。

ワークシート・オブジェクトのmax_rowおよびmax_columnメンバー変数を使用して、シートのサイズを判別できます。 対話型シェルに次のように入力します。

```python
>>> import openpyxl
>>> wb = openpyxl.load_workbook('example.xlsx')
>>> sheet = wb.get_sheet_by_name('Sheet1')
>>> sheet.max_row
7
>>> sheet.max_column
3
```

max_columnメソッドは、Excelに表示される文字ではなく整数を返します。

## 列の文字と数値の変換

文字を数字に変換するには、openpyxl.cell.column_index_from_string（）関数を呼び出します。   
数字を文字に変換するには、openpyxl.cell.get_column_letter（）関数を呼び出します。   
対話型シェルに次のように入力します。

```python
>>> import openpyxl
>>> from openpyxl.utils import get_column_letter, column_index_from_string  <--※補足
>>> get_column_letter(1)
'A'
>>> get_column_letter(2)
'B'
>>> get_column_letter(27)
'AA'
>>> get_column_letter(900)
'AHP'
>>> wb = openpyxl.load_workbook('example.xlsx')
>>> sheet = wb.get_sheet_by_name('Sheet1')
>>> get_column_letter(sheet.max_column)
'C'
>>> column_index_from_string('A')
1
>>> column_index_from_string('AA')
27
```
openpyxl バージョン2.4 から、openpyxl.cell -> openpyxl.utils になったらしい。  
https://stackoverflow.com/questions/36721232/importerror-cannot-import-name-get-column-letter  
openpyxl.cell だと下記のエラーになる。

```python
# 補足
>>> from openpyxl.cell import get_column_letter, column_index_from_string
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    from openpyxl.cell import get_column_letter, column_index_from_string
ImportError: cannot import name 'get_column_letter'
```

openpyxl.cellモジュールからこれらの2つの関数をインポートした後、get_column_letter（）を呼び出して、27のような整数を渡して、27番目の列の文字名を調べることができます。   
関数column_index_string（）は、その逆を行います。  
カラムの文字名を渡すと、そのカラムの番号がわかります。   
これらの機能を使用するためにワークブックを読み込む必要はありません。   
必要に応じて、ワークブックをロードし、ワークシート・オブジェクトを取得し、max_columnのようなワークシート・オブジェクト・メソッドを呼び出して整数を取得できます。   
次に、その整数をget_column_letter（）に渡すことができます。


## シートから行と列を取得する

ワークシートオブジェクトをスライスして、スプレッドシートの行、列、または長方形の領域にあるすべてのCellオブジェクトを取得できます。   
その後、スライス内のすべてのセルをループすることができます。 対話型シェルに次のように入力します。

```python   
>>> import openpyxl
   >>> wb = openpyxl.load_workbook('example.xlsx')
   >>> sheet = wb.get_sheet_by_name('Sheet1')
   >>> tuple(sheet['A1':'C3'])
   ((<Cell Sheet1.A1>, <Cell Sheet1.B1>, <Cell Sheet1.C1>), (<Cell Sheet1.A2>,
   <Cell Sheet1.B2>, <Cell Sheet1.C2>), (<Cell Sheet1.A3>, <Cell Sheet1.B3>,
   <Cell Sheet1.C3>))
>>> for rowOfCellObjects in sheet['A1':'C3']:
        for cellObj in rowOfCellObjects:
               print(cellObj.coordinate, cellObj.value)
        print('--- END OF ROW ---')

# 結果
   A1 2015-04-05 13:34:02
   B1 Apples
   C1 73
   --- END OF ROW ---
   A2 2015-04-05 03:41:23
   B2 Cherries
   C2 85
   --- END OF ROW ---
   A3 2015-04-06 12:46:51
   B3 Pears
   C3 14
   --- END OF ROW ---
```

ここでは、矩形領域のCellオブジェクトをA1からC3にし、その領域にCellオブジェクトを含むGeneratorオブジェクトを取得するように指定します。   
このGeneratorオブジェクトを視覚化するために、tuple（）を使用してセルオブジェクトをタプルに表示することができます。   

このタプルには、3つのタプルが含まれています。  
各タプルは、目的の領域の上端から下端までの各行に1つです。   
これらの3つの内側タプルのそれぞれは、最も左側のセルから右側に、希望の領域の1つの行にCellオブジェクトを含みます。   
全体として、シートのスライスには、A1からC3までの領域のすべてのCellオブジェクトが含まれています。  
左上のセルから始まり右下のセルで終わります。

領域内の各セルの値を印刷するには、2つのforループを使用します。   
外側のforループは、スライスの各行に移動します。   
次に、各行に対して、入れ子のforループがその行の各セルを通過します。

特定の行または列のセルの値にアクセスするには、ワークシートオブジェクトの行と列の属性を使用することもできます。   
対話型シェルに次のように入力します。

※下記を参考に修正  
https://stackoverflow.com/questions/42603795/typeerror-generator-object-is-not-subscriptable

```python
>>> import openpyxl
>>> wb = openpyxl.load_workbook('example.xlsx')
>>> sheet = wb.active
>>> list(sheet.columns[1])
(<Cell Sheet1.B1>, <Cell Sheet1.B2>, <Cell Sheet1.B3>, <Cell Sheet1.B4>,
<Cell Sheet1.B5>, <Cell Sheet1.B6>, <Cell Sheet1.B7>)
>>> for cellObj in list(sheet.columns)[1]:
        print(cellObj.value)

# 結果
Apples
Cherries
Pears
Oranges
Apples
Bananas
Strawberries
```

ワークシート・オブジェクトのrows属性を使用すると、タプルのタプルが得られます。   
これらの内部タプルはそれぞれ行を表し、その行にCellオブジェクトを含みます。   
また、columns属性はタプルのタプルを提供し、内側のタプルはそれぞれ、特定の列にCellオブジェクトを含みます。  
Example.xlsxでは、7行と3列があるため、行は7つのタプル（それぞれ3つのCellオブジェクトを含む）のタプルを提供し、列は3つのタプル（それぞれ7つのCellオブジェクトを含む）のタプルを提供します。

1つの特定のタプルにアクセスするには、より大きなタプルのインデックスで参照することができます。   
たとえば、列Bを表すタプルを取得するには、sheet.columns [1]を使用します。   
列AにCellオブジェクトを含むタプルを取得するには、sheet.columns [0]を使用します。   
1つの行または列を表すタプルがあれば、そのCellオブジェクトをループして値を出力できます。

## ワークブック、シート、セル

クイックレビューとして、スプレッドシートファイルからセルを読み込む際に使用されるすべての関数、メソッド、およびデータ型の概要を次に示します。

1. openpyxlモジュールをインポートします。
1. openpyxl.load_workbook（）関数を呼び出します。
1. ワークブックオブジェクトを取得します。
1. アクティブなメンバー変数を読み取るか、get_sheet_by_name（）ワークブックメソッドを呼び出します。
1. ワークシートオブジェクトを取得します。
1. 行と列のキーワード引数を持つindexingまたはcell（）シートメソッドを使用します。
1. Cellオブジェクトを取得します。
1. Cellオブジェクトのvalue属性を読み取ります。
