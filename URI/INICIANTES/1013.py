linha = input()
a, b, c = linha.split(" ")
a, b, c = int(a),int(b),int(c)
mab = (a + b + abs( a - b)) / 2
maior = (mab + c + abs(mab - c)) / 2
print('%i eh o maior' %(maior))