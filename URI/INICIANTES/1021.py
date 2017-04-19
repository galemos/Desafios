n = float(input())
print(n)
n100 = int(n/100)
n = n - n100*100
print(n)
n50 = int(n/50)
n = n - n50*50
print(n)
n20 = int(n/20)
n = n - n20*20
print(n)
n10 = int(n/10)
n = n - n10*10
print(n)
n5 = int(n/5)
n = n - n5*5
print(n)
n2 = int(n/2)
n = n - n2*2
print(n)
m1 = int(n)
n = n - m1
print(n)
m50 = int(n/0.5)
n = n - m50*0.5
print(n)
m25 = int(n/0.25)
n = n - m25*0.25
print(n)
m10 = int(n/0.1)
n = n - m10*0.1
print(n)
m05 = int(n/0.05)
n = n - m05*0.05
print(n)
m01 = int(n/0.01)
print(n)
print('NOTAS:\n%i nota(s) de R$ 100.00\n%i nota(s) de R$ 50.00\n%i nota(s) de R$ 20.00\n%i nota(s) de R$ 10.00\n%i nota(s) de R$ 5.00\n%i nota(s) de R$ 2.00\nMOEDAS:\n%i moeda(s) de R$ 1.00\n%i moeda(s) de R$ 0.50\n%i moeda(s) de R$ 0.25\n%i moeda(s) de R$ 0.10\n%i moeda(s) de R$ 0.05\n%i moeda(s) de R$ 0.01' %(n100,n50,n20,n10,n5,n2,m1,m50,m25,m10,m05,m01))