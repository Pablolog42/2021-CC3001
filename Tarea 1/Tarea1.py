
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

    if resultado[0] == " ":         #Saco los espacios del principio porque se ven feos unu
        resultado = resultado[1:]

    return resultado


##### Test


# for i in range(0,999):
#     print(palabras999(i))


# palabras2(1234567890)
# palabras2(567890)
#palabras2(101)


def numeroATexto(n):

    assert n < 1000000000 #Sólo se trabaja con numeros bajo cien millones

    (cM,dM, uM,cm,dm,um,c,d,u)= ((n%1000000000//100000000),(n%100000000//10000000),(n%10000000//1000000),(n%1000000//100000),(n%100000//10000),(n%10000//1000),(n%1000//100),(n%100//10),n%10) 

    resultado = palabras999(c*100 + d*10 + u)

    sumaCentena = c + d + u
    sumaMillones = cM + dM + uM
    sumaMiles = cm + dm + um

    # Voy armando de a poco el string resultado acorde a lo que se necesite
    if sumaMiles != 0:
        resultado = palabras999(cm*100 + dm*10 + um) + " mil " + resultado

    if sumaMillones != 0:
        resultado = palabras999(cM*100 + dM*10 + uM)  + " millones " + resultado    

    if sumaCentena == 0:
        resultado = resultado[0:-5] #quito el " cero" del final del resultado (-5 pq' son 5 caracteres a cortar hacia atras)

    #Para evitar que diga "uno mil cien" en vez de "mil cien"
    #if um == 1:

    return resultado


print(numeroATexto(1001000))    #TODO: ARREGLAR ESTO CON LOS UNO MILLONES Y EL UNO MIL
