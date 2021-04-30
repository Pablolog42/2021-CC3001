import numpy as np

def imprimeMatriz(C):
    i=0
    for fila in C:
        #print(" Máx mochila de: " + str(i) + " objetos")
        print(fila) 
        i = i + 1


#tesoro_maximo: list[tupla] int int -> int
# # Retorna el valor de tesoro máximo a obtener, dados 

# L = listaTesoro
# t = tiempoOxigeno;
# W = factorTiempoSubida/Bajada

# tSubida = w*d
# tBajada = 2*w*d 


def tesoro_maximo(L, w, T):

    n = len(L)

    #Matriz de tabulación (inicializada con ceros)
    C = np.zeros(shape=(n+1,T+1),dtype=int)

    assert n <= 30 # Como máximo hay 30 tesoros
    assert T <= 1000 # Como máximo el tanque dura 1000 segundos 

    #Guardamos Valores y tesoros en listas 
    # ( deberia de ser diccionario la vd pero tengo mucho sueño para acordarme como se hacia :'(      )
    listaValor = []
    listaTiempo = []

    for objeto in L:
        (t, v) = objeto[0], objeto[1]

        t_Efectivo_i = 3*w*t

        listaTiempo.append(t_Efectivo_i)
        listaValor.append(v)



    # Itero sobre la tabla (C)
    for i in range(1, n+1):
        for j in range(1, T+1):
            
            #Van con i-1 pq los for parten de 1 (pues la primera fila y columna van vacías)
            (t_i, v_i) = listaTiempo[i-1], listaValor[i-1] 

            # Caso 1
            if j - t_i >= 0:
                C[i,j] = max(C[i-1,j], v_i + C[i-1, j - t_i])

            #Caso 2
            else:
                C[i, j]  = C[i-1, j] 

    return C[n, T]




# Tests
tesoros = [(10,5), (10,1),(7,2)]
tesoros1 = [(4,2),(1, 2),(1,3),(5,7),(4,4),(12,100)]

#Este funciona
assert tesoro_maximo(tesoros, 4, 210) == 7

#Este no :(
  #da 115 en vez de 107 (se pasa)
assert tesoro_maximo(tesoros1, 4, 210) == 107



#print(tesoro_maximo(tesoros, 4, 210))
print(tesoro_maximo(tesoros1, 4, 210))
