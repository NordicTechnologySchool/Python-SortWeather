import mysql.connector
import random
import csv

def select_data():
    mydb = mysql.connector.connect(
        host="db4free.net",
        user="siapaya",
        passwd="siapasihlo",
        database="weatherdb"
    )

    mycursor = mydb.cursor()
    sql = "SELECT * FROM weather_info WHERE city_id LIKE '%1626973%'"
    mycursor.execute(sql)
    a = mycursor.fetchone()
    print(a)

    with open('updated_data.csv', 'w') as file:
        csv_writer = csv.writer(file, delimiter=',')
        file.write(str(a))

if __name__ == '__main__':
    select_data()