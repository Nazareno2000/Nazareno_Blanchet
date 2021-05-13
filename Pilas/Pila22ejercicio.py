class Misiones(object):
    def __init__(self,mision,prisionero,costo):
        self.mision = mision
        self.prisionero = prisionero
        self.costo = costo
    def __str__(self):
        return self.mision + " " +self.prisionero+" "+self.costo
from pila import Pila
Boba=Pila()
Din=Pila()

misionesboba=Misiones("Urano","Han",1200)
Boba.apilar(misionesboba)
misionesboba=Misiones("Jupiter","Arturito",100)
Boba.apilar(misionesboba)

misionesdin=Misiones("Tierra","Chubaka",3000)
Din.apilar(misionesdin)
misionesdin=Misiones("Venus","Darth",4000)
Din.apilar(misionesdin)

gananciasBoba=0;
gananciasDin=0;
while(not Boba.pila_vacia() and not Din.pila_vacia()):
    x=Boba.desapilar()
    y=Din.desapilar()
    print(x.mision)
    print(y.mision)

    gananciasDin=gananciasDin + y.costo
    gananciasBoba=gananciasBoba + x.costo
    
if (gananciasBoba > gananciasDin):
    print(gananciasBoba)
else:
     print(gananciasDin)

misionesboba=Misiones("Urano","Han",1200)
Boba.apilar(misionesboba)
misionesboba=Misiones("Jupiter","Arturito",100)
Boba.apilar(misionesboba)

misionesdin=Misiones("Tierra","Chubaka",3000)
Din.apilar(misionesdin)
misionesdin=Misiones("Venus","Darth",4000)
Din.apilar(misionesdin)
PrisioneroDin=0
PrisioneroBoba=0
while(not Boba.pila_vacia() and not Din.pila_vacia()):
    
    y=Din.desapilar()
    x=Boba.desapilar()
    if (y.prisionero!=" "):
        PrisioneroDin= PrisioneroDin+1

    if( x.prisionero !=" " ):
        PrisioneroBoba= PrisioneroBoba +1
        if(x.prisionero=="Han"):
            print(Boba.tamanio())

print(PrisioneroDin)
print(PrisioneroBoba)

    