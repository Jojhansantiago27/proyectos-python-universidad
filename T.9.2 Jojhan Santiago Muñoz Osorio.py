def par_impar(n):
    valor = n
    while valor > 1:
        valor = valor - 2
    if valor == 0:
        return f"El número {n} es par"
    else:
        return f"El número {n} es impar"
resultado1 = par_impar(25)
resultado2 = par_impar(14)

print(resultado1)
print(resultado2)
