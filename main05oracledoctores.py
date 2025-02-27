from services import service05oracledoctores as service
from models import doctor as model

print("-----CRUD DOCTORES-----")
servicio = service.ServiceOracleDoctores()
doctores = servicio.getAllDoctores()
for doc in doctores:
    print(f"{doc.idDoctor}, {doc.apellido}, Especialidad: {doc.especialidad}, {doc.salario}")

print("1.- Insertar doctor")
print("2.- Eliminar doctor")
print("Seleccione una opción")
opcion = int(input())
if (opcion == 1):
    print("ID del doctor")
    iddoctor = int(input())
    print("Apellido")
    ape = input()
    print("Especialidad:")
    espe = input()
    print("Salario")
    sal = int(input())
    print("Hospital")
    hosp = int(input())
    reg = servicio.insertarDoctor(iddoctor, ape, espe, sal, hosp)
    print(f"Doctores insertados: {reg}")
elif (opcion == 2):
    print("Introduzca ID a eliminar")
    iddoctor = int(input())
    registros = servicio.eliminarDoctor(iddoctor)
    print(f"Doctores eliminados: {registros}")
print("Fin de programa")