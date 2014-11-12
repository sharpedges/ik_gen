import csv

with open('nimed.txt', 'r') as nimed:
    names = nimed.read()

with open('isikukoodid.txt', 'r') as isikukood:
    isikukood = isikukood.read()

print (names)
a = ['asd']

with open("output.csv", "w") as my_file:
    writer = csv.writer(my_file)
    [writer.writerow(r) for r in a]
    for row,columns in zip(names, isikukood):
        my_file.write(names) + my_file.write(isikukood)
        break
