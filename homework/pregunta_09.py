"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    # Leer el archivo data.csv
    with open('files/input/data.csv', 'r') as file:
        lines = file.readlines()

    # Crear un diccionario para almacenar la frecuencia de cada clave
    key_count = {}

    # Procesar cada línea del archivo
    for line in lines:
        # Dividir la línea en columnas
        columns = line.strip().split('\t')
        
        # Obtener la columna 5 (índice 4)
        col5 = columns[4]
        
        # Dividir la columna 5 en pares clave-valor
        pairs = col5.split(',')
        
        # Procesar cada par clave-valor
        for pair in pairs:
            # Extraer la clave (parte antes del ':')
            key = pair.split(':')[0]
            
            # Incrementar el contador para esta clave
            if key in key_count:
                key_count[key] += 1
            else:
                key_count[key] = 1

    # Ordenar el diccionario por clave para facilitar la comparación con el resultado esperado
    sorted_key_count = {k: key_count[k] for k in sorted(key_count)}

    return sorted_key_count

# Llamar a la función y mostrar el resultado
print(pregunta_09())
