import csv

item_name = []
item_amount = []

with open('items.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        name = row[0]
        amount = row[1]

        item_name.append(name)
        item_amount.append(amount)

print(item_name)
print(item_amount)
