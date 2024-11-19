class Carolina:
    def __init__(self,altura,peso,edad,colorDePelo):
        self.datos = f"Su altura es {altura} y el peso de Carolina es {peso}"
        self_edad = edad
        self_colorP = colorDePelo
    
    def getEdad(self):
        return self.__edad
    
    def toString(self):
        return f"Carol tiene el color {self.__colorP} en el pelo y tiene {self.__edad} años"

scarol = Carolina(172,70.0,20,"Rubio")  
