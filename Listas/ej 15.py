from lista import Lista
lista_entrenadores = Lista()

entrenadores = [
     {'name':'naza','torneos_ganados': 1, 'batallas_perdidas' : 3, 'batallas_ganadas': 320, 'pokemons': Lista()},
     {'name':'jose','torneos_ganados': 5, 'batallas_perdidas' : 9, 'batallas_ganadas': 202, 'pokemons': Lista()},
     {'name':'federico','torneos_ganados': 8, 'batallas_perdidas' : 5, 'batallas_ganadas': 128, 'pokemons': Lista()},
]

pokemons_1_naza = {'name':'pikachu', 'nivel': 120 ,'tipo':'electrico', 'subtipo':'metal' }
pokemons_2_naza = {'name':'pikachu23', 'nivel': 128 ,'tipo':'aire','subtipo':'volador'}
pokemons_3_naza = {'name':'pikachu67', 'nivel':30 ,'tipo':'fuego'  ,'subtipo':'terreno' }


pokemons_1_jose = {'name':'bulbasur'  , 'nivel': 2 ,'tipo':'agua'  ,'subtipo':'pez' }
pokemons_2_jose =  {'name':'rocky' , 'nivel': 14 ,'tipo':'peleador'  ,'subtipo':'terrestre' }


pokemons_1_federico = {'name':'vechain,'  , 'nivel': 128 ,'tipo':'fuego'  ,'subtipo':'planta' }
pokemons_2_federico =   {'name':'rune' , 'nivel': 1 ,'tipo':'agua','subtipo':'volador' }
pokemons_3_federico  =  {'name':'grt' , 'nivel':33  ,'tipo':'fuego'  ,'subtipo':'terreno' }


for entrenador in entrenadores:
    lista_entrenadores.insertar(entrenador, 'name')


pos_naza = lista_entrenadores.busqueda('naza', 'name')
pos_jose = lista_entrenadores.busqueda('jose', 'name')
pos_federico = lista_entrenadores.busqueda('federico', 'name')

lista_entrenadores.obtener_elemento(pos_naza)['pokemons'].insertar(pokemons_1_naza,'name')
lista_entrenadores.obtener_elemento(pos_naza)['pokemons'].insertar(pokemons_2_naza,'name')
lista_entrenadores.obtener_elemento(pos_naza)['pokemons'].insertar(pokemons_3_naza,'name')

lista_entrenadores.obtener_elemento(pos_jose)['pokemons'].insertar(pokemons_1_jose,'name')
lista_entrenadores.obtener_elemento(pos_jose)['pokemons'].insertar(pokemons_2_jose,'name')

lista_entrenadores.obtener_elemento(pos_federico)['pokemons'].insertar(pokemons_1_federico,'name')
lista_entrenadores.obtener_elemento(pos_federico)['pokemons'].insertar(pokemons_2_federico,'name')
lista_entrenadores.obtener_elemento(pos_federico)['pokemons'].insertar(pokemons_3_federico,'name')

def barrido_pokemons():
    for i in range(lista_entrenadores.tamanio()):
        aux = lista_entrenadores.obtener_elemento(i)
        print('pokemons del entrenador ',aux['name'])
        print(aux['pokemons'].barrido())

#PUNTO A
def buscar_entrenador():
    return input('ingrese entrenador a buscar: ')

def buscar_pokemons():
    return input('ingrese pokemons a buscar: ')

def cantidad_pokemons():
    aux_entrenador = buscar_entrenador()
    pos_buscado = lista_entrenadores.busqueda(aux_entrenador,'name') 
    if (pos_buscado != -1):
        cant_pokemons = lista_entrenadores.obtener_elemento(pos_buscado)['pokemons'].tamanio()
        print('LA CANTIDAD DE POKEMONES DE ',aux_entrenador,' ES: ', cant_pokemons)
    else:
        print('ENTRENADOR NO ENCONTRADO')

#PUTNO B 
def ent_mas_3_torneos():
    
    for i in range(lista_entrenadores.tamanio()):
        aux = lista_entrenadores.obtener_elemento(i)
        if (aux['torneos_ganados'] > 3):
            print(aux['name'])

def mayor_nivel():
    """devuelve el pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados"""
    mayor = 0
    mayor_nivel = 0
    for i in range(lista_entrenadores.tamanio()):
        aux = lista_entrenadores.obtener_elemento(i)
        if (aux['torneos_ganados'] > mayor):
            mayor = aux['torneos_ganados']
            posicion_entrenador = i
    entrenador_mayor = lista_entrenadores.obtener_elemento(posicion_entrenador)
    print('EL ENTRENADOR CON MAYOR CANTIDAD DE TORNEOS GANADOS ES: ',entrenador_mayor['name'])
    for i in range(entrenador_mayor['pokemons'].tamanio()):
        aux = entrenador_mayor['pokemons'].obtener_elemento(i)
        if(aux['nivel']> mayor_nivel):
            mayor_nivel = aux['nivel']
            aux_nombre = aux['name']
    print('POKEMONS DE MAYOR NIVEL ES: ', aux_nombre)
    

# PUNTO D
def entrenador():
    """devuelve datos de un entrenador y sus pokemons"""
    aux_nombre = buscar_entrenador()
    pos_entrenador = lista_entrenadores.busqueda(aux_nombre, 'name')
    if (pos_entrenador != -1):
        elemento = lista_entrenadores.obtener_elemento(pos_entrenador)
        print('SUS DATOS ')
        print(elemento)
        print('SUS POKEMONES')
        print(elemento['pokemons'].barrido())
    else:
        print('EL ENTRENADOR NO SE ENCUENTRA')

