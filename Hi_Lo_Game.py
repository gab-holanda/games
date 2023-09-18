import math

i = 10
maior = 1000 #limite é 1023
menor = 1
num = maior // 2

print('\nBem-vindo(a) ao jogo "Hi Lo Game". ')
print('Pense em um número inteiro de {} a {}.'.format(menor, maior))
print('Meu objetivo é acertar seu número em até {} palpites.\n\n'.format(i))
input('ENTER para continuar...')
resp = ''
while resp != "sim":
    resp = input('Seu número é {} ? sim ou não.\n'.format(num))
    if resp.casefold() == 'sim':
        print('Ganhei!!!')
    if resp.casefold() == 'nao':
        i -= 1
        print('Ainda tenho {} chances...'.format(i))
        resp = input('Seu número é maior que {}? sim ou não\n'.format(num))
        if resp.casefold() == "sim":
            num = math.ceil((maior+num)/2)
            # num = 1 + (maior+num)//2
            print(num)
        if resp.casefold() == "nao":
            num = math.ceil((num+menor)/2)
            # num = 1 + (menor+num)//2
            print(num)
    if i<0:
        print('Perdi!')
        break
else:
    print('Até a próxima.')
