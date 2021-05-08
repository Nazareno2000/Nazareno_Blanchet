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



while(not Boba.pila_vacia()):
    x=Boba.desapilar()
    print(x.mision)
