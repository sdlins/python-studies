print('Jogo Tente Adivinhar!')
print('Tente adiviar o nome correto do time de futebol, ou digite "sair" para encerrar:')
tentativas = 0
nomeCerto = 'timao'
palpite = input()

while palpite != nomeCerto and palpite != 'sair':
    print('Você errou! Tente novamente:')
    palpite = input()

if palpite == 'sair':
    print('Você é fraco! Desiste muito rápido!!')
else:
    print('Parabéns! você acertou!!!!!!')
    
