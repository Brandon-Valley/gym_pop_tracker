import csv
row = ['2', ' Marie', ' California']
with open('test.csv', 'r') as readFile:
    reader = csv.reader(readFile)
    lines = list(reader)
    lines.append(row)
    
print(lines)
with open('people.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(lines)
readFile.close()
writeFile.close()