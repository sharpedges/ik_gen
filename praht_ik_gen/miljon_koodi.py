import csv

with open('nimed.txt', 'r') as nimed:
    names = nimed.read()

with open('isikukoodid.txt', 'r') as isikukood:
    isikukood = isikukood.read()

print (names)
a = 'SOCIAL_SECURITY_NUMBER, 	FORENAME, 	SURNAME, 	GENDER, 	DATE_OF_BIRTH' + '\n'

with open("output.csv", "w") as my_file:
    my_file.write(a)
    for row in names:
        my_file.write(names) + my_file.write(isikukood)
        break

