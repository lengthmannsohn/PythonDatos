import pyodbc

connection = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=127.0.0.1;DATABASE=HOSPITAL;UID=SA;PWD=Getafe12345@@;TrustServerCertificate=yes')

cursor = connection.cursor()

sql = "select * from EMP"

cursor.execute(sql)

for row in cursor:
    print(f"Apellido {row[1]}, Oficio: {row[2]}")

cursor.close()

cursor = connection.cursor()
cursor.execute("SELECT @@VERSION")

version = cursor.fetchone()

print (f"/nVersión de SQL Server: {version[0]}")

cursor.close()
connection.close()

print("Fin de programa")
