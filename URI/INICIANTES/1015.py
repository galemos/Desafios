from math import sqrt
linha1 = input()
linha2 = input()
x1, y1 = linha1.split(" ")
x2, y2 = linha2.split(" ")
x1,x2,y1,y2 = float(x1),float(x2),float(y1),float(y2)
distancia = sqrt((x2 - x1)**2 + (y2 - y1)**2)
print('%0.4f' %(distancia))