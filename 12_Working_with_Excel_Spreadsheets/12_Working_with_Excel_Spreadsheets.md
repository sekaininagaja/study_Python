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
