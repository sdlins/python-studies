def textualizar(lista):
    retorno = ''

    for index in range(len(lista)):
        if index == 0:
            retorno += str(lista[index])
        elif index == len(lista) - 1:
            retorno += ' and ' + str(lista[index])
        else:
            retorno += ', ' + str(lista[index])
    
    print(retorno)

l1 = ['a', 'c', 'd']
l2 = [1, 4, 6, 99]

textualizar(l1)
textualizar(l2)
