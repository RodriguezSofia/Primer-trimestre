#Primer Ejercicio
Frase="El conocimiento es poder"
print(Frase.find("conocimiento"))
print(Frase.find("poder"))

#Segundo ejercicio
Letras="La práctica hace al maestro"
print(Letras.find("práctica"))
print(Letras.find("maestro"))

#Tercer ejercicio
frase=input("Ingrese una frase: ")
frase2=input("Ingrese una palabra a buscar: ")
print(frase.find(frase2))

#Cuarto ejercicio
text="Doña Uzeada de Ribera Maldonado de Bracamonte y Anaya era baja, rechoncha, abigotada. Ya no existia razon para llamar talle al suyo. Sus colores vivos, sanos, podian mas que el albayalde y el soliman del afeite, con que se blanqueaba por simular melancolias. Gastaba dos parches oscuros, adheridos a las sienes y que fingian medicamentos. Tenia los ojitos ratoniles, maliciosos. Sabia dilatarlos duramente o desmayarlos con recato o levantarlos con disimulo. Caminaba contoneando las imposibles caderas y era dificil, al verla, no asociar su estampa achaparrada con la de ciertos palmipedos domesticos. Sortijas celestes y azules le ahorcaban las falanges"
print(text.find("Sabia")) 
print(text.find("Caminaba"))
print(text.find("falanges"))
print(text[459:655])

Texto="Las tres especies de flamencos sudamericanos obtienen su alimento desde el sedimento limoso del fondo de lagunas o espejos lacustre-salinos de salares, El pico del flamenco actúa como una bomba filtrante. El agua y los sedimentos superficiales pasan a través de lamelas en las que quedan depositadas las presas que ingieren. La alimentación consiste principalmente en diferentes especies de algas diatomeas, pequeños moluscos, crustáceos y larvas de algunos insectos..."
print(Texto.find("sedimentos"))
print(Texto.find("ingieren"))
print(Texto[219:324])

#MI PRIMER PROGRAMA
Nombre=input("ingrese su nombre: ")
nota_1=float(input("Ingrese la primera nota: "))
nota_2=float(input("Ingrese la segunda nota: "))
nota_3=float(input("Ingrese la tercera nota: "))
pro1=nota_1*0.2
pro2=nota_2*0.3
pro3=nota_3*0.5
print(pro1+pro2+pro3)