Chapter 7 – Pattern Matching with Regular Expressions  
https://automatetheboringstuff.com/chapter7/

# 正規表現とパターンマッチング 概要

この章では、正規表現を使用せずにテキストパターンを検索するプログラムを作成し、正規表現を使用してコードの膨大化を防ぐ方法を見ていきます。  
基本的な正規表現のマッチングを行い、文字列の置換や独自の文字クラスの作成など、より強力な機能に移行します。  
この章の最後に、テキストブロックから電話番号と電子メールアドレスを自動的に抽出するプログラムを作成します。  

# 正規表現を使用しないテキストのパターンの検索

文字列で電話番号を探したいとします。  
電話番号のパターンは下記のとおりです。  

```
3つの数字、ハイフン、3つの数字、ハイフン、および4つの数字
例：415-555-4242
```

文字列がこのパターンと一致するかどうかをチェックして`True`または`False`を返す`is_phone_number()`という名前の関数を作成します。

- is_phone_number()関数がチェックすること
1. 文字列が12文字であること
1. テキスト最初の3文字(市外局番)が数字だけで構成されていること
1. テキスト最初の3文字のあとにハイフンが1つ、数字が3つ、ハイフンが1つ、数字が4つ…のパターンを満たすこと
1. 以上を満たす場合は`True`

```python
# isPhoneNumber.py 結果
415-555-4242 is a phone numver:
True
Moshi moshi is a phone number:
False
```

forループの各反復で、メッセージからの12文字の新しいチャンクが変数チャンクに割り当てられます。  
たとえば、最初の反復では、iは0、チャンクにはメッセージ[0:12]（つまり、 'Call me at 4'）が割り当てられます。  
次の反復では、iは1で、チャンクにはメッセージ[1:13]（文字列 'all at at 41'）が割り当てられます。  
チャンクを`is_phone_number()`に渡して、電話番号パターンと一致するかどうかを確認します。  
一致する場合は、チャンクをprintします。

メッセージをループし続けると、最終的にチャンク内の12文字が電話番号になります。  
ループは文字列全体を調べ、各12文字のピースをテストし、`is_phone_number()` を満たすチャンクをprintします。  
すべてのメッセージを精査したら、Doneをprintします。  

```python
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
      chunk = message[i:i+12]
      if isPhoneNumber(chunk):
      print('Phone number found: ' + chunk)
print('Done')
```

``` python
# メッセージ内から電話番号だけ抜き出す
Phone number found: 415-555-1011
Phone number found: 415-555-9999
Done
```

この例でのメッセージ文字列は短いものの、数百万文字でもプログラムは1秒未満で実行されます。  
正規表現を使って電話番号を見つける同様のプログラムも1秒未満で実行されますが、正規表現ではこれらのプログラムをより早く書けます。  


# 正規表現でのテキストのパターンの検索

先ほどの電話番号検索プログラムも機能しますが、たくさんのコードを書くわりには下記のような制限があります。  
- 17行のis_phone_number()関数で、電話番号のパターンは1つしか対応できない  
  - `415.555.4242` や `(415)555-4242` のような形式に対応できない
  - 電話番号に `415-555-4242 x99` のような内線番号に対応できない
- これらに対応するためには、追加パターンのコードを書かないといけない

上記の制限は、正規表現を使って表すことができます。
たとえば、正規表現の`\d`は、数字(つまり0～9のいずれか)を表します。  
正規表現 `\d\d\d-\d\d\d-\d\d\d\d` は、`3つの数字、ハイフン、3つの数字、ハイフン、4つの数字` にマッチします。

上記の正規表現はもっと洗練できます。  
パターンの後に中括弧（{3}）を3つ追加することで、「このパターンを3回一致させる」という意味になります。  
`\d{3}-\d{3}-\d{4}`


## 正規表現オブジェクトの作成

Pythonのすべての正規表現関数はreモジュールにあります。  
このモジュールをインポートするには、対話型シェルに次のように入力します。  

```python
>>> import re
```

この章で続く例のほとんどはreモジュールを必要とするので、あなたが書いたスクリプトの始めやIDLEを再起動するときには必ず忘れずにインポートしてください。  
それ以外の場合は、`NameError: name 're' is not defined` というエラーメッセージが表示されます。   
正規表現を表す文字列値を`re.compile()`に渡すと、正規表現パターンオブジェクト(または単純に正規表現オブジェクト)が返されます。

