from arbol import Arbol
from random import randint

arbol = Arbol()

for i in range(10):
    numero = randint(1000, 9999)
    arbol.insertar_nodo(numero)
contpares=0
contimpares=0
if (arbol.info%2==0):
     contpares+=1
else:
     contimpares+=1

print(contpares)
print(contimpares)  