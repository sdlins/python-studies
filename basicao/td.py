import requests as req, time, sys
from bs4 import BeautifulSoup as bs

data = time.strftime('%Y/%-m/%d')
url = 'https://wol.jw.org/pt/wol/dt/r5/lp-t/' + data
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

res = req.get(url, headers)
res.raise_for_status()

html = bs(res.content, "html.parser")

data = html.select('article header:nth-of-type(1)')[0].getText()
texto = html.select('article header:nth-of-type(1) ~ p')[0].getText()
comentario = html.select('article header:nth-of-type(1) ~ p ~ div.bodyTxt')[0].getText()
print(data.strip('\n'), texto.strip('\n'), comentario.strip('\n'), sep='\n\n')