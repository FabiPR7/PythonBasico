#~Formato
nombre, apellido, edad = "fabian", "padilla", 17
print("mi nombre es {} {} y tengo {} años".format(nombre,apellido,edad))
print("mi nombre es %s %s y tengo %s años" %(nombre, apellido, edad))
print(f"mi nombre es {nombre} {apellido} y tengo {edad} años")

#Desempaquetado de caracteres
palabra = "Carolina Stan"
b,c,d,e,f,g,h,i,j,k,l,m,n = palabra;
print(b +f+n)

#division de caracteres
palabra2 = palabra[1:4]
print(palabra2)
palabra2 = palabra[0:8:2]
print(palabra2)
palabra2 = palabra[::-1]
print(palabra2)

#Funciones
palabra3 = "Hola Buenos dias"
print(palabra3.upper())
print(palabra3.count("o"))
print(palabra3.islower())
