Est={
    "nombre":"Sofia",
    "Edad":"23",
    "Carrera":"Cirujana",
    "promedio":"4,6"
}

print(Est)

nombre= input("Ingrese el nombre de su mascota: ")
raza= input("Ingrese la raza de su mascota: ")
edad= input ("Ingrese la edad de su mascota: ")
dueño= input ("Ingrese el nombre del dueño: ")
ciudad= input("Ingrese la ciudad donde reside la mascota: ")

mascota={
    "Nombre": nombre,
    "Raza": raza,
    "Edad" : edad,
    "Dueño": dueño,
    "Ciudad": ciudad
    
}

print(f"La informacion de su mascota es: ", mascota)

dictionary={"a":1,
            "e":2
            }
print()
print(dictionary)
print(f"clave a: {dictionary['a']}")
print(f"clave b: {dictionary['e']}")

dictionary= {"numbers": [18,20,28],
            "groups": {"a":1,"b":2}
            }

print(dictionary)
print(f"clave numbers: {dictionary['numbers']}")
print(f"clave groups: {dictionary['groups']}")

print(f"clave numbers: {dictionary['numbers'][1]}")
print(f"clave groups: {dictionary['groups'],['b']}")

print(dictionary,["z"])
