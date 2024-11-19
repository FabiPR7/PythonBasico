#Set
#Crea una lista de manera desordenada sin poder recibir repetidos
#Tampoco puedees acceder a sus valores con indices ya que no tienen

#Definicion

set_one = set()

set_two = {} # Asi es un diccionario tambien

print(type(set_one))
print(type(set_two))

#Agregar valores

set_two ={"Hola",1,2,4} #asignar valores al definir

set_one.add("Hola" )#agregarle valores

set_two = set_two.union(set_one) # Unir 2 sets en uno

#Eliminar valroes

set_one.remove("Hola") #Borra el elemento indicado

set_two.clear() #Elimina todos los valores


del set_one #Elimina el set

#Contiene el valor
print(set_two.__contains__("HOL"))
print("Hola" in set_two)