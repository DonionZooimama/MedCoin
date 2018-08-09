import random

database_directory = "database.csv"


def UpdatePatientData(id, first, last, bloodtype, allergies):
    with open(database_directory, 'r') as file:
        data = file.readlines()
        index = 0
        found = False
        for line in data:
            if int(line.split(',')[0]) == int(id):
                found = True
                new_line = "%s,%s,%s,%s,%s,\n" % (id, first, last, bloodtype, allergies)
                data[index] = new_line
                break
            index += 1

    if found:
        with open(database_directory, 'w') as file:
            file.writelines(data)
            return id + " successfully updated"
    else:
        return id + " does not exist"


def NewPatientData(first, last, bloodtype, allergies):
    with open(database_directory, 'r') as file:

        r = random.randint(100000000000, 999999999999)
        run = True
        while run:
            run = False
            for line in file:
                if int(line.split(',')[0]) == r:
                    r = random.randint(100000000000, 999999999999)
                    run = True
                    break

    with open(database_directory, 'a') as file:
        line = "%s,%s,%s,%s,%s,\n" % (r, first, last, bloodtype, allergies)
        file.write(line)
        return str(r) + " successfully created"


def GetPatientData(id):
    with open(database_directory, 'r') as file:
        data = file.readlines()
        for line in data:
            if int(line.split(',')[0]) == int(id):
                return line
