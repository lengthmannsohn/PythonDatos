import oracledb
from models import departamento

class ServiceOracleDepartamentos:
    def __init__(self):
        #CREAMOS UN OBJETO CONNECTION
        self.connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
    
    def modificarDepartamento(self, numero, nombre, localidad):
        sql = "update DEPT set DNOMBRE=:p1, LOC=:p2 where DEPT_NO=:p3"
        cursor = self.connection.cursor()
        cursor.execute(sql, (nombre, localidad, numero))
        registros = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registros

    def eliminarDepartamento(self, numero):
        sql = "delete from DEPT where DEPT_NO=:p1"
        cursor = self.connection.cursor()
        cursor.execute(sql, (numero,))
        registros = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registros
    
    def buscarDepartamentoId(self, numero):
        sql = "select * from DEPT where DEPT_NO=:p1"
        cursor = self.connection.cursor()
        cursor.execute(sql, (numero,))
        row = cursor.fetchone()
        #CREAMOS NUESTRO DEPARTAMENTO MODELO
        modelo = departamento.Departamento()
        #ASIGNAMOS LOS DATOS DEL row AL MODELO
        modelo.numero = row[0]
        modelo.nombre = row[1]
        modelo.localidad = row[2]
        cursor.close()
        return modelo

    def insertarDepartamento(self, numero, nombre, localidad):
        sql = "insert into DEPT values (:id, :nombre, :localidad)"
        cursor = self.connection.cursor()
        cursor.execute(sql, (numero, nombre, localidad))
        registros = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registros
    
    def getAllDepartamentos(self):
        sql = "select * from DEPT"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        #CREAMOS UNA LISTA PARA ALMACENAR CADA DEPARTAMENTO
        datos = []
        #RECORREMOS EL CURSOR DE DATOS
        for row in cursor:
            #DEBEMOS CREAR UN NUEVO OBJETO DEPARTAMENTO
            dept = departamento.Departamento()
            dept.numero = row[0]
            dept.nombre = row[1]
            dept.localidad = row[2]
            datos.append(dept)
        cursor.close()
        return datos

