import oauth2, json, urllib.parse

api_key = 'xxxxx'
api_secret = 'xxxxx'

access_token = 'xxxxx'
access_secret = 'xxxxx'

consumidor = oauth2.Consumer(api_key, api_secret)
token = oauth2.Token(access_token, access_secret)
cliente = oauth2.Client(consumidor, token)

pesquisa = urllib.parse.quote(input('O que você pesquisar no Twitter?\r\n'))

req = cliente.request('https://api.twitter.com/1.1/search/tweets.json?q=' + pesquisa + '&count=1&result_type=recent')
req_obj = json.loads(req[1].decode())

for twit in req_obj['statuses']:
    print(twit['user']['screen_name'], 'disse:', twit['text'])