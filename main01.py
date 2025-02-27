from services import service02prueba as service
from models import mascota

saludo = service.getSaludo()
print("Todo OK, " + saludo)
pez = service.getMascota1()
leona = service.getMascota2()
print(pez.nombre)
print(leona.nombre)
