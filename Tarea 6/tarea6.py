import numpy as np
from numpy.core.fromnumeric import mean


def myhash(x,m):
  return hash(x)%m


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

class LinearProbing:
	def __init__(self,m):
		self.t = np.empty(m, dtype=object)
		for i in range(m):
			self.t[i] = None

	def insert(self,x):
		# busca x (si no está lo inserta) y retorna el costo de búsqueda (numero de comparaciones)
		tablaHashing = self.t
		m = len(tablaHashing)
		hash = myhash(x,m)

		comparaciones = 0

		while True:

			# si está vacío, puedo insertarlo directamente
			if tablaHashing[hash] == None:
				tablaHashing[hash] = x
				return comparaciones

			# Si la palabra ya está, sigo a la siguiente.
			if x == tablaHashing[hash]:
				# Para ver si está tengo que comparar 1 vez
				comparaciones += 1
				return comparaciones


			if x != tablaHashing[hash]:
				comparaciones += 1 

				# Linear probing: avanzo uno y veo si está vacío
				hash = (hash + 1) % m
				continue


			

f=open(r"C:\Users\pablo\Desktop\Programación\Python\2021-CC3001\Tarea 6\cap1.txt","r")
texto=f.read()  
palabras=texto.split()

# ## Prueba Chaining #################
# listaChaining = Chaining(1000)
# listaComparacionChaining = []

# for palabra in palabras:
#   x = listaChaining.insert(palabra)
#   listaComparacionChaining.append(x)

# x="añsdlkañsldk"

# print(f"El promedio de comparaciones es: {mean(listaComparacionChaining)} || El máx de comparaciones es: {max(listaComparacionChaining)}")
# ######################################





# ## Prueba LinearProbing #################
listaLinearProbing = LinearProbing(1000)
listaComparacionLinearProbing = []

for palabra in palabras:
  x = listaLinearProbing.insert(palabra)
  listaComparacionLinearProbing.append(x)

print(f"El promedio de comparaciones es: {mean(listaComparacionLinearProbing)} || El máx de comparaciones es: {max(listaComparacionLinearProbing)}")

y= 234234234
# ######################################


# # TESTS DEBUGGING (no copiar a colab)
# cuentaNone = 0

# # Para ver si efectivamente hay 717 palabras distintas en linearprobing
# for item in listaLinearProbing.t:
# 	if item == None:
# 		cuentaNone = cuentaNone + 1

# print(1000 - cuentaNone)