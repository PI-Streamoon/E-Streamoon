import pydoc
import mysql.connector
ambienteDesenvolvimento = False

def getCapturaMaisRecenteDaCpu():
    conexao = mysql.connector.connect(host='localhost', database='streamoon', user='StreamoonUser', password='Moon2023')
    cursor = conexao.cursor()

    if ambienteDesenvolvimento:
        queryCPU = ("SELECT registro FROM registro WHERE fkComponenteServidor = 1 ORDER BY dtHora DESC LIMIT 1")
    else:
        queryCPU = ("SELECT registro FROM registro WHERE fkComponenteServidor = 1 ORDER BY dtHora DESC TOP 1")

    try:
        cursor.execute(queryCPU)
        capturaMaisRecenteCPU = cursor.fetchone()[0]
        cursor.close()
    except:
        capturaMaisRecenteCPU = 0
        return capturaMaisRecenteCPU
    else:
        return capturaMaisRecenteCPU

def getCapturaMaisRecenteDaMemoria():
    conexao = mysql.connector.connect(host='localhost', database='streamoon', user='StreamoonUser', password='Moon2023')
    connectionSQLServer = pyodbc.connect(
            'DRIVER={SQL Server};'
            'SERVER=18.208.1.120;'
            'DATABASE=streamoon;'
            'UID=StreamoonUser;'
            'PWD=Moon2023;'
            'TrustServerCertificate=yes;'
        )
    
    cursor = conexao.cursor()

    if ambienteDesenvolvimento:
        queryMEMORIA = ("SELECT registro FROM registro WHERE fkComponenteServidor = 3 ORDER BY dtHora DESC LIMIT 1")
    else:
        queryMEMORIA = ("SELECT registro FROM registro WHERE fkComponenteServidor = 3 ORDER BY dtHora DESC LIMIT 1")

    try:
        cursor.execute(queryMEMORIA)
        capturaMaisRecenteMEMORIA = cursor.fetchone()[0]
        cursor.close()
    except:
        capturaMaisRecenteMEMORIA = 0
        return capturaMaisRecenteMEMORIA
    else:
        return capturaMaisRecenteMEMORIA

def getCapturaMaisRecenteDoDisco():
    conexao = mysql.connector.connect(host='localhost', database='streamoon', user='StreamoonUser', password='Moon2023')
    cursor = conexao.cursor()

    if ambienteDesenvolvimento:
        queryDISCO = ("SELECT registro FROM registro WHERE fkComponenteServidor = 6 ORDER BY dtHora DESC LIMIT 1")
    else:
        queryDISCO = ("SELECT registro FROM registro WHERE fkComponenteServidor = 6 ORDER BY dtHora DESC LIMIT 1")

    try:
        cursor.execute(queryDISCO)
        capturaMaisRecenteDISCO = cursor.fetchone()[0]
        cursor.close()
    except:
        capturaMaisRecenteDISCO = 0
        return capturaMaisRecenteDISCO
    else:
        return capturaMaisRecenteDISCO

def getCapturaMaisRecenteDeUpload():
    conexao = mysql.connector.connect(host='localhost', database='streamoon', user='StreamoonUser', password='Moon2023')
    cursor = conexao.cursor()

    if ambienteDesenvolvimento:
        queryUPLOAD = ("SELECT registro FROM registro WHERE fkComponenteServidor = 9 ORDER BY dtHora DESC LIMIT 1")
    else:
        queryUPLOAD = ("SELECT registro FROM registro WHERE fkComponenteServidor = 9 ORDER BY dtHora DESC LIMIT 1")

    try:
        cursor.execute(queryUPLOAD)
        capturaMaisRecenteUPLOAD = cursor.fetchone()[0]
        cursor.close()
    except:
        capturaMaisRecenteUPLOAD = 0
        return capturaMaisRecenteUPLOAD
    else:
        return capturaMaisRecenteUPLOAD

