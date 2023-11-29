import pyodbc
import mysql.connector
ambienteDesenvolvimento = False

def getCapturaMaisRecenteDaCpu():
    connectionSQLServer = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=18.208.1.120;'
        'DATABASE=streamoon;'
        'UID=StreamoonUser;'
        'PWD=Moon2023;'
        'TrustServerCertificate=yes;'
    )

    if ambienteDesenvolvimento:
        queryCPU = ("SELECT registro FROM registro WHERE fkComponenteServidor = 1 ORDER BY dtHora DESC LIMIT 1")
    else:
        queryCPU = ("SELECT registro FROM registro WHERE fkComponenteServidor = 1 ORDER BY dtHora DESC TOP 1")

    try:
        connectionSQLServer.execute(queryCPU)
        capturaMaisRecenteCPU = connectionSQLServer.fetchone()
        connectionSQLServer.close()
    except:
        capturaMaisRecenteCPU = 0
        return capturaMaisRecenteCPU
    else:
        return capturaMaisRecenteCPU

def getCapturaMaisRecenteDaMemoria():
    connectionSQLServer = pyodbc.connect(
            'DRIVER={SQL Server};'
            'SERVER=18.208.1.120;'
            'DATABASE=streamoon;'
            'UID=StreamoonUser;'
            'PWD=Moon2023;'
            'TrustServerCertificate=yes;'
        )
    

    if ambienteDesenvolvimento:
        queryMEMORIA = ("SELECT registro FROM registro WHERE fkComponenteServidor = 3 ORDER BY dtHora DESC LIMIT 1")
    else:
        queryMEMORIA = ("SELECT registro FROM registro WHERE fkComponenteServidor = 3 ORDER BY dtHora DESC LIMIT 1")

    try:
        connectionSQLServer.execute(queryMEMORIA)
        capturaMaisRecenteMEMORIA = connectionSQLServer.fetchone()
        connectionSQLServer.close()
    except:
        capturaMaisRecenteMEMORIA = 0
        return capturaMaisRecenteMEMORIA
    else:
        return capturaMaisRecenteMEMORIA

def getCapturaMaisRecenteDoDisco():
    connectionSQLServer = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=18.208.1.120;'
        'DATABASE=streamoon;'
        'UID=StreamoonUser;'
        'PWD=Moon2023;'
        'TrustServerCertificate=yes;'
    )

    if ambienteDesenvolvimento:
        queryDISCO = ("SELECT registro FROM registro WHERE fkComponenteServidor = 6 ORDER BY dtHora DESC LIMIT 1")
    else:
        queryDISCO = ("SELECT registro FROM registro WHERE fkComponenteServidor = 6 ORDER BY dtHora DESC LIMIT 1")

    try:
        connectionSQLServer.execute(queryDISCO)
        capturaMaisRecenteDISCO = connectionSQLServer.fetchone()
        connectionSQLServer.close()
    except:
        capturaMaisRecenteDISCO = 0
        return capturaMaisRecenteDISCO
    else:
        return capturaMaisRecenteDISCO
    
    

def getCapturaMaisRecenteDeUpload():
    connectionSQLServer = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=18.208.1.120;'
        'DATABASE=streamoon;'
        'UID=StreamoonUser;'
        'PWD=Moon2023;'
        'TrustServerCertificate=yes;'
    )

    if ambienteDesenvolvimento:
        queryUPLOAD = ("SELECT registro FROM registro WHERE fkComponenteServidor = 9 ORDER BY dtHora DESC LIMIT 1")
    else:
        queryUPLOAD = ("SELECT registro FROM registro WHERE fkComponenteServidor = 9 ORDER BY dtHora DESC LIMIT 1")

    try:
        connectionSQLServer.execute()(queryUPLOAD)
        capturaMaisRecenteUPLOAD = connectionSQLServer.fetchone()[0]
        connectionSQLServer.close()
    except:
        capturaMaisRecenteUPLOAD = 0
        return capturaMaisRecenteUPLOAD
    else:
        return capturaMaisRecenteUPLOAD

