import mysql.connector

def conectar():
  mydb = mysql.connector.connect(
    host="aulateste.csx2qcm55fkg.us-east-1.rds.amazonaws.com",
    user="admin",
    password="Jose4219#",
    database="brasil"
  )
  return mydb