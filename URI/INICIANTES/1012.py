linha = input()
a, b, c = linha.split(" ")
a, b, c = float(a),float(b),float(c)
tri, cir, tra, qua, ret = (a*c)/2, 3.14159 * (c**2), ((a+b)*c)/2, b**2, a*b
print('TRIANGULO: %0.3f\nCIRCULO: %0.3f\nTRAPEZIO: %0.3f\nQUADRADO: %0.3f\nRETANGULO: %0.3f' %(tri, cir, tra, qua, ret))