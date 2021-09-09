casos = int(input())

for _ in range(casos):

    c, n = map(int, input().split())
    
    objetos = [[-1,-1]]
    objetos += [list(map(int, input().split())) for _ in range(n)]
    
    matriz = [[0 for _ in range(c+1)] for _ in range(n+1)]
    # print(matriz)
    
    for i in range(1,n+1):
        beneficio = objetos[i][1]
        peso = objetos[i][0] 
        
        for w in range(1,c+1):
            
            if peso <= w:
                # print(beneficio, matriz[i-1][w-peso])
                if beneficio + matriz[i-1][w-peso] > matriz[i-1][w]:
                    matriz[i][w] = beneficio + matriz[i-1][w-peso]
                else:
                    matriz[i][w] = matriz[i-1][w]
            else:
                matriz[i][w] = matriz[i-1][w]
            """
            for fila in matriz:
                for numero in fila:
                    print(numero,end=" ")
                print()
            print()
            """
    
    
    #print(objetos)
    print(matriz[-1][-1])
    # print(len(matriz[0]),len(matriz))
    
    
    
    {1,1},{2,2},{3,3},{4,4},{5,5},
