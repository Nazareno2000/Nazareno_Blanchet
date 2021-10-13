from arbol import Arbol
from random import randint

arbol = Arbol()

for i in range(10):
    numero = randint(1, 9999)
    arbol.insertar_nodo(numero)

arbol.preorden()
arbol.inorden()
arbol.postorden()

pos1=arbol.busqueda(10)
pos2=arbol.busqueda(13)
pos3=arbol.busqueda(14)
if pos1 and pos2 and pos3: 
        print('elemto encontrado')
        pos1.info.eliminar_nodo()
        pos2.info.eliminar_nodo()
        pos2.infoe.liminar_nodo()
        pos3.info.eliminar_nodo()
else:
    print('no encontrado')
