import requests
import mysql.connector
import pyodbc

urls = [
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/Canada%20(Central)/OnDemand/Shared/Linux/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/US%20East%20(N.%20Virginia)/OnDemand/Shared/Linux/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/US%20East%20(Ohio)/OnDemand/Shared/Linux/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/US%20West%20(N.%20California)/OnDemand/Shared/Linux/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/US%20West%20(Oregon)/OnDemand/Shared/Linux/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/South%20America%20(Sao%20Paulo)/OnDemand/Shared/Linux/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/EU%20(Spain)/OnDemand/Shared/Linux/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/EU%20(Stockholm)/OnDemand/Shared/Linux/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/EU%20(Frankfurt)/OnDemand/Shared/Linux/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/EU%20(Ireland)/OnDemand/Shared/Linux/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/EU%20(London)/OnDemand/Shared/Linux/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/EU%20(Milan)/OnDemand/Shared/Linux/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/EU%20(Paris)/OnDemand/Shared/Linux/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/EU%20(Zurich)/OnDemand/Shared/Linux/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/Israel%20(Tel%20Aviv)/OnDemand/Shared/Linux/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/Middle%20East%20(Bahrain)/OnDemand/Shared/Linux/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/Middle%20East%20(UAE)/OnDemand/Shared/Linux/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/Africa%20(Cape%20Town)/OnDemand/Shared/Linux/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/Asia%20Pacific%20(Hong%20Kong)/OnDemand/Shared/Linux/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/Asia%20Pacific%20(Hyderabad)/OnDemand/Shared/Linux/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/Asia%20Pacific%20(Jakarta)/OnDemand/Shared/Linux/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/Asia%20Pacific%20(Melbourne)/OnDemand/Shared/Linux/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/Asia%20Pacific%20(Mumbai)/OnDemand/Shared/Linux/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/Asia%20Pacific%20(Osaka)/OnDemand/Shared/Linux/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/Asia%20Pacific%20(Seoul)/OnDemand/Shared/Linux/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/Asia%20Pacific%20(Singapore)/OnDemand/Shared/Linux/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/Asia%20Pacific%20(Sydney)/OnDemand/Shared/Linux/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/Asia%20Pacific%20(Tokyo)/OnDemand/Shared/Linux/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/AWS%20GovCloud%20(US-East)/OnDemand/Shared/Linux/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/AWS%20GovCloud%20(US)/OnDemand/Shared/Linux/NA/No%20License%20required/Yes/index.json",

    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/Canada%20(Central)/OnDemand/Shared/Windows/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/US%20East%20(N.%20Virginia)/OnDemand/Shared/Windows/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/US%20East%20(Ohio)/OnDemand/Shared/Windows/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/US%20West%20(N.%20California)/OnDemand/Shared/Windows/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/US%20West%20(Oregon)/OnDemand/Shared/Windows/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/South%20America%20(Sao%20Paulo)/OnDemand/Shared/Windows/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/EU%20(Spain)/OnDemand/Shared/Windows/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/EU%20(Stockholm)/OnDemand/Shared/Windows/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/EU%20(Frankfurt)/OnDemand/Shared/Windows/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/EU%20(Ireland)/OnDemand/Shared/Windows/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/EU%20(London)/OnDemand/Shared/Windows/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/EU%20(Milan)/OnDemand/Shared/Windows/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/EU%20(Paris)/OnDemand/Shared/Windows/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/EU%20(Zurich)/OnDemand/Shared/Windows/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/Israel%20(Tel%20Aviv)/OnDemand/Shared/Windows/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/Middle%20East%20(Bahrain)/OnDemand/Shared/Windows/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/Middle%20East%20(UAE)/OnDemand/Shared/Windows/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/Africa%20(Cape%20Town)/OnDemand/Shared/Windows/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/Asia%20Pacific%20(Hong%20Kong)/OnDemand/Shared/Windows/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/Asia%20Pacific%20(Hyderabad)/OnDemand/Shared/Windows/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/Asia%20Pacific%20(Jakarta)/OnDemand/Shared/Windows/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/Asia%20Pacific%20(Melbourne)/OnDemand/Shared/Windows/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/Asia%20Pacific%20(Mumbai)/OnDemand/Shared/Windows/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/Asia%20Pacific%20(Osaka)/OnDemand/Shared/Windows/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/Asia%20Pacific%20(Seoul)/OnDemand/Shared/Windows/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/Asia%20Pacific%20(Singapore)/OnDemand/Shared/Windows/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/Asia%20Pacific%20(Sydney)/OnDemand/Shared/Windows/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/Asia%20Pacific%20(Tokyo)/OnDemand/Shared/Windows/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/AWS%20GovCloud%20(US-East)/OnDemand/Shared/Windows/NA/No%20License%20required/Yes/index.json",
    "https://calculator.aws/pricing/2.0/meteredUnitMaps/ec2/USD/current/ec2-calc/AWS%20GovCloud%20(US)/OnDemand/Shared/Windows/NA/No%20License%20required/Yes/index.json"
       ]


