from json import loads
from time import sleep
from urllib3 import PoolManager
import mysql.connector
from os import system
import csv

conexao = mysql.connector.connect(host='localhost', database='dadosCrawler', user='root', password='Kevyn@9566784062@')
comando = "INSERT INTO dados (id, dataHora, discoPercent, ramPercent, cpuPercent) VALUES (NULL, now(), %s, %s, %s)"
cursor = conexao.cursor()
system("cls")

arquivoCSV = "valoresCaptados.csv"

def conversor(valor):
    return float((valor[0:4].replace(" %",'')).replace(",","."))

with PoolManager() as pool:
        print("""                            
@================================================================================================================@
#           |   |       |                             ||                     |        |  |        |              #
#           |   |       |                             ||                     |        | [CRAWLER] |              #
#        [CRAWLER]      |                       ______LL_______              |        |    [OPENHARDWAREMONITOR] #
#               [OPENHARDWAREMONITOR]    ______/               \______       |        |                          #
#               |                       / _____|  ° °     ° °  |_____ \      |        |                          #
#               |                        / ____\   ° °   ° °   /____ \     [CRAWLER]  |                          #
#             [CRAWLER]                   /     \__/|||||||\__/     \            [OPENHARDWAREMONITOR]           #
#                                                                                                                #
#                                                                                                                #
#                                               {...Loading...}                                                  #
#                                                                                                                #
@================================================================================================================@
        \n\n""")
         
        if True:
            sleep(8.5)
            print("Collecting data...\n")
            sleep(1.5)
            while True:
                response = pool.request('GET', 'http://localhost:9000/data.json')
                data = loads(response.data.decode('utf-8'))
                cpu_value = data['Children'][0]['Children'][1]['Children'][0]['Children'][0]['Value']
                mem_value = data['Children'][0]['Children'][2]['Children'][0]['Children'][0]['Value']
                disk_value = data['Children'][0]['Children'][3]['Children'][0]['Children'][0]['Value']

                print("CPU: ",cpu_value ,"Memória: ", mem_value,",Disco: ", disk_value,"\n")
                dados = [conversor(disk_value), conversor(mem_value), conversor(cpu_value)]
                cursor.execute(comando,dados)
                conexao.commit()

                with open(arquivoCSV, mode= "a", newline='') as arquivo_csv:
                    nova_linha_CSV = csv.writer(arquivo_csv)
                    nova_linha_CSV.writerow(["Frequencia de uso CPU", "Porcentagem de uso CPU", "Porcentagem de uso Disco", "Porcentagem de uso Memoria"])
                    nova_linha_CSV.writerow([dados])

                sleep(1)
        
