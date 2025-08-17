import csv
import os
csv_file = input("enter tye path to your csv file")
if not os.path.exists(csv_file):
    print("File not found")
else:
    data = []
    with open (csv_file,r,newline='',encoding='utf-8')as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    for row in data:
        print(row)