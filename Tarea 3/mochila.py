import numpy as np
import random

def imprimeMatriz(C):
    i=0
    for fila in C:
        #print(" Máx mochila de: " + str(i) + " objetos")
        print(fila) 
        i = i + 1


#mochila1 = [(random.randint(1,50), random.randint(1,50)) for i in range(15)]

def maximoMochila(L, T):

    """ maximoMochila(ListaObjetos, PesoMaximo) """

    n = len(L)

    C = np.zeros(shape=(n+1,T+1),dtype=int)


    # Matriz de listas nativas
    #C =[[0 for p in range(T+1)] for q in range(n+1)] 

    #imprimeMatriz(C)

    listaValor = []
    listaPeso = []
    for objeto in L:
        (p_i, v_i) = objeto[0], objeto[1]
        listaPeso.append(p_i)
        listaValor.append(v_i)




    for i in range(1, n+1):
        for j in range(1, T+1):
            
            #Van con i-1 pq los for parten de 1
            (p_i, v_i) = listaPeso[i-1], listaValor[i-1] 


            if j - p_i >= 0:
                C[i,j] = max(C[i-1,j], v_i + C[i-1,j - p_i])

                # Caso 1
            else:
                C[i, j] = C[i-1, j] 

                #Caso 2

    imprimeMatriz(C)

    return C[n, T]



# (peso, Valor)
mochila = [(10,5),(5,10),(2,1)]
print("\n El Max es:" + str(maximoMochila(mochila, 15)))