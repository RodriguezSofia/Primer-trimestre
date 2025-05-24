print("Sistema calificativo")

Name=input("ingrese el nombre del estudiante: ")

print("Calificaciones del area de biologia")

bio1=float(input("Ingrese la nota de la celula: "))
bio2=float(input("Ingrese la nota de la reproduccion sexual: "))
bio3=float(input("Ingrese su nota de examen final: "))
suma1=bio1+bio2+bio3
prome1=suma1//3

print(f"El estudiante", Name,"tiene un promedio de ", prome1,"en el area de biologia.")

print("Calificaciones del area de Matematicas")

mate1=float(input("Ingrese la nota del plano cartesiano: "))
mate2=float(input("Ingrese la nota del examen 1: "))
mate3=float(input("Ingrese su nota de angulos : "))
suma2=mate1+mate2+mate3
prome2=suma2//3

print(f"El estudiante", Name,"tiene un promedio de ", prome2,"en el area de matematicas.")

print("Calificaciones del area de sociales")

soci1=float(input("Ingrese la nota de los mapas: "))
soci2=float(input("Ingrese la nota del liberalismo: "))
soci3=float(input("Ingrese su nota de su examen final: "))
suma3=soci1+soci2+soci3
prome3=suma3//3

print(f"El estudiante", Name,"tiene un promedio de ", prome3,"en el area de sociales.")

print("Calificaciones del area de Ingles")

Ingle1=float(input("Ingrese la nota de la pronouns: "))
Ingle2=float(input("Ingrese la nota de los modales: "))
Ingle3=float(input("Ingrese su nota del examen final: "))
suma4=Ingle1+Ingle2+Ingle3
prome4=suma4//3

print(f"El estudiante", Name,"tiene un promedio de ", prome4,"en el area de Ingles.")

print("Calificaciones del area de Lengua Castellana")

cast1=float(input("Ingrese la nota de pronombres: "))
cast2=float(input("Ingrese la nota de los verbos: "))
cast3=float(input("Ingrese su nota del examen final: "))
suma5=cast1+cast2+cast3
prome5=suma5//3

print(f"El estudiante", Name,"tiene un promedio de ", prome5,"en el area de Lengua castellana.")

suma_final=prome1+prome2+prome3+prome4+prome5
promedio=suma_final//5

print(f"El promedio final de ", Name, "es de  ", promedio)