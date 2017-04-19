n = int(input())
ano = int(n/365)
n = n - ano*365
mes = int(n/30)
dia = n - mes*30
print('%i ano(s)\n%i mes(es)\n%i dia(s)' %(ano, mes, dia))