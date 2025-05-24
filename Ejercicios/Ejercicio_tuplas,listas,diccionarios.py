# #TALLER DE REGISTRO SIMPLE DE PRODUCTO Y CALCULO DE COSTOS 

# print("REGISTRO SIMPLE DE PRODUCTO Y CALCULO DE COSTOS")

# produc= input("Ingrese el nombre del producto: ")
# precio= float(input("Ingrese el precio unitario del producto: "))
# c_c=int(input("Ingrese la cantidad comprada del producto: "))

# tupla=(produc,precio)
# lista= [tupla, c_c]

# diccionario={
#     "producto": lista
# }

# costo_total= precio*c_c

# print(tupla)
# print(lista)
# print(diccionario)
# print(f"El costo total es de: ", costo_total)

# #TALLER 2: FACTURA DE MULTIPLES PRODUCTOS (VERSION FIJA SIN BUCLES)

# print("TALLER 2: FACTURA DE MULTIPLES PRODUCTOS ")

# producto_1= input("Ingrese el nombre de el producto: ")
# precio_1= float(input("Ingrese el precio unitario: "))
# cant_1= int(input("Ingrese la cantidad comprada del producto: "))

# producto_2= input("Ingrese el nombre de el segundo producto: ")
# precio_2= float(input("Ingrese el precio unitario: "))
# cant_2= int(input("Ingrese la cantidad comprada del segundo producto: "))

# producto_3= input("Ingrese el nombre de el tercer producto: ")
# precio_3= float(input("Ingrese el precio unitario: "))
# cant_3= int(input("Ingrese la cantidad comprada del tercer producto: "))

# tupla_1= (producto_1,precio_1)
# tupla_2= (producto_2,precio_2)
# tupla_3= (producto_3,precio_3)

# lista_1= [tupla_1,cant_1]
# lista_2= [tupla_2,cant_2]
# lista_3= [tupla_3,cant_3]

# diccionario_1={
#     "producto 1": lista_1,
#     "producto 2": lista_2,
#     "producto 3": lista_3
# }

# total_1= precio_1*cant_1
# total_2= precio_2*cant_2
# total_3= precio_3* cant_3

# total_general= total_1+total_2+total_3

# print(f"El total general es: ", total_general)
# print(diccionario_1)

#TALLER 3: REGISTRO DE NOTAS DE UN ESTUDIANTE

print("REGISTRO DE NOTAS DE UN ESTUDIANTE")

user= input("Ingrese el nombre del estudiante: ")
materia= input("Ingrese una asignatura: ")

nota= float(input("Ingrese la primera nota de : "))
nota1= float(input("Ingrese la segunda nota de: "))
prome= (nota+nota1)//2

materia2=input("Ingrese una segunda asignatura: ")
nota_1=float(input("Ingrese la primera nota: "))
nota_2=float(input("Ingrese la segunda nota: "))
prome2=(nota_1+nota_2)//2

materia3=input("Ingrese una tercera asignatura: ")
not1=float(input("Ingrese la primera nota: "))
not2=float(input("Ingrese la segunda nota: "))
prome3=(not1+not2)//2

tupla=(materia, prome)
tupla2=(materia2,prome2)
tupla3=(materia3,prome3)

list_1=[tupla,nota,nota1]
list_2=[tupla2,nota_1,nota_2]
list_3=[tupla3,not1,not2]

lista= [list_1,list_2,list_3]

boletín={
    "nombre": user,
    "materias": lista
}
print(boletín)
Prome_final= (prome+prome2+prome3)//3
print(f"El estudiante", user, "obtuvo un promedio final de todas las asignaturas de ", Prome_final)