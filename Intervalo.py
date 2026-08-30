def intervalo_reales():
    print("Bienvenido al programa.")
    
    li = float(input("Limite inferior: "))
    ls = float(input("Limite superior: "))
    numero = float(input("Numero a evaluar: "))

    if numero < li:
        print("El numero esta a la izquierda del intervalo.")
    else:
        if numero > ls:
            print("El numero esta a derecha del intervalo.")
        else:
            print("El numero esta dentro del intervalo.")

    print("Gracias por usar el programa.")

intervalo_reales()