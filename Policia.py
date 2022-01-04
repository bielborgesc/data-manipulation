class Morte: #Classe para a lista das 10 principais formas que as pessoas foram mortas
    def __init__(self):
        self.forma = ''
        self.masculino = 0
        self.feminino = 0
class Armas:#Essa classe irá auxiliar nas contas de armas no semestre
    def __init__(self):
        self.arma = ''
        self.qtdd = 0
        self.mes = 0
        self.ano = 0
class Vitimas():#Essa classe foi criada para colocar em ordem os estados com vitimas em ordem crescente
    def __init__(self):
        self.estado = ''
        self.qtdd = 0
        self.ano = 0
def Menu():#Menu
    print('1 - Carregar dados do arquivo\n'
          '2 - Mostrar dados carregados\n'
          '3 - Lista com as 10 principais formas de morte e o número delas\n'
          '4 - Pessoas assassinadas por armas de fogo na FL\n'
          '5 - Média de Homens e Mulheres de origem asiática\n'
          '6 - Quantidade de pessoas por raca\n'
          '7 - Dados semelhantes entre 2 vitimas\n'
          '8 - Mostrar o mês com mais mortes\n'
          '9 - Ver porcentual assasinos são gravados por ano\n'
          '10 - Arma mais usada por semestre\n'
          '11 - Mostrar o percentual de vítimas brancas que fugiram\n'
          '12 - Mostrar em ordem crescente a quantidade de vitimas de cada estado\n'
          '13 - Mostrar Vitimas em cada ano em ordem crescente\n'
          '14 - Relação entre dois arquivos\n'
          '14 - Verificar se houve alguma data de violência igual entre os dois arquivos')
    op = input('Opção: ')
    return op
#Op 1
def CarregarArquivo(nome,arquivo): #Carregado os dadods do arquivo
    arquivo = open(arquivo,'r')
    for linha in arquivo:
        dados = linha.split(';')
        nome.append(dados)
    arquivo.close()
    print('Dados Carregados com sucesso')
#Op 2
def MostrarArquivo(nome): #Mostrar todos os dados carregados OP 2
    for i in range(len(nome)):
        print(nome[i])
#Op 3
def FormasDeMorte(mat):#Essa proxima def cria uma lista das formas que as pessoas foram mortas:
    lista10Formas = []
    for i in range(1,len(matriz)):
        existe = VerificarNaLista(lista10Formas,matriz[i][3])
        if existe == False:
            lista10Formas.append(matriz[i][3])
    return lista10Formas
def VerificarNaLista(lista,nome):#Essa def verifica um parametro em uma lista para ver se ele existe:
    for elemento in lista:
        if elemento == nome:
            return True
    return False
def QtddDeMortesSexo(mat):#Essa def Vai mostrar formas de mortes e a qtdd de homens e mulheres que nele há
    lista = FormasDeMorte(mat)
    listaOriginal = []
    for meio in lista:
        contM = 0
        contF = 0
        for i in range(1,len(mat)):
            if meio == mat[i][3]:
                if mat[i][6] == 'M':
                    contM += 1
                elif mat[i][6] == 'F':
                    contF += 1
        m = Morte()
        m.forma = meio
        m.masculino = contM
        m.feminino = contF
        listaOriginal.append(m)
    return listaOriginal
def ExibirResultado(mat):#Essa def mostra o resultado final
    lista = QtddDeMortesSexo(mat)
    for elemento in lista:
        print(f'Meio da morte: {elemento.forma}')
        print(f'Masculino: {elemento.masculino}')
        print(f'Feminino: {elemento.feminino}')
#Op 4
def MostrarMediaMortes(mat,estado,arma):#Essa def irá mostrar a qtdd de pessoas assasinas em determinado local e a arma
    cont = 0
    morte = 0
    for i in range(1,len(mat)):
        cont += 1
        if estado == mat[i][9] and arma == mat[i][4]:
            morte += 1
    media = (morte/cont)*100
    print(f'A média de pessoas que morreram em {estado} com {arma}\n'
          f'É igual a {media :.2f}%')
