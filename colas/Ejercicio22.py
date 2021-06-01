
class Personajes(object):
    def __init__(self,nombre,personaje,genero):
        self.nombre = nombre
        self.personaje = personaje
        self.genero = genero
        
    def __str__(self):
        return self.nombre + " " +self.personaje +""+self.genero

from cola import Cola     
cola=Cola()
actores=Personajes("tony stark","iron man","m")
cola.arribo(actores)
actores=Personajes("Steve Rogers", "Capitán América"," m ")
cola.arribo(actores)
actores=Personajes("scott lang","linterna verde"," m ")
cola.arribo(actores)
actores=Personajes("shaq","ironil"," f ")
cola.arribo(actores)

cantidad = cola.tamanio()
posicion = 0
nombre=""
while(not cola.cola_vacia()):
    x=cola.atencion()
    if (x.personaje =="Capitán América"):
        nombre=x.nombre
    if(x.genero=="f"):
        print(x.nombre)  
    if(x.nombre=="scott lang"):
        personaje=x.personaje 
    if(x.nombre[0]=="s" or x.personaje[0]=="s"):
        print(x)
    if(x.nombre=="Carol Danvers"):
        print(x.personaje)
    else:
        print("no se encuentra")

print("el nombre del personaje de Capitan america es ",nombre)
print("el personaje de scott lang ", personaje)