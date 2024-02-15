def sumaMuchos(*numeros):
    resultado = 0
    for n in numeros:
        resultado += n
    return resultado
print(sumaMuchos(1, 2, 3, 4))

lista_num = [10,20,30]
print(sumaMuchos(*lista_num))