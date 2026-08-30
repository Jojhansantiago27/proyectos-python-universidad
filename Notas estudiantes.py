def notas():
    print("Bienvenido estimado usuario")
    cant_estudiantes=int(input("Escribe la cantidad de estudiantes"))
    mayor_nota=0
    cont=0
    while cont < cant_estudiantes:
        cont+=1
        nota1=float(input("Escribe tu nota número 1"))
        nota2=float(input("Escribe tu nota número 2"))
        nota3=float(input("Escribe tu nota número 3"))
        nota_definitiva=(nota1*0.30)+(nota2*0.30)+(nota3*0.40)
        if nota_definitiva>mayor_nota:
            mayor_nota=nota_definitiva
    promedio=nota_definitiva/cant_estudiantes
    print(f"La calificación del estudiante número {cont} es de {nota_definitiva}")
    print(f"La calificación promedio es {promedio}")
    print(f"La calificación mayor es {mayor_nota}")
    print("Gracias por usar el programa")
notas()
