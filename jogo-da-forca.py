import random
import time
import os

# categorias para jogar
esportes = ['futebol','basquete','volei','atletismo','nataçao','tenis',
'hipismo','canoagem','judo']

comidas = ['ovo','macarrao','arroz','feijão','frango','leite','laranja'
, 'agua', 'sorvete', 'alface']

paises = ['brasil','argentina','suecia','china','inglaterra','japao','sudao'
,'congo', 'russia', 'canada']

animais = ['cachorro','gato','cavalo','cobra','papagaio','vaca','baleia'
,'barata', 'urso', 'macaco']

objetos = ['faca','tesoura','caneta','borracha','papel','computador','celular'
,'regua', 'copo', 'prato']

disciplinas = ['matematica','fisica','quimica', 'biologia','historia',
'geografia','ingles','portugues', 'filosofia', 'redação']

bebidas = ['agua','cafe','leite', 'cha','suco',
'refrigerante','energetico','vinho', 'cerveja', 'vodka']

mensagem_inicial = '\nQuais categorias você quer excluir? \
\n1.Esportes \n2.Comidas\n3.Paises\n4.Animais\n5.Objetos\n6.Disciplinas \
\n7.Bebidas\n0.Encerrar\nEscolha uma opção válida depois aperter "enter".'
print("-"*50 + mensagem_inicial + "\n" + "-"*50)
# escolher quais categorias o usuário não quer jogar
# excluir animais, paises, disciplinas etc.
excluir_opcoes = []
while True:
    if len(excluir_opcoes) == 7:
        print('Você excluiu todas as opções.')
        break

    resp = int(input('Escolha: '))

    if  0 > resp or resp > 7: # testa se a opção é inválida
        print('Por favor, escolha uma opção válida.')

    else:
        if resp == 0: 
            # testa se deseja encerrar a exclusão
            print('Você não deseja mais excluir categorias')
            break
    
        else:
            if resp not in excluir_opcoes: # adiciona as exclusoes sem repetir
                excluir_opcoes.append(resp)
            
            else:
                print(f'A opção {resp} já foi excluida. Tenta outra.')  

print('Categorias excluidas {0}'.format(excluir_opcoes))

if len(excluir_opcoes) < 7:
    # banco de opções que não foram excluidas:
    banco_opcoes = []
    if 1 not in excluir_opcoes:
        banco_opcoes.append(esportes)
    if 2 not in excluir_opcoes:
        banco_opcoes.append(comidas)
    if 3 not in excluir_opcoes:
        banco_opcoes.append(paises)
    if 4 not in excluir_opcoes:
        banco_opcoes.append(animais)
    if 5 not in excluir_opcoes:
        banco_opcoes.append(objetos)
    if 6 not in excluir_opcoes:
        banco_opcoes.append(disciplinas)
    if 7 not in excluir_opcoes:
        banco_opcoes.append(bebidas)

    time.sleep(2)
    print('-'*20+' Bom jogo!!! ' + '-'*20)
    time.sleep(1)
    os.system("cls")
    # seleciona aleatoriamente a uma palavra que não foi excluida
    alfabeto = list('abcdefghijklmnopqrstuvwxyz')
    num1 = random.randint(0,6-len(excluir_opcoes))
    num2 = random.randint(0,9)
    print('Sua palavra misteriosa:\n')
    #a palavra aleatoria é procurada no banco_opcoes e armazenada em palavra_encontrar
    palavra_encontrar = banco_opcoes[num1][num2]
    print(palavra_encontrar)
    # copia so serve para mostrar no ultimo print do programa
    copia = palavra_encontrar
    palavra_encontrar = list(palavra_encontrar)
    y = list('_' * len(palavra_encontrar))
    chutes = []
    while "_" in y: # inicio do jogo
        # mostra a evolução da palavra a medida que é feito os palpites
        for i in range(len(y)):
            print(y[i], end = ' ')

        palpite = input(' Digite uma letra: ')

        # acompanhar os chutes que ja foram dados:
        if palpite not in  chutes:
            chutes.append(palpite)
        else:
            print('Esse palpite ja foi dado antes... ')

        print('\nChutes até agora: {}'.format(chutes))
        if palpite.casefold() in alfabeto:
            if palpite.casefold() in palavra_encontrar:
                for i in range(len(palavra_encontrar)):
                    if palpite.casefold() == palavra_encontrar[i]:
                        y[i] = palpite.casefold()

            else:
                print()
                print('A letra '+ palpite + ' não está na palavra misteriosa.')
                
        else: # caso o palpite seja maior do que duas letras ou simbolos
            letras_no_alfabeto = True
            for chute in palpite:
                if chute.casefold() not in alfabeto:
                    letras_no_alfabeto = False
                    break
            if letras_no_alfabeto == True:
                resp = input('Você deseja chutar a palavra? sim ou não. ')
                if resp.casefold() == "sim":
                    if palpite.casefold() == copia:
                        break
                    else:
                        print("Você errou.")
            else:
                print('\nEscreva uma letra válida.\n')
   
    os.system("cls")
    print('Parabéns! Você acertou todas as letras da palavra misteriosa.')
    print('Sua palavra era {} '.format(copia))
