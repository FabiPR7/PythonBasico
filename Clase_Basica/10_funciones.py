#Funciones
#Son metodos o funciones que podemos llamar 

#Le puedo pasar paramnetros.
def sumar(a,b):
    print(a+b)

sumar(4,3)

# O tambien se puede cambiar la funcion
def sumar():
    print("No hay numeros")
sumar()

#Tambien puede retornar cosas
def sumar(a,b):
    return a + b

n = sumar(3,8)
print(n)


#Poner valores por defecto si no llegase a recibir ni uno
def sumar(a= 5,b=5):
    print(a+b)

sumar()
sumar(5,10)


#Recursivo?
lista1 = ["Esta", "es","la","lista","numero 1"]
lista2 = ["Esta", "es","la","lista","numero 2"]
lista3 = [lista1,"Esta es la lista numero 3",lista2]
lista4 = [lista3,"Esta", "es" ,"la" ,"lista" ,"numero" ,"4"]
lista5 = ["Esta", "es","la","lista","numero 5"]
listas = [lista4,lista5]


def recorrerLista(lista):
    numero = 1
    espacio = "-"
    if not type(lista) == list:
        print("No es una lista")
        return -1
    else:
        for element in lista:
            if type(element) == list:
                recorrerLista(element)
            else:
                print(f"{espacio}:{element}")
                espacio += "-"
    print("Fin de esta lista")

recorrerLista(listas)