from graph import Graph
import csv

g = Graph()
 
# Leer archivo 
file = csv.reader(open("graph_example.txt"), delimiter='\n')
graphData = [row for row in file]

for nodeGraph in graphData:
   
    # Formatear string para poder acceder a los valores del grafo 
    pairTemp = nodeGraph[0]
    pairTemp = pairTemp.replace('(', '')
    pairTemp = pairTemp.replace(')', '').split(',')
    
    # Agregamos nuevo vértice si aún no estaba
    firstValue = int(pairTemp[0])
    secondValue = int(pairTemp[1])
    g.addVertex(firstValue)
    g.addVertex(secondValue)
    
    # Agregar conexion entre los vertices 
    g.addEdge(firstValue, secondValue)


# Imprimir el grafo
print("Grafo original")
g.print_graph()

print("_____________________DFS________________________________")
g.dfs()

