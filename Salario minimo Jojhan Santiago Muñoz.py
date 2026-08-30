def salario_minimo():
    print("Hola estimado usuario, este programa calcula el salario minimo y el porcentaje de aumento entre dos años.")
    print("Ingrese el salario minimo del 2025 :")
    salario_2025 = float(input())
    print("Ingrese el salario minimo del 2026:")
    salario_2026 = float(input())
    porcentaje_aumento = ((salario_2026 - salario_2025) / salario_2025) * 100

    print("El salario minimo del 2025 es:", salario_2025)
    print("El salario minimo del 2026 es:", salario_2026)
    print("El porcentaje de aumento es:", porcentaje_aumento)
    print("La diferencia entre los dos salarios minimos es:", salario_2026 - salario_2025)
    print("Gracias por usar este programa")
salario_minimo()