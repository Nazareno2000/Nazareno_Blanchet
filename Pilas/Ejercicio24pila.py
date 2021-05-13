from pila import Pila
class Films(object):
    def __init__(self,Nombre,Cantidad):
        self.Nombre = Nombre
        self.Cantidad = Cantidad
    def __str__(self):
        return self.Nombre+ " " +self.Cantidad

pila_peliculas=Pila()
Peliculas=Films("Rocket Raccoon",3)
pila_peliculas.apilar(Peliculas)
Peliculas=Films("Saul",9)
pila_peliculas.apilar(Peliculas)
Peliculas=Films("Catman",7)
pila_peliculas.apilar(Peliculas)
Peliculas=Films("Groot",2)
pila_peliculas.apilar(Peliculas)
Peliculas=Films("Iron Man",5)
pila_peliculas.apilar(Peliculas)

BlackWidow=0
PosicionRocket=0
PosicionGroot=0
Iniciales=["C","D","G"]

while(not pila_peliculas.pila_vacia()):
    x=pila_peliculas.desapilar()
    if(x.Nombre=="Groot"  ):
       PosicionGroot=pila_peliculas.tamanio()
    else:
        if(x.Nombre=="Rocket Raccoon"):
            PosicionRocket=pila_peliculas.tamanio()
    if(x.Cantidad>5):
        print("Los actores que participaron en mas de 5 peliculas",x.Nombre)
        print("Y la cantidad total fueron " ,x.Cantidad)
    if(x.Nombre == "Black Widow"):
        BlackWidow=BlackWidow +1
    
    if(x.Nombre[0] in Iniciales):
        print("los actores que empiezan con esas letras son ",x.Nombre)

print("La posicion de la pelicula Rocket Raccoon es " ,PosicionRocket)     
print("La posicion de la pelicula Groot es " ,PosicionGroot)    
if(BlackWidow !=0):
    print("Black Widow participo en  ",BlackWidow,"peliculas") 
else:
    print("No participo")