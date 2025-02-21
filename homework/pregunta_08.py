"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
# Leer el archivo data.csv
    with open('files/input/data.csv', 'r') as file:
        lines = file.readlines()

    # Crear un diccionario para almacenar los valores de la columna 1 como clave
    # y las letras asociadas (columna 0) como valor en un conjunto (para evitar duplicados)
    col1_dict = {}

    # Procesar cada línea del archivo
    for line in lines:
        # Dividir la línea en columnas
        columns = line.strip().split('\t')
        
        # Obtener los valores de las columnas 0 y 1
        col0 = columns[0]  # Letra (columna 0)
        col1 = int(columns[1])  # Número (columna 1)
        
        # Si el valor de la columna 1 ya está en el diccionario, agregar la letra al conjunto
        if col1 in col1_dict:
            col1_dict[col1].add(col0)
        else:
            # Si no está, crear una nueva entrada en el diccionario con un conjunto que contenga la letra
            col1_dict[col1] = {col0}

    # Convertir los conjuntos a listas ordenadas y crear una lista de tuplas
    result = [(key, sorted(list(value))) for key, value in sorted(col1_dict.items())]

    return result

# Llamar a la función y mostrar el resultado
print(pregunta_08())