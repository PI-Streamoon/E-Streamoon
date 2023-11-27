from time import sleep
import bancoDao
import alertas

qtdAlertasEmSequenciaCpu = 0
qtdAlertasEmSequenciaMemoria = 0
qtdAlertasEmSequenciaDisco = 0
qtdAlertasEmSequenciaUpload = 0
qtdAlertasEmSequenciaDownload = 0
qtdAlertasEmSequenciaEntradaDisco = 0
qtdAlertasEmSequenciaSaidaDisco = 0
temporizador = 0

chatAnalista = "https://hooks.slack.com/services/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"
chatManutencao = "https://hooks.slack.com/services/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"

print( "-"*40, " Últimos Dados Captados ", "-"*40)

while True:
    cpu = bancoDao.getCapturaMaisRecenteDoDisco()
    memoria = bancoDao.getCapturaMaisRecenteDaMemoria()
    disco = bancoDao.getCapturaMaisRecenteDaCpu()
    upload = bancoDao.getCapturaMaisRecenteDeUpload()
    download = bancoDao.getCapturaMaisRecenteDeDownload()
    entradaDisco = bancoDao.getCapturaMaisRecenteDeEntradaDoDisco()
    saidaDisco = bancoDao.getCapturaMaisRecenteDeSaidaDoDisco()
    
    print("Cpu: ", cpu, " Memória: ", memoria," Disco: ", disco, " Upload: ",
    upload, " Download: ", download, " EntradaDisco: ", entradaDisco, " Saída: ", saidaDisco)

    if temporizador == 30:

        if cpu > 60:

            if qtdAlertasEmSequenciaCpu < 3:
                alertas.enviarAlertaCpu(chatManutencao)
                bancoDao.inserirtAlerta("cpu", 0)
                qtdAlertasEmSequenciaCpu += 1
            else:
                alertas.enviarAlertaCpu(chatAnalista)
                bancoDao.inserirtAlerta("cpu", 1)
                qtdAlertasEmSequenciaCpu += 1
        else:
            qtdAlertasEmSequenciaCpu = 0
        
        if memoria > 70:

            if qtdAlertasEmSequenciaMemoria < 3:
                alertas.enviarAlertaMemoria(chatManutencao)
                bancoDao.inserirtAlerta("memoria", 0)
                qtdAlertasEmSequenciaMemoria += 1
            else:
                alertas.enviarAlertaMemoria(chatAnalista)
                bancoDao.inserirtAlerta("memoria", 1)
                qtdAlertasEmSequenciaMemoria += 1
        else:
            qtdAlertasEmSequenciaMemoria = 0

        if disco > 40:

            if qtdAlertasEmSequenciaDisco < 3:
                alertas.enviarAlertaDisco(chatManutencao)
                bancoDao.inserirtAlerta("disco", 0)
                qtdAlertasEmSequenciaDisco += 1
            else:
                alertas.enviarAlertaDisco(chatAnalista)
                bancoDao.inserirtAlerta("disco", 1)
                qtdAlertasEmSequenciaDisco += 1
        else:
            qtdAlertasEmSequenciaDisco = 0

        if upload > 80:

            if qtdAlertasEmSequenciaUpload < 3:
                alertas.enviarAlertaUpload(chatManutencao)
                bancoDao.inserirtAlerta("upload", 0)
                qtdAlertasEmSequenciaUpload += 1
            else:
                alertas.enviarAlertaUpload(chatAnalista)
                bancoDao.inserirtAlerta("upload", 1)
                qtdAlertasEmSequenciaUpload += 1
        else:
            qtdAlertasEmSequenciaUpload = 0
        
        if download > 75:

            if qtdAlertasEmSequenciaDownload < 3:
                alertas.enviarAlertaDownload(chatManutencao)
                bancoDao.inserirtAlerta("download", 0)
                qtdAlertasEmSequenciaDownload += 1
            else:
                alertas.enviarAlertaDownload(chatAnalista)
                bancoDao.inserirtAlerta("download", 1)
                qtdAlertasEmSequenciaDownload += 1
        else:
            qtdAlertasEmSequenciaDownload = 0
        
        if entradaDisco > 85:

            if qtdAlertasEmSequenciaEntradaDisco < 3:
                alertas.enviarAlertaEntradaDisco(chatManutencao)
                bancoDao.inserirtAlerta("entradaDisco", 0)
                qtdAlertasEmSequenciaEntradaDisco += 1
            else:
                alertas.enviarAlertaEntradaDisco(chatAnalista)
                bancoDao.inserirtAlerta("entradaDisco", 1)
                qtdAlertasEmSequenciaEntradaDisco += 1
        else:
            qtdAlertasEmSequenciaEntradaDisco = 0

        if saidaDisco > 85:
            
            if qtdAlertasEmSequenciaSaidaDisco < 3:
                alertas.enviarAlertaSaidaDisco(chatManutencao)
                bancoDao.inserirtAlerta("saidaDisco", 0)
                qtdAlertasEmSequenciaSaidaDisco += 1
            else:
                alertas.enviarAlertaSaidaDisco(chatAnalista)
                bancoDao.inserirtAlerta("saidaDisco", 1)
                qtdAlertasEmSequenciaSaidaDisco += 1
        else:
            qtdAlertasEmSequenciaSaidaDisco = 0
        
        temporizador = 0

    temporizador += 1
    sleep(1)
    