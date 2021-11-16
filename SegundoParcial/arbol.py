
from cola import Cola
class Arbol(object):

    
    def __init__(self, info=None, datos=None,frecuencia=None):
        self.info = info
        self.datos = datos
        self.der = None
        self.izq = None
        self._altura = 0
        self.frecuencia=frecuencia

    def arbol_vacio(self):
        return self.info is None
    
    def altura(self, arbol):
        if(arbol is None):
            return -1
        else:
            return arbol._altura

    def actualizar_altura(self):
        if(self is not None):
            altura_izq = self.altura(self.izq)
            altura_der = self.altura(self.der)
            self._altura = (altura_izq if altura_izq > altura_der else altura_der) + 1
    
    def rotacion_simple(self, control):
        if(control):
            aux = self.izq
            self.izq = aux.der
            aux.der = self
        else:
            aux = self.der
            self.der = aux.izq
            aux.izq = self
        self.actualizar_altura()
        aux.actualizar_altura()
        return aux

    def rotacion_doble(self, control):
        if(control):
            self.izq = self.izq.rotacion_simple(False)
            self = self.rotacion_simple(True)
        else:
            self. der = self.der.rotacion_simple(True)
            self = self.rotacion_simple(False)
        return self

    def balancear(self):
        if(self is not None):
            if(self.altura(self.izq)-self.altura(self.der) == 2):
                if(self.altura(self.izq.izq) >= self.altura(self.izq.der)):
                    self = self.rotacion_simple(True)
                else:
                    self = self.rotacion_doble(True)
            elif(self.altura(self.der)-self.altura(self.izq) == 2):
                if(self.altura(self.der.der) >= self.altura(self.der.izq)):
                    self = self.rotacion_simple(False)
                else:
                    self = self.rotacion_doble(False)
        return self

    def insertar_nodo(self, dato, datos=None):
        if(self.info is None):
            self.info = dato
            self.datos = datos
        elif(dato < self.info):
            if(self.izq is None):
                self.izq = Arbol(dato,datos)
            else:
                self.izq = self.izq.insertar_nodo(dato, datos)
        else:
            if(self.der is None):
                self.der = Arbol(dato,datos)
            else:
                self.der = self.der.insertar_nodo(dato, datos)
        self = self.balancear()
        self.actualizar_altura()
        return self

    def inorden(self):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.inorden()
            print(self.datos)
            if(self.der is not None):
                self.der.inorden()

    def inorden_villano(self):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.inorden_villano()
            if self.datos['villano']==True:
                    print(self.info)
            if(self.der is not None):
                self.der.inorden_villano()

    def inorden_heroes_con_c(self):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.inorden_heroes_con_c()
            if self.datos['villano']==False and self.datos['name'][0]=='C' :
                    print(self.info)
            if(self.der is not None):
                self.der.inorden_heroes_con_c()
   
    def inorden_talos(self):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.inorden_talos()
            if self.datos['name']=='talos' :
                    print(self.info)
            if(self.der is not None):
                self.der.inorden_talos()
    
    def inorden_heracle(self):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.inorden_heracle()
            if self.datos['derrotado']=='Heracles' :
                    print(self.info)
            if(self.der is not None):
                self.der.inorden_heracle()

    def inorden_noderrota(self):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.inorden_noderrota()
            if self.datos['derrotado']=='-' :
                    print(self.info)
            if(self.der is not None):
                self.der.inorden_noderrota() 
    
   
    def inorden_capturados(self):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.inorden_capturados()
            if self.datos['capturado']=='Heracles' :
                    print(self.info)
            if(self.der is not None):
                self.der.inorden_capturados()  

    def postorden(self):
        if(self.info is not None):
            if(self.der is not None):
                self.der.postorden()
            print(self.info)
            if(self.izq is not None):
                self.izq.postorden()

    def preorden(self):
        if(self.info is not None):
            print(self.info, self._altura)
            if(self.izq is not None):
                self.izq.preorden()
            if(self.der is not None):
                self.der.preorden()

    def busqueda(self, clave):
        pos = None
        if(self.info is not None):
            if(self.info == clave):
                pos = self
            elif(clave < self.info and self.izq is not None):
                pos = self.izq.busqueda(clave)
            elif(self.der is not None):
                pos = self.der.busqueda(clave)
        return pos
    
    def busqueda_proximidad(self, clave):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.busqueda_proximidad(clave)
            if(self.info[0:len(clave)] == clave):
                print(self.info)
            if(self.der is not None):
                self.der.busqueda_proximidad(clave)

    def remplazar(self):
        """Determina el nodo que remplazará al que se elimina."""
        aux = None
        if(self.der is None):
            aux = self.info
            if(self.izq is not None):
                self.info = self.izq.info
                self.der = self.izq.der
                self.izq = self.izq.izq
            else:
                self.info = None
        else:
            aux = self.der.remplazar()
        return aux

    def eliminar_nodo(self, clave):
        """Elimina un elemento del árbol y lo devuelve si lo encuentra."""
        x = None
        if(self.info is not None):
            if(clave < self.info):
                if(self.izq is not None):
                    x = self.izq.eliminar_nodo(clave)
            elif(clave > self.info):
                if(self.der is not None):
                    x = self.der.eliminar_nodo(clave)
            else:
                x = self.info
                if(self.der is None and self.izq is None):
                    self.info = None
                elif(self.izq is None):
                    self.info = self.der.info
                    self.izq = self.der.izq
                    self.der = self.der.der
                elif(self.der is None):
                    self.info = self.izq.info
                    self.der = self.izq.der
                    self.izq = self.izq.izq
                else:
                    aux = self.izq.remplazar()
                    self.info = aux
                    # raiz.info, raiz.nrr = aux.info, aux.nrr
        # self = self.balancear()
        self.actualizar_altura()
        return x
    
    def contar_ocurrencias(self, buscado):
        cantidad = 0
        if(self.info is not None):
            if(self.info == buscado):
                cantidad += 1
            if(self.izq is not None):
                cantidad += self.izq.contar_ocurrencias(buscado)
            if(self.der is not None):
                cantidad += self.der.contar_ocurrencias(buscado)
        return cantidad
    
    def contar_pares_impares(self):
        pares, impares = 0, 0
        if(self.info is not None):
            if(self.info % 2 == 0):
                pares += 1
            else:
                impares += 1
            if(self.izq is not None):
                par, impar = self.izq.contar_pares_impares()
                pares += par
                impares += impar
            if(self.der is not None):
                par, impar = self.der.contar_pares_impares()
                pares += par
                impares += impar
        return pares, impares

    def barrido_por_nivel(self):
        pendientes = Cola()
        pendientes.arribo(self)
        while(not pendientes.cola_vacia()):
            nodo = pendientes.atencion()
            print(nodo.info)
            if(nodo.izq is not None):
                pendientes.arribo(nodo.izq)
            if(nodo.der is not None):
                pendientes.arribo(nodo.der)    

    def barrido_por_nivel_huff(self):
        pendientes = Cola()
        pendientes.arribo(self)
        while(not pendientes.cola_vacia()):
            nodo = pendientes.atencion()
            print(nodo.info, nodo.frecuencia)
            if(nodo.izq is not None):
                pendientes.arribo(nodo.izq)
            if(nodo.der is not None):
                pendientes.arribo(nodo.der)

      
    def contar_superheroes(self):
        cantidad = 0
        if(self.info is not None):
            if(self.datos['villano'] == False):
                cantidad += 1
            if(self.izq is not None):
                cantidad += self.izq.contar_superheroes()
            if(self.der is not None):
                cantidad += self.der.contar_superheroes()
        return cantidad
    
   
    
    def dos_arboles(self,arbol_superheroes, arbol_villanos):
            if(self.info is not None):
                if(self.datos['villano'] == False):
                    arbol_superheroes = arbol_superheroes.insertar_nodo(self.info, self.datos)
                else:
                    arbol_villanos = arbol_villanos.insertar_nodo(self.info, self.datos)
                if(self.izq is not None):
                    self.izq.dos_arboles(arbol_superheroes, arbol_villanos)
                if(self.der is not None):
                    self.der.dos_arboles(arbol_superheroes, arbol_villanos)
    
     
    def contar_nodos(self):
        cantidad = 0
        if(self.info is not None):
            if(self.izq is not None):
                cantidad += self.izq.contar_superheroes()
            if(self.der is not None):
                cantidad += self.der.contar_superheroes()
        return cantidad
    
    def conta_criaturas_derrotadas(self, dic):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.conta_criaturas_derrotadas(dic)
            #! chequear que no sea vacio
            if(self.datos['derrotado _por'] in dic):
                dic[self.datos['derrotado_por']] += 1
            else:
                dic[self.datos['derrotado_por']] = 1
            print(self.info, self.datos)
            if(self.der is not None):
                self.der.conta_criaturas_derrotadas(dic)
    
    def conta_criaturas_derrotadas(self, dic):
        """cuenta que dioses derroto mas criaturas"""
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.conta_criaturas_derrotadas(dic)
            if(self.datos['derrotado'] in dic):
                dic[self.datos['derrotado']] += 1 #si esta lo va incrementando
            else:
                dic[self.datos['derrotado']] = 1 #lo asigna y lo pone en 1
            if(self.der is not None):
                self.der.conta_criaturas_derrotadas(dic)
       
    # FUNCIONES PARA EL PARCIAL
    def inorden_T_REX(self):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.inorden_T_REX()
            if self.datos['name']=='t-rex' :
                    print(self.datos)
            if(self.der is not None):
                self.der.inorden_T_REX()  
    
    def inorden_raptores(self):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.inorden_raptores()
            if self.datos['name']=='raptores' :
                    print(self.datos['zona'])
            if(self.der is not None):
                self.der.inorden_raptores() 
                
    def contar_Diplodocus(self):
        cantidad = 0
        if(self.info is not None):
            if(self.datos['name'] == 'Diplodocus'):
                cantidad += 1
            if(self.izq is not None):
                cantidad += self.izq.contar_Diplodocus()
            if(self.der is not None):
                cantidad += self.der.contar_Diplodocus()
        return cantidad
    
    def inorden_792(self):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.inorden_792()
            if self.datos['codigo']==792 :
                    print(self.datos)
            if(self.der is not None):
                self.der.inorden_792()  
    
   


