import mysql.connector

db = mysql.connector.connect(
    host="localhost", user="root", password="peacenlove13", database="LaPlateforme")
cursor = db.cursor()
cursor.execute("select * from etudiants")
for x in cursor:
    print(x)
