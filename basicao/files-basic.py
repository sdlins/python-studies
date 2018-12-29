import pyperclip

cola = pyperclip.paste()
conteudo = cola if len(cola) > 10 else "Sem conteúdo"

arq = open("arq_test.txt", 'w')
print(arq.write(conteudo))
arq.close()

print('O arquivo recebeu o seguinte conteúdo:\n', conteudo)