import pprint

msg = 'Vamo, vamo meu timão, vamo meu timão, não para de lutar!'
contagem = {}

for letra in msg:
    contagem.setdefault(letra, 0)
    contagem[letra] = contagem[letra] + 1

pprint.pprint(contagem)
