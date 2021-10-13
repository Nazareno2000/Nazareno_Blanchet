from arbol import Arbol


arbol=Arbol()
arbolVillano=Arbol()
arbolSuper=Arbol()

superheroe = {'name': 'Doctor Strange', 'villano': True}
arbol = arbol.insertar_nodo(superheroe['name'], superheroe)
superheroe = {'name': 'Loki', 'villano': True}
arbol = arbol.insertar_nodo(superheroe['name'], superheroe)
superheroe = {'name': 'Hulk', 'villano': False}
arbol = arbol.insertar_nodo(superheroe['name'], superheroe)
superheroe = {'name': 'Capitan america', 'villano': False}
arbol = arbol.insertar_nodo(superheroe['name'], superheroe)
superheroe = {'name': 'Lagerta', 'villano': False}
arbol = arbol.insertar_nodo(superheroe['name'], superheroe)
superheroe = {'name': 'Mike tyson', 'villano': True}
arbol = arbol.insertar_nodo(superheroe['name'], superheroe)

#arbol.inorden_villano()
#arbol.inorden_heroes_con_c()
print(arbol.contar_superheroes())
# buscado=input('ingrese el que quiera buscar')
# arbol.busqueda_proximidad(buscado)
# print()
# buscado=input('ingres el nombre que desea modificar')
# pos=arbol.busqueda(buscado)
# if (pos):
#     nuevo_nombre=input('ingrese el nuevo nombre')
#     pos.datos['name']=nuevo_nombre 
arbol.dos_arboles(arbolSuper,arbolVillano)
# arbolSuper.inorden()
# arbolVillano.inorden()
print(arbolSuper.contar_nodos())