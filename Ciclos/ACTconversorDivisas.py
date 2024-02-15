def conversorDivisas(nombre, min, max, cambio):
    print(f"Hola {nombre}")
    for num in range(min, max + 1):
        print(f"{num} pesos son {num*cambio} dolares")
conversorDivisas("ALe", 1,8,20)
