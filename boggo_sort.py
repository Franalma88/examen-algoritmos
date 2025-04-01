import random
import time

lista=[9,8,7,6,5,4,3,2,1]
intentos=0
inicio=time.time()
while True:
    orden=0
    for i in range(len(lista)-1):
            if lista[i]>lista[i+1]:
                random.shuffle(lista)
                intentos+=1
                orden=1
                break
    if orden==0:
        break
final=time.time()
print(f"Tras {intentos} intentos se ha ordenado {lista}")
print(f"El tiempo total es {final-inicio} segundos")