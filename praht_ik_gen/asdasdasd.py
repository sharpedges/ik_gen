from isikukood import ee_person_code, find_bday
from random import choice


def import_names(namefile):
    """
    Returns a list of names.

    Each name is a list where list[0] = last name and list[1] = first name
    """
    names = []
    with open(namefile, "r", encoding='utf-8') as textfile:
        for row in textfile:
            name = textfile.readline()
            names.append(name.strip("\n").split(", "))
    return names


def csv_rows(num_rows, names):
    """ Returns a list of rows to write in the csv file. """
    rows = []
    for i in range(num_rows):
        name = choice(names)
        firstname = name[1] if len(name) > 1 else ""
        lastname = name[0]
        code = ee_person_code()
        gender = "N" if int(code[0]) % 2 == 0 else "M"
        date = find_bday(code)
        row = "%s,%s,%s,%s,%s" % (code, firstname, lastname, gender, date)
        rows.append(row)
    return rows


def write_to_csv(row_list, filename="person_code.csv"):
    """ Writes row_list to file. """
    with open(filename, "w", encoding='utf-8') as csvfile:
        csvfile.write("SOCIAL_SECURITY_NUMBER,FORENAME,SURNAME,GENDER,DATE_OF_BIRTH\n")
        for row in row_list:
            csvfile.write(row + "\n")


def ee_person_code_csv(rows):
    """ Creates a csv file .Has rows number of rows.

    social_security_number, forename, surname, gender, date_of_birth
    """
    names = import_names("names.txt")
    row_list = csv_rows(rows, names)
    write_to_csv(row_list)

if __name__ == '__main__':
    miljon = 1000
    ee_person_code_csv(miljon)
    names = import_names("names.txt")
