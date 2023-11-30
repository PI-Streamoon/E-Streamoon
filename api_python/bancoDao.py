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
    cursor = connectionSQLServer.cursor()
    subquery = ("SELECT registro, ROW_NUMBER() OVER (ORDER BY dtHora DESC) AS RowNum "
                "FROM registro WHERE fkComponenteServidor = 1")

    queryCPU = ("SELECT registro FROM (" + subquery + ") AS tempTable WHERE RowNum = 1")
   
    cursor.execute(queryCPU)
    capturaMaisRecenteCPU = cursor.fetchone()[0]
    cursor.close()
    connectionSQLServer.close()
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
   
    cursor = connectionSQLServer.cursor()
    subquery = ("SELECT registro, ROW_NUMBER() OVER (ORDER BY dtHora DESC) AS RowNum "
                "FROM registro WHERE fkComponenteServidor = 3")

    queryMEMORIA = ("SELECT registro FROM (" + subquery + ") AS tempTable WHERE RowNum = 1")
   
    cursor.execute(queryMEMORIA)
    capturaMaisRecenteMEMORIA = cursor.fetchone()[0]
    cursor.close()
    connectionSQLServer.close()
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

    cursor = connectionSQLServer.cursor()
    subquery = ("SELECT registro, ROW_NUMBER() OVER (ORDER BY dtHora DESC) AS RowNum "
                "FROM registro WHERE fkComponenteServidor = 6")

    queryDISCO = ("SELECT registro FROM (" + subquery + ") AS tempTable WHERE RowNum = 1")
   
    cursor.execute(queryDISCO)
    capturaMaisRecenteDISCO = cursor.fetchone()[0]
    cursor.close()
    connectionSQLServer.close()
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

    cursor = connectionSQLServer.cursor()
    subquery = ("SELECT registro, ROW_NUMBER() OVER (ORDER BY dtHora DESC) AS RowNum "
                "FROM registro WHERE fkComponenteServidor = 9")

    queryUPLOAD = ("SELECT registro FROM (" + subquery + ") AS tempTable WHERE RowNum = 1")
   
    cursor.execute(queryUPLOAD)
    capturaMaisRecenteUPLOAD = cursor.fetchone()[0]
    cursor.close()
    connectionSQLServer.close()
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

    cursor = connectionSQLServer.cursor()
    subquery = ("SELECT registro, ROW_NUMBER() OVER (ORDER BY dtHora DESC) AS RowNum "
                "FROM registro WHERE fkComponenteServidor = 10")

    queryDOWNLOAD = ("SELECT registro FROM (" + subquery + ") AS tempTable WHERE RowNum = 1")
   
    cursor.execute(queryDOWNLOAD)
    capturaMaisRecenteDOWNLOAD = cursor.fetchone()[0]
    cursor.close()
    connectionSQLServer.close()
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
    cursor = connectionSQLServer.cursor()
    subquery = ("SELECT registro, ROW_NUMBER() OVER (ORDER BY dtHora DESC) AS RowNum "
                "FROM registro WHERE fkComponenteServidor = 7")

    queryEntradaDisco = ("SELECT registro FROM (" + subquery + ") AS tempTable WHERE RowNum = 1")
   
    cursor.execute(queryEntradaDisco)
    capturaMaisRecenteEntradaDisco = cursor.fetchone()[0]
    cursor.close()
    connectionSQLServer.close()
    return capturaMaisRecenteEntradaDisco

def getCapturaMaisRecenteDeSaidaDoDisco():
    connectionSQLServer = pyodbc.connect(
            'DRIVER={SQL Server};'
            'SERVER=18.208.1.120;'
            'DATABASE=streamoon;'
            'UID=StreamoonUser;'
            'PWD=Moon2023;'
            'TrustServerCertificate=yes;'
        )
   
    cursor = connectionSQLServer.cursor()
    subquery = ("SELECT registro, ROW_NUMBER() OVER (ORDER BY dtHora DESC) AS RowNum "
                "FROM registro WHERE fkComponenteServidor = 8")

    queryUPLOAD = ("SELECT registro FROM (" + subquery + ") AS tempTable WHERE RowNum = 1")
   
    cursor.execute(queryUPLOAD)
    capturaMaisRecenteUPLOAD = cursor.fetchone()[0]
    cursor.close()
    connectionSQLServer.close()
    return capturaMaisRecenteUPLOAD

def inserirtAlerta(nomeComponente, isAnalista):

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
        return

    connectionSQLServer = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=18.208.1.120;'
        'DATABASE=streamoon;'
        'UID=StreamoonUser;'
        'PWD=Moon2023;'
        'TrustServerCertificate=yes;'
    )

    cursor = connectionSQLServer.cursor()

    queryAlerta = (f"INSERT INTO alertasSlack (descricao, fkComponente, isAnalista, dtHora) "
                    f"VALUES ('{nomeComponente}', {fkComponente}, {isAnalista}, GETDATE())")

    cursor.execute(queryAlerta)
    connectionSQLServer.commit()
    cursor.close()
    connectionSQLServer.close()
    print(f"Alerta de {nomeComponente} inserido no banco!!!")
