import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="rpg"
)

cursor = mydb.cursor()

cursor.execute("SELECT * FROM item")

for x in cursor:
  print(x)