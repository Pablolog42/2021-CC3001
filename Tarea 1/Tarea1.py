# def palabras1000(n): #Funciona hasta mil

#     unidades = ["cero","un","dos","tres","cuatro","cinco","seis","siete","ocho",
#               "nueve"]
#     decenas = ["","diez","veinte","treinta","cuarenta","cincuenta","sesenta",
#              "setenta","ochenta","noventa"]
#     centenas = ["","ciento","doscientos","trescientos","cuatrocientos","quinientos",
#               "seiscientos","setecientos","ochocientos","novecientos"]

#     (c,d,u)=(n//100,(n%100//10),n%10)

#     return centenas[c]+" "+decenas[d]+" y "+unidades[u]


# def palabras(n): #Hasta mil millones

#     assert 0<=n<1000000000

#     if n==0:
#         return "cero"

#     (a,b,c)=(n//1000000,(n%1000000)//1000,n%1000)
#     # n es de la forma "a millones b mil c"
#     return palabras1000(a) + " millones " +palabras1000(b)+ " mil " + palabras1000(c)


# ### Fallas de mercado
# ##print(palabras(42515))


# def palabrasSinMillon(cm,dm,um,c,d,u):
#     print("marco")





# Indica números de hasta 3 dígitos en palabras
def palabras999(n):

    # Listas de palabras
    unidades = ["cero","un","dos","tres","cuatro","cinco","seis","siete","ocho",
              "nueve"]
    decenas = ["","diez","veinte","treinta","cuarenta","cincuenta","sesenta",
             "setenta","ochenta","noventa"]
    centenas = ["","ciento","doscientos","trescientos","cuatrocientos","quinientos",
              "seiscientos","setecientos","ochocientos","novecientos"]

    # Lista de referencia para numeros escritos de forma irregular (los tuve que anotar a mano :'( )
    onceAlTreinta = ["once", "doce", "trece", "catorce", "quince", "dieciseís", "diecisiete", "Dieciocho", "Diecinueve", "Veinte", "Veintiuno", "Veintidós", "Veintitrés", "Veinticuatro", "Veinticinco", "Veintiséis", "Veintisiete", "Veintiocho", "Veintinueve", "Treinta"]

    # Se descompone el múmero
    # mil.Mill Cent.Mill Dec.Mill unid.Mill // cent.mil dec.mil unid.mil // cent dec unid 
    (mM,cM,dM, uM,cm,dm,um,c,d,u)= ((n%10000000000//1000000000),(n%1000000000//100000000),(n%100000000//10000000),(n%10000000//1000000),(n%1000000//100000),(n%100000//10000),(n%10000//1000),(n%1000//100),(n%100//10),n%10) 

    resultado = centenas[c] + " " + decenas[d] + " y " + unidades[u]

    ##Restricciones sobre n
    if n == 0:
        resultado = "cero"

    elif n == 100:
        resultado = "cien"

    ##Restricciones sobre d y u
    elif 10 < (10*d + u) < 30: # Si terminan entre 10 y 30, terminan irregulares (buuu)
        resultado = centenas[c] + " " + onceAlTreinta[(10*d + u)-11]

    
    elif d == 0:
        resultado = (centenas[c] +  " " + unidades[u]) if u!=1 else (centenas[c] + " uno") # Ej 401 -> "Cuatrocientos dos"
        resultado = resultado if u!=0 else (centenas[c] + " " + decenas[d])  # Ej: 570 -> "Quinientos setenta"

        
    ##Restricciones sobre u
    elif u == 0:
        largoACortar = - (len(unidades[u]) + 3) 
        resultado = resultado[0:largoACortar]       # Si termina en cero, corto el " y cero" del final del string


    elif u == 1:
        resultado = centenas[c] + " " + decenas[d] + " y " + "uno"

    print(resultado)


##### Test


for i in range(0,999):
    palabras999(i)


# palabras2(1234567890)
# palabras2(567890)
#palabras2(101)