from graph import Graph



g = Graph()

#Agregar un elemento
g.addVertex('C')
g.addVertex('A')
g.addVertex('B')
g.addVertex('D')
#Agregar conexiones
g.addEdge('A','B')
g.addEdge('C','B')
g.addEdge('C','A')

#Imprimir el grapho
print("Grafo original")
g.print_graph()

#Eliminar conexiones
print("Grafo despues de borrar conexiones")
g.remove_edge('A','B')
g.remove_edge('A','D')
g.print_graph()


#Eliminar un item
print("Grafo despues de borrar un item")
g.remove_vertex('A')
g.print_graph()
