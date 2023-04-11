import mysql.connector

db = mysql.connector.connect(
    host="localhost", user="root", password="peacenlove13", database="LaPlateforme")
cursor = db.cursor()
cursor.execute("select sum(superficie) from etage")
for x in cursor:
    print("La superficie de La Plateforme est de", x[0], "m2")
