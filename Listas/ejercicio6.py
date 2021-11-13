from lista import Lista

lista_super=Lista()

saga=[      {'name':'Black Widow','aparicion': 1960, 'casa de comic' : 'DC', 'biografia': 'garras'},
            {'name':'hulk','aparicion': 1965, 'casa de comic' : 'DC', 'biografia': 'traje'},
            {'name':'Rocket Racoonn','aparicion': 1960, 'casa de comic' : 'DC', 'biografia': 'garras'},
            {'name':'loki','aparicion': 1960, 'casa de comic' : 'DC', 'biografia': 'armadura'},
            {'name':'Capitana Marvel','aparicion': 1960, 'casa de comic' : 'Marvel', 'biografia': 'armadura'},
            {'name':'Mujer Maravilla','aparicion': 1960, 'casa de comic' : 'DC', 'biografia': 'armadura'},
            {'name':'Flash','aparicion': 1960, 'casa de comic' : 'Marvel', 'biografia': 'armadura'},
            {'name':'Star-Lord','aparicion': 1960, 'casa de comic' : 'DC', 'biografia': 'armadura'}        
             
             
        ]

for superheroes in saga:
    lista_super.insertar(superheroes,'name')




# lista_super.eliminar('Rocket Racoonn','name')

# lista_super.barrido_wolwerin()

# posBlackWidow=lista_super.busqueda('Black Widow','name')

# lista_super.obtener_elemento(posBlackWidow)['casa de comic']='marvel'

# lista_super.barrido()

# lista_super.barrido_traje()

# lista_super.barrido_aparicion()

# lista_super.barrido_mujeres()

# lista_super.barrido_flash()

# lista_super.barrido_con_letra_primera()

# lista_super.cantidad_super()