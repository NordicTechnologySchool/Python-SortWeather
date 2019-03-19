import mysql.connector
import random
import math

def cari_nilai_a_dan_b():
    mydb = mysql.connector.connect(
        host="db4free.net",
        user="siapaya",
        passwd="siapasihlo",
        database="weatherdb"
    )

    mycursor = mydb.cursor()
    print("Masukkan Longitude Kota London : ")
    lon_London = input()
    nilai_a = "UPDATE weather_info SET a = ABS('"+ lon_London +"' - lon)"
    mycursor.execute(nilai_a)
    print("Masukkan Latitude Kota London : ")
    lat_London = input()
    nilai_b = "UPDATE weather_info SET b = ABS('" + lat_London + "' - lat)"
    mycursor.execute(nilai_b)
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
    hasil = "UPDATE weather_info SET hasil = SQRT((a*a)+(b*b))"
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
    print("3 kota yang memiliki koordinat hampir sama dengan London :", mycursor.fetchall())
    mydb.close

def main():
    cari_nilai_a_dan_b()
    cari_hasil()
    order_by_hasil()

if __name__ == '__main__':
    main()