電話番号パターンと一致するRegexオブジェクトを作成するには、対話型シェルに次のように入力します。  
これで、phone_number_regex変数に正規表現オブジェクトが格納されます。  

```python
>>> phone_number_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
```

生の文字列`(r'\d\d\d-\d\d\d-\d\d\d\d')`を `re.compile()` に渡しているのはなぜか。  

Pythonでも字をエスケープするにはバックスラッシュ`\` を使用します。
文字列値 `\n` は改行文字を表します。  
単一のバックスラッシュは `\\` と表します。  
だから `\\n` は 「バックスラッシュ + 小文字のn」を表しています。  

しかし、上記の例のように文字列値の最初の引用符の前に`r`を置くと、文字列を生の文字列としてマークすることができます。  
生の文字列はバックスラッシュをエスケープ文字として解釈しません。  
正規表現ではバックスラッシュが頻繁に使用されるので、余分なバックスラッシュを入力するのではなく、生の文字列を`re.compile()` 関数に渡すほうが便利です。  

```python
# 余計なバックスラッシュがはいるとわかりにくい
\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d

# 生の文字列を使ったほうがわかりやすい
r'\d\d\d-\d\d\d-\d\d\d\d'
```

## 正規表現オブジェクトの作成

Regexオブジェクトの`search()`メソッドは、渡された文字列が正規表現に一致するかどうかを検索します。  
正規表現パターンが文字列に見つからない場合、`search()`メソッドは **None** を返します。   
パターンが見つかった場合、**Matchオブジェクト** を返します。  
Matchオブジェクトには、検索された文字列から実際に一致したテキストを返す`group()`メソッドがあります。

```python
>>> phone_number_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
>>> mo = phone_number_regex.search('My numger is 415-555-4242.')
>>> print('Phone number found: ' + mo.group())
Phone number found: 415-555-4242
```

`mo`という変数名は、Matchオブジェクトに使用する単なる一般的な名前です。  
この例は最初は複雑に思えるかもしれませんが、さきほどののis_phone_number.pyプログラムよりもずっと短く、同じことをしています。

ここでは、必要なパターンを`re.compile()`に渡し、結果のRegexオブジェクトを`phone_number_regex`に格納します。  
次に、`phone_number_regex`で`search()`を呼び出し、一致するものを検索する文字列を`search()`に渡します。  
検索の結果は変数`mo`に格納されます。  
この例では、パターンが文字列内にあることがわかっているので、Matchオブジェクトが返されることがわかります。  
`mo`にnull値ではなくMatchオブジェクトが含まれていることを知っているので、`mo`に対して`group()`を呼び出すと一致する内容が返されます。  
`mo.group()` をprintしてみると、全体の一致する「415-555-4242」が表示されます。

## 正規表現マッチングのレビュー

Pythonで正規表現を使用するにはいくつかのステップがありますが、各ステップはかなり単純です。

1. `import re` でregexモジュールをインストールする
1. `re.compile()`関数を使用してregexオブジェクトを作成する。このとき **生文字列** を使用すること。
1. 検索する文字列をregexオブジェクトの`search()`メソッドに渡す。`Matchオブジェクト`が反る。
1. Matchオブジェクトの`group()`メソッドを呼び出して、実際に一致したテキストの文字列を返す。

対話型シェルにサンプルコードを入力することをお勧めしますが、Webベースの正規表現テスターを使用して、正規表現が入力したテキストとどのように一致するかを正確に示すことができます。  
おすすめのテスター -> http://regexpal.com/

# 正規表現によるパターンマッチングの強化

Pythonで正規表現オブジェクトを作成して見つける基本的な手順を知ったので、より強力なパターンマッチング機能のいくつかを試してみましょう。  

## かっこ`()` でグループ化する
市外局番と残りの電話番号とを区別したいとします。  
かっこを追加すると正規表現にグループが作成されます。`(\d\d\d)-(\d\d\d-\d\d\d\d)`  
次に、マッチオブジェクトの`group()`メソッドを使用して、1つのグループから一致するテキストを取得します。

正規表現文字列の最初の括弧セットはグループ1になります。  
2番目のセットはグループ2になります。  
1または2の整数をマッチオブジェクトの`group()`メソッドに渡すことで、マッチしたテキストの異なる部分を取得できます。  
`group()`メソッドに0または何も渡さないと、一致したテキスト全体が返されます。  

すべてのグループを一度に取得したい場合は、`groups()`メソッドを使用してください。  
名前に複数のフォームがあることに注意してください。
`mo.groups()`は複数の値からなるタプルを返すので、`area_code, main_number = mo.groups()` のように複数の割り当てトリックを使用して各値を別々の変数に割り当てることができます。  

```python
>>> phone_number_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
>>> mo = phone_number_regex.search('My number is 415-555-4242.')

