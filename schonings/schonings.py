# Shoning's Algorithm
# Diego Araque - A01026037
# Marco Torres - A01025334
# Fernando Valdeón - A01745186
# Uriel Aguilar - A01781698

import random as r

# Leer archivos en formato CNF
def parse(file):
    
    # Variables a regresar
    clauses = []
    n_vars = 0
    n_clauses = 0

    with open(file) as fp:

        # Leer línea
        line = fp.readline()
        line_counter = 1
        while line:

            # Ignorar la primera línea
            if line_counter == 1:
                pass

            # Ignorar la última o penúltima línea
            elif line[0] == "%" or line[0] == "0":
                pass

            # Obtener cantidad de variables y clausulas de la segunda línea
            elif line_counter == 2:
                n_vars = int(line.split(" ")[2])
                n_clauses = int(line.split(" ")[3])

            # Obtener información de clausulas
            else:
                nums = map(lambda n: int(n), line.split(" ")[0:3])
                clauses.append(list(nums))
            
            # Pasar a la siguiente línea
            line_counter += 1
            line = fp.readline()
    
    return n_vars, n_clauses, clauses


# Crear arreglo de variables booleanas random
def create_random_vars(n_vars):
    return [r.randint(0,1) for _ in range(n_vars)]


# Negar el arreglo variables booleanas random
def create_negative_random_vars(rand_vars):
    return [int(not(elem)) for elem in rand_vars]


# Obtener el resultado de una clausula
def process_clause(clause, pos_vars, neg_vars, res_clauses):
    
    # Obtener las xi de la clausula (-9, 11 -3)
    index_1 = clause[0]
    index_2 = clause[1]
    index_3 = clause[2]
    
    # Obtener los resultados de las variables correspondientes
    var_1 = pos_vars[index_1 - 1] if index_1 > 0 else neg_vars[abs(index_1) - 1]
    var_2 = pos_vars[index_2 - 1] if index_2 > 0 else neg_vars[abs(index_2) - 1]
    var_3 = pos_vars[index_3 - 1] if index_3 > 0 else neg_vars[abs(index_3) - 1]
    
    # Obtener el resultado final de la clausula
    res_clause = (var_1 or var_2 or var_3)
    res_clauses.append(res_clause)
        

# Main
if __name__ == "__main__":

    # Ingresar nombre de archivo por terminal
    arch = input("Ingresa un archivo de entrada: ")

    # Leer archivo
    n_vars, n_clauses, clauses = parse(arch)
    
    # Crear variables aleatorias
    pos_vars_array = create_random_vars(n_vars)
    neg_vars_array = create_negative_random_vars(pos_vars_array)

    res_found = False # Indicador si se ya se encontró un resultado
    res_clauses = [] # Arreglo de resultados de causulas
    
    # Repetir 3n veces
    for i in range(3 * n_vars):

        # Obtener los resultados de las clausulas
        for clause in clauses:
            process_clause(clause, pos_vars_array, neg_vars_array, res_clauses)

        # Obtener clausulas falsas
        if 0 in res_clauses:

            # Obtener un array de indices de clausulas que fallaron
            false_clauses = []

            for i in range(len(res_clauses)):
                if res_clauses[i] == 0:
                    false_clauses.append(i)

            # Escoger una clausula al azar y una de sus variables al azar
            rand_false_clause_index = r.choice(false_clauses)
            random_clause = clauses[rand_false_clause_index]
            random_var = r.choice(random_clause)
            
            # Invertir el valor de la variable para volver a probar las clausulas
            pos_vars_array[abs(random_var) - 1] = int(not(pos_vars_array[abs(random_var) - 1]))
            neg_vars_array[abs(random_var) - 1] = int(not(neg_vars_array[abs(random_var) - 1]))

            res_clauses.clear()

        # Si no falló ninguna clausula imprimit resultado
        else:
            print("--- SOLUCIÓN ---")
            print("Variables que satisfacen el 3-SAT:")
            print(pos_vars_array)
            res_found = True
            break

    
    if not res_found:
        print("--- SIN RESULTADOS ---")
        print("No se encontro solucion para esta secuencia, corre el algoritmo \nde nuevo para tratar de encontrar una solucion si esta existe")
    