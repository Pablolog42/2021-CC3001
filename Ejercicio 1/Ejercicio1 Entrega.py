def particionLomuto(a,p):
    # retorna el punto de corte, el número de elementos <p y la lista particionada
    
    # escribir acá el algoritmo de partición de Lomuto
    i, j = 0,0
    n = len(a) - 1

    while j <= n :   #Mientras j sea menor a la cardinalidad de la lista
        if a[j] < p:    
            (a[i], a[j]) = (a[j], a[i]) # intercambio el elemento en el índice i con el elemento de indice j
            i += 1
        j += 1
    
    return (p, i, a) # El número de elementos menores a p será exactamente el indice i, como se puede ilustrar en la invariante del algoritmo.


def verifica_particion(t): # imprime y chequea partición
    (p,m,a)=t
    # p=punto de corte, m=número de elementos <p, a=lista completa particionada
    print(a[0:m],p,a[m:])
    print("Partición OK" if (m==0 or max(a[0:m])<p) and (m==len(a) or min(a[m:])>p)
          else "Error")

verifica_particion(particionLomuto([73,21,34,98,56,37,77,65,82,15,36],50))
verifica_particion(particionLomuto([73,21,34,98,56,37,77,65,82,15,36],0))
verifica_particion(particionLomuto([73,21,34,98,56,37,77,65,82,15,36],100))
