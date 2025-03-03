import oracledb
from models import hospital as model

class ServiceOracleHospitales:
    def __init__(self):
        self.connection = oracledb.connect(user='SYSTEM',password='oracle', dsn='localhost')
    
    def getAllHospitales(self):
        sql = "SELECT * from HOSPITAL"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        datos = []
        for row in cursor:
            hosp = model.Hospital()
            hosp.hospitalCod = row[1]
            hosp.nombre = row[2]
            hosp.direccion = row [3]
            hosp.telefono = row [4]

