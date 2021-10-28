class Death:  # Class for a list of the top 10 ways people were killed
    def __init__(self):
        self.form = ''
        self.gender = False  # True for Famale and False for Male


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
        dataBase = []
        file = open(name, 'r')
        for line in file:
            data = line.split(';')
            dataBase.append((data[0], data))
        file.close()
        showMessage('Dados Carregados com sucesso')
        return dict(dataBase)

    except:
        showMessageError('Error returned')

# Show Information about one person
def showInformation(data, key):
    columns = data[key]
    print("Name:", columns[1], "\n"
          "Date:", columns[2], "\n"
          "Manner of death:", columns[3], "\n"
          "Armed:", columns[4], "\n"
          "Age:", columns[5], "\n"
          "Gender:", columns[6], "\n"
          "Race:", columns[7], "\n"
          "City:", columns[8], "State:", columns[9], "\n"
          "Signs of mental illness:", columns[10], "\n"
          "Threat level:", columns[11], "\n"
          "Flee:", columns[12], "\n"
          "Body camera:", columns[13], "\n"
          "Arms category:", columns[14]
          )


# Op 2 - Show all data loaded
def ShowData(data):
    for key in data.keys():
        showInformation(data, key)


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
