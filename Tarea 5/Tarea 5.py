import aed_utilities as aed

class Nodoi:
    def __init__(self, izq, info, der):
        self.izq=izq
        self.info=info
        self.der=der
        
    def insert(self,x):
        assert x!=self.info
        if x<self.info:
            return Nodoi(self.izq.insert(x),self.info,self.der)
        else:
            return Nodoi(self.izq,self.info,self.der.insert(x))

    def cut(self, x):
        r = self.info
        assert x != r

        if x < r:
            izqMenorX = self.izq.cut(x)[0] 
            izqMayorX = self.izq.cut(x)[1] 

            j = Nodoi(izqMayorX, r, self.der) 

            return (izqMenorX,j)

        if x > r:
            derMenorX = self.der.cut(x)[0] 
            derMayorX = self.der.cut(x)[1] 

            j = Nodoi(self.izq, r, derMenorX)
            
            return (j,derMayorX)


class Nodoe:
    def __init__(self):
        pass
    
    def insert(self,x):
        return Nodoi(Nodoe(),x,Nodoe())

    def root_insert(self, x):
        return Nodoi(Nodoe(),x,Nodoe())

    def cut(self,x):
        #Caso base
        return(Nodoe(),Nodoe())

class Arbol:
    def __init__(self,raiz=Nodoe()):
        self.raiz=raiz     
        
    def insert(self,x):
        self.raiz=self.raiz.insert(x)
    
    def cut(self, x):
        return self.raiz.cut(x)

    def root_insert(self, x):
        corteArbol = self.raiz.cut(x) 

        izq = corteArbol[0] 
        der = corteArbol[1]  
        self.raiz = Nodoi(izq, x, der)
        
    def dibujar(self):
      btd = aed.BinaryTreeDrawer(fieldData="info", fieldLeft="izq", fieldRight="der", classNone=Nodoe, drawNull=True)
      btd.draw_tree(self, "raiz")

    
# lista=[9,6,2,7,1,8,3,5]
# a=Arbol()
# for m in lista:
#     a.insert(m)

# # a.dibujar()

# tuplaCortada = a.cut(4)

# menorX , mayorX = tuplaCortada[0], tuplaCortada[1]

# t = Arbol(tuplaCortada[0])
# t. dibujar()
# # Arbol(tuplaCortada[1]).dibujar

lista=[9,6,2,7,1,8,3,5]
a=Arbol()
for m in lista:
    a.root_insert(m)
    # a.dibujar()

a.dibujar()




