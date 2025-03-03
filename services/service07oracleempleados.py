import oracledb
from models.empleado import Empleado

class ServiceOracleEmpleados:
    def __init__(self):
        self.connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')

    def getEmpleados(self):
        sql = "select * from EMP"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        #DEBEMOS INDICAR EL TIPO DE LISTA QUE 
        #ESTAMOS DEVOLVIENDO
        # variable:list[TIPO DE CLASE] = []
        data:list[Empleado] = []
        for row in cursor:
            emp = Empleado()
            emp.idEmpleado = row[0]
            emp.apellido = row [1]
            emp.oficio = row [2]
            emp.salario = row[5]
            data.append(emp)
        cursor.close()
        return data

    def getEmpleadosSalario(self, salario):
        sql = "select * from EMP where SALARIO >= :P1"
        cursor = self.connection.cursor()
        cursor.execute(sql, (salario,))
        data:list[Empleado] = []
        for row in cursor:
            emp = Empleado()
            emp.idEmpleado = row[0]
            emp.apellido = row [1]
            emp.oficio = row [2]
            emp.salario = row[5]
            data.append(emp)
        cursor.close()
        return data