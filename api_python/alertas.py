import requests
import json

ativarMensagensDeErroNoTerminal = False

alertaCpu = {"text": f"""        
        🚨ALERTA CPU🚨    
    Cpu ultrapassou a métrica de 60%
"""}

alertaMemoria = {"text": f"""
         🚨ALERTA MEMÓRIA🚨      
    Memória ultrapassou a métrica de 70%    
"""}

alertaDisco = {"text": f"""          
         🚨ALERTA DISCO🚨    
    Disco ultrapassou a métrica de 40%    
"""}

alertaUpload = {"text": f"""          
         🚨ALERTA UPLOAD🚨      
    Upload ultrapassou a métrica de 80%  
"""}

alertaDownload = {"text": f"""          
          🚨ALERTA DOWNLOAD🚨      
    Download ultrapassou a métrica de 75%      
"""}

alertaEntradaDisco = {"text": f"""          
            🚨ALERTA ENTRADA DE DISCO🚨          
    Entrada de disco ultrapassou a métrica de 85%  
"""}

alertaSaidaDisco = {"text": f"""          
            🚨ALERTA SAIDA DE DISCO🚨          
    SAIDA DE DISCO ultrapassou a métrica de 85%        
"""}

def enviarAlertaCpu(UrlDoChat):
    postMsg = requests.post(UrlDoChat, data=json.dumps(alertaCpu))
    if ativarMensagensDeErroNoTerminal and postMsg.status_code != 200:
        print("Alerta não pôde ser enviado, verifique se a url está ativa.")

def enviarAlertaMemoria(UrlDoChat):
    postMsg = requests.post(UrlDoChat, data=json.dumps(alertaMemoria))
    if ativarMensagensDeErroNoTerminal and postMsg.status_code != 200:
        print("Alerta não pôde ser enviado, verifique se a url está ativa.")

def enviarAlertaDisco(UrlDoChat):
    postMsg = requests.post(UrlDoChat, data=json.dumps(alertaDisco))
    if ativarMensagensDeErroNoTerminal and postMsg.status_code != 200:
        print("Alerta não pôde ser enviado, verifique se a url está ativa.")

def enviarAlertaUpload(UrlDoChat):
    postMsg = requests.post(UrlDoChat, data=json.dumps(alertaUpload))
    if ativarMensagensDeErroNoTerminal and postMsg.status_code != 200:
        print("Alerta não pôde ser enviado, verifique se a url está ativa.")

def enviarAlertaDownload(UrlDoChat):
    postMsg = requests.post(UrlDoChat, data=json.dumps(alertaDownload))
    if ativarMensagensDeErroNoTerminal and postMsg.status_code != 200:
        print("Alerta não pôde ser enviado, verifique se a url está ativa.")

def enviarAlertaEntradaDisco(UrlDoChat):
    postMsg = requests.post(UrlDoChat, data=json.dumps(alertaEntradaDisco))
    if ativarMensagensDeErroNoTerminal and postMsg.status_code != 200:
        print("Alerta não pôde ser enviado, verifique se a url está ativa.")

def enviarAlertaSaidaDisco(UrlDoChat):
    postMsg = requests.post(UrlDoChat, data=json.dumps(alertaSaidaDisco))
    if ativarMensagensDeErroNoTerminal and postMsg.status_code != 200:
        print("Alerta não pôde ser enviado, verifique se a url está ativa.")