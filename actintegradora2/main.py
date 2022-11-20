# Actividad integradora 2
# Marco
# Fer
# Uriel
# Diego

from graph import Graph

def parce(file):
    """
    La funcion obtiene una
    matriz de adyacencia del grafo
    """
    
    with open(file) as f:
        matrix = []

        line = f.readline()
        line_counter = 1 
        while line:
            # Obtener el tamaño de la matriz de la primera linea
            if line_counter == 1:
                size = line
            
            # Ignorar la segunda linea
            elif line_counter == 2:
                pass
            
            # Obtener la matriz
            else:
                row = map(lambda n: int(n), line.split(" "))
                matrix.append(list(row))

            # Pasar a la siguiente línea
            line_counter += 1
            line = f.readline()
    
    return matrix
    
        
if __name__ == "__main__":
    matrix = parce("files/example.txt")
    graph = Graph(matrix)
    
    print(graph.weight_of(2,1))
