#Diccionarios

#Mapas con clave valor

#Definicon

mi_dic = dict()
mi_dic2 = {"Clave":"Valor", "Ejemplo":"Asi"}
mi_dic3 = dict.fromkeys(("Clave1", "Clave2", "Clave3"))# Crea diccionario con claves pero valor vacio

#Agregar valores
mi_dic["Nueva_Clave"] = "Valor"

#Cambiar valor
mi_dic["Clave"] = "Nuevo_Valor"

#Eliminar clave
del mi_dic["Clave"]
del mi_dic #Eliminar el diccionario

#Funciones
print(mi_dic2.keys())#Imprime todas las llaves
print(mi_dic2.values())#Imprime todas los valores
print(mi_dic2.items())#Imprime todo

print(mi_dic3)
