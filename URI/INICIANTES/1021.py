valor = float(input())

n100 = int(valor // 100)
valor -= n100*100

n50 = int(valor // 50)
valor -= n50*50

n20 = int(valor // 20)
valor -= n20*20

n10 = int(valor // 10)
valor -= n10*10

n5 = int(valor // 5)
valor -= n5*5

n2 = int(valor // 2)
valor -= n2*2

valor *= 100

m100 = int(valor // 100)
valor -= m100*100

m50 = int(valor // 50)
valor -= m50*50

m25 = int(valor // 25)
valor -= m25*25

m10 = int(valor // 10)
valor -= m10*10

m5 = int(valor // 5)
valor -= m5*5

m1 = int(valor // 1)

print('NOTAS:')
print('{} nota(s) de R$ 100.00\n'
      '{} nota(s) de R$ 50.00\n'
      '{} nota(s) de R$ 20.00\n'
      '{} nota(s) de R$ 10.00\n'
      '{} nota(s) de R$ 5.00\n'
      '{} nota(s) de R$ 2.00'.format(n100, n50, n20, n10, n5, n2))
print('MOEDAS:')
print('{} moeda(s) de R$ 1.00\n'
      '{} moeda(s) de R$ 0.50\n'
      '{} moeda(s) de R$ 0.25\n'
      '{} moeda(s) de R$ 0.10\n'
      '{} moeda(s) de R$ 0.05\n'
      '{} moeda(s) de R$ 0.01'.format(m100, m50, m25, m10, m5, m1))