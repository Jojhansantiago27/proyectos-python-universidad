def repartir_herencia():
    print("Bienvenido Estimado Usuario")
    dinero = float(input("Ingrese el dinero ahorrado por el fallecido: "))
    edad1 = int(input("Ingrese la edad de la persona 1 (primera en llegar): "))
    edad2 = int(input("Ingrese la edad de la persona 2 (segunda en llegar): "))
    edad3 = int(input("Ingrese la edad de la persona 3 (tercera en llegar): "))
    edad4 = int(input("Ingrese la edad de la persona 4 (cuarta en llegar): "))

    if edad1 % 2 == 0 and edad2 % 2 == 0 and edad3 % 2 == 0 and edad4 % 2 == 0:

        monto = dinero / 4
        print(f"Reparto por partes iguales: cada persona recibe ${monto:.2f}")
    else:
        if (edad1 < edad2 < edad3 < edad4) or (edad1 > edad2 > edad3 > edad4):

            monto1 = dinero * 0.10
            monto2 = dinero * 0.20
            monto3 = dinero * 0.30
            monto4 = dinero * 0.40
            print(f"Persona 1 (edad {edad1}): ${monto1:.2f}")
            print(f"Persona 2 (edad {edad2}): ${monto2:.2f}")
            print(f"Persona 3 (edad {edad3}): ${monto3:.2f}")
            print(f"Persona 4 (edad {edad4}): ${monto4:.2f}")
        else:
            if (edad1 + edad2 + edad3 + edad4) % 2 != 0:
                mitad = dinero / 2
                monto_persona = mitad / 4
                print(f"Cada persona recibe: ${monto_persona:.2f}")
                print(f"Obra de caridad recibe: ${mitad:.2f}")
            else:
                print(f"Obra de caridad recibe: ${dinero:.2f}")

print("Gracias por usar el programa")
repartir_herencia()