from lista import Lista
lista = Lista()
file = open('jedis.txt')

lineas = file.readlines()
lineas.pop(0)

def cargar():
    for linea in lineas:
        jedi = linea.split(';')
        jedi_data = {}
        jedi_data['name'] = jedi[0].title()
        jedi_data['rank'] = jedi[1]
        jedi_data['species'] = jedi[2]
        jedi_data['master'] = jedi[3].split('/')
        jedi_data['lightsaber_color'] = jedi[4].split('/')
        jedi_data['homeworld'] = jedi[5]
        jedi_data['birth_year'] = jedi[6]
        jedi_data['height'] = float(jedi[7].split('\n')[0])
        if(len(jedi) > 8):
            jedi_data['to_darkside'] = jedi[8]
            jedi_data['come_lightside'] = jedi[9]
        lista.insertar(jedi_data, 'species')
        

def AhsokaTano_KitFisto():
    
    pos_ahsoka = lista.busqueda('Ahsoka Tano', 'name')
    print(lista.obtener_elemento(pos_ahsoka))
    pos_kit = lista.busqueda('Kit Fisto', 'name')
    print(lista.obtener_elemento(pos_kit))


def Yoda_LukeSkywalker():
   
    pos_yoda = lista.busqueda('Yoda', 'name')
    print('MAESTROS DE YODA: ', lista.obtener_elemento(pos_yoda)['master'])
    pos_luke = lista.busqueda('Luke Skywalker','name') 
    print('MAESTROS DE LUKE: ', lista.obtener_elemento(pos_luke)['master'])


def EspecieHumana_Twilek():
    
    for i in range(lista.tamanio()):
        aux = lista.obtener_elemento(i)
        if (aux['species'] == 'human'):
            print(aux['name'],' ES ESPECIE HUMANA')
        elif(aux['species'] == 'twi´lek'):
            print(aux['name'],' ES ESPECIE TWI´LEK')


def empiezan_a():
    
    for i in range(lista.tamanio()):
        aux = lista.obtener_elemento(i)
        if(aux['name'][0] == 'A'):
            print(aux['name'])


def sable_mas_uncolor():
    
    for i in range(lista.tamanio()):
        aux = lista.obtener_elemento(i)
        if(len(aux['lightsaber_color']) > 1):
            print(aux['name'])


def sables():
    
    for i in range(lista.tamanio()):
        aux = lista.obtener_elemento(i)
        if (('yellow' in aux['lightsaber_color']) or ('purple' in aux['lightsaber_color'])):
            print(aux['name'])


def QuiGonJin_MaceWindu():
    pos_qui = lista.busqueda('Qui-Gon Jin', 'name')
    pos_mace = lista.busqueda('Mace Windu', 'name')
    if (pos_qui != -1):
        print('MAESTROS DE QUIN GON JIN: ', lista.obtener_elemento(pos_qui)['master'])
    if (pos_mace != -1):
        print('MAESTROS DE MACE WINDU : ',lista.obtener_elemento(pos_mace)['master'])


cargar()
lista.barrido()
print('--')
lista.ordenar('name')
lista.barrido()
AhsokaTano_KitFisto()
Yoda_LukeSkywalker()
EspecieHumana_Twilek()
empiezan_a()
print('USARON SABLE MAS DE UN COLOR')
sable_mas_uncolor()
print('JEDI QUE UTILIZARON SABLES AMARILLO O VIOLETA')
sables()
QuiGonJin_MaceWindu()