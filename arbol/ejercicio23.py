from arbol import Arbol
from ordenar import Ordenar
arbol=Arbol()

criatura = {'name': 'Ceto', 'derrotado': '-','descripcion':'-','capturado':'Trueno'}
arbol = arbol.insertar_nodo(criatura['name'], criatura)
criatura = {'name': 'Tifón', 'derrotado': 'Zeus','descripcion':'-','capturado':'Sol'}
arbol = arbol.insertar_nodo(criatura['name'], criatura)
criatura = {'name': 'Equidna', 'derrotado':'Argos Panoptes','descripcion':'-','capturado':'Mar' }
arbol = arbol.insertar_nodo(criatura['name'], criatura)
criatura = {'name': 'Enio', 'derrotado':'-' }
arbol = arbol.insertar_nodo(criatura['name'], criatura)
criatura = {'name': 'Medusa', 'derrotado':'Perseo','descripcion':'-' ,'capturado':'Trueno'}
arbol = arbol.insertar_nodo(criatura['name'], criatura)
criatura = {'name': 'Hidra de Lerna', 'derrotado':'Heracles','descripcion':'-' ,'capturado':'Trueno'}
arbol = arbol.insertar_nodo(criatura['name'], criatura)

arbol.inorden()

buscado = input('ingrese el nombre que desea agregar la descripcion ')
pos = arbol.busqueda(buscado)
if(pos):
    descripcion_nueva = input('ingrese la descripcion')
    pos.criatura['descripcion'] = descripcion_nueva
    
# arbol.inorden_talos()
# dic = {} 
# derrotado_por : cantidad
# arbol.conta_criaturas_derrotadas(dic)

arbol.inorden_heracle()
arbol.inorden_noderrota()

buscado = input('ingrese el nombre que desea cambiar quien atrapo ')
pos = arbol.busqueda(buscado)
if(pos):
    atrapo_nuevo = input('ingrese aqui')
    pos.criatura['capturado'] =atrapo_nuevo

buscado=input('ingrese el que quiera buscar')
arbol.busqueda_proximidad(buscado)

eliminado= input('ingrese el nombre que desea eliminar ')
pos=arbol.busqueda(eliminado)
if pos:
    arbol.eliminar_nodo(eliminado)

buscado = input('ingrese el nombre que desea cambiar  ')
pos = arbol.busqueda(buscado)
if(pos):
    modificacion = input('ingrese aqui')
    pos.criatura['derrotado'] =modificacion

nuevo_nombre = input('ingrese el nuevo nombre ')
nombre, criatura = arbol.eliminar_nodo(buscado)
criatura['name'] = nuevo_nombre
arbol = arbol.insertar_nodo(nuevo_nombre, criatura)

arbol.barrido_por_nivel()

dic = {}
arbol.conta_criaturas_derrotadas(dic) #punto d
print('LOS 3 DIOSES QUE DERROTARON MAYOR CANTIDAD DE CRIATURAS')
Ordenar(dic)