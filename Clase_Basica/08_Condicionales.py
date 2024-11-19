#Condicionales


#If aritmético
n = int(input("Di un numero: "))

if n > 4:
    print(str(n) +(" es mayor que 4"))
elif n < 4:
    print(str(n) + " es menor que 4")
else:
    print(str(n) + " es igual a 4")

#If con string
n = input("DI una frase o palabra: ")

if n == "Hola":
    print("Dice Hola")
elif n != "Hola":
    print("No dice hola")
if n.upper == "HOLA":
    print("Esta en mayuscula")

#If con el tipo de la variable
n = input("DI un numero o palabra: ")
if n.isdigit :  
    print("Es int")
elif not n.isdigit == int:
    print() 

