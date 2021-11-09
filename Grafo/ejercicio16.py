from grafo import Grafo

lugares= Grafo(dirigido=False)

lugares.insertar_vertice('Partenón',data={'latitud':199,'longitud':171})
lugares.insertar_vertice('Olimpia',data={'latitud':192,'longitud':172})
lugares.insertar_vertice('Olimpia2',data={'latitud':194,'longitud':174})
lugares.insertar_vertice('Delfos',data={'latitud':196,'longitud':175})
lugares.insertar_vertice('Sunión',data={'latitud':191,'longitud':176})
lugares.insertar_vertice('Éfeso',data={'latitud':190,'longitud':177})
lugares.insertar_vertice('Acrópolis',data={'latitud':197,'longitud':178})

lugares.insertar_arista(1, 'Partenón', 'Olimpia' )
lugares.insertar_arista(3, 'Olimpia', 'Olimpia2')
lugares.insertar_arista(5, 'Olimpia2', 'Delfos')
lugares.insertar_arista(6, 'Delfos', 'Sunión')
lugares.insertar_arista(2, 'Sunión', 'Éfeso')
lugares.insertar_arista(8, 'Éfeso', 'Acrópolis')

pos=lugares.buscar_vertice('Partenón')
print(lugares.prim(pos))


vertice_origen = lugares.buscar_vertice('Partenón')
vertice_destino = lugares.buscar_vertice('Olimpia2')

camino = lugares.dijkstra(vertice_origen, vertice_destino)

destino = 'Olimpia2'
costo = None
while(not camino.pila_vacia()):
    dato = camino.desapilar()
    if(dato[1][0] == destino):
        if(costo is None):
            costo = dato[0]
        print(dato[1][0])
        destino = dato[1][1]
print('el costo total del camino es:', costo)