>>> mo.group(1)
'415'
>>> mo.group(2)
'555-4242'
>>> mo.group(0)
'415-555-4242'
>>> mo.group()
'415-555-4242'

>>> mo.groups()
('415', '555-4242')
>>> area_code, main_number = mo.groups()
>>> print(area_code)
415
>>> print(main_number)
555-4242
```

括弧は正規表現では特別な意味を持ちますが、括弧をテキストにマッチさせる必要がある場合はどうしますか？   
たとえば、あなたが照合しようとしている電話番号に、括弧内に市外局番が設定されている可能性があります。  
この場合、`(`と`)`をバックスラッシュでエスケープする必要があります。
`re.compile()` に渡される生の文字列の `\(` および `\)` は `()` にマッチします。

```python
>>> phone_num_regex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
>>> mo = phone_num_regex.search('My phone number is (415) 555-4242.')
>>> mo.group(1)
'(415)'
>>> mo.group(2)
'555-4242'
```

## 複数のグループとパイプのマッチング

`|` はパイプと呼ばれます。多くの式のいずれかと一致したい場所であればどこでも使えます。  
たとえば、正規表現 `r'Batman|Tina Fey'` は、'Batman' または 'Tina Fey' にマッチします。  

検索された文字列に 'Batman' と 'Tina Fey' の両方が出現すると、最初に出現した方がMatchオブジェクトとして返されます。  
（のちほど説明する `findall()` を使用すると、出現するすべての文字列を検索できますが閑話休題）

```python
>>> heroRegex = re.compile(r'Batman|Tina Fey')

>>> mo1 = heroRegex.search('Batman and Tina Fey.')
>>> mo1.group()
'Batman'

>>> mo2 = heroRegex.search('Tina Fey and Batman.')
>>> mo2.group()
'Tina Fey'
```

パイプを使用して、正規表現の一部としていくつかのパターンの1つをマッチさせることもできます。  
たとえば、「Batman」「Batmobile」「Batcopter」「Batbat」のいずれかの文字列に一致させたいとします。   
これらの文字列はすべて **Bat** で始まるので、その接頭辞を1回だけ指定できるといいでしょう。  
これは、かっこで行うことができます。

`mo.group(1)` は最初のかっこのグループ 'mobile' 内の一致したテキストの一部を返しますが、メソッドコール `mo.group()` は完全一致のテキスト 'Batmobile' を返します。  
パイプ文字とグループ化括弧を使用すると、正規表現に一致させるいくつかの代替パターンを指定できます。  

```python
>>> batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
>>> mo = batRegex.search('Batmobile lost a wheel')
>>> mo.group()
'Batmobile'
>>> mo.group(1)
'mobile'
```

もし、パイプそのものにマッチさせる必要がある場合は `\|` のようにバックスラッシュでエスケープします。

## クエスチョンマーク(?) … "あってもなくても"にマッチ

オプションで一致させたいパターンがある場合もあります。  
つまり、そのビットがそこにあるかどうかにかかわらず、正規表現は一致を見つけなければなりません。  
**?** は、それをパターンのオプション部分として先行するグループにフラグを立てます。  

`(wo)?`パターンは、`wo` がオプションのグループであることを意味します。   
正規表現は、`wo`がついている、または、`wo`がついていないテキストと一致します。  
これは正規表現が 'Batwoman'と 'Batman'の両方にマッチする理由です。

```python
>>> batRegex = re.compile(r'Bat(wo)?man')

