import random
from datetime import date, timedelta

def random_birth_date():
    days = (date(2099,12,31) - date(1800,1,1)).days
    birth_date = date(1800,1,1) + timedelta(days = random.randint(0,days))
    return birth_date    

def generate_birth_date():
    birth_date = random_birth_date()
    century = str(birth_date.year)[:2]

    if century == "18":
        first_nr = random.choice("12")
    elif century == "19":
        first_nr = random.choice("34")
    elif century == "20":
        first_nr = random.choice("56")
    
    return first_nr + birth_date.strftime("%Y%m%d")[2:]
def ik():
    isikukood = generate_birth_date() + format(random.randint(0,999), '03')
    return isikukood + control_nr(isikukood)

def control_nr(isikukood):
    for kaalud in [[1,2,3,4,5,6,7,8,9,1],[3,4,5,6,7,8,9,1,2,3]]:
        jaak_kontroll = jaak(isikukood, kaalud)
        if jaak_kontroll != 10:
            return str(jaak_kontroll)
    return "0"

def jaak(isikukood, kaalud):
    summa = 0
    for i in range(len(isikukood)):
        summa += kaalud[i] + int(isikukood[i])
    return summa % 11

if __name__ == "__main__":
    print(ik())
