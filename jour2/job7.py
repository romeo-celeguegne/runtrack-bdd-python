import mysql.connector


db = mysql.connector.connect(
    host="localhost", user="root", password="peacenlove13", database="Jour2Job7")
cursor = db.cursor()
cursor.execute("select nom,prenom,salaire from employes where salaire>3000")
for x in cursor:
    print("employés adhérents au club des plus de 3k:", x)

cursor.execute(
    "select e.*, s.nom from employes e inner join services s on e.id_service = s.id;")
for x in cursor:
    print(x)