def getCapturaMaisRecenteDeDownload():
    conexao = mysql.connector.connect(host='localhost', database='streamoon', user='StreamoonUser', password='Moon2023')
    cursor = conexao.cursor()

    if ambienteDesenvolvimento:
        queryDOWNLOAD = ("SELECT registro FROM registro WHERE fkComponenteServidor = 10 ORDER BY dtHora DESC LIMIT 1")
    else:
        queryDOWNLOAD = ("SELECT registro FROM registro WHERE fkComponenteServidor = 10 ORDER BY dtHora DESC TOP 1")

    try:
        cursor.execute(queryDOWNLOAD)
        capturaMaisRecenteDOWNLOAD = cursor.fetchone()[0]
        cursor.close()
    except:
        capturaMaisRecenteDOWNLOAD = 0
        return capturaMaisRecenteDOWNLOAD
    else:
        return capturaMaisRecenteDOWNLOAD

def getCapturaMaisRecenteDeEntradaDoDisco():
    conexao = mysql.connector.connect(host='localhost', database='streamoon', user='StreamoonUser', password='Moon2023')
    cursor = conexao.cursor()

    if ambienteDesenvolvimento:
        queryEntradaDISCO = ("SELECT registro FROM registro WHERE fkComponenteServidor = 7 ORDER BY dtHora DESC LIMIT 1")
    else:
        queryEntradaDISCO = ("SELECT registro FROM registro WHERE fkComponenteServidor = 7 ORDER BY dtHora DESC LIMIT 1")

    try:
        cursor.execute(queryEntradaDISCO)
        capturaMaisRecenteEntradaDISCO = cursor.fetchone()[0]
        cursor.close()
    except:
        capturaMaisRecenteEntradaDISCO = 0
        return capturaMaisRecenteEntradaDISCO
    else:
        return capturaMaisRecenteEntradaDISCO

def getCapturaMaisRecenteDeSaidaDoDisco():
    conexao = mysql.connector.connect(host='localhost', database='streamoon', user='StreamoonUser', password='Moon2023')
    cursor = conexao.cursor()

    if ambienteDesenvolvimento:
        querySaidaDISCO = ("SELECT registro FROM registro WHERE fkComponenteServidor = 8 ORDER BY dtHora DESC LIMIT 1")
    else:
        querySaidaDISCO = ("SELECT registro FROM registro WHERE fkComponenteServidor = 8 ORDER BY dtHora DESC LIMIT 1")

    try:
        cursor.execute(querySaidaDISCO)
        capturaMaisRecenteSaidaDISCO = cursor.fetchone()[0]
        cursor.close()
    except:
        capturaMaisRecenteSaidaDISCO = 0
        return capturaMaisRecenteSaidaDISCO
    else:
        return capturaMaisRecenteSaidaDISCO

def inserirtAlerta(nomeComponente, isAnalista):

    habilitarInsert = True
    fkComponente = 0
    if nomeComponente == "cpu":
        fkComponente = 100
    elif nomeComponente == "memoria":
        fkComponente = 102
    elif nomeComponente == "disco":
        fkComponente = 105
    elif nomeComponente == "upload":
        fkComponente = 108
    elif nomeComponente == "download":
        fkComponente = 109
    elif nomeComponente == "entradaDisco":
        fkComponente = 106
    elif nomeComponente == "saidaDisco":
        fkComponente = 107
    else:
        print(f"Não foi encontrado nenhum componente com o nome: {nomeComponente}")
        habilitarInsert = False

    if habilitarInsert:
        conexao = mysql.connector.connect(host='localhost', database='streamoon', user='StreamoonUser', password='Moon2023')
        cursor = conexao.cursor()

        if ambienteDesenvolvimento:
            queryAlerta = (f"INSERT INTO alertasSlack VALUES (null, '{nomeComponente} ultrapassou as métricas estabelecidas' ,{fkComponente}, {isAnalista}, now())")
        else:
            queryAlerta = (f"INSERT INTO alertasSlack VALUES (null, '{nomeComponente} ultrapassou as métricas estabelecidas' ,{fkComponente}, {isAnalista}, GETDATE())")

        try:
            cursor.execute(queryAlerta)
            conexao.commit()
            cursor.close()
            print("Ok!")
        except:
            print("Houve um erro na instrução SQL ou no Banco de dados, pois não foi possível inserir o alerta no banco")
    else:
            print("Insert foi bloqueado pela aplicação")