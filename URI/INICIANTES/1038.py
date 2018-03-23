'''
URI Online Judge | 1038
Lanche
Adaptado por Neilor Tonin, URI  Brasil
https://www.urionlinejudge.com.br/judge/pt/problems/view/1038
'''

dados = {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50
}

linha = input()
cod, qtd = linha.split(" ")
cod = int(cod)
qtd = int(qtd)

total = qtd * dados[cod]

print('Total: R$ %0.2f' % total)