#Op 5
def MostrarMorteNacao(mat,nacao):# o percentual de homens e o de mulheres asiaticos que foram mortas
    contM = 0
    contF = 0
    for i in range(1,len(mat)):
        if mat[i][7] == nacao:
            if mat[i][6] == 'F':
                contF += 1
            else:
                contM += 1
    mediaM = (contM/len(mat))*100
    mediaF = (contF/len(mat))*100
    print(f'Origem: {nacao}\n'
          f'Homens: {mediaM :.2f}%\n'
          f'Mulheres: {mediaF :.2f}%')
#Op 6
def ListaRaca(mat):#Essa def vai criar uma lista com todas as raças
    listaRaca = []
    for i in range(1,len(mat)):
        existe = VerificarNaLista(listaRaca,mat[i][7]) #Função que utilizei no ex 3
        if existe == False:
            listaRaca.append(mat[i][7])
    return listaRaca
def QtddPorRaca(mat):#Essa def vai mostrar com o uso de um dicioário e a função VerificaLista a qtdd de mortes por raca
    dic = {}
    listaRaca = ListaRaca(mat)
    for raca in listaRaca:
        cont = 0
        for i in range(1,len(mat)):
            if mat[i][7] == raca:
                cont += 1
        dic[raca] = cont
    for chave in dic.keys():
        print(f'{chave} tem {dic[chave]} mortes')
#Op 7
def ListaNomes(mat):#Essa def cria uma lista para a verificação se o nome existe ou não
    listaNome = []
    for i in range(1,len(mat)):
        existe = VerificarNaLista(listaNome,mat[i][1])
        if existe == False:
            listaNome.append(mat[i][1])
    return listaNome
def VerificarIgualdade(mat,dadosNome1,dadosNome2):#Esse verificador compara todas as informações iguais e retorna em um dicionario
    dic = {}
    for i in range(14):# 15 colunas 0-14
        if dadosNome1[i] == dadosNome2[i]:
            dic[mat[0][i]] = dadosNome1[i]
    return dic
def MostrarDadosIguais(mat,nome1,nome2):#Essa def irá ,mostrar os dados iguais
    dadosNome1 = ''
    dadosNome2 = ''
    for i in range(1,len(mat)):
        if mat[i][1] == nome1:
            dadosNome1 = mat[i]
        if mat[i][1] == nome2:
            dadosNome2 = mat[i]
    dic = VerificarIgualdade(mat,dadosNome1,dadosNome2)
    print('Eles apresentam em comum: ')
    for chave in dic.keys():
        print(chave,'->',dic[chave])
#Op 8
def MostrarMesMaisMortes(mat):#Essa def irá mostrar o mês com mais mortes
    dic = {}
    for mes in range(1,13):
        mortes = 0
        for i in range(1,len(mat)):
            data = mat[i][2]
            data = data[3:5]
            if mes == int(data):
                mortes += 1
        dic[mes] = mortes
    maior = 0
    nomeMes = ''
    for chave in dic.keys():
        if int(dic[chave]) > maior:
            maior = dic[chave]
            nomeMes = chave
    print(f'O mês com maior mortes foi {nomeMes} com {maior} mortes')
#Op 9
def VerAssassinosGravados(mat,inicio,fim):#o ano e qual o percentual dos assassinatos que foram gravado naquele ano.
    for ano in range(inicio, fim + 1):
        contGeral = 0
        cont = 0
        for i in range(1, len(mat)):
            data = mat[i][2]
            data = data[6:]
            if int(data) == ano:
                contGeral += 1
                if mat[i][13] == 'True':
                    cont += 1
        media = (cont/contGeral)*100
        print(f'Ano: {ano} \n'
        f'Assasinos Gravados: {media :.2f}%')
#Op 10
def ListaArmas(mat):#Cria uma lista com as armas
    listaArmas = []
    for i in range(1,len(mat)):#1
        existe = VerificarNaLista(listaArmas,mat[i][4])
        if existe == False:
            listaArmas.append(mat[i][4])
    return listaArmas
