from arbol import Arbol

ArbolNombre=Arbol()
ArbolCodigo=Arbol()

dinosaurio = {'name': 't-rex', 'codigo': 12345,'zona':'7A'}
ArbolNombre = ArbolNombre.insertar_nodo(dinosaurio['name'], dinosaurio)
ArbolCodigo = ArbolCodigo.insertar_nodo(dinosaurio['codigo'], dinosaurio)
dinosaurio = {'name': 't-rex', 'codigo': 12346,'zona':'7A'}
ArbolNombre = ArbolNombre.insertar_nodo(dinosaurio['name'], dinosaurio)
ArbolCodigo = ArbolCodigo.insertar_nodo(dinosaurio['codigo'], dinosaurio)
dinosaurio = {'name': 't-rex', 'codigo': 12347,'zona':'7A'}
ArbolNombre = ArbolNombre.insertar_nodo(dinosaurio['name'], dinosaurio)
ArbolCodigo = ArbolCodigo.insertar_nodo(dinosaurio['codigo'], dinosaurio)
dinosaurio = {'name': 'hipopus', 'codigo': 792,'zona':'5A'}
ArbolNombre = ArbolNombre.insertar_nodo(dinosaurio['name'], dinosaurio)
ArbolCodigo = ArbolCodigo.insertar_nodo(dinosaurio['codigo'], dinosaurio)
dinosaurio = {'name': 'hipopus', 'codigo': 123,'zona':'57A'}
ArbolNombre = ArbolNombre.insertar_nodo(dinosaurio['name'], dinosaurio)
ArbolCodigo = ArbolCodigo.insertar_nodo(dinosaurio['codigo'], dinosaurio)
dinosaurio = {'name': 'Diplodocus', 'codigo': 1666,'zona':'17A'}
ArbolNombre = ArbolNombre.insertar_nodo(dinosaurio['name'], dinosaurio)
ArbolCodigo = ArbolCodigo.insertar_nodo(dinosaurio['codigo'], dinosaurio)
dinosaurio = {'name': 'Diplodocus', 'codigo': 12362,'zona':'17A'}
ArbolNombre = ArbolNombre.insertar_nodo(dinosaurio['name'], dinosaurio)
ArbolCodigo = ArbolCodigo.insertar_nodo(dinosaurio['codigo'], dinosaurio)
dinosaurio = {'name': 'barney', 'codigo': 34343,'zona':'70A'}
ArbolNombre = ArbolNombre.insertar_nodo(dinosaurio['name'], dinosaurio)
ArbolCodigo = ArbolCodigo.insertar_nodo(dinosaurio['codigo'], dinosaurio)
dinosaurio = {'name': 'barney', 'codigo': 9876,'zona':'70A'}
ArbolNombre = ArbolNombre.insertar_nodo(dinosaurio['name'], dinosaurio)
ArbolCodigo = ArbolCodigo.insertar_nodo(dinosaurio['codigo'], dinosaurio)
dinosaurio = {'name': 'barney', 'codigo': 123,'zona':'70A'}
ArbolNombre = ArbolNombre.insertar_nodo(dinosaurio['name'], dinosaurio)
ArbolCodigo = ArbolCodigo.insertar_nodo(dinosaurio['codigo'], dinosaurio)
dinosaurio = {'name': 'raptores', 'codigo': 1245,'zona':'3A'}
ArbolNombre = ArbolNombre.insertar_nodo(dinosaurio['name'], dinosaurio)
ArbolCodigo = ArbolCodigo.insertar_nodo(dinosaurio['codigo'], dinosaurio)
dinosaurio = {'name': 'Sgimoloch', 'codigo': 2345,'zona':'2A'}
ArbolNombre = ArbolNombre.insertar_nodo(dinosaurio['name'], dinosaurio)
ArbolCodigo = ArbolCodigo.insertar_nodo(dinosaurio['codigo'], dinosaurio)
dinosaurio = {'name': 'titanoboa', 'codigo': 1345,'zona':'9A'}
ArbolNombre = ArbolNombre.insertar_nodo(dinosaurio['name'], dinosaurio)
ArbolCodigo = ArbolCodigo.insertar_nodo(dinosaurio['codigo'], dinosaurio)
dinosaurio = {'name': 'raptores', 'codigo': 12000,'zona':'3A'}
ArbolNombre = ArbolNombre.insertar_nodo(dinosaurio['name'], dinosaurio)
ArbolCodigo = ArbolCodigo.insertar_nodo(dinosaurio['codigo'], dinosaurio)
dinosaurio = {'name': 'velociraptor', 'codigo': 12999,'zona':'10A'}
ArbolNombre = ArbolNombre.insertar_nodo(dinosaurio['name'], dinosaurio)
ArbolCodigo = ArbolCodigo.insertar_nodo(dinosaurio['codigo'], dinosaurio)


# ArbolNombre.inorden()


# pos = ArbolCodigo.busqueda('792')
# if(pos):
#      print(pos.datos)
# ArbolNombre.inorden_792()

# ArbolNombre.inorden_T_REX()



# pos = ArbolNombre.busqueda('Sgimoloch')
# if(pos):
#     nuevo_nombre = 'Stygimoloch'
#     pos.dinosaurio['name'] =nuevo_nombre

# ArbolNombre.inorden_raptores()
print(ArbolNombre.contar_Diplodocus())