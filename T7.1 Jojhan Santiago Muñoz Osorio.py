"""
Universidad Escuela Colombiana de Ingeniería
Asignatura: Introducción a la Programación (IPRO)
Profesora: Ing. Patricia Salazar Perdomo
Tarea No. 7 - Estructuras while anidadas
Estudiante: Jojhan Santiago Muñoz Osorio
Fecha: 23 de agosto de 2026

Ejemplo 3.1.34 - Escribir una secuencia de números como la que se
muestra para un número entero positivo n.
"""


def secuencia():
    print("\n\n¡Hola! Dame un número entero positivo y yo te escribo una secuencia de números.")
    print("Por ejemplo, si tú me das el 3, yo escribo 1  2  2  3  3  3.")
    print("Y si me das 4, yo escribo 1  2  2  3  3  3  4  4  4  4.")
    print("¿Ya viste en qué consiste la secuencia? Bueno, ¡intentémoslo!")
    n = int(input("\nDame un número entero positivo "))
    if n <= 0:
        print("\nVeo que no quieres jugar. Otra vez será...")
    else:
        print("\nS E C U E N C I A")
        grupo = 1
        while grupo <= n:  # Ciclo en el que se escriben n grupos de números.
            num = 1
            while num <= grupo:  # Se escribe grupo veces el valor de la variable grupo.
                print(grupo, end=" ")
                num = num + 1
            grupo = grupo + 1
        print("\n\nF I N.\n\n")


secuencia()
