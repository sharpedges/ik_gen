import csv
import random
from isikukood import ik, random_birth_date


"""def names():
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
        return kp"""

def generate_csv(number):
    eesnimed = []
    perenimed = []
    with open('nimed.txt', 'r',encoding="UTF-8") as nimed:
        for line in nimed:
            eesnimed.append(line.split(",")[0].strip())
        
    with open('nimed.txt', 'r',encoding="UTF-8") as nimed:
        for line in nimed:
            try:
                perenimed.append(line.split(",")[1].strip())
            except IndexError:
                continue
    # open a file for writing.
    csv_out = open('mycsv.csv', 'w', encoding="UTF-8")

    # create the csv writer object.
    mywriter = csv.writer(csv_out)

    # writerow - one row of data at a time.
    mywriter.writerow(['SOCIAL_SECURITY_NUMBER, FORENAME,SURNAME,GENDER,DATE_OF_BIRTH'])
    for i in range(number):
        mywriter.writerow([ik(),eesnimi(eesnimed),perenimi(perenimed),sugu(),kuupaev()])

    # always make sure that you close the file.
    # otherwise you might find that it is empty.
    csv_out.close()
    
            
def eesnimi(eesnimed):
    return random.choice(eesnimed)

def perenimi(perenimed):
    return random.choice(perenimed)

def sugu():
    return random.choice("mn")

def kuupaev():
    return random_birth_date().strftime("%d.%m.%Y")
    
if __name__ == "__main__":
    import cProfile
    cProfile.run("generate_csv(1000000)", sort="tottime")
