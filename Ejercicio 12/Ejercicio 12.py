def merge(a,b):
    i=0
    j=0
    while i<len(a) or j<len(b):
        # a[i] es una tupla de forma (numero, repeticion)
        if j>=len(b) or (i<len(a) and a[i][0]<=b[j][0]):
            # si se repiten dos tuplas con el mismo numero
            if a[i][0]==b[j][0]:
                # Sumo las repeticiones y dejo una tupla con el numero de repeticiones
                a[i] = (a[i][0], b[j][1] + a[i][1])
                j += 1
            yield a[i]
            i=i+1
        else:
            yield b[j]
            j=j+1
            

a=[(12,2),(34,1),(56,3),(74,1),(81,1)]
b=[(10,3),(12,5),(65,1),(74,1),(90,3)]

# c=[x for x in merge(a,b)]
# print(c)


d=[x for x in merge(b,a)]

print(d)

