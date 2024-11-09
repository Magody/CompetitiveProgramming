def solucionar(s:str) ->int:
    if s[0] == '0': return 0 #si empieza con 0 no hay soluciones posibles
    logs = {len(s):1}   #evita ir por el mismo camino más de una vez.
    def dfs(i, flag:bool): #funcion recursiva. S
        if i in logs: return logs[i]
        if s[i] == '0' and flag == False: return 0
        res = dfs(i+1,False)
        if (i < len(s)-2) and (s[i+1]== '1' or s[i+1] == '2' and s[i+2] in '0123456'):
            res+=dfs(i+2, True) #se usa la bandera para saber si estamos analizando un numero o dos.
        logs[i] = res
        return res

    #en caso que solo sea un numero.
    if len(s) == 1: return dfs(0,False)
    #se analiza que sea un num valido.
    if int(s[0]+s[1])>26: return dfs(0,False)
    return dfs(0,False) + dfs(1,True)


def testCode():
    casosPrueba = [
        '1220125',
        '11106',
        '12',
        '226',
        '0',
        '06',
        '1220125',
        '121',
        '27'
    ]

    salidas = [
        6,2, 2, 3, 0, 0, 6,3,1
    ]

    for i in range(len(casosPrueba)):
        solution = None
        try:
            solution = solucionar(casosPrueba[i])
            assert solution == salidas[i]
            print(
                f"respuesta correcta: test {casosPrueba[i]}, result {solution}")
        except Exception as error:
            print(
                f"Error, test {casosPrueba[i]}, expected {salidas[i]}, calculated {solution}", error)

testCode()