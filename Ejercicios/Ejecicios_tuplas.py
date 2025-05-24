#EJERCICIO 1: Crear una tupla del 1 al 5.

print("EJERCICIO 1")
tupla_1=(1,2,3,4,5)
print(tupla_1)

#Mostrar el segundo valor.
print("El segundo valor es:", tupla_1[2])

#Imprime cuantos elementos tiene la tupla
print("Numeros de elementos: ", len(tupla_1))

#Usar index para el 4
print(tupla_1.index(4))

#Usar count para el 2
print(tupla_1.count(2))

#Tupla con cadena de texto, numero entero y decimal.
tupla_2=("Hola mundo", 23, 3.56)
print(tupla_2)

#Tupla que contiene otra tupla en su interior
tupla_4=((111,222),333)
print(tupla_4[0][0])

#TALLER_2

#EJERCICIO 1

num=(1,2,3,4,5)
primer=num[0]
ultimo=num[-1]
print("El primer elemento es: ", primer, "el ultimo elemento es: ", ultimo)

#EJERCICIO 2

deci=(3.4,2.5,6.7,6.2,4.4)
segun=deci[1]
cuarto=deci[4]
print("El segundo decimal es: ", segun," el cuarto decimal es: ", cuarto )

#EJERCICIO 3

tup=("ana","boca","corazon")
var1,var2,var3 = tup
print(f"Variable: {var1}, {var2},{var3}")

#EJERCICIO 4

listA=[1,2,3,4,5]
suma= listA[0]+listA[1]+listA[2]+listA[3]+listA[4]
total= suma 
print("El total de la suma es: ", total)

#EJERCICIO 5

flotantes=(2.1,2.9,8.7)
suma2=flotantes[0]+flotantes[1]+flotantes[2]
promedio=suma2//3
print(f"El promedio de los numeros flotantes es: ", promedio)

#EJERCICIO 6

lista=[54, 455,8484,3664]
var10,var22,var33,var44 = lista
print(f"Variable: {var10}, {var22},{var33},{var44}")

#EJERCICIO 7 

tup2=(1,2)
multi=tup2[0]*tup2[1]
print("El resultado de multiplicar los valores de la tupla", tup2, " es de ", multi )

#Ejercicio 8

lista3=[10,100,1000]
lista3.append(10000)
print(lista3)
extra=lista3[0]
extra2=lista3[-1]
print(extra,extra2)

#EJERCICIO 9

tupla22=(2,22,222,2222)
suma4=tupla22[0]+tupla22[1]
print(suma4)

#EJERCICIO 10

listae44=[8,7,6,5,4]
resta=listae44[1]-listae44[3]
print(resta)

#EJERCICIO 11

tup77=(3,5,6,8,4)
mult= tup77[0]*tup77[-1]
print(mult)

#EJERCICIO 12

list0=[11,2,3]
divi=list0[0]//list0[2]
print(divi)

#EJERCICIO 13

tup33=(5,6,7,8)
extra=tup33[2]
print(extra)

#EJERCICIO 14

list00=[1.6,5.3,7.5,8.6,4.6]
sumas=sum(list00)
print(sumas)

#EJERCICIO 15

list234=[1,2,3,4]
tupla =tuple(list234)
print(tupla)

#EJERCICIO 16

la =("hola","mundo","adios")
lista=list(la)
print(lista)
lista.append(34)
print(lista)

#EJERCICIO 17
lista=[2,4,5,6,7] 
tuplaas =tuple(lista) 
extra=tuplaas [2]
print(extra) 

# EJERCICIO 18
tupla=(1,2,3) 
lista =list(tupla) 
print(lista) 
lista[1]=int(input("ingrese un numero")) 
print(lista) 

# EJERCICIO 19 
lista56=[1,2,3,4]  
tuplas =tuple(lista56) 
print(tuplas) 
print(len(tuplas)) 

#EJECICIO 20 
tupla_33=(1,2,3,4,4)
lista_22 =list(tupla_33)
lista_22.remove(4)
print(lista_22)

