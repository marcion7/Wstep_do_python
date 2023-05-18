# 1
import re

with open('strings.txt', 'r') as strings:
    lines = strings.read()
    print(re.findall('[0-9]', lines))
    print(re.findall('[0-9]{3,}', lines))
    print(re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', lines))
    print(re.findall(r'\b[A-Z]\w*\b', lines))
    print(re.findall(r'http[s]?://www\.\S*\.\S*/', lines))

with open('strings.txt', 'r') as strings:
    lines = strings.readlines()
    lines_with_four_words = [line.strip() for line in lines if len(re.findall(r'\b\S+\b', line)) >= 4]
    print(lines_with_four_words)

# 2
import csv
from datetime import datetime
from pprint import pprint

parsed_data = []

with open('auth.log', 'r') as file:
    for line in file:

        date = re.findall(r'^[A-Z][a-z]{2} {1,2}[0-9]{1,2} \d{2}:\d{2}:\d{2}', line)
        reform_date = datetime.strptime(date[0], "%b %d %H:%M:%S").replace(year=2023)
        new_date = reform_date.strftime("%Y-%m-%d %H:%M:%S")

        ip = re.findall(r'\d{2}-\d{2}-\d{2}-\d{3}', line)
        ip = ip[0].replace('-', '.')

        user = re.findall(r'[A-Z|a-z]+\S*: ', line)
        user = user[0].split('[')[0].replace(': ','')

        mess = (re.findall(r":\s(.*)$", line))
        mess = mess[0]

        parsed_data.append([new_date, ip, user, mess])
    #pprint(parsed_data)

csv_file = 'parsed_log.csv'
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    writer.writerow(['Data', 'IP', 'Service/User', 'Message'])
    writer.writerows(parsed_data)

# 3
import pickle

class Point:

    def __init__(self):
        self.x = 0
        self.y = 0

    def __str__(self):
        return f"Point({self.x},{self.y})"

    def __mul__(self, number: int):
        self.x *= number
        self.y *= number
        return self

    def __eq__(self, other):
        if isinstance(other, Point):
            if self.x == other.x and self.y == other.y:
                return True
            else:
                return False

punkt = Point()
punkt.x = 2
punkt.y = 1

# serializacja
with open('picled_inst', 'wb') as file:
    pickle.dump(punkt, file)

# deserializacja
with open('picled_inst', 'rb') as file:
    loaded = pickle.load(file)

print(loaded)

# 4

punkt2 = Point()
punkt2.x = 4
punkt2.y = 10

punkt3 = Point()
punkt3.x = 8

punkt_list = [punkt, punkt2, punkt3]

# serializacja
with open('picled_list', 'wb') as file:
    pickle.dump(punkt_list, file)

# deserializacja
with open('picled_list', 'rb') as file:
    loaded = pickle.load(file)

print(loaded)
for l in loaded:
    print(l)