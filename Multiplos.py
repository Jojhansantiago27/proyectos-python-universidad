def multiplos():
    print("Ingrese un número el primer numero para evaluar si es múltiplo del segundo.")
    num1 = int(input("Primer número: "))
    num2 = int(input("Segundo número: "))
    if num2 == 0:
        print("No se puede dividir por cero.")
    else:
        if num1 % num2 == 0:
            print(f"{num1} es múltiplo de {num2}.")
        else:
            print(f"{num1} no es múltiplo de {num2}.")
print("Gracias por usar el programa.")
multiplos()