def ListarArmasMes(mat):#Essa def irá calcular a arma mais usada por mes em cada ano
    listaGeral = []
    listaArmas = ListaArmas(mat)
    for ano in range(2015,2021):#2
        for mes in range(1,13):#3
            for elemento in listaArmas:#4
                usado = 0
                for i in range(1,len(mat)):#5
                    data = mat[i][2]
                    year = data[6:]
                    month = data[3:5]
                    if elemento == mat[i][4] and int(year) == ano and int(month) == mes:
                        usado += 1
                a = Armas()
                a.arma = elemento
                a.qtdd = usado
                a.mes = mes
                a.ano = ano
                listaGeral.append(a)
    return listaGeral
def SepararSemestre(mat):#Essa def irá separar por semestre
    listaArmas = ListarArmasMes(mat)
    listaTrimestre = []
    for ano in range(2015,2021):#6
        trimestre = 0
        maior = 0
        nome = ''
        cont = 0
        for mes in range(1,13):#7
            trimestre += 1
            for elemento in listaArmas:#8
                if int(elemento.mes) == mes:
                    if trimestre == 3:
                        listaTrimestre.append(nome)
                        maior = 0
                        nome = ''
                        trimestre = 0
                    if int(elemento.qtdd) > maior:
                        maior = int(elemento.qtdd)
                        nome = elemento.arma
    return listaTrimestre
def MostrarArmasSemestre(mat):#Essa def ira mostrar a melhor arma em cada trimestre
    lista = SepararSemestre(mat)
    ano = 2015
    trimestre = 1
    for i in range(len(lista)):#9
        if trimestre == 5:
            trimestre = 1
            ano += 1
        print(f'Trimestre {trimestre} de {ano}')
        print(f'A arma mais usada foi {lista[i]}')
        trimestre += 1
#Op 11
def ListadeVitimas(mat):#Criar uma lista de vitimas brancas que fugiram
    listaBrancos = []
    for i in range(1,len(matriz)):
        if mat[i][7] == 'White' and mat[i][12] != 'Not fleeing':
            existe = VerificarNaLista(listaBrancos,mat[i][1])
            if existe == False:
                listaBrancos.append(mat[i][1])
    return listaBrancos
def VerBrancosQueFugiram(mat):#Informa o percentual
    lista = ListadeVitimas(mat)
    qtddGeral = len(matriz)-1
    percentual = (len(lista)/qtddGeral)*100
    print(f'{len(lista)} vitimas brancas fugiram e isso da um percentual de {percentual :.2f}% de {qtddGeral}')
#Op 12
def ListaEstados(mat):#Essa def cria uma lista de estados
    listaEstados = []
    for i in range(1,len(mat)):
        existe = VerificarNaLista(listaEstados,mat[i][9])
        if existe == False:
            listaEstados.append(mat[i][9])
    return listaEstados
def VerQtddDeCadaEstado(mat):#Essa def irá mostrar o total de vitimas por estado
    listaQtdd = []
    listaEstados = ListaEstados(mat)
    for estado in listaEstados:
        vitimas = 0
        for i in range(1,len(mat)):
            if mat[i][9] == estado:
                vitimas += 1
        v = Vitimas()
        v.estado = estado
        v.qtdd = int(vitimas)
        listaQtdd.append(v)
    return listaQtdd
def ColocarEmOrdem(mat):#Essa def irá organizar por ordem crescente
    troca = ''
    lista = VerQtddDeCadaEstado(mat)
    for i1 in range(len(lista)):
        for i2 in range(len(lista)):
            if lista[i1].qtdd < lista[i2].qtdd:
                troca = lista[i1]
                lista[i1] = lista[i2]
                lista[i2] = troca
    for elemento in lista:
        print(f'Estado {elemento.estado} tem {elemento.qtdd} vitimas')
