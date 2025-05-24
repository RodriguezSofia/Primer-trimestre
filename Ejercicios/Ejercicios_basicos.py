#TALLER EJERCICIOS BASICOS

#Punto 1
Num1=int(input("Ingrese un numero a sumar: "))
Num2=int(input("Ingrese un segundo numero a sumar: "))
Sum=Num1+Num2
print(f"El resultado de la suma de", Num1, "y", Num2,"es: ", Sum)

#Punto 2
Num3=int(input("Ingrese un numero a restar: "))
Num4=int(input("Ingrese un segundo numero a restar: "))
Rest=Num3-Num4
print(f"El resultado de la resta de", Num3, "y", Num4,"es: ", Rest)

#Punto 3
Num5=int(input("Ingrese un primer numero a multiplicar: "))
Num6=int(input("Ingrese un segundo numero a multiplicar: "))
Mult=Num5*Num6
print(f"El resultado de la multiplicacion de", Num5, "y", Num6,"es: ", Mult)

#Punto 4
Num=int(input("Ingrese un primer numero a dividir: "))
Num7=int(input("Ingrese un segundo numero a dividir: "))
Div=Num//Num7
print(f"El resultado de la division de", Num, "y", Num7,"es: ", Div)

#Punto 5
Nombre= input("Ingrese su nombre: ")
Apellido= input("Ingrese su Apellido: ")
print(f"Cordial saludo,", Nombre, Apellido)

#Punto 6
Name=input("Ingrese su nombre: ")
ext=Name [0:1]
print(ext)

#Punto 7
Name2=input("Ingrese su nombre: ")
ext2=Name2[-1]
print(ext2)

#Punto 8
Bas=int(input("Ingrese la base del rectángulo: "))
Alt=int(input("Ingrese la altura del rectángulo"))
Area=Bas*Alt
print(f"El área del rectángulo es de ", Area)

#Punto 9
Nac=int(input("Ingrese el año de su nacimiento: "))
Age=2025-Nac
print(f"Su edad actual es: ", Age)

#Punto 10
user= input("Ingrese su usuario: ")
dom= input("Ingrese su dominio: ")
print(f"Su direccion de correo es", user,"@",dom)

#Punto 11
Name3= input("Ingrese su nombre: ")
print(len(Name3))

#Pumto 12
Word= input("Ingrese una palabra: ")
Word +=input("Ingrese una segunda palabra: ")
print(Word)

#Punto 13
Word1= input("Ingrese una palabra: ")
ext1= Word1 [1:2]
print(ext1)

#Punto 14
Word3= input("Ingrese una palabra: ")
ext2= Word3 [0:3]
print(ext2)

#Punto 15
Palabra=input("Ingrese una palabra: ")
extr= Palabra[::-1]
print(extr)

#Punto 16
Numx=int(input("Ingrese un número: "))
Numy=int(input("Ingrese un segundo número: "))
Suma=Numx+Numy
print(f"El resultado de la suma entre", Numx, "y", Numy,"es de: ", Suma)
resta=Numx-Numy
print(f"El resultado de la resta entre", Numx, "y", Numy,"es de: ", resta)
multi=Numx*Numy
print(f"El resultado de la multiplicacion entre", Numx, "y", Numy,"es de: ", multi)
divi= Numx//Numy
print(f"El resultado de la division entre", Numx, "y", Numy,"es de: ", divi)

#Punto 17
Numero=int(input("Ingrese un numero: "))
doble=Numero**2
print(f"El doble del numero", Numero, "es:", doble)

#Punto 18
Numero100=int(input("Ingrese un numero: "))
div33=Numero100/2
print(f"La mitad del numero", Numero100, "es:", div33)

#Punto 19
Frase=input("Ingrese una frase: ")
print(len(Frase))  #el len se utiliza para saber los caracteres de una palabra o frase

#Punto 20 
Word12= input("Ingrese una palabra: ")
print(Word12+Word12+Word12)

#Punto 21
User= input("Ingrse su nombre: ")
ext=User[0:2]
ext2= User[-2::]
print(ext,ext2)

#Punto 22
Palabra123= input("Ingrese una palabra: ")
print(len(Palabra123)//2)

#Punto23
frase22= input("Ingrese una frase: ")
ext32= frase22[0:10]
print(ext32)

#Punto 24
Numero=int(input("Ingrese un numero: "))
cuadrado=Numero*Numero
print(cuadrado)

#Punto 25
Num1=int(input("Ingrese un numero: "))
Num2=int(input("Ingrese un segundo numero: "))
res=Num1*(Num1>=Num2)+Num2*(Num2>Num1)  
print(res) 

#Punto 26
Age= int(input("Ingrese su edad: "))
day= Age*365
print(f"Usted ha vivido ", day, "dias.")

#Punto 27
Word= input("Por favor ingrese la palabra Gimnasio: ")
print (Word[1])
print (Word[2])
print (Word[3])
print (Word[4])
print (Word[5])
print (Word[6])
print (Word[7])
print (Word[8])


#Punto 28
Word= input("Ingrese una palabra: ")
print(len(Word)>5)

#Punto 29
Num90= int(input("ingrese un numero: "))
multi=Num90*10
print(f"El numero", Num90, "multiplicado por 10 es: ", multi)

#Punto 30
Word_unk= input("Ingrese un palabra: ")
print("La palabra en minusculas es: ", Word_unk.lower()) #Minusculas
print("Su palabra en mayusculas es: ", Word_unk.upper()) #Mayusculas

