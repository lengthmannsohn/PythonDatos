from services import service03persona as service
from models import persona

print("------Main de Personas----")
person = service.getPersona()
print(f"Nombre: {person.nombre}, {person.edad}, {person.email}")
print("Fin de programa")