>>> mo1 = batRegex.search('The Adventures of Batman')
>>> mo1.group()
'Batman'

>>> mo2 = batRegex.search('The Adventures of Batwoman')
>>> mo2.group()
'Batwoman'
```

以前の電話番号の例を使用すると、正規表現に市外局番を持つ電話番号があるかどうかを調べることができます。  

```python
>>> phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')

>>> mo1 = phoneRegex.search('My number is 415-555-4242')
>>> mo1.group()
'415-555-4242'

>>> mo2 = phoneRegex.search('My number is 555-4242.')
>>> mo2.group()
'555-4242'
```

もし、?そのものにマッチさせる必要がある場合は `\?` のようにバックスラッシュでエスケープします。

## スター(\*) … "0回以上の繰り返し" にマッチ

スター **\*** は、「0以上の一致」を意味します。  
スターに先行するグループは、テキスト内で何回も出現することができます。  
それは全く存在しないか、何度も繰り返すことができます。 バットマンの例をもう一度見てみましょう。  

'Batman' の場合、`(wo)*` 部分は、文字列中に `wo` 部分は出現しないのでないものとして`Batman`にマッチします。  
'Batwoman'の場合、`(wo)*` は `wo` 部分にマッチします。  
'Batwowowowoman' の場合、`(wo)*` は `wowowowowowo` 部分にマッチします。

```python
>>> batRegex = re.compile(r'Bat(wo)*man')

>>> mo1 = batRegex.search('The Adbentures of Batman')
>>> mo1.group()
'Batman'

>>> mo2 = batRegex.search('The Adbentures of Batwoman')
>>> mo2.group()
'Batwoman'

>>> mo3 = batRegex.search('The Adbentures of Batwowowowowowoman')
>>> mo3.group()
'Batwowowowowowoman'
```

もし、\*そのものにマッチさせる必要がある場合は `\*` のようにバックスラッシュでエスケープします。

## プラス(\+) … "1回以上の繰り返し" にマッチ

**\*** は「0回以上の繰り返し」を意味しました。**+** は「1回以上の繰り返し」を意味します。

```python
>>> batRegex = re.compile(r'Bat(wo)+man')

>>> mo1 = batRegex.search('The Adventures of Batwoman')
>>> mo1.group()
'Batwoman'

>>> mo2 = batRegex.search('The Adventures of Batwowowowoman')
>>> mo2.group()
'Batwowowowoman'

# (wo)+ は'Batman' にマッチしない
>>> mo3 = batRegex.search('The Adbentures of Batman')
>>> mo3 == None
True
```

もし、+そのものにマッチさせる必要がある場合は `\+` のようにバックスラッシュでエスケープします。

## 波カッコ … "特定回数の繰り返し" にマッチ

特定の回数繰り返すグループがある場合は、正規表現内のグループに続けて波括弧`{}` で囲みます。  
たとえば、`(Ha){3}` は文字列 'HaHaHa'にマッチしますが、'HaHa' にはマッチしません(Haが2つしかないため)。  

1つの数値の代わりに、波括弧の間に最小値、コンマ、最大値を書くことで範囲を指定することができます。  
たとえば、`(Ha){3,5}` は、 'HaHaHa', 'HaHaHaHa', および 'HaHaHaHaHa' にマッチします。

波括弧内の最初の番号または2番目の番号を省略して、最小値または最大値を無制限のままにすることもできます。  
たとえば、`(Ha){3,}` は 'Ha' の3つ以上の繰り返しに一致し、`(Ha){,5}` は 0〜5 の繰り返しに一致します。  
波括弧は正規表現を短くするのに役立ちます。  

これらの2つの正規表現は、同じパターンに一致します。  

```
(Ha){3}
(Ha)(Ha)(Ha)

(Ha){3,5}
((Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha)(Ha))
```

```python
>>> haRegex = re.compile(r'(Ha){3}')

# HaHaHa には一致する
>>> mo1 = haRegex.search('HaHaHa')
>>> mo1.group()
'HaHaHa'

