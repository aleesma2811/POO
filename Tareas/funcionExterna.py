def totalDuracion(**diccionario):
    total = 0
    for cancion in diccionario.keys():
        total += int(diccionario[cancion]['duracion_ms'])
    return total
