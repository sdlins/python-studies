#! /usr/bin/python3

import requests as req, time

data = time.strftime('%Y/%-m/%d')
url = 'https://wol.jw.org/pt/wol/dt/r5/lp-t/' + data
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

res = req.get(url, headers)
res.raise_for_status()

arq = open('wol.html', 'wb')
for parte in res.iter_content(1000):
    print('Escrevendo no arquivo:\n>>>>>>>>>>>>> %s' % parte)
    arq.write(parte)
arq.close()