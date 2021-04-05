import numpy as np
import random

def verifica_d_ordenado(a,d):
    for i in range(0,len(a)-d):
        assert a[i]<=a[i+d]
    print("Arreglo "+str(d)+"-ordenado OK.")
        

def d_insertar(a,k,d):
    """
    Inserta a[k] entre los elementos anteriores a distancia d
    preservando el orden ascendente (versión 2)
    """
    n=len(a)
    for k in range(d, n): #QUE NO SE QUE PASA JODER 
        b=a[k] 
        j=k 
        while j>0 and b < a[j-d]:   #Tal como se indica en el enunciado, la modificación escencial a la función insertar, es que ahora la comparación y el swap se realizan 
            (a[j], a[j-d]) = (a[j-d], a[j])           # con el elemento d casilleros atrás (en vez de a[j-1], se opera con a[j-d])
            j-=1


def d_ordena_insercion(a,d):
    """d-Ordena el arreglo a por inserción"""
    n=len(a)
    for k in range(0,n):
        d_insertar(a,k,d)






def Shellsort(a):
    """Ordena a usando Shell Sort, con la secuencia de valores …,63,31,15,7,3,1"""
    #Primero, partimos generando la secuencia de valores de d (los d_k)

    n = len(a)
    m = n//2
    k = 1

    # Se crea la secuencua de valores d, acorde al tamaño del array inicial
    listaD = []
    while k <= np.log2(m):  # d = 2**k - 1 <= n//2   ==>  k <= log2(n//2 +1)
        d = 2**k -1         #d = 2**k - 1
        listaD.append(d)
        k += 1
    listaD.reverse()
    print(listaD)



    for d in listaD:
        d_ordena_insercion(a,d)



A = np.array([46,35,95,21,82,70,72,56,64,50,70,72,56,64,50,70,72,56,64,50])

B = [random.randint(0,100) for i in range(0,20)]

# B = [10-i for i in range(0,10)]


print(B)
Shellsort(B)
print(B)


