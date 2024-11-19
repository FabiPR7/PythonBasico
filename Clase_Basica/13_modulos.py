#modulos

#Son proyectos a los que podemos aceceder para ello creo otro llamado
#mi_modulo y se importa asi:

import mi_modulo 

#Y asi se usa cualquier funcion dentro de este modulo
mi_modulo.mifuncion()


#Tambien podemos seleccionar solo una funcion asi
from mi_modulo import resta_numeros
resta_numeros(5,3)


#Tambien podemos renombrar a las funciones asi
from mi_modulo import resta_numeros as res
res(5,3)
