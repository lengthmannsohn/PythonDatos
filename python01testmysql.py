import pymysql

connection = pymysql.connect(host='localhost', port=3306,user='getafe', passwd='mysql', db='HOSPITAL')

print("Funciona MySQL")