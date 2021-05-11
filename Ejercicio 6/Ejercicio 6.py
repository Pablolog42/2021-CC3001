class Pila:
    def __init__(self):
        self.s=[]
    def push(self,x):
        self.s.append(x)
    def pop(self):
        assert len(self.s)>0
        return self.s.pop() # pop de lista, no de Pila
    def is_empty(self):
        return len(self.s)==0


#Se le pide escribir una funcion chequeo2 que reciba 3 parametros de tipo string: ``s``, ``a`` y ``b``. En ``s`` viene la secuencia de paréntesis a chequear, en ``a`` vienen los abre parentesis permitidos y en ``b`` los cierra paréntesis respectivos de modo que en ``b[i]`` está el paréntesis que cierra a ``a[i]``. 
#Por simplicidad use la implementacion de pila que viene a continuacion 
def chequeo2(s, a, b):
    
    stackParentesis = Pila()

    for parentesis in s:
        
        # Caso abre paréntesis
        if parentesis in a:
            stackParentesis.push(parentesis)
            continue
        
        #caso cierra parentesis
        if parentesis in b:
            #Si parte con un cierra parentesis, está mal escrita
            if stackParentesis.is_empty():
                return "INCORRECTA"

            tope = stackParentesis.pop()
            indiceA = a.find(tope) 
            indiceB = b.find(parentesis) 

            # en b[i] está el paréntesis que cierra a a[i]
            if indiceA == indiceB:
                continue
            
            return "INCORRECTA"
        
    return "CORRECTA"


print(chequeo2("(()())","(",")"))
print(chequeo2("{([]{()})}","{[(","}])"))
print(chequeo2("{([]()})}","{[(","}])"))
print(chequeo2("{<{<>}>}", "{<","}>"))
print(chequeo2("{<{<>>}>}", "{<","}>"))