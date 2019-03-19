import mysql.connector
import random

def insert_values():
    print("Masukkan ID Kota : ")
    city_id = input()
    print("Masukkan Nama Kota : ")
    city_name = input()
    print("Masukkan Lon : ")
    lon = input()
    print("Masukkan Lat : ")
    lat = input()
    print("Masukkan Cuaca Saat Ini : ")
    weather = input()
    print("Masukkan Temperatur : ")
    temp = input()

    mydb = mysql.connector.connect(
        host="db4free.net",
        user="siapaya",
        passwd="siapasihlo",
        database="weatherdb"
    )

    mycursor = mydb.cursor()
    sql = "INSERT INTO weather_info (city_id, city_name, lon, lat, weather, temp) "
    sql = sql + "VALUES ('"+ city_id +"','"+ city_name +"','"+ lon +"','"+ lat +"','"+ weather +"','"+ temp +"')"

    mycursor.execute(sql)
    print(mycursor.rowcount, "record inserted.")
    print("Apakah anda ingin memasukan barang lainnya?")
    answer = input()
    if(answer == "ya"):
        insert_values()
    mydb.commit()
    mycursor.fetchone()
    mydb.close

if __name__ == '__main__':
    insert_values()