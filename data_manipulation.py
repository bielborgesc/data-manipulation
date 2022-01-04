from math import ceil
import operator


class Person:
    def __init__(self):
        self.name: ''
        self.date: ''
        self.mannerOfDeath: ''
        self.weapon: ''
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
        self.unknown = ''
        self.form = ''
        self.male = 0
        self.female = 0


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
        '10 - Most used weapon per quarter\n'
        '11 - Show percentage of white victims who fled\n'
        '12 - Show in ascending order the number of victims in each state\n'
        '13 - Show Victims for each year in ascending order\n'
        '14 - Check if there was any date of similar violence between the two files\n'
        '0 - Exit'
    )
    return input('Opção: ')


# Op 1 - Load data of file
def LoadFile(name):
    try:
        firstLine = True
        dataBase = []
        dataBaseTittle = []
        dataForRetur = []
        file = open(name, 'r')
        for line in file:
            data = line.split(';')
            if not firstLine:
                p = Person()
                p.name = data[1]
                p.date = data[2]
                p.mannerOfDeath = data[3]
                p.weapon = data[4]
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
                dataBaseTittle = data
                firstLine = False
        file.close()
        showMessage('Data Loaded with success')
        dataForRetur.append(dataBase)
        dataForRetur.append(dataBaseTittle)
        return dataForRetur

    except:
        showMessageError('Error returned')


