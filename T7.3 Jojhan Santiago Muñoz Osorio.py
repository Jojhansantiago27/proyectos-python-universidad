"""
Universidad Escuela Colombiana de Ingeniería
Asignatura: Introducción a la Programación (IPRO)
Profesora: Ing. Patricia Salazar Perdomo
Tarea No. 7 - Estructuras while anidadas
Estudiante: Jojhan Santiago Muñoz Osorio
Fecha: 23 de agosto de 2026

Ejemplo 3.1.36 - Escribir las tablas de multiplicar de 1 a n, donde
n es un valor entero positivo que dará el usuario.
"""


def tablas_de_multiplicar():
    print("\n\n¡Hola! Escribo las primeras tablas de multiplicar.")
    n = int(input("\nCuántas quiere "))
    tabla = 1
    while tabla <= n:
        print("\nTabla del", tabla)
        mult = 0
        while mult <= 9:
            print(tabla, "X", mult, "=", tabla * mult)
            mult = mult + 1
        input("\nPresione Enter para continuar ")
        tabla = tabla + 1
    print("\nF I N.\n\n")


tablas_de_multiplicar()
