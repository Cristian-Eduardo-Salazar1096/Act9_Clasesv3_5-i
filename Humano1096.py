print ("Act 9 clase humano")
print ("Cristian Eduardo Salazar Rosas: 22308051281096")

class Humano1096:
    # Zona de Atributos dentro de la clase
    edad=17
    DiaNac=12
    estatura=1.8
    genero="Hombre"
    color_pelo="Cafe"
    color_fav="Gris"


    # Zona de Funciones dentro de la clase
    def correr1096(self, n):
        print(f"{n} esta corriendo ufff....")
    def caminar1096(self, n):
        print(f"{n} esta caminando")
    def gritar1096(self, n):
        print(f"{n} esta gritando AAAAAAAAAAAA.....")
    def saltar1096(self, n):
        print(f"{n} esta saltando ufff....  ufff....")
    def comer1096(self, n):
        print(f"{n} esta comiendo yam....")

    # Zona de creacion de objetos
Cristian=Humano1096()
Doge=Humano1096()
    # Zona de usando objetos
print("---------------------------")
print("Resultado para Cristian")
print(f"Edad: {Cristian.edad}")
print(f"DiaNac: {Cristian.DiaNac}")
print(f"Estatura: {Cristian.estatura}")
print(f"Genero: {Cristian.genero}")
print(f"ColorPelo: {Cristian.color_fav}")
print(f"ColorFav: {Cristian.color_pelo}")
print("---------------------------")
Cristian.gritar1096("Cristian")
Cristian.caminar1096("Cristian")
Cristian.correr1096("Cristian")
Cristian.saltar1096("Cristian")
Cristian.comer1096("Cristian")

Doge.edad=18
Doge.DiaNac=26
Doge.estatura=.80
Doge.genero="Mujer"
Doge.color_fav="Amarillo"
Doge.color_pelo="Dorado"
print("---------------------------")
print("Resultado para Doge")
print(f"Edad: {Doge.edad}")
print(f"DiaNac: {Doge.DiaNac}")
print(f"Estatura: {Doge.estatura}")
print(f"Genero: {Doge.genero}")
print(f"ColorPelo: {Doge.color_fav}")
print(f"ColorFav: {Doge.color_pelo}")
print("---------------------------")
Doge.gritar1096("Doge")
Doge.caminar1096("Doge")
Doge.correr1096("Doge")
Doge.saltar1096("Doge")
Doge.comer1096("Doge")
print("---------------------------")