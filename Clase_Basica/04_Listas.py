
#Listas
# 
# Crea una lista con valores cambiables y accesibles de manera ordenada 
 
#Crear lista
lista = list()
lista2 = []
removidos = []

#Agregar a lista
lista.append("Hola")
lista.append("Adios")
lista.append("Bye")
lista.append("Hello")

lista.insert(3,"Holanda") #Asi se agrega en el puesto que le indiques


#Copiar una lista a otra
lista2 = lista.copy()
print(lista)
print(lista2)

#Contenido
print(lista.__contains__("Bye")) #Devuelve true o false segun tenga o no lo que se le indique

#Reversa
lista2.reverse()
print(lista2)

#Borrar algo de la lista
lista.remove("Bye") #Borra el primero dato que encuentre y coincida 
lista.pop() #Borra el ultimo dato 
del lista2[2] #Borra el dato de la posicion que le digamos


print(lista)
print(lista2)
print(removidos)