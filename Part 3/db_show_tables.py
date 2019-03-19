import mysql.connector
import random

def show_tables():
    mydb = mysql.connector.connect(
        host="db4free.net",
        user="siapaya",
        passwd="siapasihlo",
        database="weatherdb"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SHOW TABLES")
    #print(mycursor.rowcount, "record inserted.")
    print(mycursor.fetchone())

if __name__ == '__main__':
    show_tables()