'''
URI Online Judge | 1037
Intervalo
Adaptado por Neilor Tonin, URI  Brasil
https://www.urionlinejudge.com.br/judge/pt/problems/view/1037
'''

entrada = float(input())

if entrada < 0 or entrada > 100:
    print("Fora de intervalo")
elif entrada <= 25:
    print("Intervalo [0,25]")
elif entrada <= 50:
    print("Intervalo (25,50]")
elif entrada <= 75:
    print("Intervalo (50,75]")
else:
    print("Intervalo (75,100]")
