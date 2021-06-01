from cola import Cola

cola = Cola()
cola2 = Cola()
cola_aux = Cola()

cola.arribo(1)
cola.arribo(5)
cola.arribo(9)
cola.arribo(20)

cola2.arribo(4)
cola2.arribo(8)
cola2.arribo(11)
cola2.arribo(89)

while (not cola.cola_vacia() and not cola2.cola_vacia()):
    aux = cola.atencion()
    aux2 = cola2.atencion()
    if (aux  >  aux2):   
        cola_aux.arribo(aux)
        cola_aux.arribo(aux2)
    elif (aux  <  aux2):   
        cola_aux.arribo(aux)
        cola_aux.arribo(aux2)
    else:
        cola_aux.arribo(aux)
        cola_aux.arribo(aux2)

while (not cola_aux.cola_vacia()):
    print(cola_aux.atencion())