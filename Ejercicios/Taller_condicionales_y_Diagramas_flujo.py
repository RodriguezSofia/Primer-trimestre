# #Taller de condicionales y diagramas
# print("EJERCICIOS CON CONDICIONALES Y OPERACIONES MATEMATICAS\n")

# #1. Verificar si un numero es positivo, negativo o cero
# print("Numero positivo, negativo o cero ")
# num= float(input("Ingrese un numero positivo, negetivo o cero: "))

# if num >0:
#     print("Su numero es positivo")
# elif num <0:
#     print("Su numero es negativo")
# else:
#     print("Su numero es cero")

# #2. Calcular el mayor de dos numeros ingresados 
# print("\nMayor de dos numeros")

# num3= int(input("Ingresa un numero: "))
# num4= int(input("Ingresa un segundo numero: "))
# if num3 > num4:
#     print(f"El numero {num3} es mayor que {num4}")
# else:
#     print(f"El numero {num4} es mayor que {num3}")

# #3. Determinar si un numero es par o impar
# print("\nPar o impar")
# numero= int(input("Ingrse un numero: "))
# if numero %2==0:
#     print("El numero es par")
# else:
#     print("El numero es impar")

# #4.Dado un número, verifica si está entre 10 y 20
# print("\nVerificar si está entre 10 y 20")

# num11= (float(input("Ingresa el numero a verificar: ")))
# if num11 >= 10 and num11 <= 20:
#     print("El numero está entre el 10 y el 20")
# else:
#     print("El numero no está entre el 10 y el 20")

# #5. Dados tres números, encuentra el mayor usando condicionales
# print("\nMayor de tres numeros")
# num00=int(input("Ingrese un primer numero a determinar: "))
# num01=int(input("Ingrese un segundo numero a determinar: "))
# num02=int(input("Ingrese un tercer numero a determinar: "))

# if num00> num01 and num00 > num02:
#     print(f"El numero {num00} es mayor que los numeros {num01} y {num02}")
# elif num01 > num00 and num01>num02:
#     print(f"El numero {num01} es mayor que los numeros {num00} y {num02}")
# else:
#     print(f"El numero {num02} es mayor que los numeros {num00} y {num01}")

# #6. Calcula el precio final con un 10% de descuento si el total es mayor a $100
# print("\nCalcular el precio final con descuento de 10%")
# total= float(input("Ingrese el total de compra: $"))
# if total> 100:
#     total1=total*0.1
#     print(f"Precio final: ${total1:.1f}")
# else:
#     print(f"Precio final por su compra: ${total}")

# # #7. Verifica si una persona puede votar (mayor o igual a 18 años).
# # print("\nVerificar si puede votar")

# edad= int(input("Ingrese su edad: "))
# if edad >=18:
#     print("Usted puede votar")
# else:
#     print("Usted no puede votar")

#8. Dado el precio y tipo de cliente (VIP o normal), aplica un descuento del 20% solo a VIP.
# print("\nCliente VIP o NORMAL")

# precio= float(input("Ingrese el precio: $ "))
# cliente= input("Ingrese a que tipo de cliente pertenece (VIP/Normal): ").upper()
# if cliente== "VIP":
#     precio0= precio*0.2
#     print(f"Precio final: ${precio0:.1f}")
# else:
#     print(f"Precio final para cliente normal: ${precio}")

# #9. Determina si un número es múltiplo de 5 y de 3 al mismo tiempo.
# print("\nMultiplo de 5 y 3")

# nume= int(input("Ingrese un número: "))

# if nume% 3 ==0 and nume% 5 == 0:
#     print(f"El número {nume} SI es múltiplo de 3 y 5")
# else:
#     print(f"El número {nume} NO es múltiplo de 3 y 5")

# #10. Dado un número, verifica si es divisible entre dos números dados.
# print("\nNúmero divisible entre dos números")

# number= int(input("Ingrese el número a verificar: "))
# divi1 = int(input("Ingrese primer divisor: "))
# divi02 = int(input("Ingrese segundo divisor: "))

# if number %divi1 ==0 and number% divi02 ==0:
#     print(f"El número registrado {number} SI es divisible entre {divi1} y {divi02}")
# else:
#     print(f"El número registrado {number} NO es divisible entre {divi1} y {divi02}")


# print("EJERCICIOS CON LISTAS (CON CONDICIONALES)")
# #11. Crea una lista con 5 números. Si el tercer número es mayor que 10, muestra “Mayor a 10”, si no, muestra “Menor o igual a 10”.
# print("\nmayor a 10, menor o igual a 10")

# num = int(input(f"Ingrese un número : "))
# nume = int(input(f"Ingrese un segundo número : "))
# numer = int(input(f"Ingrese un tercer número : "))
# numero = int(input(f"Ingrese un cuarto número : "))
# numeroo = int(input(f"Ingrese un quinto número : "))
# numero= [num,nume,numer,numero,numeroo]
# print(numero)

# if numero[2] > 10:
#     print(f"El tercer número ingresado {numero[2]} es mayor a 10")
# else:
#     print(f"El tercer número ingresado {numero[2]} es menor o igual a 10")

# #12. Verifica si el número 7 está en la lista [3, 5, 7, 9]. Si está, muestra “Está en la lista”, si no, muestra “No está en la lista”.
# print("\nNumero 7 en lista")
# list= [3, 5, 7, 9]
# if 7 in list:
#     print("El numero 7 SI está en la lista")
# else:
#     print("El numero 7 NO está en la lista")

