def numero_binario(numero):
    if (numero == 1) or (numero == 0):
        return str(numero)
    elif  ((numero % 2) == 0) and (numero < 2):
        return str(0)
    else: 
        return str(numero % 2) + numero_binario(numero // 2) 

def invertir_cadena(cadena):#! 6
    if(len(cadena) == 0):
        return ""
    else:
        return cadena[-1] + invertir_cadena(cadena[0:-1])


print(invertir_cadena(numero_binario(10)))