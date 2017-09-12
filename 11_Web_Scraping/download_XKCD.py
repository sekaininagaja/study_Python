#! python3
# download_XKCD.py - すべてのXKCDコミックをダウンロードします。

import requests, os, bs4

url = 'http://xkcd.com' # 開始URL
os.makedirs('xkcd', exist_ok=True)  # コミックスを保存するディレクトリをつくる
while not url.endswith('#'):
    # Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    # Find the URL of the comic image.
    comic_elem = soup.select('#comic img')
    if comic_elem == []:
        print('Could not find comic image.')
    else:
        try:
            comic_url = 'http:' + comic_elem[0].get('src')
            # Download the image.
            print('Downloading image %s...' % (comic_url))
            res = requests.get(comic_url)
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            # そのコミックはとばす
            prev_link = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prev_link.get('href')
            continue

    # Save the image to ./xkcd.
    image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
    for chunk in res.iter_content(100000):
        image_file.write(chunk)
    image_file.close()

    # Get the Prev button's url.
    prev_link = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prev_link.get('href')

print('Done.')
