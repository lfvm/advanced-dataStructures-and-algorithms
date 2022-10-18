# Shoning's Algorithm
# Diego Araque - A01026037
# Marco Torres - A01025334
# Fernando Valdeón - A01745186
# Uriel Aguilar - A01781698

import random as r
from turtle import pos

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
    

# Escribir el archivo de soluciones
def write_file(file, init_vars, satisfied_vars, clauses, unsatisfied_arr, satisfied_arr, modified_clauses_arr, modified_var_arr, modified_vars_arr):
    
    with(open(file, "w")) as fp:

        # Resultado
        fp.write("RESULTADO:\n")
        if satisfied_vars == None:
            fp.write("No se encontraron variables satisfactorias\n")
        else:
            fp.write("Variables satisfactorias: " + str(satisfied_vars) + "\n")

        # Clausulas
        fp.write("\nCLAUSULAS:\n")
        for i in range(len(clauses)):
            fp.write(f"{i}: {str(clauses[i])}\n")

        # Variables iniciales
        fp.write("\nVARIABLES INICIALES:\n")
        fp.write(init_vars + "\n")
        
        # Imprimir datos de iteraciones
        i = 0
        while i < (len(unsatisfied_arr)):
            fp.write("\nITERACION " + str(i) + "\n")
            fp.write("Variables evaluadas: " + str(modified_vars_arr[i]) + "\n")
            fp.write("Clausulas que se satisfacen: " + str(satisfied_arr[i]) + "\n")
            fp.write("Clausulas que no se satisfacen: " + str(unsatisfied_arr[i]) + "\n")
            fp.write("Clausulas aleatoria para modificar: " + str(modified_clauses_arr[i]) + "\n")
            fp.write("Variables aleatoria para modificar: " + str(modified_var_arr[i]) + "\n")
            if i + 1 < len(modified_vars_arr):
                fp.write("Siguientes variables a evaluar: " + str(modified_vars_arr[i+1])+"\n")
            
            i += 1

        if satisfied_vars != None:
            fp.write("\nITERACION " + str(i) + "\n")
            fp.write("Variables evaluadas: " + str(satisfied_vars) + "\n")
            fp.write("Todas las clausulas se satisfacen")


        

# Main
if __name__ == "__main__":

    # Ingresar nombre de archivo por terminal
    arch = input("Ingresa un archivo de entrada: ")

    # Leer archivo
    n_vars, n_clauses, clauses = parse(arch)
    
    # Crear variables aleatorias
    pos_vars_array = create_random_vars(n_vars)
    init_vars = str(pos_vars_array)
    neg_vars_array = create_negative_random_vars(pos_vars_array)

    # Variables para archivo de resultados final
    unsatisfied_arr = []
    satisfied_arr = []
    modified_clauses_arr = []
    modified_var_arr=[]
    modified_vars_arr=[]

    modified_vars_arr.append(str(init_vars))

    res_found = False # Indicador si se ya se encontró un resultado
    res_clauses = [] # Arreglo de resultados de causulas
    
    # Repetir 3n veces o hasta que se encuentre el resultado
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

            # Añadir al array de clausulas que fallaron
            unsatisfied_arr.append(false_clauses)

            # Añadir al array de clausulas satisfactorias
            true_clauses = []
            for i in range(len(res_clauses)):
                if res_clauses[i] == 1:
                    true_clauses.append(i)
            satisfied_arr.append(true_clauses)
            
            # Escoger una clausula al azar y una de sus variables al azar
            rand_false_clause_index = r.choice(false_clauses)
            random_clause = clauses[rand_false_clause_index]
            modified_clauses_arr.append(random_clause)
            random_var = r.choice(random_clause)
            modified_var_arr.append(random_var)
            
            # Invertir el valor de la variable para volver a probar las clausulas
            pos_vars_array[abs(random_var) - 1] = int(not(pos_vars_array[abs(random_var) - 1]))
            neg_vars_array[abs(random_var) - 1] = int(not(neg_vars_array[abs(random_var) - 1]))
            
            # Añadir siguientes variables
            modified_vars_arr.append(str(pos_vars_array))

            res_clauses.clear()

        # Si no falló ninguna clausula
        else:
            print("--- SOLUCIÓN ---")
            print(pos_vars_array)
            write_file("solution.txt", init_vars, pos_vars_array, clauses, unsatisfied_arr, satisfied_arr, modified_clauses_arr, modified_var_arr, modified_vars_arr)
            res_found = True
            break

    
    if not res_found:
        print("--- SIN RESULTADOS ---")
        print("No se encontraron variables satisfactorias")
        write_file("solution.txt", init_vars, None, clauses, unsatisfied_arr, satisfied_arr, modified_clauses_arr, modified_var_arr, modified_vars_arr)
    