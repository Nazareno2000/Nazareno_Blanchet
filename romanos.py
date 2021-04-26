Vectordecima=[(1000,'M'),(900,'CM'),(500,'D'),
               (400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),
               (10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]

def convertir(numero,pos=0):
    
    i,r=Vectordecima[pos]
    
    if numero==0:
        if pos==0:
            return "0"
        else:
            return ""
    elif numero >= i:
        numero-=i
        return r + convertir(numero, pos )
    else:
       return convertir(numero, pos + 1)

def convertirDecimal2Romano(numero):
    return convertir(numero)
      
print(convertirDecimal2Romano(1478))