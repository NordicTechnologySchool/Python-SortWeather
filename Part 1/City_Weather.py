import urllib.request
import json

def get_api_address():
    urlOpener = urllib.request.urlopen("https://openweathermap.org/api")
    statusCode = urlOpener.getcode()
    info = urlOpener.info()
    print(statusCode)
    print(info)

def get_city_based_on_name_value():
    dataAPIKota = [
        ("http://api.openweathermap.org/data/2.5/weather?q=Bekasi,id&appid=bdb4ad97d686da14764c01394d20da82"),
        ("http://api.openweathermap.org/data/2.5/weather?q=Jakarta,id&appid=bdb4ad97d686da14764c01394d20da82"),
        ("http://api.openweathermap.org/data/2.5/weather?q=Depok,id&appid=bdb4ad97d686da14764c01394d20da82"),
        ("http://api.openweathermap.org/data/2.5/weather?q=Bogor,id&appid=bdb4ad97d686da14764c01394d20da82"),
        ("http://api.openweathermap.org/data/2.5/weather?q=Tangerang,id&appid=bdb4ad97d686da14764c01394d20da82"),
        ("http://api.openweathermap.org/data/2.5/weather?q=Bandung,id&appid=bdb4ad97d686da14764c01394d20da82"),
        ("http://api.openweathermap.org/data/2.5/weather?q=Cirebon,id&appid=bdb4ad97d686da14764c01394d20da82"),
        ("http://api.openweathermap.org/data/2.5/weather?q=Banten,id&appid=bdb4ad97d686da14764c01394d20da82"),
        ("http://api.openweathermap.org/data/2.5/weather?q=Yogyakarta,id&appid=bdb4ad97d686da14764c01394d20da82"),
        ("http://api.openweathermap.org/data/2.5/weather?q=Kebumen,id&appid=bdb4ad97d686da14764c01394d20da82"),
        ("http://api.openweathermap.org/data/2.5/weather?q=Palembang,id&appid=bdb4ad97d686da14764c01394d20da82"),
        ("http://api.openweathermap.org/data/2.5/weather?q=Medan,id&appid=bdb4ad97d686da14764c01394d20da82"),
        ("http://api.openweathermap.org/data/2.5/weather?q=Aceh,id&appid=bdb4ad97d686da14764c01394d20da82"),
        ("http://api.openweathermap.org/data/2.5/weather?q=Padang,id&appid=bdb4ad97d686da14764c01394d20da82"),
        ("http://api.openweathermap.org/data/2.5/weather?q=Pekanbaru,id&appid=bdb4ad97d686da14764c01394d20da82"),
        ("http://api.openweathermap.org/data/2.5/weather?q=Denpasar,id&appid=bdb4ad97d686da14764c01394d20da82"),
        ("http://api.openweathermap.org/data/2.5/weather?q=Makassar,id&appid=bdb4ad97d686da14764c01394d20da82"),
        ("http://api.openweathermap.org/data/2.5/weather?q=Palu,id&appid=bdb4ad97d686da14764c01394d20da82"),
        ("http://api.openweathermap.org/data/2.5/weather?q=Banjarmasin,id&appid=bdb4ad97d686da14764c01394d20da82"),
        ("http://api.openweathermap.org/data/2.5/weather?q=Jayapura,id&appid=bdb4ad97d686da14764c01394d20da82")
    ]

    textCollection = " "

    for i in dataAPIKota:
        #print(dataAPIKota[i])
        urlOpener = urllib.request.urlopen(i)
        html_body = urlOpener.read()
        textCollection = textCollection + str(html_body) + '\n'
        print(textCollection)

    with open('City_JSON_Obj', 'w') as file:
        file.write(textCollection)

if __name__ == '__main__':
    get_api_address()
    get_city_based_on_name_value()