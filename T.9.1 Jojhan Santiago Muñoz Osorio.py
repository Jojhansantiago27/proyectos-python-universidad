def peso(kilo, metro):
    print("Bienvenido estimado usuario")
    IMC = kilo / (metro ** 2)  
    return IMC

R = peso(70, 1.75)
print(f"IMC = {R}")
