import csv

lines = list()
members= input("1")
with open('temp.csv', 'r') as readFile:
    reader = csv.reader(readFile)
    for row in reader:
        lines.append(row)
        for field in row:
            if field == "1":
                lines.remove(row)
with open('new.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(lines)