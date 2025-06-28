# #EJERCICIOS CON WHILE
# print("Ejercicios utilizando WHILE")

# print("\nEjercicio 1")
# print("Suma hasta cero\n")
# total= 0
# num1= int(input("Ingrese un numero a sumar: "))
# while num1 !=0:
#     num1= int(input("Ingrese un numero a sumar: "))
#     total+= num1
#     print(f"Su total es {total}")
# print(f"Programa finalizado")

# print("\nEjercicio 2")
# print("Contraseña correcta\n")
# clave=input("Escribe la contraseña: ")
# while clave!= "python123":
#     print("Contraseña incorrecta")
#     clave=input("Intenta de nuevo: ")
# print("¡Bienvenido!")

# print("\nEjercicio 3")
# print("Lista de compras\n")
# compras=[]
# while True:
#     prod1=input("Ingrese el producto a guardar en la lista de compras (fin=salir): ").lower()
#     compras.append(prod1)
#     if prod1 == "fin":
#         print(f"El programa ha finalizado{compras}")
#         break

# print("\nEjercicio 4")
# print("Contador de pares e impares\n")
# par= 0
# impar= 0
# contador=0
# while contador <10:
#     num=int(input("Ingrese un numero: "))
#     if num %2 ==0:
#         par+=1
#         print(f"El {num} es par")
#     else:
#         impar+=1
#         print(f"El {num} es impar")
#         contador+=1

# print("\nEjercicio 5")
# print("Promedio de Calificaciones\n")
# notas=[]
# entrada=input("Ingrese su nota (0-5) escribe (salir) para finalizar el programa: ")
# while entrada.lower() != "salir":
#     nota = float(entrada)
#     if 0<=  nota <=5:
#         notas.append(nota)
#     else:
#         print("Nota invalida")
#     entrada = input("Ingrese su nota (0-5) escribe (salir) para finalizar el programa: ")
# if notas:
#     promedio=sum(notas)/len(notas)
#     print(f"El promedio: {promedio:.2f}")
# else:
#     print("La nota es invalida")

# print("\nEjercicio 6")
# print("Tabla de multiplicar\n")
# contar ="si"
# while contar.lower() =="si":
#     num0=int(input("ingresar la tabla de multiplicar : "))
#     contar=1
#     print(f"\n tabla del {num0}\n")
#     while contar <=10:
#         resultado = num0* contar
#         print(f"{num0}*{contar}={resultado}")
#         contar +=1
#     contar=input("\deseas ver otra tabla de multiplicar (si/no): ")

# print("\nEjercicio 7")
# print("Adivina el número\n")
# num_secret=48
# intentos=0
# print("¡Hola! He escogido un número del 1-60, ¿Crees ser capaz de adivinar cuál es?")
# numero=int(input("Ingresa un número del 1-60: "))
# while numero != num_secret:
#     intentos+=1
#     if numero < num_secret:
#         print(f"El número secreto es mayor que {numero}")
#     else:
#         print(f"El número secreto es menor que {numero}")
#     numero=int(input("Ingresa un número del 1-60: "))
# print(f"¡Grandioso! Lograste adivinar el número en {intentos} intentos y el número secreto es: {num_secret}")

# print("\nEjercicio 8")
# print("Tupla de frutas\n")
# inten=0
# tupla=("pera","mango","kiwi","papaya")
# print("¡Bienvenido!")
# print("He creado una lista con frutas ¿Podrás adivinar alguna de las frutas que escogí?")
# fruta= input("Ingresa la fruta que crees que está en mi lista: ")
# while fruta.lower() not in tupla:
#     inten+=1
#     print(f"{fruta} no está en mi lista, ¡intentemos de nuevo!")
#     fruta= input("Ingresa la fruta que crees que está en mi lista: ")
# print(f"¡Perfecto, lograste adivinarlo! Las frutas que hay en mi lista son: {tupla}")

# print("\nEjercicio 9")
# print("Diccionario de traducción\n")
# dic={
#     "hola":"hello",
#     "adios":"goodbye",
#     "por favor":"please",
#     "gracias":"thank you",
#     "humilde":"humble"
# }
# print("Bienvenido al traductor español-ingles")
# word=input("Ingrese la palabra en español que desea traducir: ").lower()
# while word not in dic:
#     print("Lo sentimos, no tenemos la traduccion de esta palabra. Intenta de nuevo")
#     word=input("Ingrese la palabra en español que desea traducir: ")
# print(f"La palabra {word} en ingles es {dic[word]}")

# print("\nEjercicio 10")
# print("Calculadora básica\n")
# print("¡Bienvenido!")
# print("¿Qué operación deseas realizar?")
# print("\n-----------------------------------------------")
# print("Suma = 1")
# print("Resta = 2")
# print("Multiplicación = 3")
# print("División = 4")
# print("Salir = 5")
# print("-----------------------------------------------\n")
# sum=1
# rest=2
# multi =3
# divi =4
# salir =5
# while True :
#     op= int(input("Ingrese el número de la operación que desea realizar: "))
#     nume1 = float(input("Ingrese el primer número: "))
#     nume2= float(input("Ingrese el segundo número: "))
#     if op == sum:
#         resu= nume1+nume2
#         print(f"El resultado de la suma entre {nume1} y {nume2} es: {resu}")
#     elif op == rest:
#         resu= nume1-nume2
#         print(f"El resultado de la resta {nume1} y {nume2} es: {resu}")
#     elif op == multi:
#         resu= nume1*nume2
#         print(f"El resultado de la multiplicación {nume1} y {nume2} es: {resu}")
#     elif op == divi:
#         resu= nume1/nume2
#         print(f"El resultado de la división {nume1} y {nume2} es: {resu}")
#     else:
#         print("Opción no válida. Por favor, elija una opción del 1 al 5.")
#     volver=input("\n¿Deseas realizar otra operación? (si/no): ")
#     if volver.lower() == "no":
#         print("Saliendo de la calculadora...¡Hasta luego!")
#         break

# print("\nEjercicio 11")
# print("Registro de edades\n")
# perso= {}
# while True:
#     nombre = input("Ingrese el nombre de la persona ('salir' para finalizar): ")
#     if nombre.lower() == "salir":
#         break
#     edad = int(input(f"Ingrese la edad de {nombre}: "))
#     perso[nombre] = edad
# print(f"Personas registradas \n{perso}")

# print("\nEjercicio 12")
# print("Buscar en lista\n")
# inten=0
# lista=["morado","rosa","anaranjado","azul"]
# print("¡Bienvenido!")
# print("He creado una lista con colores ¿Podrás adivinar algunos de,los colores que escogí?")
# color= input("Ingresa el color que crees que está en mi lista: ")
# while color.lower() not in lista:
#     inten+=1
#     print(f"{color} no está en mi lista, ¡intentemos de nuevo!")
#     color= input("Ingresa la fruta que crees que está en mi lista: ")
# print(f"¡Perfecto, lograste adivinarlo! Los colores que hay en mi lista son: {lista}")

# print("\nEjercicio 13")
# print("Potencias de un número\n")
# print("¡Bienvenido!")
# nu=int(input("Ingresa un número del cual deseas saber la potencia: "))
# expo=1
# while expo<=5:
#     resu=nu**expo
#     print(f"{nu} elevado a {expo} = {resu}")
#     expo+=1
# print("Programa finalizado ¡Adiós!")


