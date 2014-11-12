import csv
from isikukood import ik

def names():
    with open('nimed.txt', 'r') as nimed:
        names = nimed.read.split()
        return names

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
    mywriter.writerow([names,ik(),sugu,kp])

# always make sure that you close the file.
# otherwise you might find that it is empty.
csv_out.close()
