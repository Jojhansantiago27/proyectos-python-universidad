def definitiva_ipro():
    print("Bienvenido este programa calcula la calificación definitiva en la asignatura Introducción a la Programación (IPRO).")
    tercio1 = float(input("Ingrese la calificación del primer tercio (0.0 - 5.0): "))
    tercio2 = float(input("Ingrese la calificación del segundo tercio (0.0 - 5.0): "))
    tercio3 = float(input("Ingrese la calificación del tercer tercio (0.0 - 5.0): "))
    definitiva = tercio1 * 0.3 + tercio2 * 0.3 + tercio3 * 0.4
    print(f"La calificación definitiva en la asignatura Introducción a la Programación (IPRO) es: {definitiva:.2f}")
    if definitiva >= 0.0 and definitiva <= 1.0:
        print("Quisiera saber qué pasó y por qué no solicitó cancelación.")
    else:
        if definitiva > 1.0 and definitiva <= 2.0:
            print("Veo que hubo resultados, pero no suficientes.")
        else:
            if definitiva > 2.0 and definitiva < 3.0:
                print("Puede que haya estado a punto de aprobar. Le sugiero apuntarle al 5.0, no al 3.0.")
            else:
                if definitiva >= 3.0 and definitiva < 4.0:
                    print("Buen resultado. ¡Felicitaciones!")
                else:
                    if definitiva >= 4.0 and definitiva <= 5.0:
                        print("¡Excelente resultado! Siga así.")
                    else:
                        print("La calificación ingresada no es válida.")

print("Gracias por usar el programa.")
definitiva_ipro()
