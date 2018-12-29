print ('Hello World')
print('Qual o seu nome?')
nome = input()
print('Prazer em conhecer, ' + nome)
print('Seu nome tem ' + str(len(nome)) + ' caracteres')
print('Qual a sua idade?')
idade = input()
if int(idade) <18:
    print('Vá embora, menor estúpido!')
elif int(idade) < 60:
    print('Tá no ponto!')
else:
    print('Tchau, vovô!')
print('Entao, em 5 anos voce vai estar com ' + str(int(idade) + 5) + ' anos!')
