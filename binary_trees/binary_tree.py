from node import Node

class BinaryTree:

    def __init__(self):
        #Raiz o parte mas alta del arbol
        self.root = None
    

    def insert ( self, value ):


        new_node = Node( value )

        #si el arbol esta vacio, establecer el nodo como la raiz
        if self.root is None:
            self.root = new_node
            return True
        
        temp = self.root 

        while( True ):

            #No puede haber valores repetidos en el arbol
            if new_node.value == temp.value:
                return False


            # Ir a la parte izquierda del arbol si el nuevo valor es menor al nodo actual
            if new_node.value < temp.value:
                
                #Si hay un espacio vacio en el arbol, entonces guardar el nuevo valor en ese espacio
                if temp.left is None:

                    temp.left = new_node
                    return True

                # Continuar recorriendo el arbol hacia la izquiera si no hay espacio
                temp = temp.left 
   
            
            # Hacer el recorrido por la derecha 
            else:   

                if temp.right is None:

                    temp.right = new_node
                    return True
            
                temp = temp.right



    def levelByLevel (self):

        #Breath first search
        #Itera el arbol de renglon en renglon 

        curr = self.root
        queue = []
        string = ""

        counter = 1
        queue.append(curr)

        while len(queue) > 0:
            """
                Este loop iterara mientras siga existiendo elementos 
                en el arbol 
            """
            
            for _ in range(counter):
                
                # Quita el elemento acual de la cola y agrega a la lista de resultados
                curr = queue.pop(0)
                counter -= 1

                string += str(curr.value) + " "

                #Agregar a la cola el elemento de la izquierda y el de la derecha
                if curr.left is not None:
                    counter += 1
                    queue.append(curr.left)

                if curr.right is not None:
                    counter += 1
                    queue.append(curr.right)

            print(string)
            string = ""
        
    