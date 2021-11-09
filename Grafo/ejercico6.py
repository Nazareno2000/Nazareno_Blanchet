from grafo import Grafo

dioses = Grafo(dirigido=False)

dioses.insertar_vertice('Urano', data='asdasdsa')
dioses.insertar_vertice('Cronos')
dioses.insertar_vertice('Rea')
dioses.insertar_vertice('Zeus')
dioses.insertar_vertice('Hades')
dioses.insertar_vertice('Demeter')
dioses.insertar_vertice('Atenea')
dioses.insertar_vertice('Apollo')
dioses.insertar_vertice('Persefone')

dioses.insertar_arista(1, 'Urano', 'Cronos', data={'relacion': ['padre', 'hijo']})

dioses.insertar_arista(1, 'Cronos', 'Zeus', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Cronos', 'Hades', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Cronos', 'Demeter', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Cronos', 'Rea', data={'relacion': ['pareja']})
dioses.insertar_arista(1, 'Cronos', 'Rea', data={'relacion': ['hermano']})

dioses.insertar_arista(1, 'Zeus', 'Hades', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Zeus', 'Atenea', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Zeus', 'Apollo', data={'relacion': ['padre', 'hijo']})

dioses.insertar_arista(1, 'Demeter', 'Persefone', data={'relacion': ['madre', 'hijo']})
origen = dioses.buscar_vertice('Cronos')
dioses.barrido_amplitud(origen)
print()


# for i in range(dioses.inicio.tamanio()):
#     dios = dioses.inicio.obtener_elemento(i)
#     print('aristas', dios['info'])
#     for j in range(dios['aristas'].tamanio()):
#         print(dios['aristas'].obtener_elemento(j))

#     print()

origen = dioses.buscar_vertice('Cronos')
dios = dioses.inicio.obtener_elemento(origen)
print('aristas', dios['info'])
for j in range(dios['aristas'].tamanio()):
    arista = dios['aristas'].obtener_elemento(j)
    if(len(arista['data']['relacion']) == 2):
        if(arista['data']['relacion'][1] == 'hijo'):
            print(arista)
print()
origen = dioses.buscar_vertice('Cronos')
dios = dioses.inicio.obtener_elemento(origen)
print('aristas', dios['info'])
for j in range(dios['aristas'].tamanio()):
    arista = dios['aristas'].obtener_elemento(j)
    if(len(arista['data']['relacion']) == 2):
        if(arista['data']['relacion'][1] == 'padre'):
            print(arista)

print()
origen = dioses.buscar_vertice('Cronos')
dios = dioses.inicio.obtener_elemento(origen)
print('aristas', dios['info'])
for j in range(dios['aristas'].tamanio()):
    arista = dios['aristas'].obtener_elemento(j)
    if(arista['data']['relacion'][0] == 'hermano'):
        print(arista)

print()
origen = dioses.buscar_vertice('Cronos')
dios = dioses.inicio.obtener_elemento(origen)
print('aristas', dios['info'])
for j in range(dios['aristas'].tamanio()):
    arista = dios['aristas'].obtener_elemento(j)
    if(arista['destino'] == 'Zeus'):
        print(arista)


''' vertice_origen = dioses.buscar_vertice('Urano')
vertice_destino = dioses.buscar_vertice('Atenea')

camino = dioses.dijkstra(vertice_origen, vertice_destino)

destino = 'Atenea'
costo = None
while(not camino.pila_vacia()):
    dato = camino.desapilar()
    if(dato[1][0] == destino):
        if(costo is None):
            costo = dato[0]
        print(dato[1][0])
        destino = dato[1][1]
print('el costo total del camino es:', costo)

def relacion(vertice_origen,vertice_destino):
    pos=dioses.buscar_arista(vertice_origen,vertice_destino)
    if (pos != 1):
        pos_aux=dioses.buscar_vertice('Zeus')
        print(dioses.inicio.obtener_elemento(pos_aux)['aristas'].obtener_elemento(pos))
    

resultado_relacion=dioses.es_adyacente('Zeus','Cronos')
if (resultado_relacion):
    print('hay relacion directa')
    relacion('Zeus','Cronos')

else:
    print('negativo')

dioses.barrido_profundidad()
dioses.barrido_amplitud() 

def relaciones():
    """devuelve relacion especifica"""
    buscado = input('ingrese dios ')
    relacion = input('ingrese relacion que desea consultar ')
    origen = dioses.buscar_vertice(buscado)
    if (origen != -1):
        dios = dioses.inicio.obtener_elemento(origen)
        for i in range(dios['aristas'].tamanio()):
            dio = dios['aristas'].obtener_elemento(i)
            if(relacion in dio['data']['relacion'][-1] ):
                  print(dio['destino'])
    else:
        print('dios no encontrado')

relaciones() '''
print('barrido madre',dioses.tamanio())
dioses.marcar_no_visitado()
dioses.barrido_amplitud_madre(0)

def ancestro(vertice_nombre):
    origen = dioses.buscar_vertice(vertice_nombre)
    if(origen != -1):
        dios = dioses.inicio.obtener_elemento(origen)
        for i in range(dios['aristas'].tamanio()):
            nombre_dios = dios['aristas'].obtener_elemento(i)['destino']
            dios_aux = dios['aristas'].obtener_elemento(i)['data']
            if(len(dios_aux['relacion']) > 1):
                if(dios_aux['relacion'][1] == 'padre' or dios_aux['relacion'][1] == 'madre'):
                    print(nombre_dios, dios_aux['relacion'])
                    ancestro(nombre_dios)


