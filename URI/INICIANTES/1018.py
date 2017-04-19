i = int(input())
n = i
v100 = int(n/100)
n = n-v100*100
v50 = int(n/50)
n = n-v50*50
v20 = int(n/20)
n = n-v20*20
v10 = int(n/10)
n = n-v10*10
v5 = int(n/5)
n = n-v5*5
v2 = int(n/2)
v1 = n-v2*2
print('%i\n%i nota(s) de R$ 100,00\n%i nota(s) de R$ 50,00\n%i nota(s) de R$ 20,00\n%i nota(s) de R$ 10,00\n%i nota(s) de R$ 5,00\n%i nota(s) de R$ 2,00\n%i nota(s) de R$ 1,00' %(i, v100, v50, v20, v10, v5, v2, v1))