# Ha には一致しない
>>> mo2 = haRegex.search('Ha')
>>> mo2 == None
True
```

## よくばりなマッチと控えめなマッチ

`(Ha){3,5}` という正規表現では 'HaHaHaHaHa', 'HaHaHaHa', 'HaHaHa' がマッチします。  
Pythonの正規表現はデフォルトでは欲張りです。  
つまり、あいまいな状況では可能な限り長い文字列と一致します。  
マッチする文字列のうちもっとも短い文字列に一致させるには、波括弧と疑問符で控えめなマッチをおこないます。  

```python
>>> greedyHaRegex = re.compile(r'(Ha){3,5}')
>>> mo1 = greedyHaRegex.search('HaHaHaHaHa')
>>> mo1.group()
'HaHaHaHaHa'

>>> nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
>>> mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
>>> mo2.group()
'HaHaHa'
```

疑問符(?)は、正規表現に2つの意味を持つことができます。  
つまり、非一致の一致を宣言するか、オプションのグループにフラグを付けることです。   
これらの意味は完全に無関係です。


# findall()メソッド

regexオブジェクトには、`search()` メソッドの他に、`findall()` メソッドもあります。  
`search()` は、検索された文字列の最初に一致したテキストのMatchオブジェクトを返しますが、`findall()`メソッドは、検索された文字列のすべての文字列を返します。

一方、正規表現にグループが存在しない限り、`findall()`はMatchオブジェクトを返さず、**文字列のリスト** を返します。  
リスト内の各文字列は、正規表現に一致した検索テキストの一部です。
正規表現にグループがある場合、`findall()`は **タプルのリスト** を返します。  
各タプルは見つかった一致を表し、その項目は正規表現内の各グループの一致した文字列です。  

```python
# search() は最初に一致した文字列しか返さない
>>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
>>> mo = phoneNumRegex.search('Call: 415-555-9999 Work: 212-555-0000')
>>> mo.group()
'415-555-9999'

# findall() は一致したすべての文字列のリストを返す。 ※正規表現にグループが存在しない場合
>>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
>>> phoneNumRegex.findall('Call: 415-555-9999 Work: 212-555-0000')
['415-555-9999', '212-555-0000']

