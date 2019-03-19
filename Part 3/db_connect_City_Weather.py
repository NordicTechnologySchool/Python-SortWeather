import mysql.connector
import random

def connect_to_db():
    mydb = mysql.connector.connect(
        host="db4free.net",
        user="siapaya",
        passwd="siapasihlo",
        database="weatherdb"
    )
    print("Successfully connected.")

def main():
    connect_to_db()

if __name__ == '__main__':
    main()