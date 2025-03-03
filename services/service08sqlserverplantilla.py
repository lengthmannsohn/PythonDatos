import pyodbc
from models.plantilla import Plantilla

class ServiceSqlServerPlantilla:
    def __init__(self):
        self.connection = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=127.0.0.1;DATABASE=HOSPITAL;UID=SA;PWD=Getafe12345@@;TrustServerCertificate=yes')

    def getPlantilla(self):
        sql = "select * from PLANTILLA"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        data:list[Plantilla] = []
        for row in cursor:
            plantilla = Plantilla()
            plantilla.idPlantilla = row[2]
            plantilla.apellido = row [3]
            plantilla.funcion = row [4]
            plantilla.salario = row[6]
            plantilla.hospital = row[0]
            data.append(plantilla)
        cursor.close()
        return data

    def updateSalarioPlantilla(self, incremento, numHospital):
        sql = "UPDATE PLANTILLA SET SALARIO = SALARIO + ? WHERE HOSPITAL_COD = ?"
        cursor = self.connection.cursor()
        cursor.execute(sql, (incremento, numHospital))
        registros = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registros