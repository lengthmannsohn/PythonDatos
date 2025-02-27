from models import persona

def getPersona():
    #CREAMOS UNA NUEVA PERSONA
    persona1 = persona.Persona()
    persona1.nombre = "Diana"
    persona1.edad = 30
    persona1.email = "diana@gmail.com"
    return persona1