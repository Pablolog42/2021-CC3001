import random 
import numpy as np
from numpy.lib.function_base import median

def bsort(a):
    n=len(a)
    k=n 
    while k>1:
        for j in range(0,k-1):
            if a[j]>a[j+1]:
                (a[j],a[j+1])=(a[j+1],a[j])
        k-=1

    return a


def quicksort3(a):
  qsort(a,0,len(a)-1)

#Esta es la versión del apunte que deberá modificar
def qsort(a,i,j): # ordena a[i],...,a[j]

  
  if (j-i)<3:
    # Ordenar una lista con 0 elementos es la misma lista
    if i-j == 0:
      return a

    # Los otros dos casos bases son ordenar una arreglo con a lo más 3 elementos.
    # Como son solo 3, podemos hacerlo eficientemente por, por ejemplo, bubblesort.
    return bsort(a)

  else:
    k= particionMedianaDe3(a,i,j)
    qsort(a,i,k-1)
    qsort(a,k+1,j)


def particionMedianaDe3(a,i,j): # particiona a[i],...,a[j], retorna posición del pivote

  arrayIndices = [random.randint(i,j), random.randint(i,j), random.randint(i,j)]
  l,m,n = arrayIndices[0], arrayIndices[1], arrayIndices[2]

  # Por indicación, tomamos sólo números distintos
  if l == m or m == n or n == l:
    particionMedianaDe3(a,i,j)


  # Se ordena por bubblesort el array de indices, utilizado como parametro de ordenacion el valor de "a" correspondiente a ese indice
  # Es eficiente ordenar por bubblesort para obtener los minimos, medianas y maximos, al ser arreglos de tamaño 3 fijo.
  p=len(arrayIndices)
  k1=p 
  while k1>1:
      for g in range(0,k1-1):
        # Ordeno con respecto al a[indice] correspondiente
        if a[arrayIndices[g]]>a[arrayIndices[g+1]]:
          (arrayIndices[g],arrayIndices[g+1])=(arrayIndices[g+1],arrayIndices[g])
      k1-=1

  # Al estar ordenado el array de 3 elementos
  indiceMinimo = arrayIndices[0]
  indiceMediana = arrayIndices[1]
  indiceMaximo = arrayIndices[2]


  (a[i], a[indiceMinimo])  = (a[indiceMinimo],a[i]) 
  (a[i+1], a[indiceMediana]) = (a[indiceMediana],a[i+1]) 
  (a[j], a[indiceMaximo]) = (a[indiceMaximo],a[j]) 


  # Se aplica el algoritmo ya conocido sobre a[i+2]... a[j-1] con el pivote a[i+1]
  # Muevo al pivote al borde

  (a[i+1], a[i]) = (a[i], a[i+1])


  s=i # invariante: a[i+1..s]<=a[i], a[s+1..t]>a[i]
  for t in range(s,j):
      if a[t+1]<=a[i]:
          (a[s+1],a[t+1])=(a[t+1],a[s+1])
          s=s+1

  # mover pivote al centro
  (a[i],a[s])=(a[s],a[i])
  return s





a = np.random.random(1602)
# print(particionMedianaDe3(a,2,10))

b = np.array([9,8,7,6,5,4,3,2,1])

def chequea_orden(a):
    print("Ordenado" if np.all(a[:-1]<=a[1:]) else "Desordenado")
    
print(a)
chequea_orden(a)
quicksort3(a)
print(a)
chequea_orden(a)

# print("-----------------------------")
# print(b)
# chequea_orden(b)
# quicksort3(b)
# print(b)
# chequea_orden(b)