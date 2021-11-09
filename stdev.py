import csv
import math

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

def mean(data):
    n = len(data)
    total = 0 
    for x in data:
        total += int(x)
    mean = total/n

    return mean

sqlist = []
for n in data:
    a = int(n)-mean(data)
    a = a ** 2
    sqlist.append(a)

sum = 0
for i in sqlist:
    sum =sum+i
result = sum/(len(data)-1)

stddev = math.sqrt(result)
print(stddev)