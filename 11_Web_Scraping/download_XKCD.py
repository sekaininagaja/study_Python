#! python3
# download_XKCD.py - すべてのXKCDコミックをダウンロードします。

import requests, os, bs4

url = 'http://xkcd.com' # 開始URL
os.makedirs('xkod', exist_ok=True)  # コミックスを保存するディレクトリをつくる
while not url.endswith('#'):
    # Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    # Find the URL of the comic image.
    commic_elem = soup.select('#comic img')
    if comic_elem == []:
        print('Could not find comic image.')
    else:
        try:
            comic_url = 'http:' + comic_elem[0].get('src')
            # イメージをダウンロード
            print('Downloading image %s...' % (comic_url))
            res = requests.get(comic_url)
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            # そのコミックはとばす
            prev_link = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prev_link.get('href')
            continue

    # TODO: Download the image.

    # TODO: Save the image to ./xkcd.

    # TODO: Get the Prev button's url.

print('Done.')
