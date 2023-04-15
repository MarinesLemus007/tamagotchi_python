class Tamagotchi():
    def __init__(self,nombre):
        self.nombre = nombre
        self.hambre = 100
        self.energia = 100
        self.estado = 'huevo'
    
    def seriallize(self):
        return {
            "nombre": self.nombre,
            "hambre": self.hambre,
            "energia": self.energia,
            "estado": self.estado
        } 
    

tama = Tamagotchi("patito jose")
#print(tama)
#print(tama.nombre)
print(tama.seriallize())