n, m, c = map(int,input().split())

viva = 1
muerta = 0

matriz = [[(1 if letra == '*' else 0) for letra in input()] for _ in range(n)]
# print(matriz)

def contarVecinos(i, j):
    vecinos = 0
    fila_actual = i
    columna_actual = j
    izquierda = j-1
    derecha = j+1
    arriba = i-1
    abajo = i+1
    
    if arriba >= 0:
        vecinos += matriz[arriba][columna_actual]
            
        if derecha < m:
            vecinos += matriz[arriba][derecha]
        else:
            vecinos += matriz[arriba][0]
        
        if izquierda >= 0:
            vecinos += matriz[arriba][izquierda]
        else:
            vecinos += matriz[arriba][m-1]
    else:
        vecinos += matriz[n-1][columna_actual]
            
        if derecha < m:
            vecinos += matriz[n-1][derecha]
        else:
            vecinos += matriz[n-1][0]
        
        if izquierda >= 0:
            vecinos += matriz[n-1][izquierda]
        else:
            vecinos += matriz[n-1][m-1]
    
    if abajo < n:
        vecinos += matriz[abajo][columna_actual]
        
        if derecha < m:
            vecinos += matriz[abajo][derecha]
        else:
            vecinos += matriz[abajo][0]
        
        if izquierda >= 0:
            vecinos += matriz[abajo][izquierda]
        else:
            vecinos += matriz[abajo][m-1]
    else:
        vecinos += matriz[0][columna_actual]
        
        if derecha < m:
            vecinos += matriz[0][derecha]
        else:
            vecinos += matriz[0][0]
        
        if izquierda >= 0:
            vecinos += matriz[0][izquierda]
        else:
            vecinos += matriz[0][m-1]
        
    if derecha < m:
        vecinos += matriz[fila_actual][derecha]
            
    else:
        vecinos += matriz[fila_actual][0]
        
    if izquierda >= 0:
        vecinos += matriz[fila_actual][izquierda]
    else:
        vecinos += matriz[fila_actual][m-1]
    
        
    return vecinos

registro = []
salida_total = False
for iteracion in range(1,c+1):
    
    if salida_total:
        break
    copia_matriz = [[None for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            
            vecinos = contarVecinos(i,j)
            
            if matriz[i][j] == viva:
                
                if vecinos == 2 or vecinos == 3:
                    copia_matriz[i][j] = viva
                else:
                    copia_matriz[i][j] = muerta
                
            else:
                
                if vecinos == 3:
                    copia_matriz[i][j] = viva
                else:
                    copia_matriz[i][j] = muerta
                    
    if registro != []:
        if(matriz == registro[0]):
            copia_matriz = registro[(c-iteracion+1)%len(registro)]
            salida_total = True
            break
    
    registro.append(matriz)
    
    
    matriz = copia_matriz
    


for fila in copia_matriz:
    for elemento in fila:
        print('*' if elemento == 1 else '-', end="")
    print()
    
