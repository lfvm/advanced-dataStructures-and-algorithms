# Act Integradora 1
# Marco Torres
# Diego Araque
# Fer Valdeón
# Uriel Aguilar


def kmp(mainString, pattern, prevArr):

    # longitudes del patron y el texto en el que buscaremos
    n = len(mainString)
    m = len(pattern)

    # inicializamos los indices en 0
    i = 0
    j = 0

    # el array con los indices en donde se encuentra el patron
    # empieza vacio
    locArray = []
    
    while i < n:

        #Si coinciden recorrer en ambos strings
        if mainString[i] == pattern[j]:
            i += 1 
            j += 1

            # si se llego al final del pattern y coinciden se encontro 
            if j == m:
                # añadimos el indice en donde se encontro el patron
                locArray.append(i-j)
                # reiniciamos el indice del patron
                j = prevArr[j-1]

        # si no coinciden estos valores
        else:
            # si el indice j es diferente de 0 se reinicia
            if j != 0:
                j = prevArr[j-1]
            # si es 0 se incrementa el indice del string 
            # en el que estamos buscando
            else:
                i += 1

    return locArray


def getPrevArr(pattern, length, prevArr, m):
    # nuestro iterador empieza en 1
    i = 1
    # mientras nuestro contador sea menor a la longitud del patron
    # seguiremos en este loop
    while i < m:
        # si el caracter en la posicion i es igual al caracter en la posicion length(que empieza en cero)
        # incrementamos nuestra 1, nuestra longitud del prefijo y añadimos esta al prevArray 
        if pattern[i] == pattern[length]:
            length += 1
            prevArr[i] = length
            i += 1
        # si no es igual, checamos si la longitud es mayor a 0.
        # si ese es el caso la longitud del prefijo se reinicia
        elif length != 0:
            length = prevArr[length - 1]
        # si es 0, el prefijo es 0 e incrementamos el contador
        else:
            prevArr[i] = 0
            i += 1

    return prevArr

if __name__ == "__main__":

    transmission = "61cea08d3adahp792db2d0b49012f26f1a77d8d759cc4fedadahp997e099ca6abc3ed5c7e64bc4f1adahp1adahpf26f297cca3aadahp5bb5fb0364df26f323f38a20"

    mcode1 = "adahp"
    mcode2 = "fhfh123"
    mcode3 = "f26f"

    # calculamos el array de prefijos con la funcion getPrevArr
    prevArr = getPrevArr(mcode1, 0, [i for i in range(len(mcode1))], len(mcode1))
    prevArr2 = getPrevArr(mcode2, 0, [i for i in range(len(mcode2))], len(mcode2))
    prevArr3 = getPrevArr(mcode3, 0, [i for i in range(len(mcode3))], len(mcode3))

    locArray = kmp(transmission, mcode1, prevArr)
    locArray2 = kmp(transmission, mcode2, prevArr2)
    locArray3 = kmp(transmission, mcode3, prevArr3)

    print(locArray)
    print(locArray2)
    print(locArray3)