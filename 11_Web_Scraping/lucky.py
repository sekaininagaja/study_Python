#! python3
# lucky.py - いくつかのGoogle検索結果を開きます。

import requests, sys, webbrowser, bs4

print('Googling...') # Googleページのダウンロード中にテキストを表示する
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text)
#soup = bs4.BeautifulSoup(res.text, 'html.parser')  # Beautiful Soup 4.x では parser を明示指定しよう。http://hideharaaws.hatenablog.com/entry/2016/05/06/175056

# Open a browser tab for each result.
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
