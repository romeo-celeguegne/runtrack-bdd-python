import mysql.connector

db = mysql.connector.connect(
    host="localhost", user="root", password="peacenlove13", database="LaPlateforme")
cursor = db.cursor()
cursor.execute("select sum(capacite) from salles")
for x in cursor:
    print("La capacité de toutes les salles est de :", x[0])
