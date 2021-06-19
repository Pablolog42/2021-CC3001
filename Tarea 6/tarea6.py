import numpy as np
from numpy.core.fromnumeric import mean

def myhash(x,m):
  return hash(x)%m

class LinearProbing:
    def __init__(self,m):
        self.t = np.empty(m, dtype=np.object)
        for i in range(m):
          self.t[i] = None
        
    def insert(self,x):
      # busca x (si no está lo inserta) y retorna el costo de búsqueda (numero de comparaciones)
       pass

class Nodo:
    def __init__(self, info, sgte=None):
        self.info=info
        self.sgte=sgte



class Chaining:
    # Se crea lista de punteros con todos los punteros inicializados como None
    def __init__(self,m):
        self.t = np.empty(m, dtype=np.object)
        for i in range(m):
          self.t[i] = None
        

    def insert(self,x):
      # busca x (si no está lo inserta) y retorna el costo de búsqueda (numero de comparaciones)
      tablaHashing = self.t
      m = len(tablaHashing)
      hash = myhash(x,m)

      comparaciones = 0

      # Se busca si la palabra está ya en la tabla

      # Si no hay nadie en el hash, se crea una entrada
      if tablaHashing[hash] == None:
        tablaHashing[hash] = Nodo(x)
        return comparaciones

      nodoActual = tablaHashing[hash]

      # Busco si existe el elemento en la lista encadenada
      # Es Aquí cuando se generan las ocmparaciones que toman tiempo
      while nodoActual.sgte != None:
        
        # Cada ciclo del while comparo una vez
        comparaciones += 1

        # Si existe en algun elemento de la lista, no hago nada
        if nodoActual.info == x:
          return comparaciones

        # Itero sobre la lista
        nodoActual = nodoActual.sgte

        
      
      #Si no existe en la lista, lo apendo al final
      nodoActual.sgte = Nodo(x) if nodoActual.info != x else None

      return comparaciones




        


f=open(r"C:\Users\pablo\Desktop\Programación\Python\2021-CC3001\Tarea 6\cap1.txt","r")
texto=f.read()  
palabras=texto.split()

## Prueba Chaining ################
listaChaining = Chaining(1000)
listaComparacionChaining = []

for palabra in palabras:
  x = listaChaining.insert(palabra)
  listaComparacionChaining.append(x)

print(f"El promedio de comparaciones es: {mean(listaComparacionChaining)} || El máx de comparaciones es: {max(listaComparacionChaining)}")
######################################





