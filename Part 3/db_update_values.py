import mysql.connector
import random

def update_values():
    print("Masukkan ID Kondisi Cuaca Terkini : ")
    weather_id = input()
    print("Masukkan ID Kota yang Datanya Diubah : ")
    city_id = input()

    mydb = mysql.connector.connect(
        host="db4free.net",
        user="siapaya",
        passwd="siapasihlo",
        database="weatherdb"
    )

    mycursor = mydb.cursor()
    sql = "UPDATE weather_info SET weather_id = '"+ weather_id +"' WHERE city_id = '"+ city_id +"'"
    mycursor.execute(sql)
    print(mycursor.rowcount, "record updated.")
    print("Apakah masih ada yang ingin diubah?")
    answer = input()
    if(answer == "ya"):
        update_values()
    mydb.commit()
    mycursor.fetchone()
    mydb.close

if __name__ == '__main__':
    update_values()