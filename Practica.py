#def monto_descuento():
    #print("Bienvenido estimado usuario en este programa podra conocer como le queda el valor del producto y si tiene descuento.")
    #producto1 = float(input("Ingresa el valor del producto: "))
    
    #if producto1 < 0:
       # print("Monto no valido")
    #else:
        #if producto1 >= 0 and producto1 <= 10000:
           # print(f"El producto no tiene descuento. Total a pagar: ${producto1:.2f}")
        #else:
            #if producto1 > 10000 and producto1 <= 20000:
                #total = producto1 * 0.90  # Aplica el 10% de descuento
                #print(f"Tiene 10% de descuento. Total a pagar: ${total:.2f}")
            #else:
                #if producto1 > 20000 and producto1 <= 50000:
                    #total = producto1 * 0.80  # Aplica el 20% de descuento
                   # print(f"Tiene 20% de descuento. Total a pagar: ${total:.2f}")
               # else:
                    #if producto1 > 50000:
                       # total = producto1 * 0.70  # Aplica el 30% de descuento
                        #print(f"Tiene 30% de descuento. Total a pagar: ${total:.2f}")

#print("Gracias por usar el programa")
#monto_descuento()  
#def puntaje_crediticio():
    #print("Bienvenido estimado usuario acá podra ver si una persona es apta para un credito")
    #puntaje= int(input("Ingrese el puntaje crediticio") )
    #if puntaje < 0 or puntaje > 900:
        #print("Puntaje fuera de rango")
    #else:
        #if puntaje >= 0 and puntaje <= 500:
            #print("Riego alto crédito rechazado ")
       # else:
            #if puntaje > 500 and puntaje <= 700:
               # print("Riesgo Medio - Requiere Codeudor ")
            #else:
                #if puntaje > 700 and puntaje <= 900:
                    #print("Riesgo Bajo - Crédito Aprobado ")


#print("Gracias por usar el programa")
#puntaje_crediticio()


#def edad():
    #print("Bienvenido a este clasificador de edad")
    #edad=int(input("Ingresa tu edad"))
    #if edad < 0 or edad > 110:
        #print("Edad inválida")
    #else:
        #if edad >= 0 and edad <= 12:
            #print("Usted es un niño")
        #else:
            #if edad > 12 and edad <= 17:
                #print("Usted es un adolescente")
            #else: 
                #if edad > 17 and edad <= 64:
                    #print("Usted ya es un adulto")
                #else:
                        #print ("Usted es un adulto mayor")
#edad()
#print("Gracias por usar el programa")


#def calcular_parqueadero():
  #print("Bienvenido estimado usuario acá podra ver el valor del parqueadero en base a los minutos de su estadia")
  #minutos=int(input("Ingrese los minutos que se demoro su estadia"))
 # if minutos <= 0:
   # print("Tiempo no válido")
  #else:
  #  if minutos > 0 and minutos <= 15:
     # print("El parqueadero es gratis")
    #else:
      #if minutos > 15 and minutos <= 60:
     #   print("La tarifa es de 3000")
    #  else:
   #     if minutos > 60 and minutos <= 120:
    #      print("La tarifa es de 6000")
  #      else:
 #           print("La tarifa es de 10000")
#print ("Gracias por usar el programa")
#calcular_parqueadero()


#def evaluar_beca():
 #   print("Bienvenido estimado usuario aquí evaluaremos si es merecedor de una beca")
  #  promedio=float(input("Ingrese su promedio acumulado"))
   # estrato=int(input("Ingresa tu estrato socieconomico"))
    #if (promedio < 0.0 or promedio > 5.0) or (estrato < 1 or estrato > 6):
     #   print("Datos de entrada no válidos")
    #else:
       #     if promedio >= 4.5 and (estrato==1 or estrato==2):
        #     print("Beca del 100% aprobada")
         #   else:
          #   if promedio >= 4 and (estrato ==1 or estrato ==2 or estrato ==3):
           #     print("Beca del 50% aprobada")  
            # else:
                #if promedio >=3.5 and promedio <=4:
                 #   print("Beca del 25% aprobada")
                #else:
                   # print("No aplica para la beca")
#evaluar_beca()


def clasificar_triangulo():
    print("Bienvenido usuario aquí lo ayudaramos a definir un triangulo según sus lados")
    ladoA=float(input("Ingresa la medida del lado A"))
    ladoB=float(input("Ingresa la medida del lado B"))
    ladoC=float(input("Ingresa la medida del lado C"))
    if ladoA == ladoB and ladoB == ladoC:
        print("El triángulo es equilatero")
    else:
        if (ladoA == ladoB) and (ladoC == ladoB) and (ladoA==ladoC)(ladoA < ladoC) or (ladoC > ladoA) :