# Show Information about one person
def showInformation(data, key):
    columns = data[key]
    print("Name:", columns.name, "\n"
                                 "Date:", columns.date, "\n"
                                                        "Manner of death:", columns.mannerOfDeath, "\n"
                                                                                                   "Weapon:",
          columns.weapon, "\n"
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
        if len(mainFormsOfDeath) > 10:
            break
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
        if state == element.state and weapon == element.weapon:
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


# Op 6 - Amount people per race
def AmountPerRace(data):
    dic = {}
    for element in data.values():
        if element.race not in dic:
            dic[element.race] = 1
        else:
            dic[element.race] += 1
    for chave in dic.keys():
        print(f'{chave} tem {dic[chave]} mortes')


# Op 7 - Compare data between 2 victim
def ShowList(list):
    for element in list:
        print(element)


def NamesList(data):  # Create name list with all names
    nameList = []
    for element in data.values():
        exists = VerifyElementInList(nameList, element.name)
        if not exists:
            nameList.append(element.name)
    return nameList


# Transform the dictionary in list with values
def TransformDictionaryInList(dict):
    list = []
    for value in dict.values():
        list.append(value)
    return list


def VerifyDataEquality(dataTittle, nameData1, nameData2):  # Compare information and return a dictionary
    dic = {}
    nameData1 = nameData1.__dict__
    nameData2 = nameData2.__dict__
    listData1 = TransformDictionaryInList(nameData1)
    listData2 = TransformDictionaryInList(nameData2)
    for i in range(len(listData1)):
        if listData1[i] == listData2[i]:
            dic[dataTittle[i + 1]] = listData2[i]
    return dic


def ShowDataEquality(dataTittle, data, name1, name2):  # Show data equality
    nameData1 = ''
    nameData2 = ''
    for element in data.values():
        if element.name == name1:
            nameData1 = element
        if element.name == name2:
            nameData2 = element
    dic = VerifyDataEquality(dataTittle, nameData1, nameData2)
    print('They have in common: ')
    for chave in dic.keys():
        print(chave, '->', dic[chave])


def monthInWhichThereWereMoreDeaths(data):  # month of the year with the most deaths
    dic = {}
    for value in data.values():
        month = value.date[3:5]
        if month not in dic:
            dic[month] = 1
        else:
            dic[month] += 1
    bigger = max(dic, key=dic.get)
    print(f'The month with the highest deaths was {bigger} with {dic[bigger]} deaths')


# Op 9
def RecordedMurders(fromDate, toDate, data):  # percentage of registered murders
    dic = {}
    dicCamera = {}
    for element in data.values():
        year = int(element.date[6:])
        if fromDate <= year <= toDate:
            if year not in dic:
                dic[year] = 1
            else:
                dic[year] += 1
            if element.bodyCamera == "True" and year not in dicCamera:
                dicCamera[year] = 1
            elif element.bodyCamera == "True" and year in dicCamera:
                dicCamera[year] += 1

    for key in dic.keys():
        print(dicCamera[key], dic[key])
        media = (dicCamera[key] / dic[key]) * 100
        print(f'Year: {key} \n Murderers: {dic[key]} \n'
              f'Recorded Murders: {media :.2f}%')
        print()


def checkTheBiggestWeaponUsedInAGivenPeriod(quarter, year, dataBase):
    dicWeapon = {}

    for element in dataBase.values():
        date = element.date  # day = date[0:2] month = date[3:5] year = date[6:]
        thisQuarter = ceil(int(date[
                               3:5]) / 3)  # dividing the month by 3 and rounding to the nearest whole number we can find out which quarter it is in
        if thisQuarter == quarter and date[6:] == year:
            if element.weapon not in dicWeapon:
                dicWeapon[element.weapon] = 1
            else:
                dicWeapon[element.weapon] += 1

    if len(dicWeapon.items()) > 1:
        max_key = max(dicWeapon.items(), key=operator.itemgetter(1))[0]
        return [max_key, dicWeapon[max_key]]

    return ["No records found", 0]


# Op 10
def MostUsedWeaponInTheQuarter(dataBase):  # most used weapons per quarter
    years = []  # list with years
    matriz = []  # cubic matrix with quarter year and most used weapon

    for element in dataBase.values():  # extracting some data
        if (element.date[6:] not in years):
            years.append(element.date[6:])

    for i in range(len(years)):  # creating matrix with data
        print(f'Ano: {years[i]}')
        for j in range(1, 5, 1):
            linha = ['', '', '']
            linha[0] = years[i]  # year
            linha[1] = j  # qurter
            linha[2] = checkTheBiggestWeaponUsedInAGivenPeriod(j, years[i], dataBase)
            matriz.append(linha)
            print(f'Trimestre: {j} | Weapon: {linha[2][0]} | Amout: {linha[2][1]}')
        print('-' * 10)


# Op 11
def VictimList(dataBase):  # Create a list of white victims who fled
    whitePeople = []
    for element in dataBase.values():
        if element.race == 'White' and element.threatLevel != 'Not fleeing':
            if element.name not in whitePeople:
                whitePeople.append(element.name)
    return whitePeople


def ListWhitePeopleWhoFled(dataBase):  # Informa o percentual
    list = VictimList(dataBase)
    amount = len(dataBase.values())
    percentage = (len(list) / amount) * 100
    print(f'{len(list)} vitimas brancas fugiram e isso da um percentual de {percentage :.2f}% de {amount}')


# Op 12
def TotalNumberOfVictimsByStateInAscendingOrder(dataBase):  # This def will show the total number of victims by state.
    victimsByState = {}
    for element in dataBase.values():
        if element.state not in victimsByState:
            victimsByState[element.state] = 0
        else:
            victimsByState[element.state] += 1
    sortedDict = sorted(victimsByState.items(), key=operator.itemgetter(1))
    for element in sortedDict:
        print(f'The State {element[0]} has {element[1]} victims')


# Op 13
def TotalNumberOfVictimsByYearInAscendingOrder(dataBase):  # display victims per year
    victimsByYear = {}
    for element in dataBase.values():
        if element.date[6:] not in victimsByYear:
            victimsByYear[element.date[6:]] = 0
        else:
            victimsByYear[element.date[6:]] += 1
    sortedDict = sorted(victimsByYear.items(), key=operator.itemgetter(1))
    for element in sortedDict:
        print(f'The Years {element[0]} had {element[1]} victims')


def PegarDados(mat, indice):  # Essa def vai pegar dados do arquivo
    lista = []
    for i in range(1, len(mat)):
        lista.append(mat[i][indice])
    return lista


def CompararArquivos(mat, mat2):  # Essa def vai comparar os dados
    lista1 = PegarDados(mat2, 2)
    listaAgrupada = []
    for data in lista1:
        for i in range(len(mat)):
            if mat[i][2] == data:
                listaAgrupada.append(mat[i])
    return listaAgrupada


def MostrarDados(mat, mat2):  # Essa def vai mostrar todos os dados das datas iguais do dois arquivos
    linhaMat1 = CompararArquivos(mat, mat2)  # Lista com os dados de determinada data
    datasMat2 = PegarDados(mat2, 2)  # Lista das datas
    for data in datasMat2:
        print(f'====={data}=====')
        for elemento in linhaMat1:
            if elemento[2] == data:
                print('Arquivo 1')
                print(f'Nome: {elemento[1]}'
                      f'Data: {elemento[2]}'
                      f'Sexo: {elemento[6]}'
                      f'Morte: {elemento[4]}')
        for i in range(1, len(mat2)):
            if mat2[i][2] == data:
                print('Arquivo 2')
                print(f'Nome: {mat2[i][1]}'
                      f'Data: {mat2[i][2]}'
                      f'Sexo: {mat2[i][6]}'
                      f'Morte: {mat2[i][4]}')


# Op 14
def ShowResult(dataBase1, dataBase2):  # This function will show all the data of the same dates of the two files
    for element2 in dataBase2.values():
        for element1 in dataBase1.values():
            if element1.date == element2.date:
                print(f'====={element2.date}=====')
                print('Arquivo 1')
                print(f'Name: {element1.name} \n'
                      f'Date: {element1.date} \n'
                      f'Sexo: {element1.gender} \n'
                      f'Morte: {element1.mannerOfDeath} \n')
                print('Arquivo 2')
                print(f'Name: {element2.name} \n'
                      f'Date: {element2.date} \n'
                      f'Sexo: {element2.gender} \n'
                      f'Morte: {element2.mannerOfDeath} \n')


# Data extracted from dataset
dataBase = ()
dataTittle = []
# Start Program
op = -1

# if you do not want automatic file loading, delete the next 4 lines and use option 1 from the menu #
fileName = 'Arquivo Originas Coluna.csv'
data = LoadFile(fileName)
dataBase = dict(data[0])
dataTittle = data[1]
# -------------------------------------------------------------------------------------------------- #

while op != 0:
    op = int(chooseMenuOption())
    if op == 1:
        fileName = 'Arquivo Originas Coluna.csv'
        data = LoadFile(fileName)
        dataBase = dict(data[0])
        dataTittle = data[1]
    elif op == 2:
        ShowData(dataBase)
    elif op == 3:
        ShowDetailsOfDeathPerGender(dataBase)
    elif op == 4:
        state = 'FL'
        weapon = 'gun'
        ShowAverageOfStateWithOnceWeapon(dataBase, state, weapon)
    elif op == 5:
        race = 'Asian'
        DeathByRace(dataBase, race)
    elif op == 6:
        AmountPerRace(dataBase)
    elif op == 7:
        namesList = NamesList(dataBase)
        ShowList(namesList)
        name1 = input('Victim 1: ').title()
        exists1 = VerifyElementInList(namesList, name1)
        name2 = input('Victim 2: ').title()
        exists2 = VerifyElementInList(namesList, name2)
        if not exists1 or not exists2:
            print('Name not found')
        else:
            ShowDataEquality(dataTittle, dataBase, name1, name2)
    elif op == 8:
        monthInWhichThereWereMoreDeaths(dataBase)
    elif op == 9:
        fromDate = 2015
        toDate = 2020
        RecordedMurders(fromDate, toDate, dataBase)
    elif op == 10:
        MostUsedWeaponInTheQuarter(dataBase)
    elif op == 11:
        ListWhitePeopleWhoFled(dataBase)
    elif op == 12:
        TotalNumberOfVictimsByStateInAscendingOrder(dataBase)
    elif op == 13:
        TotalNumberOfVictimsByYearInAscendingOrder(dataBase)
    elif op == 14:
        file = 'Meu escopo.csv'
        data = LoadFile(file)
        dataTittle = data[1]
        dataBase2 = dict(data[0])
        ShowResult(dataBase, dataBase2)
    else:
        print("Thanks for using our system, see you next time")
