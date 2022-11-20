# Grafo en forma de matriz de adyacencia

class Graph:
    def __init__(self, matrix):
        self.adjMatrix = matrix
        self.size = len(matrix)

    # Añadir vertice
    def add_edge(self, v1, v2, weight):
        self.adjMatrix[v1][v2] = weight
        self.adjMatrix[v2][v1] = weight

    # Imprimir matriz
    def print_matrix(self):
        for row in self.adjMatrix:
                print(row)

    # Obtener informacion de un vertice
    def vertex_info(self, v):
        return { vertex: weight for (vertex, weight) in zip(range(self.size), self.adjMatrix[v])}

    # Obtener el peso de dos vertices conectados
    def weight_of(self, v1, v2):
        return self.adjMatrix[v1][v2]

    # Tamaño de la matriz
    def __len__(self):
        return self.size

