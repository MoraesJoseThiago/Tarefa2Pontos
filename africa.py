import mysql.connector

def conectar():
  mydb = mysql.connector.connect(
    host="34.201.128.159",
    user="admin",
    password="Jose4219#",
    database="animais"
  )
  return mydb