# #13. Suma los dos primeros elementos de la lista [4, 6, 2, 8]. Si la suma es mayor que 10, muestra “Suma alta”, de lo contrario, muestra “Suma baja”
#print("\nsuma alta o suma baja")
# list00=[4, 6, 2, 8]
# sume = list00[0] + list00[1]
# if sume > 10:
#     print("Suma alta")
# else:
#     print("Suma baja")

#14. Dada la lista ["Ana", "Luis", "Pedro", "Marta"], muestra el último nombre. Si ese nombre es “Marta”, muestra “Nombre correcto”, si no, “Nombre diferente”
#print("\nNombre correcto")
# name= ["Ana", "Luis", "Pedro", "Marta"]
# ulti_name= name[-1]  
# if ulti_name == "Marta":
#     print("Nombre correcto")
# else:
#     print("Nombre diferente")

# #15. Crea una lista con tres colores. Cambia el segundo color solo si es igual a "azul", y muestra la lista actualizada.
# print("\nLista de colores")
# colors= ["magenta", "azul", "dorado"]
# print(colors)
# if colors[1] == "azul":
#     colors[1] = "amarillo" 
#     print(f"Se ha actualizado la lista {colors}")
# else:
#     print("La lista no se ha actualizado")

# print("EJERCICIOS CON TUPLAS (CON CONDICIONALES)")
# #16. Crea una tupla con los valores (5, 8, 12, 20). Si el primer valor es menor que el último, muestra “Orden ascendente”, si no, “Orden descendente”.
# print("\nOrden ascendente o descendente")
# tupla= (5, 8, 12, 20)
# print(tupla)
# if tupla[0] < tupla[-1]:
#     print("Orden ascendente")
# else:
#     print("Orden descendente")

# #17. Dada la tupla (25, 32, 28), verifica si el segundo valor es mayor a 30. Si lo es, muestra “Edad mayor a 30”, si no, “Edad menor o igual a 30”.
# print("\nEdad mayor, menor o iguala a 30")
# ages= (25, 32, 28)
#print(ages)
# if ages[1] > 30:
#     print("Edad mayor a 30")
# else:
#     print("Edad menor o igual a 30")

#18. Convierte la tupla (1, 2, 3) a lista, cambia el segundo valor a 10 solo si es igual a 2, luego vuelve a convertirla en tupla y muéstrala.
#print("\nCambiar segundo valor a 10")
# tupla1 = (1, 2, 3)
# print("Tupla original", tupla1)
# lista= list(tupla1)
# if lista[1] == 2:
#     lista[1]= 10
# tupla2 = tuple(lista)  
# print("Tupla modificada", tupla2)

# #19. Dada la tupla (4, 9), accede al segundo valor. Si es mayor que 5, muestra “Coordenada alta”, si no, “Coordenada baja”.
# print("\nVerificar si es coordenada alta o baja")
# coorde= (4, 9)
# print(coorde)
# if coorde[1] >5:
#     print("Coordenada alta")
# else:
#     print("Coordenada baja")

# #20. Compara si las tuplas (3, 4) y (3, 5) son iguales. Si lo son, muestra “Tuplas iguales”, si no, “Tuplas diferentes”
# print("\nDeterminar si son tuplas iguales")
# tupla001 = (3, 4)
# tupla002 = (3, 5)
# print(tupla001)
# print(tupla002)
# if tupla001 == tupla002:
#     print("Tuplas iguales")
# else:
#     print("Tuplas diferentes")

# # print("EJERCICIOS CON DICCIONARIOS (CON CONDICIONALES)")
# #21. Crea un diccionario con {"nombre": "Juan", "edad": 17}. Si la edad es mayor o igual a 18, muestra “Adulto”, si no, muestra “Menor de edad”.
# print("\nAdulto o menor de edad ")
# dicc1= {"nombre": "Juan", 
#            "edad": 17}
# print(dicc1)
# if dicc1["edad"] >= 18:
#     print("Adulto")
# else:
#     print("Menor de edad")

# #22. Crea un diccionario {"nombre": "Lucía", "edad": 20}. Si la edad es mayor a 18, cambia el valor de “edad” a 21. Luego muestra el diccionario
# print("\nCambiar valor de edad a 21")
# dic2 = {"nombre": "Lucía", "edad": 20}
# print(f"Diccionario original {dic2}")
# if dic2["edad"]> 18:
#     dic2["edad"] = 21
# print(f"Diccionario actualizado {dic2}")

# #23. Crea un diccionario con {"nombre": "Carlos"}. Si la clave “ciudad” no existe, agrégala con el valor “Bogotá” y muestra el diccionario
# print("\nagregar clave")
# dic3 = {"nombre": "Carlos"}
# print(dic3)
# if "ciudad" not in dic3:
#     dic3["ciudad"] = "Bogotá"
# print(f"Diccionario actualizado {dic3}")

#24. Dado el diccionario {"producto": "pan", "precio": 1200}, verifica si la clave “precio” existe. Si existe, muestra su valor, si no, muestra “No hay precio”.
print("\nMostrar valor de la clave precio")
dicc4= {"producto": "pan", "precio": 1200}
print(dicc4)
if "precio" in dicc4:
    print(f"Precio", dicc4["precio"])
else:
    print("No hay precio")

#25. Crea un diccionario con {"pan": 1200, "leche": 2000}. Si “pan” está en el diccionario, muestra su precio; si no, muestra “Producto no disponible”
print("\nmostrar el precio del pan")
factura= {"pan": 1200, "leche": 2000}
print(factura)
if "pan" in factura:
    print(f"Precio del pan:",factura["pan"])
else:
    print("Producto no disponible")