# findall() は一タプルのリストを返す。 ※正規表現にグループが存在する場合
>>> phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
>>> phoneNumRegex.findall('Call: 415-555-9999 Work: 212-555-0000')
[('415', '555', '9999'), ('212', '555', '0000')]
```

`findall()`メソッドが返す結果を要約すると、次のことを覚えておいてください。  
1. `\d\d\d-\d\d\d-\d\d\d\d`のようにグループを持たない正規表現で呼び出された場合は、一致する文字列のリストを返す。  
   例: ['415-555-9999', '212-555-0000']
1. `(\d\d\d)-(\d\d\d)-(\d\ d\d\d)`のようにグループを持つ正規表現で呼び出された場合、タプルのリストを返す。  
   例: [('415', '555', '9999'), ('212', '555', '0000')]

# 文字クラス

電話番号の正規表現の例では、`\d` が任意の数値の桁を表すことができることを学びました。   
つまり、`\d` は正規表現 `(0|1|2|3|4|5|6|7|8|9)` の短縮形です。   
下記に示すように、このような省略文字クラスが多数あります。  

- \d … 0から9の数字(整数)
- \d … 0から9の数字(文字としての数字)
- \w … 任意の文字、数字、またはアンダースコア （これを "単語"文字と一致すると考えてください）
- \W … 文字、数字、またはアンダースコア以外の文字
- \s … 任意のスペース、タブ、または改行文字 （これを "スペース"文字と一致すると考えてください）
- \S … スペース、タブ、または改行ではない文字

文字クラスは、正規表現を短縮するのに適しています。  
文字クラス`[0-5]`は0〜5の数字にマッチします。  
これは`(0|1|2|3|4|5)`と同意であり、それよりもはるかに短くなります。  

以下の例で、正規表現`\d+\s\w+`は、1つ以上の数字（\d+）、空白文字（\s）、1つ以上の文字/数字/アンダースコア（\w+）が続くテキストにマッチします。  
`findall()`メソッドは、リスト内の正規表現パターンに一致するすべての文字列を返します。

```python
>>> xmasRegex = re.compile(r'\d+\s\w+')
>>> xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3,hens, 2 doves, 1 partridge')
['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6 geese', '5 rings', '4 birds', '2 doves', '1 partridge']
```

## 独自の文字クラスを作る

一連の文字に一致させたいが、短い文字クラス(\d, \w, \s, など)が広すぎる場合があります。  
角カッコを使用して独自の文字クラスを定義することができます。  
たとえば、文字クラス[aeiouAEIOU]は、小文字と大文字のいずれの母音とも一致します。  

```python
>>> vowelRegex = re.compile(r'[aeiouAEIOU]')
>>> vowelRegex.findall('Robocop eats baby food.BABY FOOD.')
['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']
```

また、ハイフンを使用して文字や数字の範囲を含めることもできます。  
たとえば、文字クラス`[a-zA-Z0-9]`は、すべての小文字、大文字、および数字と一致します。  

角括弧の中で、通常の正規表現シンボルはそのように解釈されないことに注意してください。  
つまり、先行するバックスラッシュで `*？()` をエスケープする必要はありません。  
たとえば、文字クラス`[0-5.]`は0から5までの数字とピリオドに一致します。
`[0-5\.]`と書く必要はありません。

文字クラスの開始括弧の直後にキャレット文字 `^` を配置することで、負の文字クラスを作成できます。  
負の文字クラスは、文字クラスにないすべての文字と一致します。  
下記は、母音以外のすべての文字にマッチします。

```python
>>> consonantRegex = re.compile(r'[^aeiouAEIOU]')
>>> consonantRegex.findall('Robocop eats baby food.BABY FOOD.')
['R', 'b', 'c', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', 'B', 'B', 'Y', ' ', 'F', 'D', '.']
```

## キャレット(^) と ダラー($) 記号 … "先頭が〜〜ではじまる" "末尾が〜〜でおわる" にマッチ

先頭にキャレット記号`^`をつけると、「先頭が〜〜ではじまる」のマッチを表せます。  
同様に、最後にドル記号`$`をつけると「末尾が〜〜で終わる」を表せます。   
また、`^`と`$`を一緒に使用すると、文字列全体が正規表現と一致する必要があることを示すことができます。  
つまり、文字列の一部のサブセットで一致するには不十分です。

たとえば、`r'^Hello'` は 'Hello'で始まる文字列と一致します。

```python
>>> beginsWithHello = re.compile(r'^Hello')

# 'Hello' にマッチする
>>> beginsWithHello.search('Hello world!')
<_sre.SRE_Match object; span=(0, 5), match='Hello'>

# 'Hello' ではじまらないのでマッチしない
>>> beginsWithHello.search('He said hello.') == None
True
```

`r'\d$'` は0〜9の数字で終わる文字列と一致します。

```python
>>> endWithHello = re.compile(r'\d$')

# 最後の数字(2) にマッチ
>>> endWithHello.search('Your number is 42')
<_sre.SRE_Match object; span=(16, 17), match='2'>

# 最後が数字じゃない(.) のでマッチしない
>>> endWithHello.search('Your number is forty two.') == None
True
```

`r'^\d+$'` は1文字以上の数字で始まり、数字で終わる文字列と一致します。

```python
>>> wholeStrinlsNum = re.compile(r'^\d+$')
>>> wholeStrinlsNum.search('1234567890')
<_sre.SRE_Match object; span=(0, 10), match='1234567890'>
>>> wholeStrinlsNum.search('12345xyz67890') == None
True
>>> wholeStrinlsNum.search('12 34567890') == None
True
```

## ワイルドカード(.) … "任意の一文字"にマッチ

ドット`.` はワイルドカードと呼ばれ、改行以外の任意の文字と一致します。  
ドット文字はただ1文字にマッチすることに注意してください。  
下記の例のうち、'flat' は 'lat' としてマッチしているでしょう。  

```python
>>> atRegex = re.compile(r'.at')
>>> atRegex.findall('The cat in the hat sat on the flat mat.')
['cat', 'hat', 'sat', 'lat', 'mat']
```

もし、.そのものにマッチさせる必要がある場合は `\.` のようにバックスラッシュでエスケープします。


## ドットスター(.\*) … "すべての文字列"にマッチ

時々、あなたはすべてと何かを一致させたいと思うでしょう。   
たとえば、文字列 'First Name:' に続く任意のすべてのテキストや、'Last Name:' の後に何かが続いた場合に一致するとします。  
ドットスター `.*` を使用して「何でも」を表すことができます。  
ドット文字は「改行以外の任意の1文字」を意味し、スター文字は「0以上の先行文字」を意味します。

```python
>>> nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
>>> mo = nameRegex.search('First Name: AI Last Name: Sweigart')
>>> mo.group(1)
'AI'
>>> mo.group(2)
'Sweigart'
```

ドットスターは欲張りモードを使用します。可能な限り多くのテキストを常に一致させようとします。  
非倫理的な方法ですべてのテキストを照合するには、`.*?` を使用します。  
中括弧のときと同様に、疑問符はPythonにひかえめなマッチをするように指示します。

```python
# 控えめモード
>>> nongreedyRegex = re.compile(r'<.*?>')
>>> mo = nongreedyRegex.search('<To serve man> for dinner.>')
>>> mo.group()
'<To serve man>'

# 欲張りモード
>>> greedyRegex = re.compile(r'<.*>')
>>> mo = greedyRegex.search('<To serve man> for dinner.>')
>>> mo.group()
'<To serve man> for dinner.>'
```

両方の正規表現は大まかには「開き角括弧に一致し、その後に何かが続き、閉じ角括弧が続く」と解釈されます。  
しかし、文字列 '<To serve man>' には、閉じ角括弧に2つの一致があります。   
正規表現のひかえめなバージョンでは、Pythonは可能な限り短い文字列をマッチさせます: '<To serve man>'  
欲張りなバージョンでは、Pythonは可能な限り長い文字列と一致します: '<To serve man> for dinner.>'


## ドットで改行を含む表現

ドットスターは、改行以外のすべてにマッチします。
`re.compile()` の2番目の引数として `re.DOTALL` を渡すことで、改行文字を含むすべての文字にドット文字を一致させることができます。  

```
>>> noNewlineRegex = re.compile('.*')
>>> noNewlineRegex.search('Serve the public trust. \nProtect the inncent.\nUphold the law.').group()
'Serve the public trust. '

>>> newlineRegex = re.compile('.*',re.DOTALL)
>>> newlineRegex.search('Serve the public trust. \nProtect the inncent.\nUphold the law.').group()
'Serve the public trust. \nProtect the inncent.\nUphold the law.'
```

re.DOTALLなしの `noNewlineRegex` は、最初の改行文字までしか一致しません。  
re.DOTALLありの `newlineRegex` は、改行を含むすべてにマッチします。  


# 正規表現シンボルのレビュー

この章ではたくさんの表記法について説明しましたので、ここで学んだことを簡単に見ていきましょう。

- ？ : 前のグループの **0または1** にマッチ
- \* : 前のグループの **0回以上の繰り返し** にマッチ
- + : 前のグループの **1回以上の繰り返し** にマッチ
- {n} : 前のグループの **n回繰り返し** にマッチ
- {n,} : 前のグループの **n回〜無制限** の繰り返しにマッチ
- {,m} : 前のグループの **0からm回の繰り返し** にマッチ
- {n,m} : 先行するグループの **少なくともn個と多くともm個** にマッチ(欲張りなマッチ)
- {n,m}？ または \*？ または +？ : 前のグループの控えめなマッチ
- ^spam : 文字列がspamで始まらなければならない
- spam$ : 文字列がspamで終わらなければならない
- . : 改行文字を除く任意の文字にマッチ
- \d, \w, \s : それぞれ数字、単語、または空白文字とマッチ
- \D, \W, \S : それぞれ数字、単語、または空白文字以外のものとマッチ
- [abc] : a,b,c の任意の文字にマッチ
- [^abc] : a,b,c 以外の文字にマッチ

# 大文字と小文字を区別しないマッチング

通常、正規表現はテキストを指定した大文字と一致させます。  
たとえば、次の正規表現は完全に異なる文字列にマッチします。

しかし、大文字か小文字かを気にせずに文字をマッチングさせることだけが気になることもあります。  
regexを大文字と小文字を区別しないようにするには、`re.compile()` の第2引数として `re.IGNORECASE` または `re.I` を渡します。  

```python
# 複数のマッチさせる文字列を書かないといけない
>>> regex1 = re.compile('Robocop')
>>> regex2 = re.compile('ROBOCOP')
>>> regex3 = re.compile('robOcop')
>>> regex4 = re.compile('RobocOp')

# 大文字小文字を区別しない場合
>>> robocop = re.compile(r'robocop',re.I)
>>> robocop.search('Robocop is part man, part machine, all cop.').group()
'Robocop'

>>> robocop.search('ROBOCOP protects the innocent.').group()
'ROBOCOP'

>>> robocop.search('AI, why does your programming book talk about robocop so much?').group()
'robocop'
```

# sub()メソッドに文字列を代入する … マッチした文字列の置換

正規表現はテキストパターンを見つけるだけでなく、それらのパターンの代わりに新しいテキストを置き換えることもできます。  
Regexオブジェクトの`sub()`メソッドには2つの引数が渡されます。  
最初の引数は、一致するものを置き換える文字列です。  
2番目は正規表現の文字列です。  
`sub()` メソッドは、置換が適用された文字列を返します。

```python
>>> namesRegex = re.compile(r'Agent \w+')
>>> namesRegex.sub('CENSORED','Agent Alice gave the secret documents to Agent Bob.')
'CENSORED gave the secret documents to CENSORED.'
```

場合によっては、一致するテキスト自体を置換の一部として使用する必要があります。  
`sub()` の最初の引数には、`\1, \2, \3` などと入力して、「グループ1,2,3などのテキストを置換に入力する」ことを意味します。

たとえば、名前の最初の文字を表示するだけで、秘密エージェントの名前を検閲したいとします。  
これを行うには、regexエージェント `(\w)\w*` を使用して、`r'\1****'` を `sub()` の最初の引数として渡すことができます。  
その文字列の `\1` は、グループ1と一致するテキスト、つまり正規表現の`(\w)`グループに置き換えられます。

```python
# Agent につづく文字列は名前とみなしてマスクする
>>> agentNameRegex = re.compile(r'Agent (\w)\w*')
>>> agentNameRegex.sub(r'\1****', 'Agent Alice told Agent Carol thet Agent Eve knew Agent Bob was a double agent.')
'A**** told C**** thet E**** knew B**** was a double agent.'
```

## 複雑な正規表現の管理

一致させる必要があるテキストパターンが単純な場合、正規表現は問題ありません。  
しかし、複雑なテキストパターンにマッチさせるには、長く複雑な正規表現を必要とするかもしれません。  
正規表現文字列内の空白とコメントを無視するように `re.compile()` に指示することで、これを軽減できます。  
この "冗長モード" は `re.compile()` の第2引数として変数 `re.VERBOSE` を渡すことで有効にできます。

```python
# 読みにくい正規表現の例
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}
(\s*(ext|x|ext.)\s*\d{2,5})?)')

