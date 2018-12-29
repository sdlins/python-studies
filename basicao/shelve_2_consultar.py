import shelve, pprint

dados = shelve.open('meusdados')
pp = pprint.PrettyPrinter(indent=8, width=40, depth=5)
pp.pprint(dados['app'])
pp.pformat(dados['app'])