from lista import Lista
from random import randint

lista_uno = Lista()
lista_dos = Lista()

for i in range(5):
    lista_uno.insertar(i)
    lista_dos.insertar(randint(1,10))

print('lista uno')
lista_uno.barrido()
print()
print('lista dos')
lista_dos.barrido()
print()

print()
repeticiones=0
for i in range(lista_dos.tamanio()):
    num = lista_dos.obtener_elemento(i)
    if(lista_uno.busqueda(num) == -1):
        lista_uno.insertar(num)
    else:
        repeticiones+=1

lista_uno.barrido()
print(repeticiones)
# for i in range(lista_dos.tamanio()):
#     num = lista_dos.obtener_elemento(i)
#     lista_uno.insertar(num)

# lista_uno.barrido()
print()
while(not lista_uno.lista_vacia()):
     print(lista_uno.eliminar(lista_uno.obtener_elemento(0)))