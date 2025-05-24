print("Lista de clientes")

clientes= ["Maria", "samuel","ANA","MARIAN","juan", "jesus", "tatiana"]

clientes.append("JULIANA")
numero=len(clientes)
mayor=max(clientes)
menor=min(clientes)

print(f"El numero de nombres en la lista es ", numero,", el nombre alfabeticamente mayor es ", mayor,", el nombre alfabeticamente menor es ", menor )
indice=clientes.index("JULIANA")
print(indice)
clientes.remove("Maria")
print(f"El nombre de la mitad es: Maria")
print(clientes)
print(clientes.index("JULIANA"))


