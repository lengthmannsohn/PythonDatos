import oracledb
from models import doctor as model

class ServiceOracleDoctores:
    def __init__(self):
        self.connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
    
    def getAllDoctores(self):
        sql = "select * from DOCTOR"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        datos = []
        for row in cursor:
            doc = model.Doctor()
            doc.idDoctor = row[1]
            doc.apellido = row[2]
            doc.especialidad = row[3]
            doc.salario = row[4]
            doc.hospital = row[0]
            datos.append(doc)
        cursor.close()
        return datos
    
    def insertarDoctor(self, idDoctor, apellido, espe, salario, hospital):
        sql = "insert into DOCTOR values (:hosp,:id,:ape,:espe,:sal)"
        cursor = self.connection.cursor()
        cursor.execute(sql, (hospital, idDoctor, apellido, espe, salario))
        registros = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registros
    def eliminarDoctor(self, iddoctor):
        sql = "delete from DOCTOR where DOCTOR_NO=:p1"
        cursor = self.connection.cursor()
        cursor.execute(sql, (iddoctor,))
        registros = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registros