def laberinto(matriz, x, y,):
    
    if(x >= 0 and x <= len(matriz)-1) and (y >= 0 and y <= len(matriz[0])-1):
        if(matriz[x][y] == 2):
            
            print("Saliste del laberinto")
         
            
        elif(matriz[x][y] == 1):
            matriz[x][y] = 3
            
            
            laberinto(matriz, x, y+1, )
            
            laberinto(matriz, x, y-1, )
            
            laberinto(matriz, x-1, y, )
            
            laberinto(matriz, x+1, y, )
            
            matriz[x][y] = 1


lab = [[1, 1, 1, 1],
       [0, 0, 1, 0],
       [1, 1, 1, 1],
       [1, 0, 1, 2]]
    
laberinto(lab, 0, 0)