
n1 = 5
n2 = 3
# WHILE

while n1 > n2:
    print(f"{n1} es mayor que {n2}")
    n2 += 1
print("Ya salimos")    

#For

#Hay varios tipos de uso

#Rango
for i in range (5):
    print(i)

#Recorrer palabra
for letra in "Fabian":
    print(letra)    

lista = ["Hola", "Adios", "Que tal"]

#Recorrer listas
for palabra in lista:
    print(palabra)

# Recorrer diccionarios

dicc = {"Nombre":"Fabi", "Apellido":"Padilla"}

for n, a in dicc.items():
    print(f"{n}:{a}")


#En for y while hay dos funciones utiles que son break y continue

#Break corta el bucle por completo

nombres = ["juan", "pepe", "pedro","pablo","Jose"]
for nombre in nombres:
    print(nombre)
    if nombre == "pepe":
        break
print("Ya salio")    


#Continue solo corta desde donde esta el continue vuelve al principion
# del bucle lo que este debajo de este no se hara

#Solo deberia mostrar los pares
for i in range(10):
    if i % 2 != 0:
        
        continue
    print(i)   
