import requests
from app.objects.Integration.DB.notification import RequestNotification
from app.objects.sendGrid import SendEmail
from app.objects.Integration.DB.readKey import readDBKey
import json

def NulltoNA(input):
    if input is None or input == '':
        return "NA"
    else:
        return input

#Metodo para agregar el contenido a la base de datos (Solicitudes con sus parametros)
#Método que agrega un request

def AddRequest(purchaseRequest, userEmail):
    key = readDBKey()

    url = "https://jskr4ovkybl0gsf-db202002091757.adb.us-ashburn-1.oraclecloudapps.com/ords/tables/api/request"

    headers = {
        'X-ID': NulltoNA(purchaseRequest.userid),
        'X-DESCRIPTION': NulltoNA(purchaseRequest.description),
        'X-ITEMS': NulltoNA(purchaseRequest.items),
        'X-COMMENTS': NulltoNA(purchaseRequest.comments),
        'X-AMOUNT': NulltoNA(purchaseRequest.amount),

        'Authorization': "Basic {0}".format(key)
    }

    response = requests.request("POST", url, headers=headers)
    #Envio de la confirmacion cuando el usuario hace un request atraves de correo electornico
    if response.status_code == 200:

        serverOutput = json.loads(response.text)

        RequestNotification(purchaseRequest,userEmail, serverOutput)

    return response.status_code

