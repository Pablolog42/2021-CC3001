import numpy as np

def trepar(a,j): # El elemento a[j] trepa hasta su nivel de prioridad 
    while j>=1 and a[j]>a[(j-1)//2]:
        (a[j],a[(j-1)//2])=(a[(j-1)//2],a[j]) # intercambiamos con el padre
        j=(j-1)//2 # subimos al lugar del padre
        
def hundir(a,j,n): # El elemento a[j] se hunde hasta su nivel de prioridad
    while 2*j+1<n: # mientras tenga al menos 1 hijo
        k=2*j+1 # el hijo izquierdo
        if k+1<n and a[k+1]>a[k]: # el hijo derecho existe y es mayor
            k+=1
        if a[j]>=a[k]: # tiene mejor prioridad que ambos hijos
            break
        (a[j],a[k])=(a[k],a[j]) # se intercambia con el mayor de los hijos
        j=k # bajamos al lugar del mayor de los hijos
    
class Heap:
    def __init__(self,maxn=100):
        self.a=np.zeros(maxn)
        self.n=0
    def insert(self,x):
        assert self.n<len(self.a)
        self.a[self.n]=x    
        trepar(self.a,self.n)
        self.n+=1       
    def extract_max(self):
        assert self.n>0
        x=self.a[0] # esta variable lleva el máximo, el casillero 0 queda vacante
        self.n-=1   # achicamos el heap
        self.a[0]=self.a[self.n] # movemos el elemento sobrante hacia el casillero vacante
        hundir(self.a,0,self.n)
        return x

    def modificar(self, k, x): #Implementar esta función
        # Modifico la prioridad
        self.a[k] = x

        #Si el padre es mayor al número
        if self.a[(k-1)//2] > self.a[k]:
           #lo hundo hasta que llegue donde debería estar 
           hundir(self.a, k, self.n) 

        #Si no, trepa hasta donde deberia estar
        trepar(self.a, k)

    def imprimir(self):
        print(self.a[0:self.n])



a=Heap(20)
a.insert(55)
a.insert(50)
a.insert(70)
a.insert(12)
a.insert(36)
a.insert(10)
a.insert(21)
a.insert(24)
a.insert(20)
a.insert(62)
a.imprimir()
a.modificar(4,65)
a.imprimir()
a.modificar(3,15)
a.imprimir()