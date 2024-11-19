#Ejercicio Capicua
'''''
def esCapicua(palabra):
    palabra1 = palabra
    palabra2 = ""
    for i in range(len(palabra)-1,-1,-1):
        palabra2 += palabra[i]

    return palabra1 == palabra2

print(esCapicua("HOLAALOH"))


#hORAS Y SUELDO
def horasysueldo():
    horas = input("Cuantas horas has hecho?")
    sueldo = input("Cuanto te pagan la hora?")
    paga = float(horas) * float(sueldo)
    print(f"te deben pagar {paga}")

horasysueldo()

#Sumar todos los numeros
def sumarTodoslosNumeros(numero):
    total = 0
    for i in range(numero+1):
            total +º i
    print(total)
sumarTodoslosNumeros(5)


#Repetir nombre
def repertir_nombre():
    nombre = input("Cual es tu nombre? ") 
    repetir = input("Dime un numero? ")
    
    for i in range(int(repetir)+1):
        print(nombre)
repertir_nombre()

#Quitar fijo y extension del movil
def quitarextensionyfijo(numero):
    numero_sin_na = ""
    n = 1
    for i in range(len(numero)):
        if str(numero)[i]== "-":
            n = n + 1
            continue
        if n == 2:
            numero_sin_na += numero[i]
    print(numero_sin_na)          
quitarextensionyfijo("+34-913724710-56")

#Hacer una vocal mayuscula
def mayuscula(frase,vocal):
    resultado = ""
    for letra in frase:
        if str(letra).upper() == str(vocal).upper():
                resultado += str(letra).upper()
                continue
        resultado += letra
    print(resultado)
mayuscula("Hola a todos y todas que tal estan","a")

#Fecha de nacimiento
def fecha_nac(fecha):
    lista = list()
    numero = 0
    resultado = ""
    for car in fecha:
      lista.append(car)
    for n in lista:
       resultado += n
       numero += 1
    print(lista)
fecha_nac("11/22/2293")    

# Contraseña = Contraseña
contrasena = "HolaPepitO"
contrasena2 = input("Introduce Contraseña: ")
if contrasena.lower() == contrasena2.lower():
    print("Contraseña correcta")
else:
    print("Error, Contraseña Incorrecta")
  

#UMERO 0
#manera 1
numero1 = input("Numero 1: ")
numero2 = input("Numero 2: ")
resultado = None
if int(numero2) == 0:
    print("numero erroneo")
elif int(numero2) != 0:
    print(int(numero1) / int(numero2))

#manera 2
try:
    resultado = int(numero1) / int(numero2)
except Exception as ex:
    print("Error en el numero divisble")
print(resultado)  

#bucle contraseña
contraseña = "HOLAPEPE123"
contraseña2 = input("Escribe contraseña:")
while(contraseña != contraseña2):
     contraseña2 = input("Error intentalo de nuevo")
print("Correcto")

#PALABRA AL REVES LETRA POR LETRA
#LA FACIL
Palabra = input("Dime una palabra: ")[::-1]
for letra in Palabra:
    print(letra)
Palabra = Palabra[::-1]
#la rara
for i in range(len(Palabra)-1,-1,-1):
    print(Palabra[i])
#Contar letra en frase
frase = input("Di frase ")
letraU = input("Di letra ")
contador = 0
for letra in frase:
    if letra.lower() == letraU.lower():
        contador+=1
print(f"la letra {letraU} a aparecido {contador} veces")

#Sacar el mayor de la lista y el menor

lista =[75, 46, 22, 80, 65, 8]
lista.sort()
menor = lista[0]
mayor = lista[len(lista)-1]
print(f"El numero menor es {menor} y el mayor es {mayor}")


#Divisa 
divisas = {"Euro":"€", "Dolar":"$", "Yuan": "y"}
divisa = input("que divisa quieres? ")
n = 0
for a,b in divisas.items():
    if a == divisa:
        print(b)
        n = 1
        
if n == 0:        
    print("No se encotnro")

'''  
#   Uso de Split
fraseAseparar = "Hola, buenos, dias, que, tal, estas"
fraseSeparada = fraseAseparar.split(", ") 
print(type(fraseSeparada))
print(fraseSeparada) 
