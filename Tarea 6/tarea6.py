import numpy as np

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


      # Se busca si la palabra está ya en la tabla

      # Si no hay nadie en el hash, se crea una entrada
      if tablaHashing[hash] == None:
        tablaHashing[hash] = Nodo(x)
        return

      nodoActual = tablaHashing[hash]

      while nodoActual.sgte != None:
        # Si existe en algun elemento de la lista, no hago nada
        if nodoActual.info == x:
          return 
        nodoActual = nodoActual.sgte
      
      #Si no existe en la lista, lo apendo al final
      nodoActual.sgte = Nodo(x) if nodoActual.info != x else None




      





   


f=open(r"C:\Users\pablo\Desktop\Programación\Python\2021-CC3001\Tarea 6\cap1.txt","r")
texto=f.read()  
palabras=texto.split()


listaHash = Chaining(1000)

for palabra in palabras:
  listaHash.insert(palabra)

print("---")


# print(palabras)
#esto deja en palabras una lista python en que cada elemento es una palabra del archivo
#luego debe escribir el código para 
#   - crear una estructura Hashing1 y otra Hashing2
#   - insertar/buscar cada una de las palabras en ambas estructuras registrando el costo
#   - finalmente imprimir las estadisticas pedidas


