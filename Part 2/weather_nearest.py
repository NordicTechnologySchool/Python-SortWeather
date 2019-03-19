import mysql.connector
import random
import math

def cari_nilai_a():
    mydb = mysql.connector.connect(
        host="db4free.net",
        user="siapaya",
        passwd="siapasihlo",
        database="weatherdb"
    )

    mycursor = mydb.cursor()
    print("Masukkan ID Cuaca Kota London : ")
    weather_id_London = input()
    nilai_a = "UPDATE weather_info SET a = ABS('"+ weather_id_London +"' - weather_id)"
    mycursor.execute(nilai_a)
    mycursor.fetchone()
    mydb.commit()
    mycursor.close()
    mydb.close

def cari_hasil():
    mydb = mysql.connector.connect(
        host="db4free.net",
        user="siapaya",
        passwd="siapasihlo",
        database="weatherdb"
    )

    mycursor = mydb.cursor()
    hasil = "UPDATE weather_info SET hasil = SQRT(a*a)"
    mycursor.execute(hasil)
    mycursor.fetchone()
    mydb.commit()
    mycursor.close()
    mydb.close

def order_by_hasil():
    mydb = mysql.connector.connect(
        host="db4free.net",
        user="siapaya",
        passwd="siapasihlo",
        database="weatherdb"
    )

    mycursor = mydb.cursor()
    order = "SELECT city_name FROM weather_info ORDER BY hasil ASC, city_name ASC LIMIT 3"
    mycursor.execute(order)
    print("3 kota yang memiliki cuaca hampir sama dengan London :", mycursor.fetchall())
    mydb.close

def main():
    cari_nilai_a()
    cari_hasil()
    order_by_hasil()

if __name__ == '__main__':
    main()