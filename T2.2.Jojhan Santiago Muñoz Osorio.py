def etapa_segun_edad():
    print("Bienvenido este programa determina la etapa de vida según la edad ingresada.")
    edad = int(input("Ingrese su edad: "))
    if edad >= 0 and edad <= 12:
        print("Usted se encuentra en la etapa de niñez.")
    else:
        if edad > 12 and edad <= 18:
            print("Usted se encuentra en la etapa de adolescencia.")
        else:
            if edad > 18 and edad <= 30:
                print("Usted se encuentra en la etapa de juventud.")
            else:
                if edad > 30 and edad <= 50:
                    print("Usted se encuentra en la etapa de adultez.")
                else:
                    print("Usted se encuentra en la etapa de vejez.")
print("Gracias por usar el programa.")
etapa_segun_edad()