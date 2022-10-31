# Z - function
# Uriel, Diego, Fer, Marco

def parse(file):
    """
    Funcion que parsea un archivo csv en un array 
    """
    f = open(file)
    arr = []

    while True:
        char = f.read(1)

        if not char:
            break  

        if char != ",":
            arr.append(int(char))

    f.close()

    return arr

def compare(prefix, arr):
    """
    Funcion que cuenta cuantos substrings
    se repiten en dos arrays
    """
    counter = 0

    for i in range(len(prefix)):
        # Si el ultimo caracter coincide, no se entrara en el else,
        # para prevenir eso ocupamos el try
        try:
            if prefix[i] == arr[i]:
                counter += 1
            else:
                break
        except IndexError:
            return counter
    
    return counter    

def z_function(arr):
    """
    El resultado regresara las comparaciones de la substring en cada indice
    """
    # El prefijo contendra el primer caracter de la string al iniciar
    prefix = [arr[0]]
    result = []

    for i in range(1, len(arr)):
        prefix.append(arr[i])
        # El array para compara se pasara desde el caracter actual hasta el final
        repeated = compare(prefix, arr[i:])
        result.append(repeated)
    
    return result


if __name__ == "__main__":
    arr = parse("files/Z function-Test01.csv")
   
    
    # Ejemplo de la clase
    #arr = [0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1]
    result = z_function(arr)
    
    print(result)