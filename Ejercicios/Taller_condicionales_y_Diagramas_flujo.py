#Taller de condicionales y diagramas

#Verificar si un numero es positivo, negativo o cero
num= float(input("Ingrese un numero positivo, negetivo o cero: "))

if num >0:
    print("Su numero es positivo")
elif num <0:
    print("Su numero es negativo")
else:
    print("Su numero es cero")

#Calcular el mayor de dos numeros ingresados 

num3= int(input("Ingresa un numero: "))
num4= int(input("Ingresa un segundo numero: "))

if num3 > num4:
    print(f"El numero {num3} es mayor que {num4}")
else:
    print(f"El numero {num4} es mayor que {num3}")

#Determinar si un numero es par o impar

numero= int(input("Ingrse un numero: "))

if numero %2==0:
    print("El numero es par")
else:
    print("El numero es impar")



