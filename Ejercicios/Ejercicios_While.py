# #EJERCICIOS CON WHILE
# print("Ejercicios utilizando WHILE")

# print("\nEjercicio 1")
# print("Suma hasta cero\n")
# # Pide al usuario números enteros y súmalos hasta que ingrese un 0. Luego muestra el total.
# total = 0
# while True:
#     numero = int(input("Ingrese un numero a sumar (0 para cerrar el programa): "))
#     if numero == 0:
#         break
#     total += numero
#     print(f"Su total es {total}")
# print("Programa finalizado")

# print("\nEjercicio 2")
# print("Contraseña correcta\n")
##Crea un programa que pida una contraseña usando while hasta que escriba "python123" correctamente.
# clave=input("Escribe la contraseña: ")
# while clave!= "python123":
#     print("Contraseña incorrecta")
#     clave=input("Intenta de nuevo: ")
# print("¡Bienvenido!")

# print("\nEjercicio 3")
# print("Lista de compras\n")
##Pide productos uno por uno y guárdalos en una lista. Termina cuando el usuario escriba "fin", luego muestra toda la lista.
# compras=[]
# while True:
#     prod1=input("Ingrese el producto a guardar en la lista de compras (fin=salir): ").lower()
#     compras.append(prod1)
#     if prod1 == "fin":
#         print(f"El programa ha finalizado{compras}")
#         break

# print("\nEjercicio 4")
# print("Contador de pares e impares\n")
##Pide 10 números al usuario. Usa while para contarlos y guarda cuántos son pares y cuántos impares.
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
##Pide al usuario ingresar notas entre 0 y 5 hasta que escriba "salir". Guarda las notas en una lista y muestra el promedio.
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
##Pide un número y genera su tabla del 1 al 10 con while.
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
## El programa tiene un número secreto (ej. 17). El usuario tiene que adivinarlo. Con cada intento, el programa dice si es mayor o menor.
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
##Crea una tupla con frutas. Usa while para pedirle al usuario que adivine frutas hasta que acierte una que esté en la tupla.
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
##Crea un diccionario con 5 palabras en español y su traducción al inglés. Usa while para que el usuario ingrese una palabra en español y muestre su traducción (si está).
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
##Haz un menú dentro de un while para que el usuario elija: 1. Sumar, 2. Restar, 3. Multiplicar, 4. Dividir, 5. Salir Luego realiza la operación con dos números ingresados.
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
##Pide nombres y edades de personas y guárdalos en un diccionario. Detente cuando el usuario escriba "salir" como nombre. Luego muestra el diccionario completo.
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
##Crea una lista de 5 colores. Usa un bucle while para que el usuario escriba colores hasta encontrar uno que esté en la lista.
# inten=0
# lista=["morado","rosa","anaranjado","azul"]
# print("¡Bienvenido!")
# print("He creado una lista con colores ¿Podrás adivinar algunos de,los colores que escogí?")
# color= input("Ingresa el color que crees que está en mi lista: ")
# while color.lower() not in lista:
#     inten+=1
#     print(f"{color} no está en mi lista, ¡intentemos de nuevo!")
#     color= input("Ingresa el color que crees que está en mi lista: ")
# print(f"¡Perfecto, lograste adivinarlo! Los colores que hay en mi lista son: {lista}")

# print("\nEjercicio 13")
# print("Potencias de un número\n")
##Pide un número y muestra sus potencias desde la 1 hasta la 5 con while.
# print("¡Bienvenido!")
# nu=int(input("Ingresa un número del cual deseas saber la potencia: "))
# expo=1
# while expo<=5:
#     resu=nu**expo
#     print(f"{nu} elevado a {expo} = {resu}")
#     expo+=1
# print("Programa finalizado ¡Adiós!")

# print("\nEjercicio 14")
# print("Lista de cuadrados\n")
# #Pide 5 números con while y guarda en una lista sus cuadrados. Al final, muestra la lista.
# cua = []
# contad = 0
# while contad< 5:
#     num00 = int(input("Por favor ingrese un numero del que desee ver el cuadrado: "))
#     opera= num00 ** 2
#     cua.append(opera) 
#     print(f"El cuadrado de {num00} es {opera}")
#     contad += 1 
# print(f"\nLa lista de cuadrados ingresados es: {cua}")
# print("Programa finalizado")

# print("Ejercicio 15")
# print("Diccionario de estudiantes\n")
# #Crea un programa que te deje registrar estudiantes con su nota final (nombre y nota). Usa un diccionario. El usuario debe poder agregar varios hasta que escriba "fin".
# registro = {}
# while True:
#     estu = input("Ingresa el nombre del estudiante: ").lower()
#     if estu == "fin":
#         print("Programa finalizado")
#         break
#     nota_final = float(input("Ingresa su nota final: "))
#     registro[estu] = nota_final
#     # Pregunta al usuario si desea continuar 
#     seguir= input("¿Desea registrar otro estudiante? (si/no): ").lower()
#     if seguir == "no":
#         print("Registro finalizado")
#         break
# print(f"La lista completa de estudiantes ingresados es: \n{registro}")
# print("Programa finalizado")
