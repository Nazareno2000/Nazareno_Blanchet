from pila import Pila

pila_datos=Pila()
pila_aux=Pila()

numeros = [0, 3, 1, 7, 2, 10]

for i in range(0,6):
    num=numeros[i]
    if (pila_datos.pila_vacia()):
        pila_datos.apilar(num)
    else:
        if (num > pila_datos.elemento_cima()):
            pila_datos.apilar(num)
        else:
            while (not pila_datos.pila_vacia() and pila_datos.elemento_cima()>num):
                pila_aux.apilar(pila_datos.desapilar())
            pila_datos.apilar(num) 
            while(not pila_aux.pila_vacia()):
                pila_datos.apilar(pila_aux.desapilar())
 
                  
while(not pila_datos.pila_vacia()):
       print(pila_datos.desapilar() + "ale sos mi hijo en el burako")
            