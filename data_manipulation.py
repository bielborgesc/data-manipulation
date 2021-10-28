class Person:
    def __init__(self):
        self.name: ''
        self.date: ''
        self.mannerOfDeath: ''
        self.armed: ''
        self.age: ''
        self.gender: ''
        self.race: ''
        self.city: ''
        self.state: ''
        self.signsOfMentalIllness: ''
        self.threatLevel: ''
        self.flee: ''
        self.bodyCamera: ''
        self.armsCategory: ''


class Death:  # Class for a list of the top 10 ways people were killed
    def __init__(self):
        self.form = ''
        self.male = 0
        self.female = 0
        self.unknown = 0


class Weapons:  # This class will help with weapons accounts for the semester
    def __init__(self):
        self.weapon = ''
        self.amount = 0
        self.month = 0
        self.year = 0


class Victims:  # This class was created to sort the states with victims in ascending order
    def __init__(self):
        self.estado = ''
        self.qtdd = 0
        self.ano = 0


def showMessage(msg):
    print("====================", "\n", msg, "\n" "====================" "\n")


def showMessageError(msg):
    print("*********************", "\n", msg, "\n" "*********************" "\n")


def chooseMenuOption():  # The Menu
    showMessage("Menu")
    print(
        '1 - Load data of file\n'
        '2 - Show data loaded\n'
        '3 - List with the top 10 forms of death and their number\n'
        '4 - People murdered by firearms in FL\n'
        '5 - Average of Asian Men and Women\n'
        '6 - Number of people by race\n'
        '7 - Similar data between 2 victims\n'
        '8 - Show the month with the most deaths\n'
        '9 - See percentage murderers are recorded per year\n'
        '10 - Most used weapon per semester\n'
        '11 - Show percentage of white victims who fled\n'
        '12 - Show in ascending order the number of victims in each state\n'
        '13 - Show Victims for each year in ascending order\n'
        '14 - Relationship between two files\n'
        '14 - Check if there was any date of similar violence between the two files\n'
        '0 - Exit'
    )
    return input('Opção: ')


# Op 1 - Load data of file
def LoadFile(name):
    try:
        firstLine = True
        dataBase = []
        file = open(name, 'r')
        for line in file:
            if not firstLine:
                data = line.split(';')
                p = Person()
                p.name = data[1]
                p.date = data[2]
                p.mannerOfDeath = data[3]
                p.armed = data[4]
                p.age = data[5]
                p.gender = data[6]
                p.race = data[7]
                p.city = data[8]
                p.state = data[9]
                p.signsOfMentalIllness = data[10]
                p.threatLevel = data[11]
                p.flee = data[12]
                p.bodyCamera = data[13]
                p.armsCategory = data[14]
                dataBase.append((data[0], p))
            else:
                firstLine = False
        file.close()
        showMessage('Data Loaded with success')
        return dict(dataBase)

    except:
        showMessageError('Error returned')


# Show Information about one person
def showInformation(data, key):
    columns = data[key]
    print("Name:", columns.name, "\n"
                                 "Date:", columns.date, "\n"
                                                        "Manner of death:", columns.mannerOfDeath, "\n"
                                                                                                   "Armed:",
          columns.armed, "\n"
                         "Age:",
          columns.age, "\n"
                       "Gender:", columns.gender, "\n"
                                                  "Race:", columns.race, "\n"
                                                                         "City:", columns.city, "State:", columns.state,
          "\n"
          "Signs of mental illness:",
          columns.signsOfMentalIllness, "\n"
                                        "Threat level:", columns.threatLevel, "\n"
                                                                              "Flee:", columns.flee, "\n"
                                                                                                     "Body camera:",
          columns.bodyCamera, "\n"
                              "Arms category:",
          columns.armsCategory
          )


# Op 2 - Show all data loaded
def ShowData(data):
    for key in data.keys():
        showInformation(data, key)


def MainFormsOfDeath(data):  # Creating a list of the top 10 forms of death
    mainFormsOfDeath = []
    for value in data.values():
        exist = VerifyElementInList(mainFormsOfDeath, value.mannerOfDeath)
        if not exist:
            mainFormsOfDeath.append(value.mannerOfDeath)
    return mainFormsOfDeath


def VerifyElementInList(list, name):  # Verify if some element is in a list
    if name in list:
        return True
    else:
        return False


def AmountOfDeathsSex(data):  # Create detail list of death per gender
    listOfFormsDeath = MainFormsOfDeath(data)
    listWithAmount = []
    for form in listOfFormsDeath:
        contM = 0
        contF = 0
        contUnknown = 0
        for value in data.values():
            if form == value.mannerOfDeath:
                if value.gender == 'M':
                    contM += 1
                elif value.gender == 'F':
                    contF += 1
                else:
                    contUnknown += 1
        d = Death()
        d.form = form
        d.male = contM
        d.female = contF
        d.unknown = contUnknown
        listWithAmount.append(d)
    return listWithAmount


# Op 3 - Show Death detail per gender
def ShowDetailsOfDeathPerGender(data):  # Show the final result
    list = AmountOfDeathsSex(data)
    for elemento in list:
        print(f'Manner of Death: {elemento.form}')
        print(f'Amount Male: {elemento.male}')
        print(f'Amount Female: {elemento.female}')
        print(f'Amount Unknown: {elemento.unknown}')
        print()


# Op 4 - Average of state deaths from a specific weapon
def ShowAverageOfStateWithOnceWeapon(data, state, weapon):
    cont = 0
    amountDeath = 0
    for element in data.values():
        cont += 1
        if state == element.state and weapon == element.armed:
            amountDeath += 1
    average = (amountDeath / cont) * 100
    print(f'The average of people who died in {state} with {weapon}\n'
          f'is {average :.2f}%')


# Op 5
def DeathByRace(data, race):  # the percentage of men and women of a race who were killed
    contM = 0
    contF = 0
    contUnknown = 0
    for element in data.values():
        if element.race == race:
            if element.gender == 'F':
                contF += 1
            elif element.gender == 'M':
                contM += 1
            else:
                contUnknown += 1
    averageM = (contM / len(data)) * 100
    averageF = (contF / len(data)) * 100
    averageUnknown = (contUnknown / len(data)) * 100
    print(f'Origin: {race}\n'
          f'Men: {averageM :.2f}%\n'
          f'Women: {averageF :.2f}%\n'
          f'Women: {averageUnknown :.2f}%')

def AmountPerRace(data):
    dic = {}
    for element in data.values():
        if element.race not in dic:
            dic[element.race] = 1
        else:
            dic[element.race] += 1
    for chave in dic.keys():
        print(f'{chave} tem {dic[chave]} mortes')


# Data extracted from dataset
dataBase = ()
# Start Program
op = -1
while op != 0:
    op = int(chooseMenuOption())
    if op == 1:
        fileName = 'Arquivo Originas Coluna.csv'
        dataBase = LoadFile(fileName)
    elif op == 2:
        ShowData(dataBase)
    elif op == 3:
        ShowDetailsOfDeathPerGender(dataBase)
    elif op == 4:
        state = 'FL'
        weapon = 'gun'
        ShowAverageOfStateWithOnceWeapon(dataBase, state, weapon)
    elif op == 5:
        race = 'White'
        DeathByRace(dataBase, race)
        print()
        race = 'Black'
        DeathByRace(dataBase, race)
    elif op == 6:
        AmountPerRace(dataBase)
