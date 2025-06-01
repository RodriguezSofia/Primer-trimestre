# #Flujo: Forma de entender las sucesiones de las intrucciones de un programa

# #CONDICIONALES:Para elegir entre distintas posibilidades
# #IF
# #Determinar si una persona es mayor de edad con interaccion de usuario
# edad= int(input("Por favor ingrese su edad: "))
# if edad>=18:
#     print ("Es mayor de edad")
# if True:
#     ("Se cumple la función")

# #== igual
# #AND OR Y NOT
# a= 195
# b= 30
# c= 400
# if a >b and c>a:
#     print("Ambas condiciones son verdaderas")

# #ELSE
# numero= int(input("Ingrese un numero: "))
# if numero> 36:
#     print("El numero es grande")
# else:
#     print("El numero es chico")

# #Ejemplos de multiples IF

# x= int(input("Ingrese un numero: "))
# if x>10:
#     print("Por encima de diez")
#     if x> 20:
#         print("Y tambien por encima de 20!")
#     else:
#         print("pero no por encima de 20")

#Elif: si no, si

# c= int(input("Ingrese el primer numero a multiplicar: "))*int(input("Ingrese el segundo numero a multiplicar: "))

# if c > 5:
#     print("El resultado es mayor a cinco")
# elif c > 10:
#     print("El resultado es mayor a diez")
# elif c > 20:
#     print("El resultado es mayor a veinte")
# elif c > 50:
#     print("El resultado es mayor a cincuenta")
# elif c > 100:
#     print("El resultado es mayor a cien")
# else:
#     print("No se cumple la condicion")

# print("Clasificador de generacion")
# generacion= int(input("Ingrese el año de su nacimiento: "))

# if generacion >=1920 and generacion<= 1945:
#     print("Usted pertenece a la generacion silenciosa")
# elif generacion >=1946 and generacion<= 1964:
#     print("Usted pertenece a la generacion Baby Boomer")
# elif generacion >=1965 and generacion <= 1979:
#     print("Usted pertenece a la generacion X")
# elif generacion >=1980 and generacion<= 2000:
#     print("Usted pertenece a la generacion Y")
# elif generacion >= 2001:
#     print("Usted pertenece a la generacion Z")
# else:
#     print("La fecha de nacimiento no entra dentro de la clasificacion")

# #LITERATIVAS:Para repetir un bloque de instrucciones
