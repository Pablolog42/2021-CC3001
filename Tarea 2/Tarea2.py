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
    for k in range(0,n):
        b=a[k] 
        j=k 
        while j>0 and b < a[j-d]:   #Tal como se indica en el enunciado, la modificación escencial a la función insertar, es que ahora la comparación y el swap se realizan 
            a[j] = a[j-d]           # con el elemento d casilleros atrás (en vez de a[j-1], se opera con a[j-d])
            j-=1
        a[j]=b

def d_ordena_insercion(a,d):
    """d-Ordena el arreglo a por inserción"""

    n=len(a)
    for k in range(0,n):
        d_insertar(a,k,d)


# A = np.array([46,35,95,21,82,70,72,56,64,50])

# A = np.array([random.randint(1,100) for i in range(0,200)])


# # d tiene que ser por lo menos menor a n-1 (si no se rompe el código)
# d_ordena_insercion(A,3)
# print(A)
# verifica_d_ordenado(A,3)





def Shellsort(a):
    """Ordena a usando Shell Sort, con la secuencia de valores …,63,31,15,7,3,1"""
    #Primero, partimos generando la secuencia de valores de d (los d_k)


    n = len(a)

    # Genero la lista con la sucesión de valores de k a utilizar. (la doy vuelta para que quede en el orden …,63,31,15,7,3,1)
    # valoresD = [(2**k - 1) for k in range(1, 4)]


    valores= []
    k=1

    while 2**k <= n:    #Me armo la lista de los valores d que me sirven (esto porque d tiene que ser menor a n-1)
        d = 2**k - 1
        k += 1

        valores.append(d)

    valores.reverse() # al verre

    for d in valores:
        
        # whoops esto falla de pana
        # Para no comparar con algun elemento en un índice fuera de la lista, restingimos el d
        # while d > n:
        #      d = valoresD[]
        #     
        
        print(d)
        d_ordena_insercion(a,d)


    # while d 
    #     d = (2^k) - 1

    #     d_ordena_insercion(a, d)


    # n = len(a)
    # k = n // 2
    # d = 2 # d es la mayor potencia de dos que quepa dentro de n

    # while a:
    #     pass



A = np.array([46,35,95,21,82,70,72,56,64,50])
#A = np.array([random.randint(1,100) for i in range(0,200)])
Shellsort(A)
print(A)
verifica_d_ordenado(A,1)

