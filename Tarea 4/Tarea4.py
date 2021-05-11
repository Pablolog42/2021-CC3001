import aed_utilities as aed
from copy import copy

#Nodo interno
class Nodoi:
    def __init__(self, izq, info, der):
        self.izq=izq
        self.info=info
        self.der=der
    def postorden(self):
        self.izq.postorden()   
        self.der.postorden()
        print(self.info, end=" ")


    def derivada(self,x):

        if self.info == "+" or self.info == "-":
            self.izq = self.izq.derivada(x)
            self.der = self.der.derivada(x)

        if self.info == "*":
           
           #No quiero aliasing ni cosas raras :(
           #Acá ocupo la copia para no tener problemas de punteros que se me modifiquen
           izquierdoOriginal = copy(self.izq)
           derechoOriginal = copy(self.der)

            # Regla de la derivada de un producto
           self.info = "+"
           self.izq =  Nodoi(self.izq.derivada(x), "*", derechoOriginal)
           self.der =  Nodoi(self.der.derivada(x), "*", izquierdoOriginal) 

        if self.info == "/":
           
           #CUIDADO CON EL ALIASING ACA QUE OCUPAS EL DERECHOORIGINAL MAS DE UNa VEZ (al parecer funca igual, vamos chile)
           izquierdoOriginal = copy(self.izq)
           derechoOriginal = copy(self.der)

            # Regla de la derivada de un cociente
           self.info = "/"
           self.izq =  Nodoi(Nodoi(self.izq.derivada(x), "*", derechoOriginal), "-", Nodoi(self.der.derivada(x),"*", izquierdoOriginal)) #Numerador en la regla del cuociente
           self.der =  Nodoi(derechoOriginal, "^", Nodoe(2)) #denominador va al cuadrado

        #HAY QUE ARREGLAR ESTO
        if self.info == "^":
            
            #Juan segura vivió muchos años (su RAM no tanto si)
            izquierdoOriginal = copy(self.izq)
            derechoOriginal = copy(self.der)

            #REGLA DE LA CADENA AAAAAA
            #Regla exponente entero x^n -> (n)*(x^(n-1))
            self.info = "*"
            # self.der = Nodoe(self.der) Básicamente puedo dejar el lado del exponente como estaba (pues la multiplicacion conmuta) (en vez de (n)*(x^(n-1)), estoy computando (x^(n-1))*(n) )
            self.izq = Nodoi(izquierdoOriginal, "^", Nodoi(derechoOriginal,"-", Nodoe(1))) # Lo multiplico por el numero elevado a uno menos

        return self


# Nodo externo
class Nodoe:
    def __init__(self, info):
        self.info=info
    def postorden(self):
        print(self.info, end=" ")

    def derivada(self,x):
        # Me van a quedar en los nodos externos solamente o la variable solita (derivada 1), o una constante con derivada 0
        return Nodoe(1) if self.info == str(x) else Nodoe(0)



#Toma un string de tipo "ax+b" y lo pasa a arbol binario
class Arbol:
    def __init__(self,formula):
        if type(formula)!=str: # se supone que viene el árbol ya construído
          self.raiz=formula
          return

        # la fórmula viene en forma de string
        global k
        global s
        s=formula+";" # agregamos una marca de fin de la entrada
        k=0 # indica próximo caracter por procesar
        # definimos funciones para analizar la fórmula
        def expresion(): # retorna puntero a la raíz de un árbol que representa a la fórmula s
            global k
            global s
            a=factor()
            while s[k]=="+" or s[k]=="-":
                op=s[k]
                k+=1
                b=factor()
                a=Nodoi(a,op,b)
            return a
        def factor():
            global k
            global s
            a=termino()
            while s[k]=="*" or s[k]=="/":
                op=s[k]
                k+=1
                b=termino()
                a=Nodoi(a,op,b)
            return a
        def termino():
            global k
            global s
            a=primario()
            if s[k]=="^":
                op=s[k]
                k+=1
                b=termino()
                a=Nodoi(a,op,b)
            return a
        def primario(): # posible constante, variable o formula parentizada
            global k
            global s
            if s[k].isalpha() or s[k].isdigit():
                a=Nodoe(s[k])
                k+=1
                return a
            if s[k]=="(": # fórmula parentizada
                k+=1
                a=expresion()
                if s[k]!=")":
                    print("Error: Falta cierra paréntesis: "+formula[k:])
                    assert False
                k+=1
                return a
            print("Error: Falta variable, número o abre paréntesis: "+formula[k:])
            assert False
              
        a=expresion()
        if s[k]!=";":
            print("Error: Basura al final de la fórmula: "+formula[k:])
            assert False                
        self.raiz=a
    
    def derivada(self,x):
        return Arbol(self.raiz.derivada(x))
      
    def dibujar(self):
      btd = aed.BinaryTreeDrawer(fieldData="info", fieldLeft="izq", fieldRight="der",classNone=Nodoe )
      btd.draw_tree(self, "raiz")


def probar_derivada(formula,x):
    f=Arbol(formula)
    print("Fórmula original:")
    f.dibujar()
    g=f.derivada(x)
    print("Derivada respecto de "+x+":")
    g.dibujar()


#probar_derivada("(2+x)+(x+3)","x")


# arbolh = Arbol("(2+x)+(x+3)") 
# hDerivado = arbolh.derivada("x")
# hDerivado.dibujar()

#probar_derivada("(2*x)*(3*x)","x")


#probar_derivada("(x+1)/(x-1)","x")

#probar_derivada("x^2","x")


#ARRGLAR ESTO
#PROBLAMAS CON REGLA DE LA CADENA Y EL EXPONENTE AAAA
probar_derivada("(2*x)^2","x")

# arboli = Arbol("x^2") 
# iDerivado = arboli.derivada("x")


# a=122313


