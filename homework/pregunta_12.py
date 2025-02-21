"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    with open("files/input/data.csv", "r") as file:
        lines = file.readlines()

    sum_dict = {}

    for line in lines:
        columns = line.strip().split("\t")  # Separar por tabulaciones
        letter = columns[0]  # Columna 1
        key_values = columns[4].split(",")  # Columna 5 (diccionario de claves-valores)

        total_sum = sum(int(pair.split(":")[1]) for pair in key_values)  # Sumar los valores de la columna 5

        if letter not in sum_dict:
            sum_dict[letter] = 0
        sum_dict[letter] += total_sum  # Acumular la suma en el diccionario

    return dict(sorted(sum_dict.items()))  # Ordenar el diccionario y devolver

# Llamar a la función y mostrar el resultado
print(pregunta_12())
