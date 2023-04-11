import mysql.connector

db = mysql.connector.connect(
    host="localhost", user="root", password="peacenlove13", database="LaPlateforme")
cursor = db.cursor()
cursor.execute("select nom,capacite from salles")
for x in cursor:
    print(x)
