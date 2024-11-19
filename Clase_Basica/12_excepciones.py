#Excepciones
#Controlamos los errores

n1 = 2
n2 = "3"

#Try básico
try:
    print(n1+n2)
except:
    print("Ocurrio algun error con la suma")

#Try con finally
try:
    print(n1+n2)
except:
    print("Ocurrio algun error con la suma")
finally: 
    print("Esto se  ejecutara siempre")     

#Try con else 
try:
    print(n1+n2)
except:
    print("Ocurrio algun error con la suma")
else: 
    print("Esto se  ejecutara si no encuentra nignun error")





#Try con el tipo de error
try:
    n3 = input("Dime un numero1: ") 
    n4 =input("Dime un numero2: ") 
    
    print(int(n3) + int(n4))
except ValueError:
    print("Error en el valor")

#Try con el tipo de error convertido en variable
try:
    n3 = input("Dime un numero1: ") 
    n4 =input("Dime un numero2: ") 
    
    print(int(n3) + int(n4))
except ValueError as mi_errorcito:
    print(mi_errorcito)    


