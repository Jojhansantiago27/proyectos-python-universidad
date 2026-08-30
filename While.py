'''def alcancia():
    print("Bienvenido a tu alcancia virtual")
    limite = float(input("Ingresa el limite o tu objetivo de ahorro: "))
    total = 0
    while total <= limite:
        deposito = float(input("Ingresa cuanto dinero vas a depositar: "))
        total += deposito
    print(f"\nEl dinero total ahorrado es: {total}")
    print("Alcanzaste el objetivo final")

alcancia()
'''
'''def adivinar():
    print("Bienvenido a este juego, deberás poner un número del 1 al 10 hasta que lo adivines")
    x = 7
    cont = 0
    num = int(input("Ingresa un número del 1 al 10: "))

    while num != x:
        cont += 1
        if num > x:
            print("El número que digitaste es muy alto")
        elif num < x:
            print("El número que digitaste es muy bajo")
        num = int(input("Intenta de nuevo: "))

    cont += 1
    print(f"\n¡Acertaste! El número era: {x}")
    print(f"Te tomó {cont} intentos")

adivinar()
'''
'''def cajero():
    print("\nBienvenido al cajero automático")
    contraseña = int(input("\nIngrese su contraseña por favor: "))
    dinero_cajero = 100000
    usuario = 1

    if contraseña == 1013614139:
        print("Acceso concedido")

        while True:  # se repite indefinidamente hasta que hagamos "break"
            print(f"\nUsuario {usuario}")
            servicio = int(input("¿Qué servicio desea? (1=Consultar saldo, 2=Depositar, 3=Retirar, 4=Salir): "))

            if servicio == 1:
                print(f"Tu saldo es: ${dinero_cajero}")
            elif servicio == 2:
                depositar = float(input("¿Cuánto desea depositar? "))
                dinero_cajero += depositar
                print(f"Depósito exitoso. Nuevo saldo: ${dinero_cajero}")
            elif servicio == 3:
                retirar = float(input("¿Cuánto desea retirar? "))
                if retirar > dinero_cajero:
                    print("Fondos insuficientes")
                else:
                    dinero_cajero -= retirar
                    print(f"Retiro exitoso. Nuevo saldo: ${dinero_cajero}")
            elif servicio == 4:
                print("Gracias por usar el cajero. ¡Hasta pronto!")
                break  # rompe el while, termina el bucle
            else:
                print("Opción no válida")

            usuario += 1  # esto está fuera del if/elif, se ejecuta siempre

    else:
        print("Acceso inválido")

cajero() '''
'''def presupuesto():
    print("Bienvenido al programa")
    limite = float(input("Escribe tu presupuesto límite: "))
    saldo = limite  # el saldo EMPIEZA siendo el límite completo

    while saldo > 0:
        retiro = float(input("Cuánto vas a retirar: "))
        saldo -= retiro
        print(f"Te queda: {saldo}")

    print("\nTe quedaste sin presupuesto")
    print(f"Saldo final: {saldo}")

presupuesto()'''


'''def pedidos():
    print("Bienvenido Estimado Usuario")
    stock = 100
    pedidos_atendidos = 0

    while stock > 0:
        unidades = int(input(f"\nStock disponible: {stock}. ¿Cuántas unidades deseas? "))

        if unidades > stock:
            print("No hay suficiente stock para este pedido")
        else:
            stock -= unidades
            pedidos_atendidos += 1
            print(f"Pedido atendido. Quedan {stock} unidades")

    print("\nTe quedaste sin stock")
    print(f"Se atendieron {pedidos_atendidos} pedidos con éxito")

pedidos()'''

'''def propina():
    print("Bienvenido Estimado Usuario")
    total = 0
    cantidad_propinas = 0   # con "=", no con ":"
    mayor_propina = 0

    while True:  # se repite siempre, hasta que hagamos "break"
        dinero = float(input("¿Cuánto dinero en propinas recibiste? (-1 para terminar): "))

        if dinero == -1:
            break  # aquí se sale del while

        if dinero <= 0:
            print("Valor inválido")
        else:
            total += dinero
            cantidad_propinas += 1
            if dinero > mayor_propina:
                mayor_propina = dinero
            print(f"Llevas acumulado: {total}")

    print(f"\nTotal de propinas recibidas: {total}")
    if cantidad_propinas > 0:
        print(f"Promedio por propina: {total / cantidad_propinas}")
        print(f"Propina más alta: {mayor_propina}")
    else:
        print("No obtuviste ganancias")

propina()
'''
'''def contraseña():
    print("Bienvenido Estimado Usuario")
    contraseña = 1013614139
    intentos = 0  # con "=", así la variable sí existe de verdad

    while True:
        clave = int(input("Escribe tu pin: "))

        if clave == contraseña:
            print("Bienvenido a su cuenta")
            break  # acertó -> termina el bucle aquí

        else:
            intentos += 1  # cada clave incorrecta suma un intento

            if intentos >= 3:
                print("Usted se quedó sin intentos")
                break  # se acabaron los intentos -> termina el bucle aquí
            else:
                print(f"Clave incorrecta. Le quedan {3 - intentos} intentos")
                # aquí NO hay break, para que el while vuelva a preguntar

contraseña()
'''
def maquina_expendedora():
    print("Bienvenido a la maquina expendedora")
    producto=2500
    monedas=0
    while producto > 0:
        dinero=float(input("Escribe cuanto dinero ingresaste en la primera moneda"))
        if dinero>=producto:
            print("\nUsted compro el producto")
        else:
            producto-=dinero 
            monedas+=1
    print(f"El dinero que le falta para comprar el producto es:{producto}")
    print("\nTe falto dinero")
    print("Gracias por usar el programa")
maquina_expendedora()    

