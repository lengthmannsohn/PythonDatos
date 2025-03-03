import pyodbc
from models.empleado import Empleado

class ServiceSqlServerEmpleados:
    def __init__(self):
        self.connection = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=127.0.0.1;DATABASE=HOSPITAL;UID=SA;PWD=Getafe12345@@;TrustServerCertificate=yes')

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
        sql = "select * from EMP where SALARIO >= ?"
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