# #Sistema para Credito bancario
#print("Sistema para Credito bancario")
# name=input("Ingrese su nombre completo: ")
# edad=int(input("Ingrese su edad: "))
# credit= float(input("Ingrese el monto deseado para pedir el credito: "))

# if edad >= 18 and credit>= 2000000:
#     print(f"{name} cumple con los requirimientos, puede solicitar el credito")
# else:
#     print(f"{name} no cumple los requerimientos para solicitar el credito")


# #Sistema de precios de boletas
#print("Sistema de precios de boletas")
# edad=int(input("Ingrese su edad: "))

# if edad ==0 and edad <4:
#     print("La entreda es gratis ")
# elif edad ==4 and edad <= 18:
#     print("Su entrada cuesta 5 EUROS")
# else: 
#     print("Usted es mayor de edad, su entrada cuesta 18 EUROS")


#Sistema de operaciones

print("Sistema de operaciones")
print("""""""MENU""""""""""""""""
        Suma= s
        Resta= r
        Multiplicacion= m
        Division= d """)

letra= input("Ingrese la letra de la operacion que quiere realizar: ").lower()

if letra== "s":
    num1= float(input("Ingrese un primer número: "))
    num2= float(input("Ingrese un segundo número: "))
    sum= num1+num2
    print(f"\nEl resultado de la suma es {sum}")
elif letra == "r":    
    num1= float(input("Ingrese un primer numero: "))
    num2=float(input("Ingrese un segundo número: "))
    rest= num1-num2
    print(f"\nSu resultado de la resta es {rest}")
    
elif letra== "m":
    num1= float(input("Ingrese el primer número: "))
    num2=float(input("Ingrese el segundo numero: "))
    multi= num1*num2
    print(f"\nSu resultado de la multiplicacion o el producto es {multi}")
    
elif letra== "d":
    num1=float(input("Ingrese su primer numero: "))
    num2=float(input("Ingrese su segundo numero: "))
    divi=num1//num2
    print(f"\nSu resultado de la division es {divi:.2f}")
    
else:
    print("No se admite esta letra")