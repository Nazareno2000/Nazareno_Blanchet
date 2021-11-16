from Grafo import Grafo

Esquema = Grafo(dirigido=False)


Esquema.insertar_vertice('switch1',data={'switch'})
Esquema.insertar_vertice('switch2',data={'switch'})
Esquema.insertar_vertice('router2',data={'router'})
Esquema.insertar_vertice('router1',data={'router'})
Esquema.insertar_vertice('router3',data={'router'})

Esquema.insertar_vertice('debian', data={'notebook'})
Esquema.insertar_vertice('arch',data={'notebook'})
Esquema.insertar_vertice('red hat',data={'notebook'})
Esquema.insertar_vertice('ubuntu', data={'pc'})
Esquema.insertar_vertice('mint',data={'pc'})
Esquema.insertar_vertice('fedora',data={'pc'})
Esquema.insertar_vertice('manjaro',data={'pc'})
Esquema.insertar_vertice('parrot',data={'pc'})
Esquema.insertar_vertice('impresora',data={'impresora'})
Esquema.insertar_vertice('mongodb',data={'servidor'})
Esquema.insertar_vertice('guarani',data={'servidor'})

Esquema.insertar_vertice('switch2',data='switch')
Esquema.insertar_vertice('router2',data='router')
Esquema.insertar_vertice('router1',data='router')



Esquema.insertar_arista(17, 'switch1', 'debian')
Esquema.insertar_arista(18, 'switch1', 'ubuntu')
Esquema.insertar_arista(22, 'switch1', 'impresora')
Esquema.insertar_arista(80, 'switch1', 'mint')
Esquema.insertar_arista(29, 'switch1', 'router1')


Esquema.insertar_arista(40, 'switch2', 'manjaro')
Esquema.insertar_arista(12, 'switch2', 'parrot')
Esquema.insertar_arista(5, 'switch2', 'mongodb')
Esquema.insertar_arista(56, 'switch2', 'arch')
Esquema.insertar_arista(3, 'switch2', 'fedora')
Esquema.insertar_arista(61, 'switch2', 'router3')

Esquema.insertar_arista(37, 'router2', 'router1')
Esquema.insertar_arista(50, 'router2', 'router3')
Esquema.insertar_arista(9, 'router2', 'guarani')
Esquema.insertar_arista(25, 'router2', 'red hat')

Esquema.insertar_arista(45, 'router1', 'router3')


# vertice_origen = Esquema.buscar_vertice('debian')
# vertice_destino = Esquema.buscar_vertice('mongodb')
# camino = Esquema.dijkstra(vertice_origen, vertice_destino)

# while(not camino.pila_vacia()):
#      dato = camino.desapilar()
#      print(dato)

# vertice_origen2 = Esquema.buscar_vertice('red hat')
# vertice_destino2 = Esquema.buscar_vertice('mongodb')
# print()

# camino2 = Esquema.dijkstra(vertice_origen2, vertice_destino2)

# while(not camino2.pila_vacia()):
#      dato1 = camino2.desapilar()
#      print(dato1)


# Esquema.eliminar_vertice('impresora')
# Esquema.barrido_profundidad(0)

# Esquema.prim()

vertice_origen3 = Esquema.buscar_vertice('red hat')
Esquema.barrido_amplitud(vertice_origen3)
Esquema.marcar_no_visitado()
Esquema.barrido_profundidad(vertice_origen3)
Esquema.marcar_no_visitado()
vertice_origen4 = Esquema.buscar_vertice('debian')
Esquema.barrido_amplitud(vertice_origen4)
Esquema.marcar_no_visitado()
Esquema.barrido_profundidad(vertice_origen4)
Esquema.marcar_no_visitado()
vertice_origen5 = Esquema.buscar_vertice('arch')
Esquema.barrido_amplitud(vertice_origen5)
Esquema.marcar_no_visitado()
Esquema.barrido_profundidad(vertice_origen5)
