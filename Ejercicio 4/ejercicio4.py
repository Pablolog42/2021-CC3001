# salida: int int -> bool
# salida(i,j) que retorna verdadero si existe
# un camino hacia la salida a partir de la coordenada (i,j)

def salida(i,j):
    if L[i][j] == "=": # encontramos la salida
        return True
    if L[i][j] != " ": # espacio ocupado
        return False

    # Intentos no exitosos
    L[i] = L[i][:j] + "." + L[i][j+1:] # Rellename justo la casilla sin salidas con un ".", dejanto todo el resto de la fila igual
    
    # Busco la salida recursivamente en las 4 direcciones cardianales
    # Notar que si uno da true, no se llama a los siguientes "or"
    if salida(i,j-1) \
    or salida(i,j+1) \
    or salida(i-1,j) \
    or salida(i+1,j):

        L[i] = L[i][:j] + "x" + L[i][j+1:] # Todos estos fueron intentis exitosos, pues se cumplió el if
        return True
    return False  

L = [
"+--+-----+--+",
"|  |     |  |",
"|  +--+     =",
"|     |  |  |",
"+--+  |  |  |",
"|  |        |",
"|  |     |  |",
"+--+-----+--+"
]

print(salida(4,10))
for linea in L:
    print(linea)




# Tests##################

L = [
"+--+-----+--+",
"|  |     |  |",
"|  +--+     =",
"|     |  |  |",
"+--+  |  |  |",
"|  |        |",
"|  |     |  |",
"+--+-----+--+"
]
print(salida(1,1))

for linea in L:
    print(linea)