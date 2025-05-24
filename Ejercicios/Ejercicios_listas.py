

lista_1=[1,2,3,4,5]
lista_2=["hola","mundo","Colombia"]

print(lista_1[0])
print(lista_2[0])
print(lista_2[-3])

#APPEND

frutas=["pera","uva","banano"]
frutas.append("manzana")
print(frutas)

num=[1,2,7,5,8]
print(num)
num.append(int(input("Ingrese un numero: ")))
print(num)

utiles=["colores","marcadores","block cuadriculado"]
print(utiles)
utiles.append(input("Ingrese un nuevo utile a la lista: "))
print(utiles)


# #EJERCICIOS

print("Actividad en clase")

print("Ejercicio 1")
productos=[]
productos.append(input("Ingrese un producto: "))
productos.append(input("Ingrese un segundo producto: "))
productos.append(input("Ingrese un tercer producto: "))
print(productos)

print("Ejercicio 2")

precios=[float(input("Ingrese el precio de la leche entera: ")), float(input("Ingrese el precio del queso: ")), float(input("Ingrese el precio del yogurt: "))]
precio_total=precios[0]+precios[1]+precios[2]
print(precio_total) 

print("Ejercicio 3")


#MAYOR Y MENOR
Numeros=[]

Numeros.append (int(input("Ingrese un numero: ")))
Numeros.append (int(input("Ingrese su segundo numero: ")))
Numeros.append (int(input("Ingrese un tercer mumero: ")))
Numeros.append (int(input("Ingrese un cuarto numero: ")))
maximo=max(Numeros)
minimo=min(Numeros)

print("El numero mayor de los ingresados es: ", maximo, "el numero minimo fue: ", minimo)

# #INSERT

lista=[1,2,4]
lista.insert(2,3)
print(lista)

# #REMOVE

lista23=[1,2,4]
lista23.remove(2)
print(lista23)

numeros=[1,2,3,2]
numeros[3]=4
numeros.remove(4)
print(numeros)