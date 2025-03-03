import oracledb
from models.plantilla import Plantilla

class ServiceOraclePlantilla:
    def __init__(self):
        self.connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')

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
        sql = "UPDATE PLANTILLA SET SALARIO = SALARIO + :p1 WHERE HOSPITAL_COD = :p2"
        cursor = self.connection.cursor()
        cursor.execute(sql, (incremento, numHospital))
        registros = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registros