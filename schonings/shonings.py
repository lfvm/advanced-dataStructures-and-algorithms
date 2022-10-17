# Shoning's Algorithm
# Uriel
# Diego
# Marco
# Fer

import random as r

# Leer archivos en formato CNF
def parse(file):
    
    # Variables a regresar
    clauses = []
    n_vars = 0
    n_clauses = 0

    # Crear array de n indices
    with open(file) as fp:

        # Leer línea
        line = fp.readline()
        line_counter = 1
        while line:
            # Ignorar la primera línea
            if line_counter == 1:
                pass

            # Ignorar la última o penúltima slínea
            elif line[0] == "%" or line[0] == "0":
                pass

            # Obtener cantidad de variables y clausulas de la segunda línea
            elif line_counter == 2:
                n_vars = int(line.strip().split(" ")[2])
                n_clauses = int(line.strip().split(" ")[3])

            # Obtener información de clausulas
            else:
                nums = map(lambda n: int(n), line.strip().split(" ")[0:3])
                clauses.append(list(nums))
            
            # Pasar a la siguiente línea
            line_counter += 1
            line = fp.readline()
    
    return n_vars, n_clauses, clauses


# Crear arreglo de variables booleanas
def create_random_vars(n_vars):
    return [r.randint(0,1) for _ in range(n_vars)]


# Negar el arreglo variables booleanas
def create_negative_random_vars(rand_vars):
    return [int(not(elem)) for elem in rand_vars]


# Analizar todas las las clausulas
def process_clauses(clause, pos_vars, neg_vars, res_clauses):
    
    # Para cada clausula
    # clause = clauses[0]

    index_1 = clause[0]
    index_2 = clause[1]
    index_3 = clause[2]

    #print("Indexes:", index_1, index_2, index_3)
    
    var_1 = pos_vars[index_1 - 1] if index_1 > 0 else neg_vars[abs(index_1) - 1]
    var_2 = pos_vars[index_2 - 1] if index_2 > 0 else neg_vars[abs(index_2) - 1]
    var_3 = pos_vars[index_3 - 1] if index_3 > 0 else neg_vars[abs(index_3) - 1]
    
    #print("Vars:", var_1, var_2, var_3)
    
    
    res_clause = (var_1 or var_2 or var_3)
    res_clauses.append(res_clause)
    #print("result", res_clauses)
        


# Main
if __name__ == "__main__":

    # Leer archivos
    n_vars, n_clauses, clauses = parse("04. Instance_3SAT_example.txt")

    # Crear variables aleatorias
    pos_vars_array = create_random_vars(n_vars)
    neg_vars_array = create_negative_random_vars(pos_vars_array)

    # Arreglo de resultados de causulas
    res_found = False
    res_clauses = []
    
    for i in range(3 * n_vars):
        # Recorrer cada clausula de la matriz
        for clause in clauses:
            # Res clauses se esta pasando por referencia
            process_clauses(clause, pos_vars_array, neg_vars_array, res_clauses)

        # Comprobar si hay clausulas falsas
        if 0 in res_clauses:
            false_clauses = []

            # Obtener un array de indices de clausulas que son 0
            for i in range(len(res_clauses)):
                if res_clauses[i] == 0:
                    false_clauses.append(i)

            #Escoger al azar entre las clausulas y los indices de esa clausula
            rand_false_clause_index = r.choice(false_clauses)
            random_clause = clauses[rand_false_clause_index]
            random_var = r.choice(random_clause)
            
            #Invertir el valor de la variable
            pos_vars_array[abs(random_var) - 1] = int(not(pos_vars_array[abs(random_var) - 1]))
            neg_vars_array[abs(random_var) - 1] = int(not(neg_vars_array[abs(random_var) - 1]))

            res_clauses.clear()

        else:
            print("Variables que satisfacen el 3-SAT:")
            print(pos_vars_array)
            res_found = True
            break

    
    if not res_found:
        print("No se encontro solucion para esta secuencia, corre el algoritmo de nuevo para tratar de encontrar una solucion si esta existe")
    