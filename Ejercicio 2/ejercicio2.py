
def permutaciones(x,ini,fin):

    if ini == fin:
        resultado = ""
        resultado = resultado.join([str(numero) for numero in x]) # Para que imprima los elementos en el formato que se pide (como número y no como arreglo)
        return print(resultado)

    for i in range(ini, fin+1):
        (x[ini], x[i]) = (x[i], x[ini])
        permutaciones(x, ini+1, fin)
        (x[ini], x[i]) = (x[i], x[ini])
        


permutaciones([1,2,3] , 0, 2)

permutaciones([3] , 0, 0)