#Op 13
def VitimasPorAno(mat):#Coloca os dados em um lista
    lista = []
    for ano in range(2015,2021):
        vitima = 0
        for i in range(1,len(mat)):
            data = mat[i][2]
            data = data[6:]
            if ano == int(data):
                vitima += 1
        v = Vitimas()
        v.ano = int(ano)
        v.qtdd = int(vitima)
        lista.append(v)
    return lista
def MostrarAnoVitimas(mat):#Mostra o resultado obitido
    lista = VitimasPorAno(mat)
    troca = ''
    for i1 in range(len(lista)):
        for i2 in range(len(lista)):
            if lista[i1].qtdd < lista[i2].qtdd:
                troca = lista[i1]
                lista[i1] = lista[i2]
                lista[i2] = troca
    for elemento in lista:
        print(f'O ano {elemento.estado} teve {elemento.qtdd} vitimas')
#Op 14
def PegarDados(mat,indice):#Essa def vai pegar dados do arquivo
    lista = []
    for i in range(1,len(mat)):
        lista.append(mat[i][indice])
    return lista
def CompararArquivos(mat,mat2):#Essa def vai comparar os dados
    lista1 = PegarDados(mat2,2)
    listaAgrupada = []
    for data in lista1:
        for i in range(len(mat)):
            if mat[i][2] == data:
                listaAgrupada.append(mat[i])
    return listaAgrupada
def MostrarDados(mat,mat2):#Essa def vai mostrar todos os dados das datas iguais do dois arquivos
    linhaMat1 = CompararArquivos(mat,mat2)#Lista com os dados de determinada data
    datasMat2 = PegarDados(mat2,2)#Lista das datas
    for data in datasMat2:
        print(f'====={data}=====')
        for elemento in linhaMat1:
            if elemento[2] == data:
                print('Arquivo 1')
                print(f'Nome: {elemento[1]}'
                      f'Data: {elemento[2]}'
                      f'Sexo: {elemento[6]}'
                      f'Morte: {elemento[4]}')
        for i in range(1,len(mat2)):
            if mat2[i][2] == data:
                print('Arquivo 2')
                print(f'Nome: {mat2[i][1]}'
                      f'Data: {mat2[i][2]}'
                      f'Sexo: {mat2[i][6]}'
                      f'Morte: {mat2[i][4]}')

#Váriaveis globais
matriz = []
matriz2 = []
op = -1

#Programa principal
while op != 0:
    op = int(Menu())
    if op == 1:
        arquivo = 'Arquivo Originas Coluna.csv'
        CarregarArquivo(matriz,arquivo)
    elif op == 2:
        MostrarArquivo(matriz)
    elif op == 3:
        ExibirResultado(matriz)
    elif op == 4:
        estado = 'FL'
        arma = 'gun'
        MostrarMediaMortes(matriz,estado,arma)
    elif op == 5:
        nacionalidade = 'Asian'
        MostrarMorteNacao(matriz,nacionalidade)
    elif op == 6:
        QtddPorRaca(matriz)
    elif op == 7:
        lista = ListaNomes(matriz)
        nome1 = input('Vítma 1: ').title()
        existe1 = VerificarNaLista(lista,nome1)
        nome2 = input('Vítima 2: ').title()
        existe2 = VerificarNaLista(lista,nome2)
        if existe1 == False or existe2 == False:
            print('Um dos nomes não foram encontrados')
        else:
            MostrarDadosIguais(matriz,nome1,nome2)
    elif op == 8:
        MostrarMesMaisMortes(matriz)
    elif op == 9:
        de = 2015
        ate = 2020
        VerAssassinosGravados(matriz,de,ate)
    elif op == 10:
        MostrarArmasSemestre(matriz)
    elif op == 11:
        VerBrancosQueFugiram(matriz)
    elif op == 12:
        ColocarEmOrdem(matriz)
    elif op == 13:
        MostrarAnoVitimas(matriz)
    elif op == 14:
        arquivo = 'Meu escopo.csv'
        CarregarArquivo(matriz2, arquivo)
        MostrarDados(matriz,matriz2)