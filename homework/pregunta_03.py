"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_03():
    sums = {}
    with open("files/input/data.csv", "r") as file:
        for line in file:
            columns = line.strip().split("\t")  # Suponiendo que el separador es tabulador
            letter = columns[0]  # Primera columna
            value = int(columns[1])  # Segunda columna convertida a entero
            sums[letter] = sums.get(letter, 0) + value
    
    sorted_sums = sorted(sums.items())  # Ordenar alfabéticamente
    return sorted_sums

# Llamada a la función y muestra del resultado
print(pregunta_03())

"""
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
