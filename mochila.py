vector_mochila = ['lata' , 'botella' ,'revista henati' ,'sable azul']

def jeidi(vector_mochila,inicio,fin):
    if  (inicio < fin):
        if (vector_mochila[inicio] == 'sable azul'):
            return inicio
        else:
            return  jeidi(vector_mochila,inicio +1 , fin)
    else:
        return -1

    
if (jeidi(vector_mochila, 0, len(vector_mochila)) == -1):
    print('El zable azul no esta')
else:
    print('El zable azul esta en la posicion ', jeidi(vector_mochila, 0, len(vector_mochila))+1)
    print('tuvo que sacar ',jeidi(vector_mochila, 0, len(vector_mochila)))