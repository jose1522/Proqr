import json
import requests
from app.objects.Integration.DB.notification import RequestNotification
from app.objects.sendGrid import SendEmail
from app.objects.Integration.DB.readKey import readDBKey

#Metodo para modificar el contenido en la base de datos (Solicitudes con sus parametros)
#Se encarga de modificar los requestes, en este caso permitimos los status y los comentarios

def ModifyRequest(purchaseRequest, userEmail):
    key = readDBKey()

    url = "https://jskr4ovkybl0gsf-db202002091757.adb.us-ashburn-1.oraclecloudapps.com/ords/tables/api/request"

    headers = {
        'X-ID': purchaseRequest.requestid,
        'X-COMMENTS': json.dumps(purchaseRequest.comments),
        'X-STATUS': purchaseRequest.status,

        'Authorization': "Basic {0}".format(key)
    }

    response = requests.request("PUT", url, headers=headers)
    #Envio de la confirmacion del cambio en el request al usuario atraves de correo electornico

    if response.status_code == 200:
        serverOutput = json.loads(response.text)
        RequestNotification(purchaseRequest, userEmail, serverOutput)

    return response.status_code




