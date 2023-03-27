import mysql.connector

try :
   mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="rpg"
)
   print("Connection réussie.")
except:
   print("Connection echouée.")


cursor = mydb.cursor()

#fetchall sert à print chaque ligne indépendemment et non une seule et même ligne
cursor.execute("SELECT * FROM item")
column_names = [description[0] for description in cursor.description]
print("\n\nListe d'items: \n")
print(column_names)
results = cursor.fetchall()
for row in results:
    print(row)

cursor.execute("SELECT * FROM caracter")
column_names = [description[0] for description in cursor.description]
print("\n\nListe de caracters: \n")
print(column_names)
results = cursor.fetchall()
for row in results:
    print(row)

