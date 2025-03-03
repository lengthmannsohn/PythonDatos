from services import service08sqlserverplantilla as service
from models import plantilla

servicio = service.ServiceSqlServerPlantilla()
plantilla = servicio.getPlantilla()

for plan in plantilla:
    print(f" Id: {plan.idPlantilla}, Apellido: {plan.apellido}, Funcion: {plan.funcion}, Salario: {plan.salario}, Hospital {plan.hospital}")

print("Introduzca el salario a incrementar")
salario = int(input())
print("Introduzca el numero de hospital de la plantilla que quiere incrementar su salario:")
hospital = int(input())

registros = servicio.updateSalarioPlantilla(salario, hospital)
print (f"Empleados modificados: {registros}")