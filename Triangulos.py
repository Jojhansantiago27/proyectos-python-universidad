def triangulos():
    print("Bienvenido estimado usuario")
    cantidad=int(input("Introduce la cantidad de triangulos: "))
    mayor_area=0
    mayor_perimetro=0
    cont=0
    while cont < cantidad:
        print(f"\n Triangulo{cont+1}")
        lado1=float(input("Introduce la medida del lado 1: "))
        lado2=float(input("Introduce la medida del lado 2: "))
        lado3=float(input("Intoduce la medidad del lado 3: "))
        if lado1==lado2 and lado2==lado3:
            area=(lado1**2*(3**0.5))/4
            if area>mayor_area:
             mayor_area=area
        else:
           perimetro=lado1+lado2+lado3
           if perimetro>mayor_perimetro:
              mayor_perimetro=perimetro
        cont=cont+1
    print(f"mayor área de triángulos equilateros:{mayor_area}")
    print(f"mayor perimetro de triángulos no equilateros:{mayor_perimetro}")
triangulos()

        
