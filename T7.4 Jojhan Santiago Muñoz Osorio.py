"""
Universidad Escuela Colombiana de Ingeniería
Asignatura: Introducción a la Programación (IPRO)
Profesora: Ing. Patricia Salazar Perdomo
Tarea No. 7 - Estructuras while anidadas
Estudiante: Jojhan Santiago Muñoz Osorio
Fecha: 23 de agosto de 2026

Ejemplo 3.1.37 - Pedir la cantidad de estudiantes de una institución
educativa y, para cada uno, el valor de la matrícula, el número de
integrantes que aportan al presupuesto familiar y con qué monto cada
uno. Calcular la matrícula promedio de los n estudiantes y, para
cada uno de ellos, el porcentaje que representa el valor de la
matrícula en relación con los ingresos de su grupo familiar.
"""


def porc_y_mat_prom():
    # Se supone que los datos ingresados son correctos.
    print("\nCalculo la matrícula promedio de los estudiantes de una institución")
    print("y, para cada uno de ellos, el porcentaje que representa el valor de la")
    print("matrícula en relación con los ingresos del grupo familiar del estudiante.")
    ne = int(input("\n¿Cuántos estudiantes son? "))
    totmat = 0
    cont_e = 0
    while cont_e < ne:
        print("\nValor de la matrícula del estudiante #", cont_e + 1, end=": ")
        valmat = float(input())
        totmat = totmat + valmat
        mfaport = int(input("\nCuántos integrantes de su familia aportan a la casa: "))
        cont_aport = 0
        totalaport = 0
        print("Ingreso mensual del familiar:")
        while cont_aport < mfaport:
            print("#", cont_aport + 1, end=" ")
            ingmes = float(input())
            totalaport = totalaport + ingmes
            cont_aport = cont_aport + 1
        print("\n\tEstudiante No.", cont_e + 1)
        print("\tMatrícula: $", valmat)
        print("\t% que representa (de $", totalaport, "):",
              round((valmat / totalaport) * 100, 1))
        cont_e = cont_e + 1
    print("\nEl valor promedio de la matrícula pagada por los", ne, "estudiantes de")
    print("la institución educativa es $", totmat / ne, end=".")
    print("\n\nFin.\n\n")


porc_y_mat_prom()
