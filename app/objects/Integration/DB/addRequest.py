import requests
from app.objects.Integration.DB.readKey import readDBKey
from app.objects.Integration.DB.notification import RequestNotification
import json

#Metodo para agregar el contenido a la base de datos (Solicitudes con sus parametros)
def AddRequest(purchaseRequest, userEmail):
    key = readDBKey()

    url = "https://jskr4ovkybl0gsf-db202002091757.adb.us-ashburn-1.oraclecloudapps.com/ords/tables/api/request"

    headers = {
        'X-ID': purchaseRequest.userid,
        'X-DESCRIPTION': purchaseRequest.description,
        'X-ITEMS': purchaseRequest.items,
        'X-COMMENTS': purchaseRequest.comments,
        'X-AMOUNT': purchaseRequest.amount,

        'Authorization': "Basic {0}".format(key)
    }

    response = requests.request("POST", url, headers=headers)
    #Envio de la confirmacion cuando el usuario hace un request atraves de correo electornico
    if response.status_code == 200:

        serverOutput = json.loads(response.text)
        if response.status_code == 200:
            RequestNotification(purchaseRequest,userEmail, serverOutput)
    return response.status_code