# KPM algorithm
# Marco Torres
# Diego Araque
# Fer Valdeón
# Uriel Aguilar


def kmp(mainString, pattern):

    n = len(mainString)
    m = len(pattern)

    i = 0
    j = 0

    locArray = []
    
    while i < n:

        #Si coinciden recorrer en ambos strings
        if mainString[i] == pattern[j]:
            i += 1 
            j += 1

            # si se llego al final del pattern y coinciden se encontro 
            if j == m:
                locArray.append(i-j)
                j = 0
           
        else:
            # si coincide un caracter que no es el primero regresa el indice de j
            if j > 0:
                j -= 1
            else: 
                i += 1

    return locArray
                

if __name__ == "__main__":

    mainString = input("Ingresa la cadena de texto: ")
    pattern = input("Ingresa el patron que estas buscando: ")

    locArray = kmp(mainString, pattern)
    print(locArray)

        

  