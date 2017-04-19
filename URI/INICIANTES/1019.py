tempo = int(input())
horas = int(tempo/3600)
tempo = tempo - horas*3600
minutos = int(tempo/60)
segundos = tempo - minutos*60
print('%i:%i:%i' %(horas, minutos, segundos))