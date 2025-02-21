"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    months = {}
    with open("files/input/data.csv", "r") as file:
        for line in file:
            columns = line.strip().split("\t")  # Suponiendo que el separador es tabulador
            date = columns[2]  # Tercera columna (fecha)
            month = date.split("-")[1]  # Extraer el mes
            months[month] = months.get(month, 0) + 1
    
    sorted_months = sorted(months.items())  # Ordenar por mes
    return sorted_months

# Llamada a la función y muestra del resultado
print(pregunta_04())

"""
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
