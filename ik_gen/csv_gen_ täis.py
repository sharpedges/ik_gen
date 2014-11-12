import csv
from isikukood import ik

namefile_content = [line.strip() for line in open('nimed.txt', 'r', encoding="utf8")]
namefile_content = [item for item in namefile_content if "," in item]

for nimi in namefile_content:
    asd = nimi

andmed = []

def sugu():
    with open('gender.txt', 'r') as gender:
        sugu = gender.readline()
        return sugu

def kp():
    with open('date.txt', 'r') as kp:
        kp = kp.readline()
        return kp
    
# open a file for writing.
csv_out = open('mycsv.csv', 'w')

# create the csv writer object.
mywriter = csv.writer(csv_out)

# writerow - one row of data at a time.
mywriter.writerow(['SOCIAL_SECURITY_NUMBER, FORENAME,SURNAME,GENDER,DATE_OF_BIRTH'])
for i in range(5):
    andmed.append(asd)
mywriter.writerow(andmed)

# always make sure that you close the file.
# otherwise you might find that it is empty.
csv_out.close()
