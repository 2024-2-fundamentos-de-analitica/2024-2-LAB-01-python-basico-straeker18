"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_06():
    with open("files/input/data.csv", "r") as file:
        lines = file.readlines()
    
    values_dict = {}
    
    for line in lines:
        columns = line.strip().split("\t")  # Suponiendo que las columnas están separadas por tabulaciones
        key_values = columns[4].split(",")  # La columna 5 (índice 4) tiene pares clave:valor
        
        for pair in key_values:
            key, value = pair.split(":")
            value = int(value)
            
            if key not in values_dict:
                values_dict[key] = [value, value]  # Inicializa con [mínimo, máximo]
            else:
                values_dict[key][0] = min(values_dict[key][0], value)  # Actualiza el mínimo
                values_dict[key][1] = max(values_dict[key][1], value)  # Actualiza el máximo
    
    result = sorted([(key, values[0], values[1]) for key, values in values_dict.items()])
    
    return result

# Llamar la función y mostrar el resultado
print(pregunta_06())
"""
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