def getCapturaMaisRecenteDeDownload():
    connectionSQLServer = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=18.208.1.120;'
        'DATABASE=streamoon;'
        'UID=StreamoonUser;'
        'PWD=Moon2023;'
        'TrustServerCertificate=yes;'
    )

    if ambienteDesenvolvimento:
        queryDOWNLOAD = ("SELECT registro FROM registro WHERE fkComponenteServidor = 10 ORDER BY dtHora DESC LIMIT 1")
    else:
        queryDOWNLOAD = ("SELECT registro FROM registro WHERE fkComponenteServidor = 10 ORDER BY dtHora DESC TOP 1")

    try:
        connectionSQLServer.execute()(queryDOWNLOAD)
        capturaMaisRecenteDOWNLOAD = connectionSQLServer.fetchone()[0]
        connectionSQLServer.close()
    except:
        capturaMaisRecenteDOWNLOAD = 0
        return capturaMaisRecenteDOWNLOAD
    else:
        return capturaMaisRecenteDOWNLOAD

def getCapturaMaisRecenteDeEntradaDoDisco():
    connectionSQLServer = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=18.208.1.120;'
        'DATABASE=streamoon;'
        'UID=StreamoonUser;'
        'PWD=Moon2023;'
        'TrustServerCertificate=yes;'
    )

    if ambienteDesenvolvimento:
        queryEntradaDISCO = ("SELECT registro FROM registro WHERE fkComponenteServidor = 7 ORDER BY dtHora DESC LIMIT 1")
    else:
        queryEntradaDISCO = ("SELECT registro FROM registro WHERE fkComponenteServidor = 7 ORDER BY dtHora DESC LIMIT 1")

    try:
        connectionSQLServer.execute()(queryEntradaDISCO)
        capturaMaisRecenteEntradaDISCO = connectionSQLServer.fetchone()[0]
        connectionSQLServer.close()
    except:
        capturaMaisRecenteEntradaDISCO = 0
        return capturaMaisRecenteEntradaDISCO
    else:
        return capturaMaisRecenteEntradaDISCO

def getCapturaMaisRecenteDeSaidaDoDisco():
    connectionSQLServer = pyodbc.connect(
            'DRIVER={SQL Server};'
            'SERVER=18.208.1.120;'
            'DATABASE=streamoon;'
            'UID=StreamoonUser;'
            'PWD=Moon2023;'
            'TrustServerCertificate=yes;'
        )

    if ambienteDesenvolvimento:
        querySaidaDISCO = ("SELECT registro FROM registro WHERE fkComponenteServidor = 8 ORDER BY dtHora DESC LIMIT 1")
    else:
        querySaidaDISCO = ("SELECT registro FROM registro WHERE fkComponenteServidor = 8 ORDER BY dtHora DESC LIMIT 1")

    try:
        connectionSQLServer.execute()(querySaidaDISCO)
        capturaMaisRecenteSaidaDISCO = connectionSQLServer.fetchone()[0]
        connectionSQLServer.close()
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
        connectionSQLServer = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=18.208.1.120;'
        'DATABASE=streamoon;'
        'UID=StreamoonUser;'
        'PWD=Moon2023;'
        'TrustServerCertificate=yes;'
        )


        if ambienteDesenvolvimento:
            queryAlerta = (f"INSERT INTO alertasSlack VALUES (null, '{nomeComponente} ultrapassou as métricas estabelecidas' ,{fkComponente}, {isAnalista}, now())")
        else:
            queryAlerta = (f"INSERT INTO alertasSlack VALUES (null, '{nomeComponente} ultrapassou as métricas estabelecidas' ,{fkComponente}, {isAnalista}, GETDATE())")

        try:
            connectionSQLServer.execute(queryAlerta)
            connectionSQLServer.commit()

            connectionSQLServer.close()
            print("Ok!")
        except:
            print("Houve um erro na instrução SQL ou no Banco de dados, pois não foi possível inserir o alerta no banco")
    else:
            print("Insert foi bloqueado pela aplicação")