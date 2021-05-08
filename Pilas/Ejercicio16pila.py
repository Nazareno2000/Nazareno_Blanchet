from pila import Pila

pila_star2=Pila()
pila_star3=Pila()
pila_star_actores=Pila()
pila_aux=Pila()

Pelicula1=["luke","chuwaka","jedy"]
Pelicula2=["luke","arturito","dark"]

for i in range(0,3):
    actores1=Pelicula1[i]
    actores2=Pelicula2[i]
   
    pila_star2.apilar(actores1)
   
    pila_star3.apilar(actores2)
while(not pila_star2.pila_vacia()):
    aux=pila_star2.desapilar()
    while(not pila_star3.pila_vacia()):
        aux2=pila_star3.desapilar()
        if (aux==aux2):
            pila_star_actores.apilar(aux)
        pila_aux.apilar(aux2)
    while(not pila_aux.pila_vacia()):
        pila_star3.apilar(pila_aux.desapilar())

while(not pila_star_actores.pila_vacia()):
       print (pila_star_actores.desapilar())
