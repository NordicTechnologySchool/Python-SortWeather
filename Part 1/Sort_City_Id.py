import csv
import json

with open("City_JSON_Obj") as csv_file:
    result_reader = csv.reader(csv_file, delimiter=',')
    list_result_reader = list(result_reader)

def sorting_city_id():
    sorting = sorted(list_result_reader, key=lambda x: x[-3])
    print(sorting)

if __name__ == '__main__':
    sorting_city_id()