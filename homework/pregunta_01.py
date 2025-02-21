"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_01():
    total = 0
    with open("files/input/data.csv", "r") as file:
        for line in file:
            columns = line.strip().split("\t")  # Suponiendo que el separador es tabulador
            total += int(columns[1])  # Segunda columna (índice 1) convertida a entero
    return total

# Llamada a la función y muestra del resultado
print(pregunta_01())