#PUNTO E
def batallas_ganadas():
    cont=0
    """muestra entrenadores con batallas ganadas mayor a 79%"""
    for i in range(lista_entrenadores.tamanio()):
        cantidad_batallas = 0
        aux = lista_entrenadores.obtener_elemento(i)
        cantidad_batallas = aux['batallas_ganadas'] + aux['batallas_perdidas']
        if ((aux['batallas_ganadas']/cantidad_batallas*100) > 79):
            print(aux['name'])
            cont+= 1

#PUNTO F
def pokemons_tipo():
    """entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador(tipo y subtipo)"""
    for i in range(lista_entrenadores.tamanio()):
        aux_ent = lista_entrenadores.obtener_elemento(i)
        print(aux_ent['name'],' TIENE POKEMONS: ')
        for i in range(aux_ent['pokemons'].tamanio()):
            aux_pok = aux_ent['pokemons'].obtener_elemento(i)
            if ((aux_pok['tipo'] == 'fuego') and (aux_pok['subtipo'] == 'planta')):
                print(' fuego/planta')
            elif((aux_pok['tipo'] == 'agua') and (aux_pok['subtipo'] == 'volador')):
                print(' agua/volador')

#PUNTO G
def nivel_pokemons():
        """muestra promedio de nivel de los Pokémons de un determinado entrenador"""
        acu_niveles = 0
        pos_ent = lista_entrenadores.busqueda(buscar_entrenador(), 'name')
        if (pos_ent != -1):
            aux_ent = lista_entrenadores.obtener_elemento(pos_ent)
            for i in range(aux_ent['pokemons'].tamanio()):
                aux_pok = aux_ent['pokemons'].obtener_elemento(i)
                acu_niveles = acu_niveles + aux_pok['nivel']
            print(acu_niveles/aux_ent['pokemons'].tamanio())

#PUNTO H
def entrenadores_pokemons():
    """determina cuántos entrenadores tienen a un determinado Pokémon"""
    cantidad_entrenadores = 0
    nombre_pokemons = buscar_pokemons()
    for i in range(lista_entrenadores.tamanio()):
        aux = lista_entrenadores.obtener_elemento(i)
        busqueda = aux['pokemons'].busqueda(nombre_pokemons,'name')
        if (busqueda != -1):
            cantidad_entrenadores +=1 
    print('LA CANTIDAD DE ENTRENADORES QUE TIENEN AL POKEMONS ',nombre_pokemons, 'es: ',cantidad_entrenadores)

#PUNTO I
def ent_pokemones_repetidos():
    """mostrar los entrenadores que tienen Pokémons repetidos"""
    vector = [] #cargo los pokemones de un entrenador para que no se repita a la hora de comparar
    for i in range(lista_entrenadores.tamanio()):
        aux_ent = lista_entrenadores.obtener_elemento(i)
        vector = []
        for i in range(aux_ent['pokemons'].tamanio()):
            contador = 0
            aux_pok = aux_ent['pokemons'].obtener_elemento(i)['name']
            if (aux_pok not in vector):
                vector.append(aux_pok)
                for j in range(aux_ent['pokemons'].tamanio()):
                    aux_pok2 = aux_ent['pokemons'].obtener_elemento(j)['name']
                    if(aux_pok == aux_pok2):
                        contador+= 1
                if (contador != 1):
                    print('EL ENTRENADOR ',aux_ent['name'],' TIENE REPETIDO AL POKEMONS: ',aux_pok)

#PUNTO j
def entrenadores():
    """muestra entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull"""
    vector = ['tyrantrum', 'terrakion', 'wingull']
    for i in range(lista_entrenadores.tamanio()):
        aux_ent = lista_entrenadores.obtener_elemento(i)
        vector_pokemons = [] #cargo pokemones de un entrenador para que no se repitan y lo evalue dos veces
        for i in range(aux_ent['pokemons'].tamanio()):
            aux_pok = aux_ent['pokemons'].obtener_elemento(i)['name']
            if (aux_pok not in vector_pokemons):
                vector_pokemons.append(aux_pok)
                if(aux_pok in vector):
                    print(aux_ent['name'],' TIENE AL POKEMONS ',aux_pok)


#PUNTO k
def consulta_entrenadores_pokemons():
    pos_ent = lista_entrenadores.busqueda(buscar_entrenador(),'name')
    if (pos_ent != -1):
        aux_ent = lista_entrenadores.obtener_elemento(pos_ent)
        pos_pok = aux_ent['pokemons'].busqueda(buscar_pokemons(),'name')
        if (pos_pok != -1):
            aux_pok = aux_ent['pokemons'].obtener_elemento(pos_pok)
            print('ENTRENADOR')
            print(aux_ent)
            print('SU POKEMONS')
            print(aux_pok)
        else:
            print('POKEMONS NO ENCONTRADO')
    else:
        print('ENTRENADOR NO ENCONTRADO')


cantidad_pokemons()
print('entrenadores con mas de 3 torneos ganados')
ent_mas_3_torneos()
mayor_nivel()
entrenador()
batallas_ganadas()
pokemons_tipo()
nivel_pokemons()
entrenadores_pokemons()
ent_pokemones_repetidos()
entrenadores()
consulta_entrenadores_pokemons()