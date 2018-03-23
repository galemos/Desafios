linha = input()
a, b, c = linha.split(" ")
a, b, c = float(a), float(b), float(c)
pi = 3.14159
tri = (a*c)/2
cir = pi * (c**2)
tra = ((a+b)*c)/2
qua = b**2
ret = a*b
print('TRIANGULO: %0.3f\nCIRCULO: %0.3f\nTRAPEZIO: %0.3f\nQUADRADO: %0.3f\nRETANGULO: %0.3f' %(tri, cir, tra, qua, ret))