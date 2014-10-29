import random

first_nr = random.randint(1,8)
month = format(random.randint(1,12), '02') ## http://stackoverflow.com/questions/16645844/python-generate-random-string-in-range-01-12
last_nr  = format(random.randint(0,9999), '04')
day = format(random.randint(1,31), '02')
first_nr = str(first_nr)
##sex = random.randint(1,2) <-- kui teha juurde aasta arvuga seotud esimese numbri valimine
year = 0
leap_year = 0

if year % 4 == 0 or year % 100 == 0 or year % 400 == 0:
    leap_year_in = 1
else:
    leap_year_in = 0

year = random.randint(1800,2199)
year = str(year)
year = year[-2:]
leap_year_in = str(leap_year_in)

if month == (1, 3, 5, 7, 8, 10, 12):
    day = format(random.randint(1,31), '02')
elif month == (4, 6, 9, 11):
    day = format(random.randint(1,30), '02')
elif leap_year_in == 1 and month == 2:
    day = format(random.randint(1,28), '02')
elif month == 2:
    day = format(random.randint(1,29), '02')
    
day = str(day)
month = str(month)
last_nr = str(last_nr)
isikukood = first_nr + year + month + day + last_nr
print ("esimene nr " + first_nr)
print ("year " + year)
print ("month " + month)
print ("day " + day)
print ("last " + last_nr)
print ("ik " + isikukood)