con = mysql.connector.connect(
                    host='localhost',
                    database='streamoon',
                    user='StreamoonUser',
                    password='Moon2023'
                )

conSQLServer = pyodbc.connect(
            'DRIVER={SQL Server};'
            'SERVER=18.208.1.120;'
            'DATABASE=streamoon;'
            'UID=StreamoonUser;'
            'PWD=Moon2023;'
            'TrustServerCertificate=yes;'
        )

def dadosEC2(tipo: str, vCPU: int, preco: float, so: str, memoria: float, fkLocais: int):
    mySql_insert = f"INSERT INTO dadosec2 VALUES (NULL ,'{tipo}', {vCPU}, {preco}, '{so}', {memoria}, {fkLocais});"

    cursor = con.cursor()
    cursor.execute(mySql_insert)
    con.commit()
    cursor.close()
    
    cursorSQL = conSQLServer.cursor()
    cursorSQL.execute(mySql_insert)
    conSQLServer.commit()
    cursorSQL.close()
    
def locais(region: str):
    mySql_insert = f"INSERT INTO locais (fkEmpresa, descricao)VALUES (1, '{region}');"

    cursor = con.cursor()
    cursor.execute(mySql_insert)
    con.commit()
    cursor.close()
    
    cursorSQL = conSQLServer.cursor()
    cursorSQL.execute(mySql_insert)
    conSQLServer.commit()    
    cursorSQL.close()

def selecLocais(region: str):
    mySql_select = f"SELECT idLocais FROM locais WHERE descricao = '{region}';"

    cursor = con.cursor()
    cursor.execute(mySql_select)
    resultado = cursor.fetchall()
    cursor.close()
    
    cursorSQL = conSQLServer.cursor()
    cursorSQL.execute(mySql_select)
    resultadoSLQ = cursorSQL.fetchall()
    cursorSQL.close()    

    return resultado[0] if resultado else None

def truncate():
    mysql_truncate = "TRUNCATE TABLE dadosec2;"
    cursor = con.cursor()
    cursor.execute(mysql_truncate)
    con.commit()
    cursor.close()
    
    cursorSQL = conSQLServer.cursor()
    cursorSQL.execute(mysql_truncate)
    conSQLServer.commit()    
    cursorSQL.close()

try:

    truncate()

except mysql.connector.Error as error:
        
        print(f"Erro ao truncar a tabela dadosec2: {error}")
        

for i in urls:
    response = requests.get(i)

    if response.status_code == 200:
        data = response.json()

        for region, region_data in data.get("regions", {}).items():
            try:

                if selecLocais(region) is not None:
                    fkLocais = selecLocais(region)[0]
                else:
                    locais(region)
                    fkLocais = selecLocais(region)[0]

            except mysql.connector.errors as error:
                print("Failed to insert record into table {}".format(error))

            for service_name, service_details in region_data.items():
                if 'OnDemand Shared Linux No License required Yes Hrs' in service_name:

                    modified_service_detail = service_name.replace("OnDemand Shared Linux No License required Yes Hrs", "")
                else:
                    modified_service_detail = service_name.replace("OnDemand Shared Windows No License required Yes Hrs", "")

                tipo = modified_service_detail

                for key, value in service_details.items():
                    if key == "vCPU":
                        vCPU = value
                    if key == "price":
                        preco = value
                    if key == "Operating System":
                        so = value
                    if key == "Memory":
                        memoria = value.replace("GiB", "")

                try:
                    dadosEC2(tipo, vCPU, preco, so, memoria, fkLocais)
                    print("\n" + str(tipo) + "\nCPU: " + str(vCPU) + " preco: " + str(preco) + " SO: " + str(so) +" RAM: " + str(memoria) +" Local: " + str(fkLocais))

                except mysql.connector.Error as error:
                    print("Failed to insert record into table {}".format(error))


    else:
        print(f"Erro ao obter JSON. Código de status: {response.status_code}")