# トリプルクオートで複数行に分割し、re.VERBOSEで空白を無視する。さらにコメントをつけ、読みやすくしている。
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)
```

正規表現文字列内のコメントルールは、通常のPythonコードと同じです。  
また、正規表現の複数行文字列の余分なスペースは、一致するテキストパターンの一部とはみなされません。  
これにより正規表現を整理して読みやすくなります。

## re.IGNORECASE, re.DOTALL, and re.VERBOSE の組み合わせ

`re.VERBOSE` を使用して正規表現でコメントを書く場合、`re.IGNORECASE` を使用して大文字小文字を無視したい場合はどうすればよいですか？  
残念ながら、`re.compile()`関数は2つ目の引数として1つの値しか取りません。  
そんなときは、 `re.IGNORECASE` `re.DOTALL` `re.VERBOSE` 変数を、パイプ文字（|）を使用して組み合わせることで、この制限を回避することができます。  
この文字列はビット単位または演算子として知られています。

したがって、大文字と小文字を区別せず、ドット文字に一致する改行を含む正規表現が必要な場合は、次のように`re.compile()`を呼び出します。

```python
>>> someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
```

この構文は古風なもので、Pythonの初期のバージョンに由来しています。  
ビット単位の演算子の詳細は、この本の範囲を超えていますが、詳細は http://nostarch.com/automatestuff/ のリソースを参照してください。  
2番目の引数には他のオプションも渡すことができます。これらは珍しいですが、リソースについてももっと詳しく読むことができます。  
