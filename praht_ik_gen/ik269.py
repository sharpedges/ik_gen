import random
for i in range (270):
    first_nr = random.randint(1,8)
    month = format(random.randint(1,12), '02') ## http://stackoverflow.com/questions/16645844/python-generate-random-string-in-range-01-12
    last_nr_1  = format(random.randint(0,999), '03')
    day = format(random.randint(1,31), '02')
    first_nr = str(first_nr)
    #sex = random.randint(1,2) <-- kui teha juurde aasta arvuga seotud esimese numbri valimine
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
    last_nr_1 = str(last_nr_1)
    isikukood_1 = first_nr + year + month + day + last_nr_1

    for i in range(len(isikukood_1)):
        kaal_1_1 = int(isikukood_1[0]) * 1
        kaal_1_2 = int(isikukood_1[1]) * 2
        kaal_1_3 = int(isikukood_1[2]) * 3
        kaal_1_4 = int(isikukood_1[3]) * 4
        kaal_1_5 = int(isikukood_1[4]) * 5
        kaal_1_6 = int(isikukood_1[5]) * 6
        kaal_1_7 = int(isikukood_1[6]) * 7
        kaal_1_8 = int(isikukood_1[7]) * 8
        kaal_1_9 = int(isikukood_1[8]) * 9
        kaal_1_10 = int(isikukood_1[9]) * 1
        kaal_2_1 = int(isikukood_1[0]) * 3
        kaal_2_2 = int(isikukood_1[1]) * 4
        kaal_2_3 = int(isikukood_1[2]) * 5
        kaal_2_4 = int(isikukood_1[3]) * 6
        kaal_2_5 = int(isikukood_1[4]) * 7
        kaal_2_6 = int(isikukood_1[5]) * 8
        kaal_2_7 = int(isikukood_1[6]) * 9
        kaal_2_8 = int(isikukood_1[7]) * 1
        kaal_2_9 = int(isikukood_1[8]) * 2
        kaal_2_10 = int(isikukood_1[9]) * 3

    kaalud_1 = kaal_1_1 + kaal_1_2 + kaal_1_3 + kaal_1_4 + kaal_1_5 + kaal_1_6 + kaal_1_7 + kaal_1_8 + kaal_1_9 + kaal_1_10
    kaalud_2 = kaal_2_1 + kaal_2_2 + kaal_2_3 + kaal_2_4 + kaal_2_5 + kaal_2_6 + kaal_2_7 + kaal_2_8 + kaal_2_9 + kaal_2_10
    jaak_1 = kaalud_1 / 11
    jaak_2 = kaalud_2 / 11
    jaak_1_kontroll = (kaalud_1 - (int(jaak_1) * 11))
    jaak_2_kontroll = (kaalud_2 - (int(jaak_2) * 11))

    if (jaak_1_kontroll == 10 or jaak_1_kontroll == 0) and jaak_2_kontroll == 10:
        last_nr = 0
    elif (jaak_1_kontroll == 10 or jaak_1_kontroll == 0) and jaak_2_kontroll != 10:
        last_nr = jaak_2_kontroll
    else:
        last_nr = kaalud_1 - (int(jaak_1) * 11)

    last_nr = str(last_nr)


    isikukood = isikukood_1 + last_nr
    i += i

print (isikukood)
