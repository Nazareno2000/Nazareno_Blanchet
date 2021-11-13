from lista import Lista
from random import randint

lista=Lista()

for i in range(5):
    lista.insertar(randint(0,100))
lista.barrido()
print()
for i in range(lista.tamanio()):
    contador=0
    if (i<lista.tamanio()):
        num=lista.obtener_elemento(i)
        if (num==1):
            lista.eliminar(num)
        for j in range(2,num+1):
            if (num % j ==0):
                contador+=1
        
        if (contador==1):
            lista.eliminar(num)
            
lista.barrido()