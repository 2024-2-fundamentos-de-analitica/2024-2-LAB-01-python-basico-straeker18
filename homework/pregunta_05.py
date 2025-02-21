"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    min_max_values = {}
    with open("files/input/data.csv", "r") as file:
        for line in file:
            columns = line.strip().split("\t")  # Suponiendo que el separador es tabulador
            letter = columns[0]  # Primera columna
            value = int(columns[1])  # Segunda columna convertida a entero
            
            if letter not in min_max_values:
                min_max_values[letter] = [value, value]  # Inicializar con [min, max]
            else:
                min_max_values[letter][0] = min(min_max_values[letter][0], value)
                min_max_values[letter][1] = max(min_max_values[letter][1], value)
    
    sorted_min_max = sorted((k, v[1], v[0]) for k, v in min_max_values.items())  # Ordenar y estructurar salida
    return sorted_min_max

# Llamada a la función y muestra del resultado
resultado = pregunta_05()
print(resultado)
"""
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
