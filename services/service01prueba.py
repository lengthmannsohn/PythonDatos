from models import mascota
#ESTE SERVICIO SERA EL QUE TENDRA METODOS 
#PARA SER UTILIZADOS EN EL MAIN
def getSaludo():
    return "Bienvenido a Matrix"

def getMascota1():
    dato = mascota.Mascota()
    dato.nombre = "Flounder"
    dato.raza = "Pez"
    dato.edad = 22
    return dato

def getMascota2():
    dato = mascota.Mascota()
    dato.nombre = "Nala"
    dato.raza = "Leona"
    dato.edad = 17
    return dato