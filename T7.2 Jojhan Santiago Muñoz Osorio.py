"""
Universidad Escuela Colombiana de Ingeniería
Asignatura: Introducción a la Programación (IPRO)
Profesora: Ing. Patricia Salazar Perdomo
Tarea No. 7 - Estructuras while anidadas
Estudiante: Jojhan Santiago Muñoz Osorio
Fecha: 23 de agosto de 2026

Ejemplo 3.1.35 - Pedir a cada uno de los g grupos de Historia la
cantidad de estudiantes y el peso en kilogramos y la estatura en
metros de cada uno, para cada grupo el peso promedio y el número de
estudiantes que miden más de 1.60 m.
"""


def peso_estatura():
    print("\n\nAveriguo el peso promedio y la cantidad de estudiantes")
    print("que miden más de 1.60 m en los grupos de Historia.")
    cant_grupos = int(input("\nCantidad de grupos "))
    cont_g = 1
    while cont_g <= cant_grupos:
        print("\nGrupo", cont_g)
        ce = int(input("\tCantidad de estudiantes: "))
        est_mayor_160 = 0
        peso_prom = 0
        c_est = 1
        while c_est <= ce:
            print("\tEstudiante", c_est)
            peso = float(input("\t\tPeso en kg: "))
            estatura = float(input("\t\tEstatura en m: "))
            peso_prom = peso_prom + peso
            if estatura > 1.60:
                est_mayor_160 = est_mayor_160 + 1
            c_est = c_est + 1
        print("\n\tHistoria -", cont_g)
        print("\n\tPeso promedio:", peso_prom / ce)
        print("\tNúmero de estudiantes que miden más de 1.60 m:", est_mayor_160)
        input("\n\tPresione Enter para continuar ")
        cont_g = cont_g + 1
    print("\n\nF I N.\n\n")


peso_estatura()
