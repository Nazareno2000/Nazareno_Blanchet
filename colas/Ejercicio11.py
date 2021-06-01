
class Personajes(object):
    def __init__(self,nombre,planeta):
        self.nombre = nombre
        self.planeta = planeta
        
    def __str__(self):
        return self.nombre + " " +self.planeta
from cola import Cola        
cola=Cola()
cola_aux=Cola()
cantidad = cola.tamanio()
posicion = 0;
actores=Personajes("Luke Skywalker","Alderaan")
cola.arribo(actores)
actores=Personajes("yoda","Endor")
cola.arribo(actores)
actores=Personajes("Han Sol","Tatooine")
cola.arribo(actores)
actores=Personajes("Jar Jar Binks","martes")
cola.arribo(actores)
actores=Personajes("Ema","Jupiter")
cola.arribo(actores)
actor_nuevo=Personajes("Naza","tierra")
while(not cola.cola_vacia()):
    x=cola.atencion()
    if (x.planeta=="Alderaan" or x.planeta=="Endor" or x.planeta=="Tatooine"):
        print(x.nombre)
    if (x.nombre =="Luke Skywalker" or x.nombre=="Han Solo"):
        print(x.planeta)

actores=Personajes("Luke Skywalker","Alderaan")
cola.arribo(actores)
actores=Personajes("yoda","Endor")
cola.arribo(actores)
actores=Personajes("Han Sol","Tatooine")
cola.arribo(actores)
actores=Personajes("Jar Jar Binks","martes")
cola.arribo(actores)
actores=Personajes("Ema","Jupiter")
cola.arribo(actores)
cantidad = cola.tamanio()
posicion = 0;

while(posicion <= cantidad):
    x=cola.en_frente() 
    if (x.nombre == "yoda"):
        cola.arribo(actor_nuevo)
        cola.mover_final()
    else:
        cola.mover_final()
        
    posicion+=1

cont=0
while(not cola.cola_vacia()):
    
    x=cola.atencion() 
    if (cont!= 0):
        print("")
    else:
        if(x.nombre !="Jar Jar Binks"):
            cola_aux.arribo(x)
        else:
            cola_aux.arribo(x)
            cont+=1


while(not cola_aux.cola_vacia()):
    x=cola_aux.atencion()
    print(x.nombre)
while(not cola.cola_vacia()):
    x=cola.atencion()
    print(x.nombre)
    
           
