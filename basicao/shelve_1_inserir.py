import shelve

dados = shelve.open('meusdados')
dados['app'] = {
    'version': 1.0,
    'author': 'Sidney Lins',
    'e-mail': 'sdlins.dev@gmail.com'
}
dados['foo'] = 'bar'
dados.close()
