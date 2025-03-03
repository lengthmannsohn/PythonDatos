import pymysql

connection = pymysql.connect(host='localhost', port=3306,user='getafe', passwd='mysql', db='HOSPITAL')

cursor = connection.cursor()

sql = "select * from EMP"

cursor.execute(sql)

#cursor.execute("SELECT VERSION()")

for row in cursor:
    print(f"Apellido {row[1]}, Oficio: {row[2]}")

#version = cursor.fetchone()

#print (f"/nVersión de MySql: {version[0]}")

cursor.close()
connection.close()


print("Funciona MySQL")