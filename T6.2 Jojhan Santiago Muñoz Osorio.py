def perros():
    print("Bienvenido estimado usuario")
    cont=0
    cant_misma=0
    cant_perro=0
    cant=int(input("Escribe la cantidad a evaluar"))
    while cont<cant:
        cont+=1
        edadH=int(input("Escribe la edad del humano a evaluar"))
        edadP=int(input("Escribe la edad del perro a evaluar"))
        cant_perro+=edadP
        equivalente = 20 + 4 * (edadP - 1)
        if edadH == equivalente:
            cant_misma += 1
    promedio_perro = cant_perro / cant
    equivalente_promedio = 20 + 4 * (promedio_perro - 1)
    print(f"La cantidad con misma edad es: {cant_misma}")
    print(f"La edad promedio de las mascotas es {promedio_perro} y el equivalente es {equivalente_promedio}")
    print("Gracias por usar el programa")
perros()
