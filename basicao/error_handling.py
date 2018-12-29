def teste(divisor):
    try:
        return 42/divisor
    except ZeroDivisionError:
        print('Erro: impossível dividir por zero')

print(teste(10))
print(teste(999))
print(teste(0)) # gera erro
print(teste(2))
