import random
numSecreto = random.randint(1,20)

print('Descubra o número secreto entre 1 e 10: ')

for tentativa in range(4, -1, -1):
    palpite = int(input());

    if palpite < numSecreto:
        print('O número secreto é maior do que o digitado.')
    elif palpite > numSecreto:
        print('O número secreto é menor do que o digitado.')
    else:
        break #acertou

    if tentativa > 0:
        print('Voce ainda tem ' + str(tentativa) + ' tentativa(s).')

if palpite == numSecreto:
    print('Parabens, você acertou!')
else:
    print('Suas chanves acabaram! Você perdeu.')
    print('O número secreto era ', numSecreto)
