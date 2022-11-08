# KPM algorithm
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

    mainString = input("Ingresa la cadena de texto: ")
    pattern = input("Ingresa el patron que estas buscando: ")

    # mainString = "101001101011100001111110001010101001100111110001001101011100011110110111000011101101110100110111101101011111101110001101110011000010000011100100011000011000000111101011110101101101100011111000000111000000010000011000010111111011001010011100000011101001111000110110111001100001111110001010001010111100101000100000101110010000111101101110111010101000101001010011101010100011000011100000000111100110100"
    # pattern = "110001"

    # calculamos el array de prefijos con la funcion getPrevArr
    prevArr = getPrevArr(pattern, 0, [i for i in range(len(pattern))], len(pattern))

    locArray = kmp(mainString, pattern, prevArr)
    print(locArray)

  