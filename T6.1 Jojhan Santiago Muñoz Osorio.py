def donaciones():
    print("Bienvenido al programa")
    can_familias=int(input("Escribe la cantidad de familias que van a donar"))
    cont=0
    cont_no_donar=0
    max_arroz=0
    familia_max=""
    huevos_totales=0
    while cont < can_familias:
        cont +=1
        nombre=str(input("Escriba el nombre de su familia"))
        libras_arroz=int(input("Escribe las cantidad de libras que vas a donar"))
        cantidad_canastas=int(input("Escribe la cantidad de canastas que deseas donar"))
        if libras_arroz>max_arroz:
            max_arroz=libras_arroz
            familia_max=nombre
        if cantidad_canastas>=1:
            huevos_totales+=cantidad_canastas*30
        if libras_arroz==0:
            cont_no_donar+=1
    promedio=huevos_totales/can_familias
    print(f"El promedio de huevos es {promedio}")
    print(f"El nombre de la familia que dono más libras de arroz es:{familia_max} y la cantidad: {max_arroz}")
    print(f"Las familias que no donaron arroz son: {cont_no_donar}")
    print("Gracias por usar el programa")
donaciones()
      