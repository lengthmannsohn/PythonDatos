from services import service04oracledepartamentos as service
from models import departamento

print("----SERVICIO ORACLE DEPARTAMENTOS")
#NECESITAMOS UNA OBJETO DE TIPO SERVICIO PARA TRABAJAR
servicio = service.ServiceOracleDepartamentos()
print("------------DEPARTAMENTOS----------")
datos = servicio.getAllDepartamentos()
for dept in datos:
    print(f"{dept.numero}, {dept.nombre}, {dept.localidad}")
print("-----------------------------------")
print("1.- Insertar departamento")
print("2.- Buscar departamento")
print("3.- Eliminar departamento")
print("4.- Modificar departamento")
print("Seleccione una opción")
opcion = int(input())
if (opcion == 1):
    print("Insertar departamento")
    print("Id del departamento")
    numero = int(input())
    print("Nombre del departamento")
    nombre = input()
    print("Localidad")
    localidad = input()
    afectados = servicio.insertarDepartamento(numero,nombre, localidad)
    print(f"Departamentos insertados: {afectados}")
elif (opcion == 2):
    print("Buscador de departamentos por ID")
    print("Introduzca el id del departamento")
    iddept = int(input())
    #DECLARAMOS UNA VARIABLE PARA GUARDAR EL DEPARTAMENTO
    dept = servicio.buscarDepartamentoId(iddept)
    print(f"{dept.numero}, {dept.nombre}, {dept.localidad}")
elif (opcion == 3):
    print("Eliminar departamento")
    print("Introduzca el ID a eliminar")
    iddept = int(input())
    registros = servicio.eliminarDepartamento(iddept)
    print(f"Departamentos eliminados: {registros}")
elif (opcion == 4):
    print("----Modificar departamento----")
    print("Introduzca el ID del departamento")
    iddept = int(input())
    print("Nuevo nombre de departamento")
    nombre = input()
    print("Localidad:")
    localidad = input()
    registros = servicio.modificarDepartamento(iddept, nombre, localidad)
    print(f"Departamentos modificados: {registros}")
print("Fin de programa")