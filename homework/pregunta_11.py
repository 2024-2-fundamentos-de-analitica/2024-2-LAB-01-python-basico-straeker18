"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    with open("files/input/data.csv", "r") as file:
        lines = file.readlines()

    sum_dict = {}

    for line in lines:
        columns = line.strip().split()  # Separar por tabulaciones
        number = int(columns[1])  # Convertir la columna 2 a entero
        letters = columns[3].split(",")  # Obtener las letras de la columna 4

        for letter in letters:
            if letter not in sum_dict:
                sum_dict[letter] = 0
            sum_dict[letter] += number  # Sumar el valor de la columna 2

    return dict(sorted(sum_dict.items()))  # Ordenar alfabéticamente y devolver

# Llamar a la función y mostrar el resultado
print(pregunta_11())

